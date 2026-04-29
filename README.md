# Antigravity OS — Kernel v2.1 (Locked)

Global execution system for high-end software engineering.

## 1. GLOBAL INSTALLATION
OS lives at `C:\Users\Kapish\.antigravity\.agents`. 
Apply to any project via Master Initializer:
```powershell
powershell -ExecutionPolicy Bypass -File C:\Users\Kapish\.antigravity\ag-init.ps1
```
This links:
- `.agents/` -> Kernel logic, rules, and commands.
- `agents/` -> Persona discovery for UI mentions (@reviewer, etc).
- Seeds local `STATE.md` and `task.md`.

## 2. SYSTEM HIERARCHY (The Authority)
1. `AGENTS.md` - Master policy & routing.
2. `skills/CAPABILITIES.md` - 17 Master Skills registry.
3. `skills/SYSTEM_ORCHESTRATION.md` - Workflow logic.
4. `skills/RUNTIME_CONTROL.md` - State & Fatigue.

## 3. COMPLEXITY GATE
Every request follows Section 0:
- **Trivial?** -> Fast Path (Direct execution).
- **Complex?** -> Full Workflow (Planning -> Build -> Audit -> Ship).

## 4. COMMAND TIERS
- **Tier 1:** Auto-run (Reads, Tests, Lint).
- **Tier 2:** Propose (Installs, Commits).
- **Tier 3:** High-Impact (Migrations).
- **Tier 4:** BLOCKED (rm -rf, force push, cat .env).

## 5. REPOSITORY SKILLS (17 Master Skills)
- `repo-analysis`, `backend-dev-guidelines`, `ui-design-expert`, `api-design-principles`, `caveman-mode`, etc.
- See `CAPABILITIES.md` for full list.

## 6. PROJECT MEMORY
- `STATE.md`: Long-term tech decisions.
- `task.md`: Current session progress.
Files stay local to project root. Never leaked.

---
*Locked for Production. No Drift Allowed.*
