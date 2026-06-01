# ✦ ANTIGRAVITY OS ✦

<p align="left">
  <a href="https://github.com/KapishMittal128/AntiGravity-CustomConfiguration"><img src="https://img.shields.io/badge/OS_Kernel-v3.0.0-6D28D9?style=flat-square&logo=google" /></a>
  <img src="https://img.shields.io/badge/Skills_Library-40_Canonical-10B981?style=flat-square&logo=codeforces" />
  <img src="https://img.shields.io/badge/Build_Validator-0_Errors_/_0_Warnings-059669?style=flat-square&logo=github-actions" />
  <img src="https://img.shields.io/badge/Performance-60FPS_Target-EC4899?style=flat-square&logo=googlechrome" />
  <img src="https://img.shields.io/badge/Accessibility-WCAG_AA-3B82F6?style=flat-square" />
</p>

> **Global execution kernel for high-fidelity, production-grade software engineering.**  
> Build Awwwards-caliber landing pages, high-density analytics dashboards, pgvector ingestion pipelines, and safety-audited service backends with zero slop.

<p align="left">
  <kbd>PLANNING</kbd> ➔ <kbd>BUILD</kbd> ➔ <kbd>AUDIT</kbd> ➔ <kbd>SHIP</kbd>
</p>

---

## 1. Core Operating Philosophy

Antigravity OS converts any standard language model into a structured software build system. The system enforces strict architectural layers, data modeling priority, and rigorous verification gates.

```
                  ┌────────────────────────┐
                  │   Incoming Request     │
                  └───────────┬────────────┘
                              │
                              ▼
                [ Complexity Gate Check ]
                              │
             Is it small, local, and single-pass?
             ┌───────────────┴───────────────┐
             │ YES                           │ NO
             ▼                               ▼
       [ FAST PATH ]                 [ FULL WORKFLOW ]
     Direct execution.               PLANNING → BUILD → AUDIT → SHIP
     Skip workflows/skills.          Lazy-load max 2-3 skills.
```

### The Complexity Gate
Every task must pass the Complexity Gate prior to execution:
* **Fast Path (DirectOps)**: Selected for small, local, single-pass tasks under ~15 minutes of work with zero architectural impact. Skip agent switching and skill loading.
* **Full Workflow**: Selected for tasks that modify data models, schemas, shared interfaces, delete existing code, or have architectural ambiguity.

---

## 2. Context Hygiene & The 40% Rule

Reasoning capabilities degrade exponentially as the context window fills. Antigravity OS enforces three context management rules:
* **The 40% Threshold**: Reasoning peaks below 40% context usage. When context exceeds 40%, prime the environment for high-intelligence tasks (Debugging, Architecture) by using isolated subagents.
* **Proactive Compaction**: If context exceeds 60%, immediately perform a compaction step. Sync the current state to the project-root `STATE.md`, record active frontiers in `task.md`, and clean the terminal session.
* **History Rewinding**: If an implementation path encounters repeated regressions, abort immediately. Rewind or start a clean session instead of writing cumulative code patches.

---

## 3. Agent Selection Engine

Antigravity OS structures expertise into six designated agents. Mentions in the format `@agent-name` trigger the respective agent mindset.

| Agent | Mindset | Key Tool Priorities | Active Rule |
| :--- | :--- | :--- | :--- |
| `@planner` | Technical specification, file architecture, schema planning. | `grep_search`, `list_dir` | `rules/project-structure.md` |
| `@debugger` | Root-cause diagnosis, raw log analysis, regression trace. | `view_file`, `grep_search` | `rules/done-criteria.md` |
| `@frontend` | Visual hierarchy, responsive layout, motion curves, 3D/WebGL. | `view_file`, `write_to_file` | `rules/frontend.md` |
| `@backend` | Data flow, service abstraction, REST/GraphQL endpoints, security. | `view_file`, `write_to_file` | `rules/backend.md` |
| `@ai-engineer` | Prompt engineering, vector search, embeddings, RAG architectures. | `view_file`, `write_to_file` | `rules/api.md` |
| `@reviewer` | Code quality gates, performance auditing, TDD coverage, security. | `grep_search`, `run_command` | `rules/performance.md` |

---

## 4. Skill Loading Engine (Lazy Loading)

Skills are specialized knowledge bases loaded on-demand. Loading too many skills causes "attention dilution."
* **Budget Limits**: Max 2 skills for simple full-workflow tasks. Max 3 skills for complex tasks. 0 skills for Fast Path.
* **Routing Index**: Located in `skills/CAPABILITIES.md`. Refer to this file to select correct combinations.

### The 40 Active Skills Registry

```
skills/
├── advanced-responsive-patterns   # Breakpoints, fluid clamp spacing, touch targets
├── ai-rag-architectures           # Embeddings, vector schemas, retrieval pipelines
├── api-design-principles          # REST/GraphQL interface schemas, DX controls
├── backend-dev-guidelines         # Service boundaries, security policies, background jobs
├── caveman-mode                   # High-efficiency terse communication protocol
├── devops-deployment-automation   # CI/CD pipelines, Docker networks, Vercel/Railway
├── ecc-database-migrations        # Production DDL/DML, safe rolling migrations
├── ecc-docker-patterns            # Multi-stage Dockerfiles, compose cache builds
├── ecc-postgres-patterns          # Indexes, partial indexes, RLS security queries
├── ecc-taste-dials                # BRIEF inference, DESIGN_VARIANCE motion dials
├── ecc-aesthetic-tones            # Monospace brutalism, minimal pastels, glassmorphism
├── ecc-design-critique            # Descender grid alignment, contrast check, emoji bans
├── ecc-hydration-performance      # Fontaine CLS overrides, Next.js hydration mount traps
├── framer-motion-patterns         # motion/react mount transitions, stagger paths
├── frontend-architecture-patterns # Modular components, Zustand state, grid systems
├── graphify                       # BFS knowledge graph pipeline, community clustering
├── gsap-scroll-patterns           # ScrollTrigger pinning, scrub timelines, useGSAP cleanup
├── huashu-deck-pdf-export         # CSS media print styling, page-break overrides
├── huashu-html-to-pptx-conversion # Pure JSON to PptxGenJS direct transformation
├── huashu-video-rendering         # remotion video compiler configurations
├── microinteractions              # MIL checkmark spring, magnetic hover, canvas confetti
├── modern-database-orchestration  # Prisma/Drizzle ORM schemas, safe data seeding
├── motion-accessibility           # WCAG AA vestibular safety, reduced-motion swaps
├── nextjs-app-router-patterns     # layouts vs templates, loading skeletons, route groups
├── performance-engineering        # Bundle budgets, Lighthouse thresholds, Draco assets
├── react-performance-optimizations# Virtualized list arrays, RSC layouts, useMemo guidelines
├── remotion-* (6 skills)          # Sequence delay, frame index, video rendering templates
├── repo-analysis                  # Dependency structures, dynamic call tracing
├── seo-metadata-patterns          # OG tags, rich JSON-LD schema graphs, robots/sitemap
├── skill-generation-expert        # Ingestion of dynamic web links to custom skills
├── spec-driven-build              # PRD to specs, detailed implementation maps
├── testing-quality-engineering    # AAA Vitest/Playwright, TDD, mock strategies
├── threejs-r3f-fundamentals       # Canvas settings, lighting grids, GLB model loaders
├── ui-design-expert               # Aesthetic guidelines, spatial balance, contrast ratios
└── webgl-shader-basics            # Vertex fragment uniforms, GLSL custom noises
```

---

## 5. Command & Slash Bridge Protocol

Commands structure execution into explicit sequential phases: `PLANNING` → `BUILD` → `AUDIT` → `SHIP`.

### Slash Commands
Standard prompts starting with `/` are routed directly to `commands/`:
* `/build-feature` → `commands/build-feature.md`
* `/fix-issue` → `commands/fix-issue.md`
* `/review-code` → `commands/review-code.md`
* `/refactor` → `commands/refactor.md`
* `/ship-ui` → `commands/ship-ui.md`
* `/research` → `commands/research.md`
* `/caveman` → `skills/caveman-mode/SKILL.md`

### Command Proposal Protocol (Tiers)
* **Tier 1 (Auto-Execute)**: Safe read and standard checks (`git status`, `npm run test`, `validate_agents.py`). Run directly.
* **Tier 2 (Propose First)**: Changes environment or code (`npm install`, `git commit`, `git add`). State command and reason clearly, wait for user confirmation.
* **Tier 3 (Explicit Approval)**: High-impact changes (`git rebase`, production migrations). Proceed only after explicit confirmation.
* **Tier 4 (Permanently Blocked)**: Dangerous operations (`cat .env`, `rm -rf`, `git push --force`). Never execute.

---

## 6. High-Fidelity Production Blueprints

Use these blueprints to execute standardized product builds.

### Blueprint A: Awwwards-Caliber SaaS Marketing Site
* **Mindset / Agent**: `@frontend`
* **Skill Mix**: `threejs-r3f-fundamentals`, `gsap-scroll-patterns`, `advanced-responsive-patterns`
* **Rule**: `rules/frontend.md`

#### Activation Recipe
1. Initialize a dynamic template layout (`template.tsx` in Next.js) to isolate page entrance transitions.
2. Load GSAP `ScrollTrigger` and register the `useGSAP` hook for safe mounting and memory garbage collection.
3. Configure `threejs-r3f-fundamentals` inside a dynamic, client-side only component (`ssr: false`) to split the canvas out of the initial bundle.
4. Set device pixel ratio (`dpr`) limits to `[1, 1.5]` and implement dynamic vertex math under `webgl-shader-basics` to cap frame budgets at 60fps.

#### Prompt Template
```
@frontend Load skills `threejs-r3f-fundamentals`, `gsap-scroll-patterns`, and `advanced-responsive-patterns`. 

Implement an Awwwards-style SaaS marketing hero section:
1. Define a Dynamic Canvas inside `template.tsx` loading a Draco-compressed GLB model.
2. Animate camera target along a GSAP timeline synced to ScrollTrigger pinning.
3. Set ScrollTrigger `anticipatePin: 1` and cap scroll `scrub` value at `0.8` for smooth movement.
4. Handle prefers-reduced-motion using `gsap.matchMedia()` to disable movement while preserving static layout blocks.
```

#### Anti-Patterns
* ❌ Importing Framer Motion alongside GSAP in the same page boundary.
* ❌ Animating raw layout properties like CSS `top`, `left`, `width`, or `height` (destroys 60fps).
* ❌ Loading full, uncompressed 3D models (>5MB) without progressive loaders.

---

### Blueprint B: High-Density Analytics Dashboard
* **Mindset / Agent**: `@frontend`
* **Skill Mix**: `frontend-architecture-patterns`, `react-performance-optimizations`, `ui-design-expert`
* **Rule**: `rules/frontend.md`

#### Activation Recipe
1. Select a designated tone pack from `ecc-aesthetic-tones` (e.g. Utilitarian Pastel or Monospace Brutalist) to secure spacing and color variables.
2. Calibrate taste dials in `ecc-taste-dials` to low motion intensity and high visual density.
3. Implement `react-performance-optimizations` virtualized rendering arrays for lists exceeding 100 rows.
4. Apply the `ecc-design-critique` typographic leading audit to eliminate Cumulative Layout Shift (CLS).

#### Prompt Template
```
@frontend Load skills `frontend-architecture-patterns`, `react-performance-optimizations`, and `ui-design-expert`.

Build a high-density, three-column SaaS dashboard shell:
1. Apply layout spacing rules using HSL customized design tokens from the Utilitarian Pastel theme.
2. Wrap the primary table with a virtualized container rendering dynamic analytics records.
3. Ensure button contrast meets WCAG AA guidelines (>4.5:1) for normal text inputs.
4. Set exact line height rules using Fontaine `size-adjust` values to lock down layout shifts.
```

#### Anti-Patterns
* ❌ Nesting scrollable dashboard grids inside standard viewport scroll layouts.
* ❌ Hardcoding plain primary colors instead of design token systems.
* ❌ Triggering complete table list mounts on user scroll without virtualization.

---

### Blueprint C: Production-Grade AI RAG Product
* **Mindset / Agent**: `@ai-engineer`
* **Skill Mix**: `ai-rag-architectures`, `graphify`, `modern-database-orchestration`
* **Rule**: `rules/backend.md`

#### Activation Recipe
1. Initialize the vector DB client configuration using dynamic connection pools.
2. Write raw extraction transforms to parse unstructured files into normalized markdown nodes.
3. Build the community clustering index to map cross-file relationships.
4. Implement semantic search traversal logic with strict token budgets.

#### Prompt Template
```
@ai-engineer Load skills `ai-rag-architectures`, `graphify`, and `modern-database-orchestration`.

Construct a vector RAG pipeline for document ingestion:
1. Define a Postgres schema supporting pgvector indices and RLS access controls.
2. Build an ingestion transform that reads uploaded text, parses metadata, and splits content at 500-token boundaries.
3. Wire the semantic similarity query logic using Cosine Distance calculations.
4. Implement BFS graph query routines that load community summary nodes into prompt templates.
```

#### Anti-Patterns
* ❌ Sending raw, unchunked document contents directly into the LLM context.
* ❌ Storing vector embeddings in databases without explicit query indices.
* ❌ Running synchronous embedding creation inside backend HTTP server loops.

---

### Blueprint D: Bulletproof Database & API Backend
* **Mindset / Agent**: `@backend`
* **Skill Mix**: `api-design-principles`, `backend-dev-guidelines`, `modern-database-orchestration`
* **Rule**: `rules/backend.md`

#### Activation Recipe
1. Setup type-safe database schemas with Prisma or Drizzle ORM.
2. Write isolated DDL/DML migrations separating schema changes from data transformations.
3. Enforce Postgres partial indexes and Row Level Security (RLS) security gates on sensitive tables.
4. Declare strict REST endpoint responses returning standard envelope schemas.

#### Prompt Template
```
@backend Load skills `api-design-principles`, `backend-dev-guidelines`, and `modern-database-orchestration`.

Implement a transaction creation API route:
1. Create a Prisma schema mapping user accounts to transaction records.
2. Generate an isolated migration file applying partial indices on active transactions.
3. Apply Row Level Security guidelines blocking unauthorized cross-tenant data queries.
4. Return responses wrapped in standard data/error JSON envelopes.
```

#### Anti-Patterns
* ❌ Executing raw, unparameterized SQL queries in API endpoints.
* ❌ Combining DDL schema changes and data updates in a single migration file.
* ❌ Exposing internal database keys or raw error traces to API client responses.

---

## 7. Direct Prompt Tuning

Use this guide to structure requests to get high-performance output.

### Bad Prompts vs Good Prompts

#### SaaS Landing Page
* ❌ **Bad Prompt**: *"Make me a cool landing page with cool 3D animations and page transitions in NextJS."*
  * *Why it fails*: Indefinite, stack-diluted, lacks specific performance boundaries, and forces the model to guess variables.
  * *Result*: Jerky animations, slow canvas rendering, and mixed Framer Motion/GSAP conflict errors.
* ✅ **Good Prompt**:
  ```
  @frontend Load skills `threejs-r3f-fundamentals`, `gsap-scroll-patterns`, and `advanced-responsive-patterns`. Apply rule `rules/frontend.md`.
  
  Build a Next.js App Router landing page with a scroll-pinned 3D hero canvas:
  1. Dynamic import standard Three.js canvas with ssr: false.
  2. Map layout parameters to 5 breakpoints using mobile-first tailwind grids.
  3. Bind camera rotation to ScrollTrigger timelines using `useGSAP`.
  4. Enforce prefers-reduced-motion using gsap.matchMedia().
  ```

#### Database Schema Update
* ❌ **Bad Prompt**: *"Write a database migration to add a metadata column to the user table and update existing values."*
  * *Why it fails*: Combines schema modifications and data updates into one step, risking locking active production databases.
  * *Result*: Locked user tables, production down times, and broken rollback histories.
* ✅ **Good Prompt**:
  ```
  @backend Load skills `ecc-database-migrations` and `ecc-postgres-patterns`. Apply rule `rules/database.md`.
  
  Write a database schema update for the User table:
  1. Generate a DDL schema migration adding a nullable `metadata` JSONB column.
  2. Implement an isolated DML migration script updating existing rows in batches of 500 to prevent table locks.
  3. Add a partial index on non-null metadata records.
  4. Draft rollback DDL resetting the schema.
  ```

## 8. Token Management & Cost Optimization Protocol

Every LLM query incurs a token cost. Antigravity OS is optimized to balance deep reasoning capabilities with strict context limits:

### Caching and Baseline Overhead
* **System Prompt Tax**: The configuration files (`AGENTS.md`, `README.md`, `skills/CAPABILITIES.md`, and system rules) create a baseline cost of **~15,000 to ~20,000 input tokens** per message.
* **Prompt Caching**: If your developer workspace/IDE integration supports prompt caching (e.g. Anthropic, Gemini context caching, OpenAI), this baseline prompt is cached automatically. The cost for cached input is **reduced by up to 90%** (you pay only 10% of standard rates).

### Operational Strategies to Prevent Token Waste

#### A. DirectOps Bypass
* Always choose the **Fast Path (DirectOps)** for isolated edits, simple search/grep operations, or simple bug fixes.
* **Benefit**: Bypasses `@agent` loading and skill loading entirely, saving **10,000+ input tokens** per turn.

#### B. Active Skill Budget
* Strictly respect on-demand loading budgets:
  * **Trivial tasks**: 0 skills.
  * **Simple tasks**: Max 2 skills (1 primary, 1 supporting).
  * **Complex tasks**: Max 3 skills.
* **Benefit**: Prevents memory bloat and protects model reasoning depth from diluting.

#### C. Wiping Chat History (Wipe-and-Refresh)
* As you build, conversation history accumulates transcripts of old edits, which the model must re-read on every message.
* **The 40% Rule**: Once your context window usage grows large (exceeding 40%), perform a **compaction**:
  1. Record key decisions in the project-root `STATE.md` and check off milestones in `task.md`.
  2. Start a fresh, clean chat session to wipe the historical conversation log.
  3. Preload only `STATE.md` and `task.md` to restore strategic continuity.
* **Benefit**: Instantly recovers **20,000 to 50,000+ context tokens**.

#### D. Terse Output (Caveman Mode)
* Activate **Caveman Mode** by typing `/caveman` or loading `skills/caveman-mode/SKILL.md`. This instructs the model to eliminate pleasantries, articles, and filler words, keeping output compressed while retaining code block syntax.
* **Benefit**: Drops output length by **~75%**. Since output tokens are 4x to 5x more expensive than input tokens, this is the highest possible financial saving per message.

#### E. Line-Bounded File Views
* When inspecting files, never read whole source directories or massive modules. Always pass explicit `StartLine` and `EndLine` parameters to `view_file` to target only the active code block.
* **Benefit**: Avoids bloating the context window with thousands of lines of unedited code.

---
*Locked for Production. Antigravity OS v3.0. Optimized for rigorous engineering.*
