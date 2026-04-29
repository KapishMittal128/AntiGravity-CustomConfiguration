#!/usr/bin/env bash
# .agents/hooks/pre-commit.sh
# Lightweight pre-commit sanity checks for both repo code and the .agents OS itself.

set -euo pipefail

echo "Running pre-commit checks..."

# 1. Check for accidental secret file staging
STAGED_FILES=$(git diff --cached --name-only)
for file in $STAGED_FILES; do
  case "$file" in
    .env | .env.* | secrets/* | *.pem | *.key | *.p12)
      echo "BLOCKED: Refusing to commit sensitive file: $file"
      echo "Remove the file from staging and handle it explicitly before retrying."
      exit 1
      ;;
  esac
done

# 2. Detect accidental debug artifacts
if git diff --cached | grep -qE '^\+.*(console\.log|debugger;|pdb\.set_trace|breakpoint\(\))'; then
  echo "WARNING: Staged code contains debug statements (console.log / debugger / pdb)."
  echo "Continuing, but remove these before shipping to production."
fi

# 3. Run project lint if available (non-blocking)
if [ -f "package.json" ] && grep -q '"lint"' package.json; then
  echo "Running lint..."
  if ! npm run lint --silent 2>&1; then
    echo "WARNING: Lint issues found. Resolve before merging to main."
  fi
fi

# 4. Verify no merge conflict markers remain
if git diff --cached | grep -qE '^[+](<<<<<<|>>>>>>|=======$)'; then
  echo "BLOCKED: Merge conflict markers found in staged files."
  exit 1
fi

# 5. Validate the .agents operating system itself
if [ -f ".agents/validate_agents.py" ]; then
  echo "Validating .agents OS..."
  python .agents/validate_agents.py
fi

echo "Pre-commit checks passed."
exit 0
