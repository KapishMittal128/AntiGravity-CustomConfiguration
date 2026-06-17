# Command: /orchestrate

## Purpose

A structured workflow for executing complex, multi-agent tasks that benefit from parallel dispatch. Use this when a goal can be decomposed into independent work units that should run concurrently rather than sequentially.

## When to Use

- A task spans 3+ independent files or systems with no shared state
- Multiple agent domains are involved (e.g., frontend + backend + research)
- The user explicitly requests parallel execution
- The Planner detects parallelizable work during decomposition
- A long-running process (build, test suite) should run in the background while other work continues

---

## Execution Workflow

### Phase 1: Decompose

1. Break the goal into the smallest independent work units
2. For each work unit, define:
   - **Objective**: What specific outcome is expected
   - **Agent**: Which execution agent owns this unit (frontend, backend, debugger, reviewer)
   - **Files**: Which files/directories this worker will touch
   - **Acceptance Criteria**: How to verify this unit is complete
3. Classify each work unit:
   - `PARALLEL` -- no shared files, no data dependencies, can run concurrently
   - `SEQUENTIAL` -- depends on output of another unit
   - `BACKGROUND` -- non-blocking, results needed later
4. Verify: no two PARALLEL units touch the same file. If they do, reclassify one as SEQUENTIAL.

**Output:** Numbered work unit list with classifications and file ownership

---

### Phase 2: Dispatch

1. Launch all PARALLEL units concurrently:
   - Terminal tasks: use `run_command` with `WaitMsBeforeAsync` set appropriately
   - Research tasks: use `browser_subagent` for web research
   - Analysis tasks: use `grep_search` and `view_file` in rapid succession
2. Launch BACKGROUND units and set a `schedule` timer for the expected completion window
3. Hold SEQUENTIAL units until their dependencies complete
4. Track each unit's status: DISPATCHED / RUNNING / COMPLETE / FAILED

**Output:** All workers dispatched with status tracking

---

### Phase 3: Monitor

1. Do NOT poll task status in a loop -- wait for system notifications or timer fires
2. When a worker completes, collect its output
3. If a worker fails:
   - Read the error output
   - Decide: retry (max 2 retries) or abort that unit and continue with others
4. Continue executing SEQUENTIAL units as their dependencies become available

**Output:** All workers complete (or failed with documented reasons)

---

### Phase 4: Synthesize

1. Merge all worker outputs into a single unified deliverable
2. Resolve any conflicts between worker outputs (e.g., two workers both modified a shared config)
3. Verify the merged result is internally consistent
4. Present the synthesized output to the user

**Output:** Unified deliverable combining all worker results

---

### Phase 5: Evaluate

**Stage 1 — Mechanical Verification (run before subjective review):**
1. Run type checker: `npx tsc --noEmit` (TypeScript) or equivalent — skip if not applicable
2. Run linter: `npm run lint` or `npx eslint .` (JS/TS), `python -m ruff check` (Python) — skip if not applicable
3. Run tests: `npm run test` or `python -m pytest` — skip if no test suite exists
4. If any mechanical check fails: fix the failure before proceeding to Stage 2

**Stage 2 — Reviewer Evaluation:**
1. Pass the synthesized output to the Reviewer agent in Evaluator Mode
2. The Reviewer checks against the original acceptance criteria
3. If PASS: deliver to user
4. If NEEDS_REVISION: route the specific failing component back to its execution agent
5. If FAIL: escalate to user with the Reviewer's findings
6. Maximum 3 evaluation iterations before hard stop

**Output:** Mechanically verified, evaluated final deliverable

---

### Phase 6: POST-MORTEM (Self-Improvement)

1. Review the terminal history for this session. Did we experience Terminal Thrashing (a command failing 2+ times before success)?
2. Did the user explicitly correct a behavior or reject an action?
3. If yes to either, extract the specific failure and the working fix.
4. Append it as a strict IF/THEN constraint to `./project_heuristics.md`.
5. If the heuristic is universally applicable across all projects, suggest the user run `/propose-os-upgrade`.

**Output:** Updated heuristics file (if learning occurred).

---

## Output Expectations

- A numbered list of work units with their dispatch classifications
- Status of each worker (completed / failed / retried)
- The synthesized final output
- Reviewer's evaluation verdict
- Any follow-up work flagged

---

## Constraints

- Maximum 4 concurrent background tasks
- No two parallel workers may touch the same file
- All workers must have defined acceptance criteria before dispatch
- SEQUENTIAL units must not be dispatched until their dependencies complete
- The Evaluator gate is mandatory -- no orchestrated output ships without review
