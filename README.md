<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0D0D0D,50:6D28D9,100:EC4899&height=220&section=header&text=DAWG%20OS&fontSize=70&fontColor=FFFFFF&animation=fadeIn&fontAlignY=35&desc=The%20AI%20Execution%20Kernel&descSize=18&descAlignY=55&descAlign=50" width="100%" />

<br/>

<img src="https://img.shields.io/badge/Full--Stack_Architecture-Ship_Frontend_%26_Backend-6D28D9?style=for-the-badge&logo=vercel&logoColor=white" />
<img src="https://img.shields.io/badge/AI%2FRAG_Pipelines-Vector_Search_%26_Embeddings-EC4899?style=for-the-badge&logo=openai&logoColor=white" />
<img src="https://img.shields.io/badge/Production_Databases-Postgres_%7C_Prisma_%7C_Drizzle-10B981?style=for-the-badge&logo=postgresql&logoColor=white" />
<br/>
<img src="https://img.shields.io/badge/3D_%26_Motion-Three.js_%7C_GSAP_%7C_Framer-3B82F6?style=for-the-badge&logo=threedotjs&logoColor=white" />
<img src="https://img.shields.io/badge/CI%2FCD_%26_DevOps-Docker_%7C_Vercel_%7C_Railway-F59E0B?style=for-the-badge&logo=docker&logoColor=white" />
<img src="https://img.shields.io/badge/40_Loaded_Skills-Lazy--Load_On_Demand-059669?style=for-the-badge&logo=stackblitz&logoColor=white" />

<br/><br/>

<samp>
<b>Turn any language model into a disciplined software build system.</b>
<br/>
Awwwards-caliber frontends. Production-grade backends. AI/RAG pipelines. Zero slop.
</samp>

<br/><br/>

<kbd>&nbsp; PLANNING &nbsp;</kbd>&nbsp;&nbsp;&#9654;&nbsp;&nbsp;<kbd>&nbsp; BUILD &nbsp;</kbd>&nbsp;&nbsp;&#9654;&nbsp;&nbsp;<kbd>&nbsp; AUDIT &nbsp;</kbd>&nbsp;&nbsp;&#9654;&nbsp;&nbsp;<kbd>&nbsp; SHIP &nbsp;</kbd>

<br/><br/>

<a href="#quickstart">Quickstart</a>&nbsp;&nbsp;|&nbsp;&nbsp;<a href="#how-it-works">How It Works</a>&nbsp;&nbsp;|&nbsp;&nbsp;<a href="#agent-roster">Agents</a>&nbsp;&nbsp;|&nbsp;&nbsp;<a href="#skill-library">Skills</a>&nbsp;&nbsp;|&nbsp;&nbsp;<a href="#three-prompts-to-master-everything">Prompts</a>&nbsp;&nbsp;|&nbsp;&nbsp;<a href="#architecture">Architecture</a>&nbsp;&nbsp;|&nbsp;&nbsp;<a href="#cost-control">Cost Control</a>

</div>

<br/>

---

## Quickstart

```bash
# 1. Clone into your global agents directory
git clone https://github.com/KapishMittal128/AntiGravity-CustomConfiguration.git ~/.antigravity/.agents

# 2. Symlink into any project
# PowerShell
New-Item -ItemType Junction -Path ".agents" -Target "$HOME\.antigravity\.agents"

# 3. Start prompting with structure
@frontend Load skills `gsap-scroll-patterns`, `threejs-r3f-fundamentals`. Build a scroll-pinned 3D hero.
```

> [!TIP]
> The OS activates automatically when your IDE's AI assistant detects the `.agents/` directory junction in your project root. No config files, no env vars, no setup commands.

---

## How It Works

DAWG OS intercepts every request and routes it through a **Complexity Gate** before executing anything. This is the core decision engine.

```
                    +---------------------------+
                    |    Incoming Request        |
                    +-------------+-------------+
                                  |
                                  v
                   +--------------+--------------+
                   |    COMPLEXITY GATE CHECK     |
                   +--------------+--------------+
                                  |
              +-------------------+-------------------+
              |                                       |
     +--------v--------+                 +------------v-----------+
     |    FAST PATH     |                 |    FULL WORKFLOW       |
     |                  |                 |                        |
     |  Direct execute  |                 |  PLAN > BUILD > AUDIT  |
     |  Zero overhead   |                 |  Lazy-load 2-3 skills  |
     |  No agents       |                 |  Agent-routed          |
     +---------+--------+                 +-----------+------------+
```

**Fast Path (DirectOps)** -- For small, local, single-pass tasks under ~15 minutes with zero architectural impact. No agent switching, no skill loading. Execute directly.

**Full Workflow** -- For tasks that modify data models, schemas, shared interfaces, delete existing code, or carry architectural ambiguity. Follows strict phases: `PLANNING` then `BUILD` then `AUDIT` then `SHIP`. Skills are lazy-loaded on demand (max 2 for simple, 3 for complex). An agent is selected and activated for the task duration.

**Anti-Overkill Check** -- Before defaulting to Full Workflow, the system verifies that escalation is justified. If the task can realistically be done in one file, one pass, under 15 minutes, and has no risk conditions (no destructive changes, no shared interface modifications, no schema changes, no security implications), it stays on Fast Path. This prevents token waste on trivial work.

---

## Agent Roster

Six specialized agents. One active at a time. Each brings a distinct engineering mindset. Mention `@agent-name` to activate.

<table>
<tr>
<td align="center" width="16.6%">
<br/>
<samp><b>@planner</b></samp>
<br/><br/>
<img src="https://img.shields.io/badge/-Architecture-6D28D9?style=flat-square" />
<br/><br/>
<sub>Specs / File layout<br/>Schema planning<br/>Tech decisions</sub>
<br/><br/>
</td>
<td align="center" width="16.6%">
<br/>
<samp><b>@debugger</b></samp>
<br/><br/>
<img src="https://img.shields.io/badge/-Diagnosis-EF4444?style=flat-square" />
<br/><br/>
<sub>Root-cause analysis<br/>Log parsing<br/>Regression tracing</sub>
<br/><br/>
</td>
<td align="center" width="16.6%">
<br/>
<samp><b>@frontend</b></samp>
<br/><br/>
<img src="https://img.shields.io/badge/-UI%2FUX-EC4899?style=flat-square" />
<br/><br/>
<sub>Visual hierarchy<br/>Motion / WebGL<br/>Responsive layout</sub>
<br/><br/>
</td>
<td align="center" width="16.6%">
<br/>
<samp><b>@backend</b></samp>
<br/><br/>
<img src="https://img.shields.io/badge/-Services-10B981?style=flat-square" />
<br/><br/>
<sub>APIs / Auth<br/>Data pipelines<br/>Security gates</sub>
<br/><br/>
</td>
<td align="center" width="16.6%">
<br/>
<samp><b>@ai-engineer</b></samp>
<br/><br/>
<img src="https://img.shields.io/badge/-AI%2FRAG-F59E0B?style=flat-square" />
<br/><br/>
<sub>Embeddings / RAG<br/>Prompt systems<br/>Vector search</sub>
<br/><br/>
</td>
<td align="center" width="16.6%">
<br/>
<samp><b>@reviewer</b></samp>
<br/><br/>
<img src="https://img.shields.io/badge/-Quality-3B82F6?style=flat-square" />
<br/><br/>
<sub>Code audit<br/>Perf review<br/>TDD coverage</sub>
<br/><br/>
</td>
</tr>
</table>

**Routing logic**: Bug or failure goes to `@debugger`. New feature goes to `@planner` then `@backend` or `@frontend`. UI polish goes to `@frontend`. AI/LLM work goes to `@ai-engineer`. Code review goes to `@reviewer`. Scope unclear goes to `@planner` first. Never activate two agents simultaneously for overlapping scope.

---

## Skill Library

**40 production-grade skills**, lazy-loaded on demand. Budget: **0** for trivial tasks / **2** for simple / **3** max for complex. Full routing index lives in `skills/CAPABILITIES.md`.

<details>
<summary><b>Frontend and Motion</b> -- 16 skills</summary>
<br/>

| Skill | Purpose |
|:------|:--------|
| `advanced-responsive-patterns` | Breakpoints, fluid clamp spacing, touch targets |
| `framer-motion-patterns` | motion/react mount transitions, stagger paths |
| `frontend-architecture-patterns` | Modular components, Zustand state, grid systems |
| `gsap-scroll-patterns` | ScrollTrigger pinning, scrub timelines, useGSAP |
| `microinteractions` | Checkmark springs, magnetic hover, canvas confetti |
| `motion-accessibility` | WCAG AA vestibular safety, reduced-motion fallbacks |
| `threejs-r3f-fundamentals` | Canvas settings, lighting, GLB model loaders |
| `webgl-shader-basics` | Vertex/fragment uniforms, GLSL custom noise |
| `ecc-aesthetic-tones` | Monospace brutalism, minimal pastels, glassmorphism |
| `ecc-design-critique` | Descender grid alignment, contrast audits |
| `ecc-hydration-performance` | Fontaine CLS overrides, hydration mount traps |
| `ecc-taste-dials` | BRIEF inference, DESIGN_VARIANCE motion dials |
| `ui-design-expert` | Aesthetic guidelines, spatial balance, contrast ratios |
| `nextjs-app-router-patterns` | Layouts vs templates, loading skeletons, route groups |
| `react-performance-optimizations` | Virtualized lists, RSC layouts, useMemo guidelines |
| `performance-engineering` | Bundle budgets, Lighthouse thresholds, Draco assets |

</details>

<details>
<summary><b>Backend and Data</b> -- 9 skills</summary>
<br/>

| Skill | Purpose |
|:------|:--------|
| `api-design-principles` | REST/GraphQL interface schemas, DX controls |
| `backend-dev-guidelines` | Service boundaries, security policies, background jobs |
| `ecc-database-migrations` | Production DDL/DML, safe rolling migrations |
| `ecc-docker-patterns` | Multi-stage Dockerfiles, compose cache builds |
| `ecc-postgres-patterns` | Indexes, partial indexes, RLS security queries |
| `modern-database-orchestration` | Prisma/Drizzle ORM schemas, safe data seeding |
| `testing-quality-engineering` | AAA Vitest/Playwright, TDD, mock strategies |
| `devops-deployment-automation` | CI/CD pipelines, Docker networks, Vercel/Railway |
| `seo-metadata-patterns` | OG tags, rich JSON-LD schema graphs, robots/sitemap |

</details>

<details>
<summary><b>AI and Knowledge</b> -- 4 skills</summary>
<br/>

| Skill | Purpose |
|:------|:--------|
| `ai-rag-architectures` | Embeddings, vector schemas, retrieval pipelines |
| `graphify` | BFS knowledge graph pipeline, community clustering |
| `skill-generation-expert` | Ingest web links into custom skill definitions |
| `repo-analysis` | Dependency structures, dynamic call tracing |

</details>

<details>
<summary><b>Media and Export</b> -- 9 skills</summary>
<br/>

| Skill | Purpose |
|:------|:--------|
| `huashu-deck-pdf-export` | CSS media print styling, page-break overrides |
| `huashu-html-to-pptx-conversion` | JSON to PptxGenJS direct transformation |
| `huashu-video-rendering` | Remotion video compiler configurations |
| `remotion-*` (6 skills) | Sequence delay, frame index, video rendering |

</details>

<details>
<summary><b>System and Workflow</b> -- 2 skills</summary>
<br/>

| Skill | Purpose |
|:------|:--------|
| `caveman-mode` | High-efficiency terse output (75% token savings) |
| `spec-driven-build` | PRD to specs, detailed implementation maps |

</details>

---

## Commands and Slash Bridge

Type a slash command to trigger a structured execution workflow. Commands enforce phased execution -- you cannot skip from PLAN to SHIP.

| Command | Action | Phase |
|:--------|:-------|:------|
| `/build-feature` | New feature, endpoint, or page | `PLAN > BUILD > AUDIT > SHIP` |
| `/fix-issue` | Bug diagnosis and fix | `DIAGNOSE > FIX > VERIFY` |
| `/review-code` | Code quality audit | `SCAN > REPORT > RECOMMENDATIONS` |
| `/refactor` | Clean up, simplify, restructure | `ANALYZE > REFACTOR > VERIFY` |
| `/ship-ui` | Polish UI to production quality | `AUDIT > POLISH > SHIP` |
| `/research` | Tech decision, library comparison | `GATHER > ANALYZE > RECOMMEND` |
| `/caveman` | Activate terse output mode | Immediate |

**Safety tiers**: Tier 1 (auto-execute) covers safe reads like `git status`, `npm run test`. Tier 2 (propose first) covers environment changes like `npm install`, `git commit`. Tier 3 (explicit approval) covers production migrations and git history rewrites. Tier 4 (permanently blocked) covers `cat .env`, `rm -rf`, `git push --force` -- these never execute regardless of justification.

---

## Three Prompts to Master Everything

These three prompts demonstrate the full power of the OS. Each one activates the correct agent, loads the right skills, applies the matching rule file, and provides specific, numbered implementation steps. Copy and adapt them.

### Prompt 1 -- Awwwards-Caliber Frontend

```
@frontend Load skills `threejs-r3f-fundamentals`, `gsap-scroll-patterns`, and
`advanced-responsive-patterns`. Apply rule `rules/frontend.md`.

Build a Next.js App Router landing page with a scroll-pinned 3D hero section:
1. Dynamic import the R3F Canvas component with ssr: false to split it from the
   initial JS bundle entirely.
2. Load a Draco-compressed GLB model (under 2MB) and set canvas DPR to [1, 1.5].
3. Create a GSAP ScrollTrigger timeline using the useGSAP hook. Bind camera
   rotation to scroll progress with anticipatePin: 1 and scrub: 0.8.
4. Map all layout spacing to 5 breakpoints using mobile-first fluid clamp values.
5. Handle prefers-reduced-motion using gsap.matchMedia() to disable all motion
   while preserving the static layout.
```

**Why it works**: Named agent (`@frontend`). Three skills loaded (the maximum for complex work). Rule file specified. Five numbered steps with exact API calls, exact values, exact constraints. No ambiguity for the model to fill in.

---

### Prompt 2 -- Bulletproof Backend API

```
@backend Load skills `api-design-principles`, `ecc-database-migrations`, and
`ecc-postgres-patterns`. Apply rule `rules/backend.md`.

Implement a transaction ledger API for a multi-tenant SaaS application:
1. Create a Prisma schema with User, Tenant, and Transaction models. Enforce
   tenant isolation using a required tenantId foreign key on every table.
2. Generate a DDL migration adding a partial index on active transactions
   (WHERE status = 'active') to optimize dashboard queries.
3. Write a separate DML migration that backfills existing rows in batches of
   500 to prevent table locks during deployment.
4. Implement Row Level Security policies blocking cross-tenant data access
   at the database level, not the application level.
5. Return all API responses in a standard { data, error, meta } JSON envelope.
   Never expose internal database IDs or raw error stack traces.
```

**Why it works**: Named agent (`@backend`). Skills target the exact domain (API design + migrations + Postgres patterns). Rule file locks the quality standard. Steps separate DDL from DML (a critical production safety practice). Specifies the exact envelope format.

---

### Prompt 3 -- AI/RAG Ingestion Pipeline

```
@ai-engineer Load skills `ai-rag-architectures`, `graphify`, and
`modern-database-orchestration`. Apply rule `rules/backend.md`.

Build a document ingestion pipeline for semantic search over uploaded PDFs:
1. Define a Postgres schema with pgvector extension. Create a documents table
   storing raw text, a chunks table with vector(1536) embeddings, and a
   communities table for graph cluster summaries.
2. Write an ingestion transform that extracts text from uploaded PDFs, strips
   formatting artifacts, and splits content at 500-token boundaries with
   50-token overlap between adjacent chunks.
3. Generate embeddings asynchronously using a background job queue, not inside
   the HTTP request handler. Store each embedding with its source chunk ID
   and document metadata.
4. Build a BFS graph traversal routine using the graphify skill that maps
   cross-document entity relationships into community summary nodes.
5. Implement the search endpoint using cosine distance similarity. Return the
   top 5 chunks ranked by relevance, with their source document metadata and
   community context prepended to the LLM prompt template.
```

**Why it works**: Named agent (`@ai-engineer`). Skills cover the full stack (RAG architecture + knowledge graphs + database orchestration). Specifies exact vector dimensions, chunk sizes, overlap strategy, and async processing requirements. The model has no room to guess.

---

> [!IMPORTANT]
> **The formula**: `@agent` + `skill names` + `rule file` + numbered, specific implementation steps = consistently excellent output. Vague prompts produce vague code. Precise prompts produce production code.

---

## Architecture

The globe below shows the full system topology. DAWG OS sits at the center. Agents, Skills, and Rules orbit as independent subsystems. Corner nodes represent supporting infrastructure -- commands, persistent state, hooks, and the skill authoring system.

<div align="center">

<img src="https://raw.githubusercontent.com/KapishMittal128/AntiGravity-CustomConfiguration/main/assets/globe.svg" width="700" />

</div>

<details>
<summary><b>Directory Structure</b></summary>
<br/>

```
.agents/
+-- AGENTS.md                    # System authority (source of truth)
+-- README.md                    # This file
+-- settings.json                # Permission flags and behavior config
+-- STATE.md                     # Long-term architectural state
+-- task.md                      # Active session operations
|
+-- agents/                      # 6 specialized agent definitions
|   +-- planner.md      +-- debugger.md       +-- frontend.md
|   +-- backend.md      +-- ai-engineer.md    +-- reviewer.md
|
+-- workflows/                   # Slash command workflows
|   +-- build-feature.md    +-- fix-issue.md     +-- review-code.md
|   +-- refactor.md         +-- ship-ui.md       +-- research.md
|
+-- rules/                       # Engineering constraints (VERIFY phase)
|   +-- frontend.md    +-- backend.md    +-- api.md
|   +-- database.md    +-- project-structure.md   +-- done-criteria.md
|
+-- skills/                      # 40 lazy-loaded skill modules
|   +-- <skill-name>/SKILL.md
|
+-- skill-system/                # Skill creation and maintenance
+-- hooks/                       # Pre-commit and lint-on-save scripts
```

</details>

---

## Cost Control

Every LLM call costs tokens. DAWG OS is designed to minimize waste without sacrificing reasoning depth.

| Strategy | Mechanism | Savings |
|:---------|:----------|:--------|
| **DirectOps Bypass** | Fast Path skips agent activation and skill loading entirely | 10,000+ input tokens per turn |
| **Skill Budget** | Strict 0/2/3 limits prevent attention dilution from excessive context | Preserves reasoning quality |
| **40% Rule** | Compact context at 40% usage -- sync to STATE.md, start fresh session | Recovers 20-50K+ tokens |
| **Caveman Mode** | `/caveman` drops output length by ~75% with zero information loss | Highest dollar/msg savings (output tokens cost 4-5x input) |
| **Line-Bounded Views** | Always pass StartLine/EndLine when reading files | Prevents multi-thousand-line context bloat |
| **Prompt Caching** | System prompt baseline (~15-20K tokens) cached by Anthropic/Gemini/OpenAI | Up to 90% reduction on cached input |

**Context Hygiene Protocol**: When context exceeds 40%, record decisions in `STATE.md`, check off milestones in `task.md`, start a fresh chat session, and preload only `STATE.md` + `task.md` to restore strategic continuity. If an implementation path hits repeated regressions, abort and start clean instead of patching.

---

<div align="center">

<samp><b>For engineers. For dawgs.</b></samp>

<br/><br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0D0D0D,50:6D28D9,100:EC4899&height=120&section=footer" width="100%" />

</div>
