$ErrorActionPreference = "Stop"

$staged = git diff --cached --name-only

if ($staged | Select-String -Pattern '^(src/|app/|lib/|components/)' -Quiet) {
    if (-not ($staged | Select-String -Pattern '(task\.md|STATE\.md)' -Quiet)) {
        Write-Output "[ANTIGRAVITY OS HALT] State Out of Sync!"
        Write-Output "You are committing code without synchronizing task.md or STATE.md."
        Write-Output "Run the agent to dump memory or update task.md manually before committing."
        Write-Output "Do not bypass the hook. Update task.md or STATE.md before retrying."
        exit 1
    }
}

$changedFiles = @($staged).Count
if ($changedFiles -gt 20) {
    Write-Output "[ANTIGRAVITY OS WARNING] Mega Task Detected! ($changedFiles files changed)"
    Write-Output "Executing overly large execution cycles degrades intelligence and context."
    Write-Output "Consider breaking tasks into smaller atomic commits."
}

exit 0
