#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parent
SKILLS_DIR = ROOT / "skills"
AGENTS_DIR = ROOT / "agents"
COMMANDS_DIR = ROOT / "commands"
RULES_DIR = ROOT / "rules"
MCPS_DIR = ROOT / "mcps"
SETTINGS_PATH = ROOT / "settings.json"

SKILL_REQUIRED_HEADINGS = [
    "## Purpose",
    "## When to Use This Skill",
    "## Output Format / Delivery",
    "## Behavior Rules",
    "## Maintenance Notes",
]
SKILL_PHASE_RE = re.compile(r"(?m)^## Phase \d+: .+")
KABAB_TOKEN_RE = re.compile(r"`([a-z0-9]+(?:-[a-z0-9]+)*)`")
PATH_TOKEN_RE = re.compile(r"`((?:\.agents/)?[A-Za-z0-9_./-]+\.(?:md|json|sh|ps1|py))`")
VERSION_RE = re.compile(r'^version:\s*"([^"]+)"\s*$', re.MULTILINE)
DATE_RE = re.compile(r"^verified_date:\s*(\d{4}-\d{2}-\d{2})\s*$", re.MULTILINE)
CATEGORY_RE = re.compile(r"^category:\s*([a-z]+)\s*$", re.MULTILINE)
NAME_RE = re.compile(r"^name:\s*([a-z0-9-]+)\s*$", re.MULTILINE)
DESCRIPTION_RE = re.compile(r"^description:\s*(.+)\s*$", re.MULTILINE)

ALLOWED_CATEGORIES = {
    "core",
    "frontend",
    "backend",
    "api",
    "database",
    "integrations",
    "infra",
    "research",
    "design",
    "growth",
    "ai",
}
ALLOWED_NON_SKILL_TOKENS = {
    "build-feature",
    "fix-issue",
    "review-code",
    "refactor",
    "ship-ui",
    "research",
}
MCP_ACTIVATION_ALIASES = {
    "filesystem",
    "playwright",
    "apify",
    "21st-dev-magic",
    "supabase",
    "postgres",
    "sqlite",
    "github",
    "memory",
}
EXEMPT_REFERENCE_TOKENS = {
    "spec.md",
}


@dataclass
class Finding:
    level: str
    path: str
    message: str


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def add(findings: list[Finding], level: str, path: Path, message: str) -> None:
    findings.append(Finding(level, str(path.relative_to(ROOT)), message))


def get_skill_dirs() -> list[Path]:
    return sorted([p for p in SKILLS_DIR.iterdir() if p.is_dir() and not p.name.startswith("_")], key=lambda p: p.name)


def get_skill_names(skill_dirs: Iterable[Path]) -> set[str]:
    return {p.name for p in skill_dirs}


def validate_skills(findings: list[Finding], skill_dirs: list[Path]) -> None:
    for skill_dir in skill_dirs:
        skill_path = skill_dir / "SKILL.md"
        if not skill_path.exists():
            add(findings, "ERROR", skill_dir, "Missing SKILL.md")
            continue

        raw = read_text(skill_path)
        if not raw.startswith("---"):
            add(findings, "ERROR", skill_path, "Skill file must start with YAML frontmatter")
            continue

        for heading in SKILL_REQUIRED_HEADINGS:
            if heading not in raw:
                add(findings, "ERROR", skill_path, f"Missing required section: {heading}")

        if not SKILL_PHASE_RE.search(raw):
            add(findings, "ERROR", skill_path, "Missing at least one phase heading")

        name_match = NAME_RE.search(raw)
        if not name_match:
            add(findings, "ERROR", skill_path, "Missing frontmatter field: name")
        elif name_match.group(1) != skill_dir.name:
            add(findings, "ERROR", skill_path, f"Frontmatter name '{name_match.group(1)}' does not match folder '{skill_dir.name}'")

        desc_match = DESCRIPTION_RE.search(raw)
        if not desc_match:
            add(findings, "ERROR", skill_path, "Missing frontmatter field: description")
        else:
            if "Use when" not in desc_match.group(1):
                add(findings, "ERROR", skill_path, "Description must include the phrase 'Use when'")

        if not VERSION_RE.search(raw):
            add(findings, "ERROR", skill_path, "Missing frontmatter field: version")

        date_match = DATE_RE.search(raw)
        if not date_match:
            add(findings, "ERROR", skill_path, "Missing or malformed frontmatter field: verified_date")
        else:
            try:
                date.fromisoformat(date_match.group(1))
            except ValueError:
                add(findings, "ERROR", skill_path, f"Invalid verified_date: {date_match.group(1)}")

        cat_match = CATEGORY_RE.search(raw)
        if not cat_match:
            add(findings, "ERROR", skill_path, "Missing or malformed frontmatter field: category")
        elif cat_match.group(1) not in ALLOWED_CATEGORIES:
            add(findings, "ERROR", skill_path, f"Invalid category: {cat_match.group(1)}")


def validate_settings(findings: list[Finding], skill_dirs: list[Path]) -> None:
    settings = json.loads(read_text(SETTINGS_PATH))

    def expect_path(rel_path: str, context: str) -> None:
        target = ROOT / rel_path.replace(".agents/", "")
        if not target.exists():
            add(findings, "ERROR", SETTINGS_PATH, f"{context} points to missing path: {rel_path}")

    expect_path(settings["skillSystem"]["skillsDirectory"], "skillsDirectory")
    expect_path(settings["skillSystem"]["systemDirectory"], "systemDirectory")
    expect_path(settings["projectState"]["stateFile"], "stateFile")
    expect_path(settings["hooks"]["preCommit"], "preCommit hook")
    expect_path(settings["hooks"]["lintOnSave"], "lintOnSave hook")
    validator_path = settings["hooks"].get("validator")
    if validator_path:
        expect_path(validator_path, "validator hook")

    agent_files = {p.stem for p in AGENTS_DIR.glob("*.md")}
    configured_agents = set(settings["agents"]["available"])
    if agent_files != configured_agents:
        add(findings, "ERROR", SETTINGS_PATH, f"Configured agents {sorted(configured_agents)} do not match files {sorted(agent_files)}")

    command_files = {p.stem for p in COMMANDS_DIR.glob("*.md")}
    configured_commands = set(settings["commands"]["available"])
    if command_files != configured_commands:
        add(findings, "ERROR", SETTINGS_PATH, f"Configured commands {sorted(configured_commands)} do not match files {sorted(command_files)}")

    rule_files = {p.stem for p in RULES_DIR.glob("*.md")}
    configured_rules = set(settings["rules"]["enforced"])
    if not configured_rules.issubset(rule_files):
        add(findings, "ERROR", SETTINGS_PATH, f"Configured enforced rules {sorted(configured_rules)} are not all present in rules/ {sorted(rule_files)}")

    if settings["skillSystem"]["maxActiveSkillsSimple"] > settings["skillSystem"]["maxActiveSkills"]:
        add(findings, "ERROR", SETTINGS_PATH, "maxActiveSkillsSimple cannot exceed maxActiveSkills")
    if settings["skillSystem"]["maxActiveSkillsTrivial"] > settings["skillSystem"]["maxActiveSkillsSimple"]:
        add(findings, "ERROR", SETTINGS_PATH, "maxActiveSkillsTrivial cannot exceed maxActiveSkillsSimple")

    if len(skill_dirs) < 1:
        add(findings, "ERROR", SETTINGS_PATH, "No skill directories found")


def validate_markdown_references(findings: list[Finding]) -> None:
    md_files = list(ROOT.glob("*.md")) + list((ROOT / "skills").glob("*.md")) + list((ROOT / "mcps").glob("*.md")) + list((ROOT / "skill-system").glob("*.md"))
    for path in md_files:
        raw = read_text(path)
        for token in PATH_TOKEN_RE.findall(raw):
            if token in EXEMPT_REFERENCE_TOKENS:
                continue

            candidates = []
            if token.startswith(".agents/"):
                candidates.append(ROOT / token.replace(".agents/", ""))
            else:
                candidates.append(path.parent / token)
                candidates.append(ROOT / token)

            if not any(candidate.exists() for candidate in candidates):
                add(findings, "ERROR", path, f"References missing file: {token}")


def validate_skill_token_references(findings: list[Finding], skill_names: set[str]) -> None:
    doc_paths = [
        ROOT / "AGENTS.md",
        ROOT / "evaluation.md",
        ROOT / "versionperformance.md",
        ROOT / "skills" / "CAPABILITIES.md",
        ROOT / "skills" / "SYSTEM_ORCHESTRATION.md",
    ]
    allowed = skill_names | ALLOWED_NON_SKILL_TOKENS
    for path in doc_paths:
        raw = read_text(path)
        for token in KABAB_TOKEN_RE.findall(raw):
            if token not in allowed:
                add(findings, "ERROR", path, f"References unknown skill/command token: `{token}`")


def validate_capabilities(findings: list[Finding], skill_names: set[str]) -> None:
    path = SKILLS_DIR / "CAPABILITIES.md"
    raw = read_text(path)
    tokens = set(KABAB_TOKEN_RE.findall(raw))
    referenced_skills = {token for token in tokens if token in skill_names}
    missing = skill_names - referenced_skills
    if missing:
        add(findings, "ERROR", path, f"Skills missing from routing index: {sorted(missing)}")


def validate_mcp_docs(findings: list[Finding]) -> None:
    activation_raw = read_text(MCPS_DIR / "activation-packs.md")
    installed_raw = read_text(MCPS_DIR / "installed.md")

    activation_tokens = set(KABAB_TOKEN_RE.findall(activation_raw))
    unsupported = {token for token in activation_tokens if token in {"firecrawl"}}
    if unsupported:
        add(findings, "ERROR", MCPS_DIR / "activation-packs.md", f"Unsupported MCP aliases in activation packs: {sorted(unsupported)}")

    for alias in ("filesystem", "playwright", "apify", "21st-dev-magic", "supabase", "sqlite", "github", "memory"):
        label_map = {
            "filesystem": "Filesystem",
            "playwright": "Playwright",
            "apify": "Apify",
            "21st-dev-magic": "21st.dev Magic",
            "supabase": "Supabase",
            "sqlite": "SQLite",
            "github": "GitHub",
            "memory": "Memory",
        }
        if label_map[alias] not in installed_raw:
            add(findings, "ERROR", MCPS_DIR / "installed.md", f"Installed MCP doc is missing expected label for activation alias: {alias}")

    if "`apify`" not in activation_raw:
        add(findings, "ERROR", MCPS_DIR / "activation-packs.md", "Activation packs should use `apify` for web crawling")


def validate_doc_counts(findings: list[Finding], skill_dirs: list[Path]) -> None:
    skill_count = len(skill_dirs)
    agents_count = len(list(AGENTS_DIR.glob("*.md")))

    agents_raw = read_text(ROOT / "AGENTS.md")
    if f"all {skill_count} skills" not in agents_raw:
        add(findings, "WARN", ROOT / "AGENTS.md", f"Expected AGENTS.md to mention current skill count ({skill_count}) in lazy-load guidance")
    if f"all {agents_count} agents" not in agents_raw:
        add(findings, "WARN", ROOT / "AGENTS.md", f"Expected AGENTS.md to mention current agent count ({agents_count}) in agent-loading guidance")

    evaluation_raw = read_text(ROOT / "evaluation.md")
    if str(skill_count) not in evaluation_raw or "normalized live skill library" not in evaluation_raw:
        add(findings, "ERROR", ROOT / "evaluation.md", "Evaluation snapshot should mention the current normalized live skill library count")


def main() -> int:
    findings: list[Finding] = []
    skill_dirs = get_skill_dirs()
    skill_names = get_skill_names(skill_dirs)

    validate_skills(findings, skill_dirs)
    validate_settings(findings, skill_dirs)
    validate_markdown_references(findings)
    validate_skill_token_references(findings, skill_names)
    validate_capabilities(findings, skill_names)
    validate_mcp_docs(findings)
    validate_doc_counts(findings, skill_dirs)

    errors = [f for f in findings if f.level == "ERROR"]
    warnings = [f for f in findings if f.level == "WARN"]

    if not findings:
        print("OK: .agents validation passed with no findings.")
        return 0

    for finding in findings:
        print(f"{finding.level}: {finding.path}: {finding.message}")

    print(f"\nSummary: {len(errors)} error(s), {len(warnings)} warning(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
