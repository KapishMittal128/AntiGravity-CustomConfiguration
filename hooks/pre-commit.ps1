$ErrorActionPreference = "Stop"

Write-Output "Running pre-commit checks..."

$stagedFiles = git diff --cached --name-only

foreach ($file in $stagedFiles) {
    if ($file -match '^(?:\.env(?:\..*)?|secrets/.*|.*\.pem|.*\.key|.*\.p12)$') {
        Write-Output "BLOCKED: Refusing to commit sensitive file: $file"
        Write-Output "Remove the file from staging and handle it explicitly before retrying."
        exit 1
    }
}

$stagedDiff = git diff --cached
if ($stagedDiff -match '^\+.*(console\.log|debugger;|pdb\.set_trace|breakpoint\(\))') {
    Write-Output "WARNING: Staged code contains debug statements (console.log / debugger / pdb)."
    Write-Output "Continuing, but remove these before shipping to production."
}

if (Test-Path "package.json") {
    $packageJson = Get-Content "package.json" -Raw
    if ($packageJson -match '"lint"') {
        Write-Output "Running lint..."
        try {
            npm run lint --silent | Out-Host
        }
        catch {
            Write-Output "WARNING: Lint issues found. Resolve before merging to main."
        }
    }
}

if ($stagedDiff -match '^[+](<<<<<<|>>>>>>|=======$)') {
    Write-Output "BLOCKED: Merge conflict markers found in staged files."
    exit 1
}

if (Test-Path ".agents\validate_agents.py") {
    Write-Output "Validating .agents OS..."
    py .agents\validate_agents.py
}

Write-Output "Pre-commit checks passed."
exit 0
