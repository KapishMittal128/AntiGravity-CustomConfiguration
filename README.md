<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0D0D0D,50:6D28D9,100:EC4899&height=220&section=header&text=ANTIGRAVITY%20OS&fontSize=60&fontColor=FFFFFF&animation=fadeIn&fontAlignY=35&desc=The%20AI%20Execution%20Kernel&descSize=18&descAlignY=55&descAlign=50" width="100%" />

<br/>

<a href="https://github.com/KapishMittal128/AntiGravity-CustomConfiguration"><img src="https://img.shields.io/badge/Kernel-v3.0.0-6D28D9?style=for-the-badge&logo=atom&logoColor=white" /></a>
<img src="https://img.shields.io/badge/Skills-40_Active-10B981?style=for-the-badge&logo=stackblitz&logoColor=white" />
<img src="https://img.shields.io/badge/Validator-0_Errors-059669?style=for-the-badge&logo=checkmarx&logoColor=white" />
<img src="https://img.shields.io/badge/Target-60_FPS-EC4899?style=for-the-badge&logo=speedtest&logoColor=white" />
<img src="https://img.shields.io/badge/WCAG-AA_Compliant-3B82F6?style=for-the-badge&logo=accessibility&logoColor=white" />

<br/><br/>

<samp>
<b>Turn any language model into a disciplined software build system.</b>
<br/>
Awwwards-caliber frontends · Production-grade backends · AI/RAG pipelines · Zero slop.
</samp>

<br/><br/>

<kbd>&nbsp; PLANNING &nbsp;</kbd>&nbsp;&nbsp;▸&nbsp;&nbsp;<kbd>&nbsp; BUILD &nbsp;</kbd>&nbsp;&nbsp;▸&nbsp;&nbsp;<kbd>&nbsp; AUDIT &nbsp;</kbd>&nbsp;&nbsp;▸&nbsp;&nbsp;<kbd>&nbsp; SHIP &nbsp;</kbd>

<br/><br/>

<a href="#-quickstart">Quickstart</a>&nbsp;&nbsp;•&nbsp;&nbsp;<a href="#-how-it-works">How It Works</a>&nbsp;&nbsp;•&nbsp;&nbsp;<a href="#-agent-roster">Agents</a>&nbsp;&nbsp;•&nbsp;&nbsp;<a href="#-skill-library">Skills</a>&nbsp;&nbsp;•&nbsp;&nbsp;<a href="#-blueprints">Blueprints</a>&nbsp;&nbsp;•&nbsp;&nbsp;<a href="#-prompt-guide">Prompts</a>&nbsp;&nbsp;•&nbsp;&nbsp;<a href="#-cost-control">Cost Control</a>

</div>

<br/>

## ⚡ Quickstart

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

<br/>

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=27&height=2" width="100%" />
</div>

<br/>

## 🧠 How It Works

Every incoming request passes through the **Complexity Gate** before a single line of code is written:

```
                    ╭─────────────────────────╮
                    │    Incoming Request      │
                    ╰────────────┬────────────╯
                                 │
                                 ▼
                   ┌─────────────────────────┐
                   │   COMPLEXITY GATE CHECK  │
                   └────────────┬────────────┘
                                │
              ┌─────────────────┴──────────────────┐
              │                                    │
     ╭────────▼────────╮              ╭────────────▼────────────╮
     │   ✅ FAST PATH   │              │   🔄 FULL WORKFLOW      │
     │                  │              │                         │
     │  Direct execute  │              │  PLAN → BUILD → AUDIT   │
     │  Zero overhead   │              │  Lazy-load 2-3 skills   │
     │  No agents       │              │  Agent-routed execution │
     ╰──────────────────╯              ╰─────────────────────────╯
```

<table>
<tr>
<td width="50%">

### 🟢 Fast Path (DirectOps)

Tasks that are **small, local, and single-pass**:
- Isolated bug fixes
- File reads & grep searches
- Simple terminal commands
- Single-file edits under ~15 min

**Result →** Zero skill loading, zero agent switching, zero overhead.

</td>
<td width="50%">

### 🟣 Full Workflow

Tasks with **architectural impact**:
- Data model / schema changes
- Shared interface modifications
- Multi-file feature builds
- Destructive or ambiguous operations

**Result →** Phased execution with verification gates at every stage.

</td>
</tr>
</table>

<br/>

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=27&height=2" width="100%" />
</div>

<br/>

## 🤖 Agent Roster

Six specialized agents. One active at a time. Each brings a distinct engineering mindset.

<table>
<tr>
<td align="center" width="16.6%">
<br/>
<samp><b>@planner</b></samp>
<br/><br/>
<img src="https://img.shields.io/badge/-Architecture-6D28D9?style=flat-square" />
<br/><br/>
<sub>Specs · File layout<br/>Schema planning<br/>Tech decisions</sub>
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
<sub>Visual hierarchy<br/>Motion · WebGL<br/>Responsive layout</sub>
<br/><br/>
</td>
<td align="center" width="16.6%">
<br/>
<samp><b>@backend</b></samp>
<br/><br/>
<img src="https://img.shields.io/badge/-Services-10B981?style=flat-square" />
<br/><br/>
<sub>APIs · Auth<br/>Data pipelines<br/>Security gates</sub>
<br/><br/>
</td>
<td align="center" width="16.6%">
<br/>
<samp><b>@ai-engineer</b></samp>
<br/><br/>
<img src="https://img.shields.io/badge/-AI%2FRAG-F59E0B?style=flat-square" />
<br/><br/>
<sub>Embeddings · RAG<br/>Prompt systems<br/>Vector search</sub>
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

<br/>

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=27&height=2" width="100%" />
</div>

<br/>

## 📦 Skill Library

**40 production-grade skills**, lazy-loaded on demand. Budget: **0** for trivial tasks · **2** for simple · **3** max for complex.

<details>
<summary><b>🎨 Frontend & Motion</b> — 16 skills</summary>
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
<summary><b>⚙️ Backend & Data</b> — 9 skills</summary>
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
<summary><b>🧠 AI & Knowledge</b> — 4 skills</summary>
<br/>

| Skill | Purpose |
|:------|:--------|
| `ai-rag-architectures` | Embeddings, vector schemas, retrieval pipelines |
| `graphify` | BFS knowledge graph pipeline, community clustering |
| `skill-generation-expert` | Ingest web links into custom skill definitions |
| `repo-analysis` | Dependency structures, dynamic call tracing |

</details>

<details>
<summary><b>🎬 Media & Export</b> — 9 skills</summary>
<br/>

| Skill | Purpose |
|:------|:--------|
| `huashu-deck-pdf-export` | CSS media print styling, page-break overrides |
| `huashu-html-to-pptx-conversion` | JSON to PptxGenJS direct transformation |
| `huashu-video-rendering` | Remotion video compiler configurations |
| `remotion-*` (6 skills) | Sequence delay, frame index, video rendering |

</details>

<details>
<summary><b>🛠️ System & Workflow</b> — 2 skills</summary>
<br/>

| Skill | Purpose |
|:------|:--------|
| `caveman-mode` | High-efficiency terse output (75% token savings) |
| `spec-driven-build` | PRD to specs, detailed implementation maps |

</details>

<br/>

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=27&height=2" width="100%" />
</div>

<br/>

## 🗡️ Commands & Slash Bridge

Type a slash command to trigger a structured execution workflow.

<div align="center">

| Command | Action | Phase |
|:--------|:-------|:------|
| `/build-feature` | New feature, endpoint, or page | `PLAN → BUILD → AUDIT → SHIP` |
| `/fix-issue` | Bug diagnosis and fix | `DIAGNOSE → FIX → VERIFY` |
| `/review-code` | Code quality audit | `SCAN → REPORT → RECOMMENDATIONS` |
| `/refactor` | Clean up, simplify, restructure | `ANALYZE → REFACTOR → VERIFY` |
| `/ship-ui` | Polish UI to production quality | `AUDIT → POLISH → SHIP` |
| `/research` | Tech decision, library comparison | `GATHER → ANALYZE → RECOMMEND` |
| `/caveman` | Activate terse output mode | Immediate |

</div>

### Command Safety Tiers

> [!NOTE]
> **Tier 1 — Auto-Execute**: `git status`, `npm run test`, `npx tsc --noEmit`
>
> **Tier 2 — Propose First**: `npm install`, `git commit`, `prisma migrate dev`
>
> **Tier 3 — Explicit Approval**: Production migrations, git history rewrites
>
> **Tier 4 — Permanently Blocked**: `cat .env`, `rm -rf`, `git push --force` ⛔

<br/>

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=27&height=2" width="100%" />
</div>

<br/>

## 🏗️ Blueprints

Production-ready recipes for common build patterns. Each blueprint specifies the exact agent, skills, and rules.

<details>
<summary><b>Blueprint A — Awwwards-Caliber SaaS Marketing Site</b></summary>
<br/>

**Agent**: `@frontend` · **Skills**: `threejs-r3f-fundamentals`, `gsap-scroll-patterns`, `advanced-responsive-patterns` · **Rule**: `rules/frontend.md`

**Recipe:**
1. Initialize dynamic template layout (`template.tsx` in Next.js) for page entrance transitions
2. Load GSAP `ScrollTrigger` with `useGSAP` hook for safe mounting/cleanup
3. Configure R3F canvas inside dynamic `ssr: false` component to split from initial bundle
4. Cap DPR at `[1, 1.5]` and use `webgl-shader-basics` for 60fps frame budgets

**Prompt Template:**
```
@frontend Load skills `threejs-r3f-fundamentals`, `gsap-scroll-patterns`, `advanced-responsive-patterns`.

Implement an Awwwards-style SaaS marketing hero:
1. Dynamic Canvas in template.tsx loading a Draco-compressed GLB model.
2. Camera target animated along GSAP timeline synced to ScrollTrigger pinning.
3. ScrollTrigger anticipatePin: 1, scrub capped at 0.8.
4. prefers-reduced-motion handled via gsap.matchMedia().
```

**Anti-Patterns:** ❌ Mixing Framer Motion + GSAP · ❌ Animating `top`/`left`/`width` · ❌ Uncompressed 3D models >5MB

</details>

<details>
<summary><b>Blueprint B — High-Density Analytics Dashboard</b></summary>
<br/>

**Agent**: `@frontend` · **Skills**: `frontend-architecture-patterns`, `react-performance-optimizations`, `ui-design-expert` · **Rule**: `rules/frontend.md`

**Recipe:**
1. Select tone pack from `ecc-aesthetic-tones` (Utilitarian Pastel or Monospace Brutalist)
2. Calibrate taste dials: low motion intensity, high visual density
3. Virtualized rendering for lists exceeding 100 rows
4. Typographic leading audit via `ecc-design-critique` to eliminate CLS

**Anti-Patterns:** ❌ Nested scrollable grids · ❌ Hardcoded primary colors · ❌ Full table re-renders on scroll

</details>

<details>
<summary><b>Blueprint C — Production-Grade AI RAG Product</b></summary>
<br/>

**Agent**: `@ai-engineer` · **Skills**: `ai-rag-architectures`, `graphify`, `modern-database-orchestration` · **Rule**: `rules/backend.md`

**Recipe:**
1. Initialize vector DB with dynamic connection pools
2. Parse unstructured files into normalized markdown nodes
3. Build community clustering index for cross-file relationships
4. Semantic search with strict token budgets

**Anti-Patterns:** ❌ Unchunked documents in LLM context · ❌ Embeddings without query indices · ❌ Synchronous embedding in HTTP loops

</details>

<details>
<summary><b>Blueprint D — Bulletproof Database & API Backend</b></summary>
<br/>

**Agent**: `@backend` · **Skills**: `api-design-principles`, `backend-dev-guidelines`, `modern-database-orchestration` · **Rule**: `rules/backend.md`

**Recipe:**
1. Type-safe schemas with Prisma or Drizzle ORM
2. Isolated DDL/DML migrations separating schema from data transforms
3. Postgres partial indexes + RLS security gates on sensitive tables
4. Standard REST envelope responses

**Anti-Patterns:** ❌ Raw unparameterized SQL · ❌ Mixed DDL+DML migrations · ❌ Exposed internal keys in responses

</details>

<br/>

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=27&height=2" width="100%" />
</div>

<br/>

## 💬 Prompt Guide

The difference between mediocre output and production-grade output is prompt structure.

<table>
<tr>
<td width="50%">

### ❌ Bad Prompt

```
Make me a cool landing page with
cool 3D animations and page
transitions in NextJS.
```

<sub><b>Why it fails:</b> Indefinite scope, no performance boundaries, forces the model to guess everything. You get jerky animations, slow canvas, and Framer/GSAP conflicts.</sub>

</td>
<td width="50%">

### ✅ Good Prompt

```
@frontend Load skills
`threejs-r3f-fundamentals`,
`gsap-scroll-patterns`,
`advanced-responsive-patterns`.
Apply rule `rules/frontend.md`.

Build a Next.js App Router landing
page with a scroll-pinned 3D hero:
1. Dynamic import canvas, ssr: false
2. 5 breakpoints, mobile-first grids
3. Camera → ScrollTrigger + useGSAP
4. prefers-reduced-motion fallback
```

<sub><b>Why it works:</b> Named agent, explicit skills, specific constraints, measurable output criteria.</sub>

</td>
</tr>
</table>

> [!IMPORTANT]
> **The formula:** `@agent` + `skill names` + `rule file` + numbered, specific implementation steps = consistently excellent output.

<br/>

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=27&height=2" width="100%" />
</div>

<br/>

## 💰 Cost Control

Every LLM call costs tokens. Antigravity OS is designed to minimize waste without sacrificing depth.

<table>
<tr>
<td align="center" width="25%">
<br/>
<h3>🟢</h3>
<samp><b>DirectOps</b></samp>
<br/><br/>
<sub>Fast Path bypasses agent & skill loading<br/><b>Saves 10K+ tokens/turn</b></sub>
<br/><br/>
</td>
<td align="center" width="25%">
<br/>
<h3>📦</h3>
<samp><b>Skill Budget</b></samp>
<br/><br/>
<sub>0 / 2 / 3 skill limits<br/><b>Prevents attention dilution</b></sub>
<br/><br/>
</td>
<td align="center" width="25%">
<br/>
<h3>🔄</h3>
<samp><b>40% Rule</b></samp>
<br/><br/>
<sub>Compact at 40% context usage<br/><b>Recovers 20-50K+ tokens</b></sub>
<br/><br/>
</td>
<td align="center" width="25%">
<br/>
<h3>🦴</h3>
<samp><b>Caveman Mode</b></samp>
<br/><br/>
<sub>75% shorter output via <code>/caveman</code><br/><b>Highest $/msg savings</b></sub>
<br/><br/>
</td>
</tr>
</table>

### Context Hygiene Checklist

```
✦ Record decisions → STATE.md
✦ Check off milestones → task.md  
✦ Start fresh session → wipe history
✦ Preload only STATE.md + task.md → strategic continuity restored
✦ Use line-bounded file views → never read whole modules
```

> [!TIP]
> **Prompt caching** (supported by Anthropic, Gemini, OpenAI) reduces the ~15-20K system prompt baseline cost by up to **90%**. The OS is designed to be cache-friendly.

<br/>

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=27&height=2" width="100%" />
</div>

<br/>

<div align="center">

## 📐 Architecture

</div>

```
.agents/
├── AGENTS.md                    # System authority (source of truth)
├── README.md                    # This file
├── settings.json                # Permission flags & behavior config
├── STATE.md                     # Long-term architectural state
├── task.md                      # Active session operations
│
├── agents/                      # 6 specialized agent definitions
│   ├── planner.md
│   ├── debugger.md
│   ├── frontend.md
│   ├── backend.md
│   ├── ai-engineer.md
│   └── reviewer.md
│
├── commands/                    # Slash command workflows
│   ├── build-feature.md
│   ├── fix-issue.md
│   ├── review-code.md
│   ├── refactor.md
│   ├── ship-ui.md
│   └── research.md
│
├── rules/                       # Engineering constraints (VERIFY phase)
│   ├── frontend.md
│   ├── backend.md
│   ├── api.md
│   ├── database.md
│   ├── project-structure.md
│   └── done-criteria.md
│
├── skills/                      # 40 lazy-loaded skill modules
│   └── <skill-name>/SKILL.md
│
├── skill-system/                # Skill creation & maintenance
│   ├── skill-ingestion.md
│   └── skill-template.md
│
└── hooks/                       # Pre-commit & lint-on-save scripts
    └── *.ps1
```

<br/>

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=27&height=2" width="100%" />
</div>

<br/>

<div align="center">

<samp>Built for engineers who ship. Not for engineers who chat.</samp>

<br/><br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0D0D0D,50:6D28D9,100:EC4899&height=120&section=footer" width="100%" />

</div>
