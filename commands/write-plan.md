# Command: /write-plan

## Purpose

Drafts a detailed, phased implementation plan for a non-trivial task. This is the mandatory entry point for any [STANDARD PATH] or [SECURITY PATH] work.

---

## Execution Workflow

### Phase 1: Requirement Analysis
1. Read the user request and existing code.
2. Identify all files that will be touched.
3. Identify any risky boundaries or breaking changes.

### Phase 2: Plan Generation
1. Write the plan into `implementation_plan.md` at the project root.
2. The plan must include:
   - **Goal:** One-sentence outcome.
   - **Acceptance Criteria:** What done looks like.
   - **Phases:** Discrete steps (Plan, Build, Audit, Ship).
   - **Verification:** Specific tests or checks for each phase.

### Phase 3: Review & Lock
1. Present the plan summary to the user.
2. **STOP.** Do not proceed to implementation until the user approves the plan.

---

## Constraints
- No code implementation during this phase.
- Use the `implementation_plan.md` template found in the OS root.
- If the task is trivial, the system may suggest [FAST PATH] instead.
