# Command: /orchestrate

## Purpose
A structured workflow for complex, multi-agent tasks that benefit from parallel dispatch. Use when a goal can be decomposed into independent work units that run concurrently rather than sequentially.

---

## Applicability
Requires agent runtimes exposing: `run_command` (async), `browser_subagent`, `grep_search`, `view_file`, and a scheduler (`schedule`/`sleep`). Otherwise use the **Sequential Fallback** at the bottom.

---

## When to Use
- Task spans 3+ independent files or systems with no shared state
- Multiple agent domains involved (e.g., frontend + backend + research)
- User explicitly requests parallel execution
- Planner detects parallelizable work during decomposition
- A long-running process (build, test suite) should run in background while other work continues

---

## Phase 1: Decompose

### 1.1 — Define work units
For each unit define: **ID** (slug), **Objective**, **Agent** (`frontend`/`backend`/`debugger`/`reviewer`/`research`), **Files** (exact paths), **Acceptance Criteria** (testable, not vague), **Dependencies** (unit IDs or empty).

**Example:**
| ID | Agent | Files | Acceptance Criteria | Deps |
|---|---|---|---|---|
| `api-oauth` | backend | `src/auth/oauth.ts` | `/auth/google` redirects, token exchanged, session created | — |
| `fe-avatar` | frontend | `src/components/Avatar.tsx` | Renders with fallback initials, accepts `imageUrl` prop | — |
| `db-schema` | backend | `migrations/004_avatar.sql` | Migration runs, column present in schema | — |
| `fe-wire` | frontend | `src/components/Header.tsx` | Avatar displays logged-in user photo | `api-oauth`, `fe-avatar`, `db-schema` |

### 1.2 — Classify
- `PARALLEL` — no shared files, no data dependencies, run now
- `SEQUENTIAL` — depends on another unit's output; blocked until complete
- `BACKGROUND` — non-blocking; results needed before Phase 4 only

### 1.3 — File-ownership verification
Build a table mapping every file to exactly one unit. If two PARALLEL/BACKGROUND units claim the same file: reclassify the consumer as SEQUENTIAL, or if both modify independently, add a SEQUENTIAL merge unit after both complete.

**No two PARALLEL or BACKGROUND units may own the same file. Absolute.**

### 1.4 — Concurrent task cap
If PARALLEL + BACKGROUND count exceeds **4**, promote lowest-priority units to SEQUENTIAL. Cap exists because beyond 4, context-window pressure and tool-call interleaving increase failure rates.

**Output:** Work unit list with IDs, classifications, file ownership table, acceptance criteria.

---

## Phase 2: Dispatch

### 2.1 — Pre-dispatch checklist (mandatory)
- [ ] Every unit has explicit, testable acceptance criteria
- [ ] No two PARALLEL/BACKGROUND units share a file
- [ ] SEQUENTIAL units are NOT in the dispatch queue
- [ ] Concurrent count ≤ 4
- [ ] Required environment primitives confirmed available

Resolve all failures before proceeding. No partial launches.

### 2.2 — Launch PARALLEL units
- Terminal: `run_command` with `WaitMsBeforeAsync` tuned to task (200 ms scripts / 2000 ms builds)
- Research: `browser_subagent` with enumerated specific questions, not just a topic
- Analysis: `grep_search` + `view_file` in rapid succession
- Record dispatch timestamp per unit in status registry

### 2.3 — Launch BACKGROUND units
Same tool rules as 2.2. Set `schedule` timer for expected completion. Record timer ID in registry.

### 2.4 — Stage SEQUENTIAL units
Do not launch. Place in staged queue with dependency IDs. Dispatch only when all dependencies reach COMPLETE.

### 2.5 — Status registry
```
DISPATCHED → RUNNING → COMPLETE | FAILED | BLOCKED
```
Log every transition with timestamp. Registry is single source of truth.

**Example mid-run:**
```
api-oauth  COMPLETE  10:00:43  validation=PASS
fe-avatar  COMPLETE  10:00:38  validation=PASS
db-schema  RUNNING   dispatched=10:00:01
fe-wire    STAGED    waiting_on=[api-oauth, fe-avatar, db-schema]
```

**Output:** Workers dispatched with timestamps; registry initialized; SEQUENTIAL units staged.

---

## Phase 3: Monitor and Progress Sequential Units

### 3.1 — Do not poll
Wait for notifications or timer fires. Polling wastes context and creates timing-dependent failures.

### 3.2 — On completion
1. Mark COMPLETE with timestamp
2. Collect output
3. Run local acceptance criteria validation immediately (3.4)
4. Check staged queue — dispatch any SEQUENTIAL unit whose dependencies are all COMPLETE

### 3.3 — On failure
Read full error output before classifying.

| Type | Examples | Response |
|---|---|---|
| **Transient** | Network timeout, flaky test | Exponential backoff: 2 s then 8 s. Max 2 retries. |
| **Config error** | Missing env var, wrong path | Fix root cause first, then retry. Never retry same misconfigured command. |
| **Logic error** | Wrong output, failed assertion | No retry. Mark FAILED, document, flag for Phase 5. |

If FAILED unit is a dependency of SEQUENTIAL units → mark those BLOCKED, escalate to user. Never silently skip.

**Example registry failure entry:**
```
db-schema  FAILED  error="relation 'users' does not exist — wrong DB targeted"
           type=Config  retries=0  action=Fix DATABASE_URL then retry
fe-wire    BLOCKED  waiting_on=[db-schema]  escalated=true
```

### 3.4 — Local acceptance criteria validation (mandatory, per unit)
Validate output against unit's acceptance criteria before synthesis or unblocking dependents. If unmet → treat as FAILED, apply 3.3. A unit with unmet criteria must never unblock SEQUENTIAL units or enter synthesis.

**Output:** All workers COMPLETE/FAILED with reasons; local validation done per unit; SEQUENTIAL units progressed.

---

## Phase 4: Synthesize

### 4.1 — Collect outputs
- **Critical path FAILED unit:** halt synthesis for affected scope, escalate to user
- **Non-critical FAILED unit:** document as explicit omission. Never silently skip.

### 4.2 — Conflict resolution protocol
1. **No overlap** → assemble directly
2. **Additive overlap** (no line collision) → apply both, verify compiles/parses
3. **Destructive overlap** (same lines differ) → diff against baseline, apply higher-priority change, annotate lower-priority as TODO with unit ID, log decision with reasoning
4. **Schema/interface conflict** → BLOCK consuming worker, re-run against new contract before synthesis

If step 3 or 4 cannot be resolved algorithmically → stop, show user a diff of both versions. Do not guess.

**Example conflict log:**
```
CONFLICT: Header.tsx
  fe-avatar: added <Avatar /> import line 3
  fe-wire:   added <Avatar /> import line 3 + wired user prop line 21
  resolution: applied fe-wire (superset — no information lost)
```

### 4.3 — Internal consistency check
- All imports and cross-unit references resolve
- No dead references (called but never produced)
- No duplicate definitions (same symbol, route, or schema field)
- All files from Phase 1 ownership table accounted for

**Output:** Unified deliverable; conflict log; consistency verified.

---

## Phase 5: Evaluate

### Stage 1 — Mechanical Verification
Run all applicable checks. Skip only if genuinely not applicable (no TypeScript = skip tsc). Never skip for speed.

| Check | Command |
|---|---|
| TypeScript | `npx tsc --noEmit` |
| JS/TS lint | `npm run lint` or `npx eslint .` |
| Python lint | `python -m ruff check` |
| Python types | `python -m mypy .` |
| Tests | `npm run test` or `python -m pytest` |
| Build | `npm run build` |

On failure: fix, re-run affected worker if needed, re-synthesize scope, re-run all Stage 1 checks from scratch before Stage 2.

### Stage 2 — Reviewer Evaluation
Pass to Reviewer agent with: original goal, all unit IDs + acceptance criteria, conflict log, FAILED/BLOCKED unit reasons.

| Verdict | Action |
|---|---|
| **PASS** | Deliver to user |
| **NEEDS_REVISION** | Return failing unit to its agent → fix → re-run Stage 1 + Stage 2 for that scope only |
| **FAIL** | Escalate to user with full Reviewer findings. Do not deliver. |

**Max 3 iterations.** After 3 without PASS → stop, deliver findings + current state, request user guidance.

**Output:** Verified, Reviewer-approved deliverable — or documented escalation.

---

## Phase 6: Post-Mortem (Self-Improvement)
Run after every session regardless of outcome.

### 6.1 — Terminal thrashing audit
Flag any command that failed 2+ times before succeeding. Note what failed and what fixed it.

### 6.2 — Behavioral corrections audit
Flag: user corrections, outputs that failed local validation on first attempt, conflicts requiring user escalation, SEQUENTIAL units blocked by dependency failure.

### 6.3 — Extract and record
For each flagged item: state failure precisely → state working fix → express as IF/THEN constraint.

**Example:**
```
IF npm run build fails with "Cannot find module 'dotenv'"
THEN run npm install before retrying — node_modules missing or stale
```

Append to `./project_heuristics.md`. Never overwrite existing constraints.

### 6.4 — Promote universal heuristics
If a constraint applies across all projects, suggest user run `/propose-os-upgrade`.

**Output:** Updated `./project_heuristics.md` (if learning occurred).

---

## Sequential Fallback
Use when async primitives unavailable or task has ≤ 2 units.

1. Execute units in dependency order, one at a time
2. Local acceptance validation after each unit (Phase 3.4)
3. Conflict resolution after any overlapping unit (Phase 4.2)
4. Run Phase 5 once after all units complete
5. Run Phase 6 post-mortem

---

## Output Expectations
Every run produces:
- Work unit list: IDs, classifications, file ownership table, acceptance criteria
- Dispatch log with timestamps
- Per-unit local validation results (PASS/FAIL + criteria checked)
- Worker status log (COMPLETE/FAILED/BLOCKED) with retry history
- Synthesized deliverable with conflict log
- Reviewer verdict and iteration count
- Updated `./project_heuristics.md` (if applicable)
- Any unresolved escalations with current state

---

## Constraints Reference

| Constraint | Value | Rationale |
|---|---|---|
| Max concurrent tasks | 4 | Limits context pressure and interleaving failures |
| Max retries per worker | 2 | Forces root-cause analysis over blind retries |
| Max evaluation iterations | 3 | Forces escalation over indefinite revision |
| Parallel file exclusivity | Absolute | Eliminates race conditions and merge ambiguity |
| Pre-dispatch checklist | Mandatory | Catches config errors before wasting compute |
| Local acceptance validation | Per-unit, immediate | Catches failures at source not global review |
| Conflict escalation | On unresolvable overlap | Never guess on destructive merge |
| BLOCKED escalation | Mandatory | Never silently skip blocked work |
