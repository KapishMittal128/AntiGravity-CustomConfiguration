# ANTIGRAVITY SYSTEM ORCHESTRATION

## 1. Purpose
This file governs the **meta-execution logic** of the Antigravity OS. It sits above `CAPABILITIES.md` to dictate multi-skill coordination, execution order, task handoffs, ambiguity handling, fallback routing, and conflict resolution. It transforms isolated skills into a coordinated, testable, and execution-safe operating system.

## 2. Single-Skill vs Multi-Skill Decision Rule
Antigravity must deterministically decide whether to execute a single skill or break the prompt into multiple sequential sub-tasks.
*   **Use single-skill execution when:** The prompt targets a narrow, bounded domain (e.g., "Refactor this auth class," "Apply Framer Motion attributes to this button," "Review this webhook for race conditions").
*   **Use multi-skill implementation (Decompose) when:** The prompt spans multiple domains, phases, or technologies (e.g., "Build a SaaS dashboard," "Clone this UI and wire it to my database," "Optimize performance and harden the API").

## 3. Task Decomposition Protocol
When a large prompt is received, Antigravity must break it into discrete sub-problems. For each sub-task, define:
1.  **Objective:** What specific asset or logic is being produced.
2.  **Required Skill:** Strictly selected from `CAPABILITIES.md`.
3.  **Order of Execution:** Based on Phase Sequencing Rules.
4.  **Handoff Check:** Whether completion requires stopping and resetting context for the next skill.

*Mandatory behavior:* Complex builds must NEVER be forced through a single skill (e.g., do not use `ui-design-expert` to handle backend configuration just because it's convenient).

## 4. Skill Handoff Rules
One skill must explicitly STOP and hand off context to the next skill when moving across domain boundaries.
*   `repo-analysis` **STOPS** after extracting the layout blueprint and layout tokens. It MUST hand off to `ui-design-expert` for React prop writing.
*   `ui-design-expert` **STOPS** at the edge of the framework router. It MUST hand off to `backend-dev-guidelines` (or equivalent) for server components/routing logic.
*   `spec-driven-build` **STOPS** after architectural approval and component planning. It MUST hand off to execution modules like `backend-dev-guidelines`.
*   `repo-analysis` **STOPS** after producing a reasoning/audit report on pre-existing code. It MUST hand off to an implementation skill if the user approves changes.

## 5. Conflict Resolution Rules
When multiple skills appear relevant, Antigravity resolves the conflict strictly using functional-risk priorities:
1.  **Security/Scale Overrides Stack:** `backend-dev-guidelines` absolutely overrides generic implementation skills for tasks involving money, auth, webhooks, or high-throughput concurrency.
2.  **Specialized Overrides Generic:** `ui-design-expert` handles all core frontend and animation requests. `api-design-principles` handles all external data ingestion endpoints.
3.  **Master vs. Atomic Selection:**
    *   **Master Skills** (`ui-design-expert`, `backend-dev-guidelines`) MUST be used for the primary implementation of a feature.
    *   **Atomic Skills:** Use specific sub-skills (e.g., `remotion-*` for video) only when the master skill requires granular domain-specific execution.
    *   **Contextual Overlap:** If specialized logic is needed for a specific deliverable (e.g., PDF or PPTX), prioritize the dedicated conversion skills over generic UI skills.
4.  **Decomposition Overrides Monolith:** If the request requires both a framework-specific feature (Next.js server action) and a complex UI update, DO NOT overlap. Split the task and run sequentially.

## 6. Fallback Escalation Rules
If a prompt is incomplete, overly broad, multi-intent, or doesn't map to a clear skill mapping:
1.  **Level 1 Escalation:** Trigger `repo-analysis` if the user says "Make this app better" or "Fix this codebase" where there is existing code.
2.  **Level 2 Escalation:** Trigger `repo-analysis` if the user wants wide-sweeping system changes without defining where to start.
3.  **Level 3 Escalation:** Trigger `spec-driven-build` if the user asks to build an entirely new nebulous concept (e.g., "Build an Uber clone").
*Never guess and start mutating code under ambiguous conditions.*

## 7. Phase Sequencing Rules
Antigravity must sequence work strictly across the following operational phases in order:
1.  **PLANNING:** `repo-analysis`, `spec-driven-build`, `api-design-principles`. MUST occur before implementation.
2.  **BUILD:** `backend-dev-guidelines`, `ui-design-expert`. Actual file mutation phase.
3.  **AUDIT:** `repo-analysis`. MUST occur after BUILD but before SHIP.
4.  **SHIP:** `backend-dev-guidelines`.

## 8. "Stop Conditions" & Runtime Discipline
While this document defines *when* skills stop naturally, the **physical enforcement** of cycle limits and context boundaries is governed by the global RUNTIME_CONTROL logic.
- `SYSTEM_ORCHESTRATION.md` decides the logic of the stop (e.g., "Stopping because the React node tree is assembled").
- Global execution rules decide the system response (e.g., "Yielding to user for a clean context window because we hit a checkpoint").

To prevent bleeding, explicit Stop Conditions are enforced across major clusters:
*   **Security/Audit:** Stops immediately upon rendering a Markdown threat model/audit report. Cannot edit application logic directly within the same step.
*   **Frontend Design:** Stops when the React node tree and prop logic are assembled. Cannot touch page routers (`layout.tsx`/`page.tsx`).
*   **Architecture Analysis:** Stops when the implementation plan (`spec.md`) is approved by the user. Cannot touch source files.
*   **Visual Cloning:** Stops immediately when CSS/Tailwind layouts match the reference structure visually. Cannot hook up live data fetching.

## 9. Common Multi-Skill Execution Patterns
Reusable orchestration sequences for Antigravity:

### A. Website Clone Flow
1. `repo-analysis` (Blueprint extraction)
2. `ui-design-expert` (Component creation, Token & styling application, Interaction loops)
3. `backend-dev-guidelines` (Integration)

### B. SaaS Feature Build Flow
1. `repo-analysis` (System mapping)
2. `spec-driven-build` (Feature spec)
3. `api-design-principles` (Service contract)
4. `backend-dev-guidelines` (Core implementation)
5. `ui-design-expert` (Component UI)

### C. Backend API Launch Flow
1. `api-design-principles` (REST/GraphQL schema)
2. `spec-driven-build` (Model schemas)
3. `backend-dev-guidelines` (Service handlers, CI/CD / IaC)

### D. Legacy Code Repair Flow
1. `repo-analysis` (Context map, Dead code elimination)
2. `backend-dev-guidelines` (Targeted repair, Regression validation)

### E. ML Product Build Flow
1. `spec-driven-build` (Resource allocation plan, Model/Data validation)
2. `backend-dev-guidelines` (Pipeline execution)
3. `ui-design-expert` (User input wiring)

## 10. Global Execution Protocol (MANDATORY GATE)
Before generating ANY output based on a skill module, the OS MUST run this exact sequence internally:
1. **TIER CHECK:** Identify the active skill's Tier classification (1, 2, or 3).
2. **CONSTRAINT APPLICATION:** Read the "Hard Usage Rules" for that specific skill in its SKILL.md. If the current task violates a FORBIDDEN clause, **ABORT** and switch skills.
3. **VALIDATION GATING:**
   - If **Tier 1**: Execute normally.
   - If **Tier 2**: Run the output through the "Patched Failure Prevention Rules" logic block internally. If it fails, auto-correct or **REJECT**.
   - If **Tier 3**: Execute the "New Strategy" Redesign. Never use legacy logic.
4. **DELIVERY:** Only stream output if steps 1-3 pass flawlessly.

*Any failure in this sequence results in a hard stop, protecting the workspace from architectural drift and destructive code execution.*
