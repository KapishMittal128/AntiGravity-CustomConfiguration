#!/usr/bin/env python3
import os
import sys
import json
import re
import argparse
import subprocess
from datetime import datetime, timedelta
from pathlib import Path

try:
    from colorama import init, Fore, Style
    init(autoreset=True)
except ImportError:
    class Dummy:
        def __getattr__(self, name): return ""
    Fore = Style = Dummy()

ROOT = Path(__file__).resolve().parent

# Core components that are implicitly active/referenced
IMPLICIT_ROOT_FILES = {
    "AGENTS.md", "settings.json", "validate_agents.py", 
    "update_registry.py", "ag-audit.py", "README.md",
    "evaluation.md", "CHANGELOG.md", 
    "USAGE.md", "STATE.md", "task.md",
    "implementation_plan.md", "project_heuristics.md"
}

def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="replace")

def get_actual_skill_count() -> int:
    skills_dir = ROOT / "skills"
    if not skills_dir.exists():
        return 0
    return len([d for d in skills_dir.iterdir() if d.is_dir() and not d.name.startswith("_")])

def check_skill_counts(issues, fix_plan):
    actual = get_actual_skill_count()
    
    files_to_check = {
        "skills/CAPABILITIES.md": r"(?:Available Skills \(|)([0-9]+)\s+Master Skills",
        "USAGE.md": r"([0-9]+)\s+Master Skills",
        "evaluation.md": r"normalized live skill library.*?([0-9]+)\s+skills|all\s+([0-9]+)\s+live skills",
        "README.md": r"([0-9]+)\s+Loaded Skills",
        "AGENTS.md": r"all\s+([0-9]+)\s+skills"
    }

    for rel_path, pattern in files_to_check.items():
        path = ROOT / rel_path
        if not path.exists():
            continue
        content = read_text(path)
        matches = re.finditer(pattern, content, re.IGNORECASE)
        for match in matches:
            found_num = int(match.group(1) if match.group(1) else match.group(2))
            if found_num != actual:
                issues.append({
                    "level": "ERROR",
                    "category": "Skill Count Mismatch",
                    "file": rel_path,
                    "message": f"Found {found_num} skills mentioned, but actual count is {actual}."
                })
                fix_plan.append({
                    "file": rel_path,
                    "action": f"Update skill count from {found_num} to {actual}"
                })

def check_version_numbers(issues, fix_plan):
    settings_path = ROOT / "settings.json"
    if not settings_path.exists():
        return
    
    try:
        settings = json.loads(read_text(settings_path))
        ground_truth_version = settings.get("version", "0.0.0")
    except Exception:
        ground_truth_version = "0.0.0"

    # Extract base version without 'v' prefix
    base_version = ground_truth_version.lstrip('v')

    files_to_check = {
        "evaluation.md": r"\*\*Current Version:\*\*\s*v?([0-9.]+)",
        "CHANGELOG.md": r"^##\s*\[v?([0-9.]+)\]",
        "USAGE.md": r"Antigravity OS v?([0-9.]+)"
    }

    for rel_path, pattern in files_to_check.items():
        path = ROOT / rel_path
        if not path.exists():
            continue
        content = read_text(path)
        match = re.search(pattern, content, re.MULTILINE)
        if match:
            found_version = match.group(1)
            # Compare up to minor or patch depending on match length if necessary
            # For simplicity, string match
            if found_version != base_version and not base_version.startswith(found_version):
                issues.append({
                    "level": "ERROR",
                    "category": "Version Mismatch",
                    "file": rel_path,
                    "message": f"Found version {found_version}, expected {base_version}."
                })
                fix_plan.append({
                    "file": rel_path,
                    "action": f"Update version from {found_version} to {base_version}"
                })

def check_changelog_staleness(issues, fix_plan):
    changelog_path = ROOT / "CHANGELOG.md"
    if not changelog_path.exists():
        return
    
    content = read_text(changelog_path)
    # Match ## [version] - YYYY-MM-DD
    dates = re.findall(r"^##\s*\[.*?\]\s*-\s*([0-9]{4}-[0-9]{2}-[0-9]{2})", content, re.MULTILINE)
    
    if not dates:
        issues.append({
            "level": "WARN",
            "category": "Changelog Stale",
            "file": "CHANGELOG.md",
            "message": "No valid dates found in CHANGELOG.md."
        })
        return

    latest_date_str = dates[0]
    try:
        latest_date = datetime.strptime(latest_date_str, "%Y-%m-%d").date()
        days_old = (datetime.now().date() - latest_date).days
        if days_old > 30:
            issues.append({
                "level": "WARN",
                "category": "Changelog Stale",
                "file": "CHANGELOG.md",
                "message": f"Last update was {days_old} days ago ({latest_date_str}). Documentation has gone stale."
            })
            fix_plan.append({
                "file": "CHANGELOG.md",
                "action": "Add a new changelog entry covering recent changes."
            })
    except ValueError:
        pass

def extract_all_references() -> set:
    all_refs = set()
    # Regex to find anything that looks like a file path or backticked name
    ref_patterns = [
        r"`([A-Za-z0-9_./-]+\.(?:md|json|sh|ps1|py))`",  # Backticked files
        r"\]\(([A-Za-z0-9_./-]+\.(?:md|json|sh|ps1|py))\)" # Markdown links
    ]
    
    for md_file in ROOT.rglob("*.md"):
        content = read_text(md_file)
        for pattern in ref_patterns:
            for match in re.finditer(pattern, content):
                val = match.group(1).replace(".agents/", "").replace("\\", "/")
                all_refs.add(val.split("/")[-1]) # store just filename for loose matching
                all_refs.add(val) # store full relative path
                
    for json_file in ROOT.rglob("*.json"):
        content = read_text(json_file)
        # simplistic string path extraction
        for match in re.finditer(r'"([A-Za-z0-9_./-]+\.(?:md|json|sh|ps1|py))"', content):
            val = match.group(1).replace(".agents/", "").replace("\\", "/")
            all_refs.add(val.split("/")[-1])
            all_refs.add(val)
            
    return all_refs

def check_orphans_and_references(issues, fix_plan):
    agents_md = ROOT / "AGENTS.md"
    content = read_text(agents_md)
    # Extract references from AGENTS.md
    agent_refs = re.findall(r"`([A-Za-z0-9_./-]+\.(?:md|json|sh|ps1|py))`", content)
    
    for ref in agent_refs:
        clean_ref = ref.replace(".agents/", "").replace("\\", "/")
        target = ROOT / clean_ref
        if not target.exists() and not (ROOT / clean_ref.split('/')[-1]).exists():
            issues.append({
                "level": "ERROR",
                "category": "Broken Reference",
                "file": "AGENTS.md",
                "message": f"References missing file: {ref}"
            })
            fix_plan.append({
                "file": "AGENTS.md",
                "action": f"Remove or fix missing reference to {ref}"
            })

    # Find orphans
    all_refs = extract_all_references()
    
    # Iterate all files in .agents
    for file_path in ROOT.rglob("*"):
        if not file_path.is_file():
            continue
        
        # Skip .git, node_modules, etc
        if any(part.startswith(".") for part in file_path.parent.parts):
            continue
            
        rel_path = str(file_path.relative_to(ROOT)).replace("\\", "/")
        filename = file_path.name
        
        # Exceptions
        if filename in IMPLICIT_ROOT_FILES or rel_path.startswith("scripts/"):
            continue
        if file_path.parent.name == "skills" and filename == "SKILL.md":
            continue
        if file_path.suffix not in [".md", ".json", ".ps1", ".sh", ".py"]:
            continue
            
        # Check if referenced
        if rel_path not in all_refs and filename not in all_refs:
            issues.append({
                "level": "WARN",
                "category": "Orphaned File",
                "file": rel_path,
                "message": f"File is not referenced by any documentation or config."
            })
            fix_plan.append({
                "file": rel_path,
                "action": "Delete file or add reference in AGENTS.md / docs"
            })


def run_validator(issues):
    validator_path = ROOT / "validate_agents.py"
    if not validator_path.exists():
        return
    
    try:
        result = subprocess.run(
            [sys.executable, str(validator_path)],
            cwd=str(ROOT),
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            for line in result.stdout.splitlines():
                if line.startswith("ERROR:") or line.startswith("WARN:"):
                    parts = line.split(":", 2)
                    issues.append({
                        "level": parts[0].strip(),
                        "category": "Subprocess Validator",
                        "file": parts[1].strip() if len(parts) > 1 else "validate_agents.py",
                        "message": parts[2].strip() if len(parts) > 2 else line
                    })
    except Exception as e:
        issues.append({
            "level": "ERROR",
            "category": "Subprocess Error",
            "file": "validate_agents.py",
            "message": f"Failed to run validator: {e}"
        })

def print_terminal(issues):
    print(f"{Fore.CYAN}{Style.BRIGHT}=== Antigravity OS Audit Report ==={Style.RESET_ALL}\n")
    
    if not issues:
        print(f"{Fore.GREEN}[OK] All checks passed! The OS is perfectly synchronized.{Style.RESET_ALL}")
        return
    
    errors = [i for i in issues if i["level"] == "ERROR"]
    warnings = [i for i in issues if i["level"] == "WARN"]
    
    for i in errors:
        print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} {Fore.YELLOW}{i['file']}{Style.RESET_ALL}: {i['message']}")
        
    for i in warnings:
        print(f"{Fore.YELLOW}[WARN]{Style.RESET_ALL} {Fore.YELLOW}{i['file']}{Style.RESET_ALL}: {i['message']}")
        
    print(f"\n{Fore.CYAN}Summary:{Style.RESET_ALL} {len(errors)} error(s), {len(warnings)} warning(s).")
    
    health_score = max(0, 100 - (len(errors) * 10) - (len(warnings) * 2))
    color = Fore.GREEN if health_score >= 90 else Fore.YELLOW if health_score >= 70 else Fore.RED
    print(f"Health Score: {color}{health_score}/100{Style.RESET_ALL}")

def print_json(issues):
    print(json.dumps(issues, indent=2))

def print_fix(fix_plan):
    print(f"{Fore.MAGENTA}{Style.BRIGHT}=== Proposed Fix Plan (Read-Only) ==={Style.RESET_ALL}\n")
    if not fix_plan:
        print("No fixes needed.")
        return
        
    for fix in fix_plan:
        print(f"File: {Fore.YELLOW}{fix['file']}{Style.RESET_ALL}")
        print(f"Action: {Fore.GREEN}{fix['action']}{Style.RESET_ALL}\n")

def main():
    parser = argparse.ArgumentParser(description="Audit Antigravity OS consistency")
    parser.add_argument("--json", action="store_true", help="Output JSON format")
    parser.add_argument("--fix", action="store_true", help="Show a read-only fix plan")
    args = parser.parse_args()

    issues = []
    fix_plan = []

    check_skill_counts(issues, fix_plan)
    check_version_numbers(issues, fix_plan)
    check_changelog_staleness(issues, fix_plan)
    check_orphans_and_references(issues, fix_plan)
    run_validator(issues)

    if args.json:
        print_json(issues)
    elif args.fix:
        print_fix(fix_plan)
    else:
        print_terminal(issues)

if __name__ == "__main__":
    main()
