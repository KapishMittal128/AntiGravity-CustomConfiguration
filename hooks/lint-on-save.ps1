param(
    [string]$Target = ""
)

$ErrorActionPreference = "Continue"

Write-Output "lint-on-save"

if (Test-Path "package.json") {
    $packageJson = Get-Content "package.json" -Raw

    if ($Target) {
        if (Get-Command npx -ErrorAction SilentlyContinue) {
            if ($packageJson -match '"eslint"' -or (Test-Path ".eslintrc") -or (Test-Path "eslint.config.js") -or (Test-Path "eslint.config.mjs") -or (Test-Path "eslint.config.cjs")) {
                Write-Output "ESLint: $Target"
                npx eslint $Target --max-warnings=0
            }
            if ((Test-Path "prettier.config.js") -or (Test-Path "prettier.config.cjs") -or (Test-Path ".prettierrc") -or (Test-Path ".prettierrc.json")) {
                Write-Output "Prettier check: $Target"
                npx prettier --check $Target
            }
        }
    }
    elseif ($packageJson -match '"lint"') {
        Write-Output "npm run lint"
        npm run lint
    }
}

if ((Test-Path "pyproject.toml") -or (Test-Path "setup.py") -or (Test-Path "requirements.txt")) {
    if (Get-Command ruff -ErrorAction SilentlyContinue) {
        Write-Output "ruff check"
        if ($Target) { ruff check $Target } else { ruff check . }
    }
    elseif (Get-Command flake8 -ErrorAction SilentlyContinue) {
        Write-Output "flake8"
        if ($Target) { flake8 $Target } else { flake8 . }
    }
}

if ((Test-Path "go.mod") -and (Get-Command go -ErrorAction SilentlyContinue)) {
    Write-Output "go vet"
    go vet ./...
}

Write-Output "lint-on-save complete."
exit 0
