# Command: /execute-plan

## Purpose

Executes a previously approved `implementation_plan.md` phase-by-phase. Ensures discipline and prevents scope drift during the build.

---

## Execution Workflow

### Phase 1: Context Loading
1. Read `implementation_plan.md`.
2. Identify the first incomplete phase.
3. Verify that all prerequisites for this phase are met.

### Phase 2: Phased Execution
1. Perform the file edits and command runs specified in the current phase.
2. After each phase, perform the **Verification** steps listed in the plan.
3. Update `task.md` with progress.

### Phase 3: Transition
1. If the phase is complete and verified, proceed to the next phase.
2. If a blocking issue is found, stop and report to the user.
3. Upon final completion, trigger the **AUDIT** phase as defined in `SYSTEM_ORCHESTRATION.md`.

---

## Constraints
- Do not skip verification steps.
- Do not implement features not explicitly listed in the plan.
- Maintain state sync with `task.md` throughout.
