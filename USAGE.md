# Antigravity OS — Usage Guide

## 1. WHY AG-INIT WORKS
When you run `ag-init.ps1`, it creates a `.agents/` junction. 
The AI is hard-coded (via `GEMINI.md`) to look for `.agents/AGENTS.md`.
**Presence = Authority.** If the folder exists, the AI is FORCED into "OS Mode". It will automatically read Section 0 (Complexity Gate) before acting.

## 2. EFFECTIVE FOLDER USAGE
- **`agents/`**: Use `@reviewer` or `@planner` to switch modes.
- **`commands/`**: Use `/fix-issue` or `/ship-ui` to trigger industrial workflows.
- **`rules/`**: The AI auto-reads these during its "VERIFY" phase.
- **`skills/`**: The AI "Lazy Loads" these based on your task.

## 3. MASTER PROMPTS (THE "FORCE" PROMPTS)
Copy-paste these to force absolute compliance:

### Start of Project
> `@repo-analysis Analyze this project. Initialize STATE.md and task.md based on AGENTS.md Section 12.`

### Building Features
> `/build-feature Build [feature name]. Strictly follow PLANNING -> BUILD -> AUDIT phases in SYSTEM_ORCHESTRATION.md.`

### Strict UI Polish
> `/ship-ui [UI task]. Enforce rules/frontend.md. No prop-drilling. No hardcoded widths.`

### Code Review
> `@reviewer Review [file/PR]. Audit against all files in rules/ directory.`

## 4. PRO-TIP: THE "CONSTRAIN" PROMPT
If the AI gets lazy:
> `You are violating AGENTS.md Section 9 (Anti-Slop). Re-read Section 10 (Quality Standards) and rewrite.`

---
*Locked for Production. v2.1.*
