<#
.SYNOPSIS
    Antigravity OS — Project Initializer
.DESCRIPTION
    Creates directory junctions from the current project to the global OS kernel.
    Links both the .agents kernel and the agents/ persona directory.

    Also scaffolds project-local state files (STATE.md, task.md,
    implementation_plan.md) so each project has its own state instead
    of sharing state across all junction-linked projects.
.USAGE
    cd C:\path\to\your\project
    powershell -ExecutionPolicy Bypass -File C:\Users\Kapish\.antigravity\ag-init.ps1
#>

$GlobalAgentsPath = "C:\Users\Kapish\.antigravity\.agents"
$LocalAgentsPath = Join-Path (Get-Location) ".agents"

# Verify global OS exists
if (-not (Test-Path $GlobalAgentsPath)) {
    Write-Host "[ERROR] Global OS not found at: $GlobalAgentsPath" -ForegroundColor Red
    Write-Host "        Install the OS first before linking projects." -ForegroundColor Yellow
    exit 1
}

# 1. Create/Verify .agents junction
if (Test-Path $LocalAgentsPath) {
    $item = Get-Item $LocalAgentsPath -Force
    if ($item.Attributes -band [System.IO.FileAttributes]::ReparsePoint) {
        $target = (Get-Item $LocalAgentsPath -Force).Target
        Write-Host "[OK] .agents junction already exists -> $target" -ForegroundColor Green
    } else {
        Write-Host "[WARNING] .agents already exists as a real directory." -ForegroundColor Yellow
        exit 1
    }
} else {
    try {
        New-Item -ItemType Junction -Path $LocalAgentsPath -Target $GlobalAgentsPath -ErrorAction Stop | Out-Null
        Write-Host "[OK] Linked .agents -> $GlobalAgentsPath" -ForegroundColor Green
    } catch {
        Write-Host "[ERROR] Failed to create .agents junction: $_" -ForegroundColor Red
        exit 1
    }
}

# 2. Create/Verify agents junction (for UI persona discovery)
$GlobalPersonasPath = Join-Path $GlobalAgentsPath "agents"
$LocalPersonasPath = Join-Path (Get-Location) "agents"

if (Test-Path $LocalPersonasPath) {
    Write-Host "[OK] agents folder/junction already exists" -ForegroundColor Cyan
} else {
    try {
        New-Item -ItemType Junction -Path $LocalPersonasPath -Target $GlobalPersonasPath -ErrorAction Stop | Out-Null
        Write-Host "[OK] Linked agents -> $GlobalPersonasPath" -ForegroundColor Green
    } catch {
        Write-Host "[WARNING] Failed to link agent personas: $_" -ForegroundColor Yellow
    }
}

# Quick validation
if (Test-Path (Join-Path $LocalAgentsPath "AGENTS.md")) {
    Write-Host "[OK] Kernel accessible through junction" -ForegroundColor Green
}

# Scaffold project-local state files
$stateFiles = @{
    "STATE.md" = @"
# STATE.md — Project Memory

> **This file is strategic memory, not a changelog.**
> It records durable decisions that a future session needs to know.

## Project Identity

| Field | Value |
|-------|-------|
| **Project name** | $(Split-Path (Get-Location) -Leaf) |
| **Type** | *(web app / API / CLI / library)* |
| **Framework** | *(Next.js / FastAPI / etc.)* |
| **OS last reviewed** | $(Get-Date -Format 'yyyy-MM-dd') |

## Active Tech Decisions

## Work In Progress
"@
    "task.md" = @"
# task.md — Session Execution Tracker

## Current Frontier

- Task: Initializing Antigravity OS
- Goal: System link and state seeding

## Session Steps

1. [x] Create .agents junction
2. [x] Create agents junction
3. [x] Seed local state files
"@
    "project_heuristics.md" = @"
# project_heuristics.md — Self-Improvement Heuristics

> **This is the local self-improvement memory for this project.**
> Do not exceed 10 rules. If you learn something new, replace the least-used rule.
> Rules must be strictly actionable IF/THEN constraints based on past terminal failures.

## Learned Constraints

- IF running commands, THEN prioritize the project's specific conventions.
"@
}

Write-Host ""
foreach ($file in $stateFiles.Keys) {
    $filePath = Join-Path (Get-Location) $file
    if (-not (Test-Path $filePath)) {
        Set-Content -Path $filePath -Value $stateFiles[$file] -Encoding UTF8
        Write-Host "[OK] Created project-local $file" -ForegroundColor Green
    } else {
        Write-Host "[OK] $file already exists (kept as-is)" -ForegroundColor Cyan
    }
}

Write-Host ""
Write-Host "Antigravity OS linked successfully." -ForegroundColor Green
Write-Host "Run validation: python .agents\validate_agents.py" -ForegroundColor Cyan
