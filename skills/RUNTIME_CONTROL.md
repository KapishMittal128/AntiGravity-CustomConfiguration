# RUNTIME CONTROL

This is the single authoritative source for Antigravity OS execution logic.

## 1. SESSION ARCHITECTURE (STATE VS. TASK)
The OS manages memory across two distinct layers:
- **`STATE.md` (STRATEGIC TRUTH):** Architecture diagrams, durable tech decisions, schema definitions. ONLY update after a Phase completion.
- **`task.md` (TACTICAL EXECUTION):** To-do list, current context, immediate bugs. Updated continuously during a Session.

## 2. HARD CHECKPOINT LAWS
To prevent "Agentic Drift," you MUST follow these stop conditions:
- **Phase Transitions:** You MUST stop and request user approval after any `PLANNING` phase before entering `BUILD`.
- **Unit Completion:** After completing a cluster of file edits, you MUST run a validation command before proceeding to the next task item.
- **Session Reset:** If the `task.md` exceeds 10 items or the context window feels saturated, you MUST summarize progress to `STATE.md` and request a session reset.

## 3. COMPLEXITY GATE ENFORCEMENT
- **[FAST PATH]:** Single-file fixes, UI tweaks, or documentation. (Trigger: Skip Planning, proceed directly to `BUILD`).
- **[STANDARD PATH]:** Logic changes, new endpoints, or structural refactors. (Trigger: Mandatory `PLANNING` -> `IMPLEMENTATION_PLAN` -> `BUILD`).
- **[SECURITY PATH]:** Database migrations, security patches, or high-risk infra. (Trigger: Mandatory `RED_TEAMING` and `AUDIT` phases).

## 4. PHASE LOCKOUTS
- No code mutation allowed during `PLANNING`.
- No new file creation allowed during `AUDIT`.
- No architectural changes allowed during `BUILD` without a Plan revision.

## 5. TOKEN FATIGUE MITIGATION
- **Rule:** If the conversation length exceeds 5,000 tokens, the agent MUST summarize the "Current Frontier" (what we are doing right now) and move it to the top of `task.md`.
- **Action:** Truncate irrelevant thought history once the "Frontier" is established in memory.
