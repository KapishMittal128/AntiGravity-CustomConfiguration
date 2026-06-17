<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0D0D0D,50:6D28D9,100:EC4899&height=220&section=header&text=DAWG%20OS&fontSize=70&fontColor=FFFFFF&animation=fadeIn&fontAlignY=35&desc=The%20AI%20Execution%20Kernel&descSize=18&descAlignY=55&descAlign=50" width="100%" />

<br/>

<img src="https://img.shields.io/badge/Full--Stack_Architecture-Ship_Frontend_%26_Backend-6D28D9?style=for-the-badge&logo=vercel&logoColor=white" />
<img src="https://img.shields.io/badge/AI%2FRAG_Pipelines-Vector_Search_%26_Embeddings-EC4899?style=for-the-badge&logo=openai&logoColor=white" />
<img src="https://img.shields.io/badge/Production_Databases-Postgres_%7C_Prisma_%7C_Drizzle-10B981?style=for-the-badge&logo=postgresql&logoColor=white" />
<br/>
<img src="https://img.shields.io/badge/3D_%26_Motion-Three.js_%7C_GSAP_%7C_Framer-3B82F6?style=for-the-badge&logo=threedotjs&logoColor=white" />
<img src="https://img.shields.io/badge/CI%2FCD_%26_DevOps-Docker_%7C_Vercel_%7C_Railway-F59E0B?style=for-the-badge&logo=docker&logoColor=white" />
<img src="https://img.shields.io/badge/39_Loaded_Skills-Lazy--Load_On_Demand-059669?style=for-the-badge&logo=stackblitz&logoColor=white" />

<br/><br/>

<samp>
<b>Turn any language model into a disciplined software build system.</b>
<br/>
Awwwards-caliber frontends. Production-grade backends. AI/RAG pipelines. Zero slop.
</samp>

<br/><br/>

<kbd>&nbsp; PLANNING &nbsp;</kbd>&nbsp;&nbsp;&#9654;&nbsp;&nbsp;<kbd>&nbsp; BUILD &nbsp;</kbd>&nbsp;&nbsp;&#9654;&nbsp;&nbsp;<kbd>&nbsp; EVALUATE &nbsp;</kbd>&nbsp;&nbsp;&#9654;&nbsp;&nbsp;<kbd>&nbsp; AUDIT &nbsp;</kbd>&nbsp;&nbsp;&#9654;&nbsp;&nbsp;<kbd>&nbsp; SHIP &nbsp;</kbd>

</div>

<br/>

---

## Table of Contents

- [Quickstart](#quickstart)
- [How the System Works](#how-the-system-works)
- [The Complexity Gate](#the-complexity-gate)
- [Agents](#agents)
- [Orchestrator Mode (Parallel Dispatch)](#orchestrator-mode-parallel-dispatch)
- [Evaluator Mode (Auto-Quality Gate)](#evaluator-mode-auto-quality-gate)
- [Commands & Slash Bridge](#commands--slash-bridge)
- [Command Safety Tiers](#command-safety-tiers)
- [Phase Pipeline (EVALUATE with Mechanical Verification)](#phase-pipeline)
- [Skill Library (39 Skills)](#skill-library)
- [State Files & Session Continuity](#state-files--session-continuity)
- [Rule Enforcement](#rule-enforcement)
- [Directory Structure](#directory-structure)
- [The Prompt Formula](#the-prompt-formula)
- [Cost Control](#cost-control)
- [Complete LLM Reference (Paste-Ready)](#complete-llm-reference)

---

## Quickstart

```powershell
# 1. Clone the global OS kernel
git clone https://github.com/KapishMittal128/AntiGravity-CustomConfiguration.git $HOME\.antigravity\.agents

# 2. Link it into any project
cd C:\path\to\your\project
powershell -ExecutionPolicy Bypass -File $HOME\.antigravity\.agents\scripts\ag-init.ps1

# 3. Start prompting
@frontend /build-feature Build a responsive dashboard with dark mode toggle
```

`scripts/ag-init.ps1` creates two directory junctions (`.agents/` → global OS kernel, `agents/` → agent persona files for IDE discovery) and scaffolds three project-local state files (`STATE.md`, `task.md`, `project_heuristics.md`). Every project links to the same global OS, so updates to the kernel are instantly live everywhere.

---

## How the System Works

DAWG OS is a prompt-engineering architecture that sits inside an AI coding IDE (Gemini CLI, Cursor, Windsurf, etc.) and controls how the AI reasons about tasks. It is **not** a runtime, a framework, or a separate process. It is a structured set of markdown files that the AI reads and follows.

The core loop:
1. Every request hits the **Complexity Gate** — is this trivial or complex?
2. Trivial → **Fast Path** (execute directly, zero overhead)
3. Complex → **Full Workflow** (select agent → load skills → phase execution → evaluate → ship)
4. The AI reads agent files, skill files, and rule files **on demand** — never all at once

The system works because modern LLMs (Claude, Gemini, GPT) are strong instruction-followers. The markdown files constrain and guide the AI's behavior. This is advisory, not mechanical — but the consistency improvement over raw prompting is significant (~2-3x).

---

## The Complexity Gate

This runs first, every time, before any work begins.

```
Three questions:
1. Is this a single file, single location, zero architectural impact?
2. Is it one focused pass, under ~15 minutes?
3. Is the outcome completely unambiguous?

ALL THREE yes → FAST PATH (no agents, no skills, just execute)
ANY no → check for risk conditions:
  - Deletes/renames existing functionality?
  - Changes a shared interface?
  - Modifies data models, schemas, migrations?
  - Has security implications?
  - Approach is genuinely ambiguous?

  NO risk conditions → FAST PATH (don't invent complexity)
  ANY risk condition → FULL WORKFLOW
```

**Fast Path (DirectOps)**: No agent selection, no skill loading, no phase workflow. Read the request, execute it, deliver the result. This handles ~80% of daily work.

**Full Workflow**: Agent is selected from the routing table. Skills are lazy-loaded (max 2 for simple, 3 for complex). Execution follows the phase pipeline: `PLANNING → BUILD → EVALUATE → AUDIT → SHIP`.

---

## Agents

Six specialized agents. One active at a time. Each is a markdown file at `.agents/agents/<name>.md` that the AI reads when activating that persona.

| Agent | Role | Activates When |
|-------|------|----------------|
| **@planner** | Decompose goals, make architecture decisions, orchestrate parallel work | Scope unclear, multiple steps, multi-agent task |
| **@debugger** | Root-cause analysis, log parsing, regression tracing | Something is broken or behaving unexpectedly |
| **@frontend** | Visual hierarchy, motion/WebGL, responsive layout, UI polish | UI, layout, page, component, CSS |
| **@backend** | APIs, auth, data pipelines, security, database work | Service logic, data access, backend infrastructure |
| **@ai-engineer** | Embeddings, RAG pipelines, prompt systems, vector search | LLM integration, AI features |
| **@reviewer** | Code audit, PR-style review, quality verdicts | Code critique, quality audit, post-BUILD evaluation |

**Routing rule**: Never activate two agents simultaneously for overlapping scope. Sequence them. Read an agent file only when first activating it — don't pre-load all six.

---

## Orchestrator Mode (Parallel Dispatch)

The Planner has two modes:
- **Plan Mode**: Standard task decomposition for sequential execution through a single agent
- **Orchestrator Mode**: Activated when a task has **2+ independent work units with no shared state**

### How Orchestrator Mode Works

```
User: "Audit the frontend accessibility, run backend tests, and check for SQL injection"

PLANNER classifies each sub-task:
  ├── Worker 1: "Lint frontend for a11y"    → PARALLEL (no shared files)
  ├── Worker 2: "Run backend test suite"    → PARALLEL (no shared files)  
  └── Worker 3: "Grep for SQL injection"    → PARALLEL (no shared files)

PLANNER dispatches all three as background terminal commands
PLANNER sets a timer to check completion
PLANNER collects results and synthesizes into a single audit report
PLANNER passes merged output through the EVALUATE phase
```

### Dispatch Types

| Type | Definition | How It Runs |
|------|-----------|-------------|
| `PARALLEL` | No shared files, independent outcome | Background terminal processes run concurrently |
| `SEQUENTIAL` | Depends on a prior task's output | Executed in order, output passed forward |
| `BACKGROUND` | Non-blocking, results needed later | Async with a timer to check completion |

### Constraints
- Maximum 4 concurrent background tasks
- No two parallel workers may touch the same file (reclassify as SEQUENTIAL if they do)
- All workers must have defined acceptance criteria before dispatch
- The Evaluator gate is mandatory — no orchestrated output ships without review

### What Is Actually Parallel (Honest)
**Parallel**: Terminal commands (tests, builds, lints), browser research tasks. These are real OS-level concurrent processes.
**NOT parallel**: LLM reasoning. There is one AI brain. It dispatches dumb workers and synthesizes their results. It cannot spawn five independent copies of itself.

---

## Evaluator Mode (Auto-Quality Gate)

After BUILD completes, the Reviewer automatically activates in **Evaluator Mode** — a structured pass/fail assessment, not a free-form review.

### Two-Stage Evaluation

**Stage 1 — Mechanical Verification (mandatory, runs first):**
1. Type checker: `npx tsc --noEmit` (TypeScript) or equivalent
2. Linter: `npm run lint` or `npx eslint .` (JS/TS), `python -m ruff check` (Python)
3. Tests: `npm run test` or `python -m pytest` (if test suite exists)
4. If any check fails → fix before proceeding to Stage 2

**Stage 2 — Reviewer Evaluation:**
The Reviewer receives the output + the original acceptance criteria and returns one of:
- **PASS** — All criteria met. Ship it.
- **NEEDS_REVISION** — Partially correct. Returns which criteria failed, what needs to change, and which agent should fix it.
- **FAIL** — Fundamentally wrong or dangerous. Returns root cause and whether it's a scope problem (needs replanning) or execution problem (needs rebuild).

Maximum 3 retry iterations before escalating to the user.

---

## Commands & Slash Bridge

Type a slash command at the start of your prompt to trigger a structured workflow. Each command maps to a file at `.agents/workflows/<name>.md`.

| Command | Action | Phase Flow |
|:--------|:-------|:-----------|
| `/build-feature` | New feature, endpoint, or page | `PLAN → BUILD → EVALUATE → AUDIT → SHIP` |
| `/fix-issue` | Bug diagnosis and fix | `DIAGNOSE → FIX → VERIFY` |
| `/review-code` | Code quality audit | `SCAN → REPORT → RECOMMENDATIONS` |
| `/refactor` | Clean up, simplify, restructure | `ANALYZE → REFACTOR → VERIFY` |
| `/ship-ui` | Polish UI to production quality | `AUDIT → POLISH → SHIP` |
| `/research` | Tech decision, library comparison | `GATHER → ANALYZE → RECOMMEND` |
| `/orchestrate` | Parallel multi-agent execution | `DECOMPOSE → DISPATCH → MONITOR → SYNTHESIZE → EVALUATE` |
| `/brainstorm` | Creative ideation session | Interactive |
| `/write-plan` | Draft an implementation plan | `RESEARCH → PLAN → REVIEW` |
| `/execute-plan` | Execute an approved plan | `LOAD → BUILD → VERIFY` |
| `/caveman` | Terse output mode (~75% fewer tokens) | Immediate |

**Execution rules:**
1. The AI MUST read the workflow file before executing — never from memory
2. The Complexity Gate runs on the task BEFORE loading the workflow
3. If the task is Fast Path, the slash command is just a routing hint — execute directly
4. If Full Workflow, follow the workflow file's phases exactly
5. Non-slash prompts are unaffected

---

## Command Safety Tiers

Every terminal command follows this protocol. No exceptions.

### Tier 1 — Auto-Execute (safe reads)
```
git status / diff / log / branch / stash
npm run lint / test / build / typecheck / dev
npx tsc --noEmit / eslint / prettier --check / jest / vitest
npx prisma migrate status
python -m pytest / ruff check
```

### Tier 2 — Propose First (state changes)
```
npm install / pip install
npx prisma migrate dev
git commit / git add
```
State the exact command + reason. Wait for user approval.

### Tier 3 — Explicit Approval Required (high impact)
```
Any command that modifies git history
Any migration on production
Any file removal outside the project
Any external network request
```

### Tier 4 — Permanently Blocked (never run)
```
cat .env / cat .env.* / cat secrets/**
rm -rf / rm -r
git push --force / git push -f
git reset --hard HEAD~
curl * | bash / wget * | bash
npx prisma migrate reset
DROP TABLE / DELETE FROM * WHERE 1
chmod 777
```
No justification overrides a Tier 4 block.

---

## Phase Pipeline

The Full Workflow executes in this exact order:

```
PLANNING → BUILD → EVALUATE → AUDIT → SHIP

PLANNING: Decompose the task, research, write specs, define acceptance criteria
    │
    v
BUILD: Write code, create/modify files, actual implementation
    │
    v
EVALUATE (two-stage):
    ├── Stage 1: Mechanical verification (tsc, lint, tests) — MUST pass
    └── Stage 2: Reviewer in Evaluator Mode (PASS/FAIL/NEEDS_REVISION)
        └── If FAIL/NEEDS_REVISION → route back to BUILD (max 3 retries)
    │
    v
AUDIT: Run repo-analysis, testing/QA, regression checks
    │
    v
SHIP: Deploy, deliver, final documentation
```

The EVALUATE phase is the key difference from naive "generate code and ship it." Mechanical checks catch type errors, lint violations, and test failures. The Reviewer catches logic errors and missed acceptance criteria. Together they prevent the most common failure mode: shipping code that looks right but doesn't work.

---

## Skill Library

**39 production-grade skills**, lazy-loaded on demand. Budget: **0** for trivial / **2** for simple / **3** max for complex.

Each skill is a markdown file at `.agents/skills/<name>/SKILL.md` with structured sections: Purpose, When to Use, Phases, Behavior Rules, Output Format.

### Frontend and Motion — 15 skills

| Skill | Use When |
|:------|:---------|
| `ui-design-expert` | Building any web component, page, or interactive application |
| `frontend-architecture-patterns` | Determining macro-level layout for landing pages, SaaS apps |
| `nextjs-app-router-patterns` | Structuring any Next.js 14+ project |
| `advanced-responsive-patterns` | Building layouts that must work across all devices |
| `framer-motion-patterns` | Building entrance, exit, stagger, or gesture animations |
| `gsap-scroll-patterns` | Building scroll-driven animations, section pinning, parallax |
| `threejs-r3f-fundamentals` | Building 3D heroes, product showcases, interactive WebGL |
| `webgl-shader-basics` | Building custom visual effects beyond standard Three.js materials |
| `microinteractions` | Designing tactile feedback, spring animations, confetti, hover effects |
| `motion-accessibility` | Auditing WCAG 2.2 AA motion compliance, reduced-motion handling |
| `ecc-design-critique` | Auditing layout hierarchy, typography contrast, section rhythm |
| `ecc-taste-dials` | Calibrating composition symmetry, spacing density, animation intensity |
| `ecc-hydration-performance` | Configuring web typography, font preloading, hydration safety |
| `react-performance-optimizations` | Optimizing sluggish React apps, virtualization, RSC logic |
| `performance-engineering` | Enforcing bundle budgets, Lighthouse thresholds, Core Web Vitals |

### Backend and Data — 9 skills

| Skill | Use When |
|:------|:---------|
| `backend-dev-guidelines` | Building APIs, background workers, data services |
| `api-design-principles` | Designing new REST, GraphQL, or RPC interfaces |
| `modern-database-orchestration` | Designing schemas, writing migrations, integrating ORMs |
| `ecc-postgres-patterns` | Writing SQL, designing indexes, implementing RLS |
| `ecc-database-migrations` | Creating/altering tables, running data migrations |
| `ecc-docker-patterns` | Containerizing apps, Docker Compose, multi-stage Dockerfiles |
| `devops-deployment-automation` | Setting up CI/CD pipelines, deploying to Vercel/AWS/Railway |
| `testing-quality-engineering` | Writing tests, setting up test infrastructure, TDD |
| `seo-metadata-patterns` | Shipping public-facing pages with proper SEO |

### AI and Knowledge — 4 skills

| Skill | Use When |
|:------|:---------|
| `ai-rag-architectures` | Building RAG systems, semantic search, AI knowledge bases |
| `graphify` | Converting code/docs/papers into knowledge graphs |
| `skill-generation-expert` | Creating new skills from external documentation |
| `repo-analysis` | Deep-diving into unknown codebases |

### Media and Export — 9 skills

| Skill | Use When |
|:------|:---------|
| `huashu-deck-pdf-export` | Exporting web layouts to PDF |
| `huashu-html-to-pptx-conversion` | Generating PowerPoint from application data |
| `huashu-video-rendering` | Rendering Remotion compositions to MP4 |
| `remotion-composition-metadata` | Configuring video FPS, duration, dimensions |
| `remotion-dynamic-frame-logic` | Mapping frame counts to style properties |
| `remotion-sequence-timing` | Orchestrating layered sequences and delays |
| `remotion-video-config-context` | Calculating relative animation offsets |
| `remotion-video-template` | Creating animated visual assets or title cards |
| `remotion-web-player-integration` | Embedding videos in React with @remotion/player |

### System — 2 skills

| Skill | Use When |
|:------|:---------|
| `caveman-mode` | User requests terse output (~75% token savings) |
| `spec-driven-build` | Transforming a spec into a verified implementation plan |

### Skill Loading Rules
- Load a skill ONLY when the task explicitly matches its "Use when" trigger
- Load ONLY the most specific match — don't stack generic skills
- Never pre-load all skills for orientation
- Skills are reference docs, not executable code — the AI reads them and follows their guidance

---

## State Files & Session Continuity

Three project-local files maintain memory across sessions:

| File | Purpose | Written When |
|------|---------|-------------|
| `STATE.md` | Strategic memory — durable architectural decisions, tech choices, project identity | After any significant decision |
| `task.md` | Tactical tracker — current work items, checkpoints, session progress | During and after execution |
| `project_heuristics.md` | Self-improvement memory — IF/THEN constraints learned from past failures | After terminal thrashing or user corrections |

**Session start protocol**: At the start of any non-trivial session, read `STATE.md` and `task.md` from the project root. Identify current phase, last major decision, next logical step. Resume from that point — don't reconstruct from scratch.

**Resolution order**: Project root first (`./STATE.md`), then `.agents/STATE.md` as fallback.

**Heuristics example**: If a `npm test` command fails twice with the same error, the AI records: `IF running tests in this project, THEN use --forceExit flag because Jest doesn't exit cleanly`. This persists across sessions.

---

## Rule Enforcement

Rules in `.agents/rules/` are engineering constraints applied during the **VERIFY** phase — after implementation, before delivery.

| Domain | Rule File | Applied When |
|--------|-----------|-------------|
| Frontend | `rules/frontend.md` | Any UI, layout, component, CSS work |
| Backend | `rules/backend.md` | Any API, service, auth, data work |
| API Design | `rules/api.md` | Any new API surface |
| Database | `rules/database.md` | Any schema, migration, query work |
| File Structure | `rules/project-structure.md` | Any file or folder changes |
| Completion | `rules/done-criteria.md` | Before declaring ANY task done |

Rules are NOT read at task start (that would bloat context). They are loaded at VERIFY and checked against the output. If the output violates a rule, it is fixed before delivery — never flagged as "tech debt."

---

## Directory Structure

```
.agents/
├── AGENTS.md                      # THE source of truth — all routing, safety, delivery rules
├── README.md                      # This file
├── settings.json                  # Machine-readable config (agents, commands, permissions)
├── evaluation.md                  # Current-state assessment
├── ag-audit.py                    # Quick structural health check
├── validate_agents.py             # Deep structural integrity validator
│
├── agents/                        # 6 specialized agent definitions
│   ├── planner.md                 #   Plan Mode + Orchestrator Mode (parallel dispatch)
│   ├── debugger.md                #   Root-cause diagnosis
│   ├── frontend.md                #   UI/UX engineering
│   ├── backend.md                 #   Services and data
│   ├── ai-engineer.md             #   LLM/RAG pipelines
│   └── reviewer.md                #   Code audit + Evaluator Mode (PASS/FAIL)
│
├── workflows/                     # Slash command workflows (one file per command)
│   ├── build-feature.md           #   /build-feature
│   ├── fix-issue.md               #   /fix-issue
│   ├── review-code.md             #   /review-code
│   ├── refactor.md                #   /refactor
│   ├── ship-ui.md                 #   /ship-ui
│   ├── research.md                #   /research
│   ├── orchestrate.md             #   /orchestrate (parallel dispatch)
│   ├── brainstorm.md              #   /brainstorm
│   ├── write-plan.md              #   /write-plan
│   ├── execute-plan.md            #   /execute-plan
│   └── caveman.md                 #   /caveman
│
├── rules/                         # Engineering constraints (applied at VERIFY phase)
│   ├── frontend.md    ├── backend.md     ├── api.md
│   ├── database.md    ├── project-structure.md
│   ├── done-criteria.md           #   Checked before declaring ANY task done
│   └── graphify.md
│
├── skills/                        # 39 lazy-loaded skill modules
│   ├── CAPABILITIES.md            #   Skill routing index (which skill handles what)
│   ├── SYSTEM_ORCHESTRATION.md    #   Multi-skill phase sequencing rules
│   ├── RUNTIME_CONTROL.md         #   Token limits, checkpoints, state sync
│   └── <skill-name>/SKILL.md     #   Individual skills (one folder each)
│
├── skill-system/                  # Tools for creating and maintaining skills
├── hooks/                         # Pre-commit (PowerShell) and lint-on-save scripts
├── scripts/
│   └── ag-init.ps1                #   Project linker (creates junctions + scaffolds state)
└── mcps/                          # MCP server documentation and setup checklists
```

---

## The Prompt Formula

```
@agent + skill names + rule file + numbered specific steps = production-quality output
```

The more specific you are, the better the output. Vague prompts → vague code. Precise prompts → production code.

### Example 1: Awwwards-Caliber Frontend

```
@frontend Load skills `threejs-r3f-fundamentals`, `gsap-scroll-patterns`, and
`advanced-responsive-patterns`. Apply rule `rules/frontend.md`.

Build a Next.js App Router landing page with a scroll-pinned 3D hero section:
1. Dynamic import the R3F Canvas component with ssr: false
2. Load a Draco-compressed GLB model (under 2MB), set canvas DPR to [1, 1.5]
3. Create a GSAP ScrollTrigger timeline with anticipatePin: 1 and scrub: 0.8
4. Map all spacing to 5 breakpoints using mobile-first fluid clamp values
5. Handle prefers-reduced-motion via gsap.matchMedia()
```

### Example 2: Parallel Codebase Audit

```
/orchestrate Audit the entire codebase:
- Worker 1: Run the full test suite
- Worker 2: Lint all frontend components for accessibility
- Worker 3: Check backend for SQL injection patterns
Synthesize results into a single audit report with severity ratings.
```

### Example 3: Bulletproof Backend API

```
@backend Load skills `api-design-principles`, `ecc-database-migrations`, and
`ecc-postgres-patterns`. Apply rule `rules/backend.md`.

Implement a transaction ledger API for a multi-tenant SaaS:
1. Prisma schema with User, Tenant, Transaction — tenantId FK on every table
2. DDL migration with partial index on active transactions (WHERE status = 'active')
3. DML migration backfilling existing rows in batches of 500
4. Row Level Security blocking cross-tenant access at the DB level
5. Standard { data, error, meta } JSON envelope — never expose internal IDs
```

### Example 4: Simple Fix (No Formula Needed)

```
Fix the TypeError on line 42 of utils.ts
```
Fast Path. No agent, no skills, no ceremony.

---

## Cost Control

| Strategy | How It Works | Impact |
|:---------|:-------------|:-------|
| **Fast Path Bypass** | Trivial tasks skip all agent + skill loading | Saves ~10K input tokens/turn |
| **Skill Budget 0/2/3** | Strict limits prevent context pollution | Preserves peak reasoning quality |
| **40% Rule** | At 40% context usage, compact to STATE.md and start fresh | Recovers 20-50K+ tokens |
| **Caveman Mode** | `/caveman` drops output ~75% with zero info loss | Biggest $/msg savings (output costs 4-5x input) |
| **Line-Bounded Reads** | Always specify StartLine/EndLine when reading files | Prevents multi-K context bloat |

---

## Complete LLM Reference

> **This section exists so you can copy this entire README into any LLM and say: "Given this OS specification, write me a prompt for [goal]."** The LLM will understand the agents, commands, skills, routing, and prompt formula. No additional files needed.

### Quick Reference Card

```
AGENTS:    @planner | @debugger | @frontend | @backend | @ai-engineer | @reviewer
MODES:     @planner has Orchestrator Mode (parallel dispatch)
           @reviewer has Evaluator Mode (PASS/FAIL/NEEDS_REVISION)

COMMANDS:  /build-feature | /fix-issue | /review-code | /refactor | /ship-ui
           /research | /orchestrate | /brainstorm | /write-plan | /execute-plan | /caveman

PHASES:    PLANNING → BUILD → EVALUATE (mechanical + reviewer) → AUDIT → SHIP

SKILLS:    39 total. Load by backtick name. Max 0 (trivial) / 2 (simple) / 3 (complex).
RULES:     rules/frontend.md | rules/backend.md | rules/api.md | rules/database.md
           rules/project-structure.md | rules/done-criteria.md

SAFETY:    Tier 1 auto | Tier 2 propose | Tier 3 confirm | Tier 4 permanently blocked
STATE:     STATE.md (strategic) | task.md (tactical) | project_heuristics.md (learned)

FORMULA:   @agent + skill names + rule file + numbered steps = production output
PARALLEL:  /orchestrate + list independent workers = concurrent terminal execution
FAST:      Simple request with no ceremony = Fast Path (skip everything)
```

### Meta-Prompt (Paste README + This to Any LLM)

```
I have an AI coding OS called DAWG OS. Its full specification is in the document
I just pasted. Given this OS, write me a prompt to accomplish the following goal.

Requirements for the prompt you generate:
- Use the correct @agent from the routing table
- Load the right skills by backtick name (max 3)
- Specify the matching rule file from rules/
- Write numbered implementation steps with exact API calls and values
- If the task has independent sub-tasks, use /orchestrate with labeled workers
- If the task is trivially simple, skip all ceremony and just state the fix
- Do not be vague — every step should have a concrete, verifiable output

My goal: [describe what you want to build/fix/audit]
My stack: [e.g., Next.js 14, Prisma, PostgreSQL, Tailwind]
```

---

<div align="center">

<samp><b>For engineers. For dawgs.</b></samp>

<br/><br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0D0D0D,50:6D28D9,100:EC4899&height=120&section=footer" width="100%" />

</div>
