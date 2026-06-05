# CAPABILITIES.md — Live Skill Routing Index

This file is a machine-readable index of all available skills in the Antigravity OS.
It is used by the system to identify which skills can be loaded for a given task.

## Available Skills (33 Master Skills — Consolidated Registry)

### TIER 1 — Production Safe
- `advanced-responsive-patterns`
- `api-design-principles`
- `backend-dev-guidelines` *(Tier 1 for CRUD; Tier 2 under distributed/ORM constraints)*
- `caveman-mode`
- `ecc-database-migrations`
- `ecc-docker-patterns`
- `ecc-postgres-patterns`
- `ecc-taste-dials`
- `ecc-design-critique`
- `ecc-hydration-performance`
- `framer-motion-patterns`
- `gsap-scroll-patterns`
- `motion-accessibility`
- `microinteractions`
- `nextjs-app-router-patterns`
- `performance-engineering`
- `repo-analysis`
- `seo-metadata-patterns`
- `spec-driven-build`
- `skill-generation-expert`
- `testing-quality-engineering`
- `threejs-r3f-fundamentals`
- `devops-deployment-automation`

### TIER 2 — Conditional (Validation Required Before Output)
- `frontend-architecture-patterns`
- `graphify`
- `ui-design-expert`
- `modern-database-orchestration`
- `ai-rag-architectures`
- `webgl-shader-basics`

### TIER 3 — Redesigned (New Strategy Only, Legacy Logic Forbidden)
- `react-performance-optimizations`
- `huashu-deck-pdf-export`
- `huashu-html-to-pptx-conversion`

### VIDEO RENDERING SUITE (Remotion)
- `huashu-video-rendering`
- `remotion-composition-metadata`
- `remotion-dynamic-frame-logic`
- `remotion-sequence-timing`
- `remotion-video-config-context`
- `remotion-video-template`
- `remotion-web-player-integration`

---

## Skill Routing Quick Reference

| Task Category | Primary Skill | Supporting Skill |
|---------------|---------------|------------------|
| Unit/Integration/E2E testing | `testing-quality-engineering` | `backend-dev-guidelines` |
| Database schema + ORM work | `modern-database-orchestration` | `ecc-database-migrations`, `ecc-postgres-patterns` |
| Database migrations (safe) | `ecc-database-migrations` | `ecc-postgres-patterns` |
| Docker / CI/CD / Deployment | `devops-deployment-automation` | `ecc-docker-patterns` |
| Containerization patterns | `ecc-docker-patterns` | `devops-deployment-automation` |
| RAG / Vector search / Embeddings | `ai-rag-architectures` | — |
| REST/GraphQL API design | `api-design-principles` | `backend-dev-guidelines` |
| Backend service logic | `backend-dev-guidelines` | `testing-quality-engineering` |
| Frontend page architecture | `frontend-architecture-patterns` | `ecc-design-critique`, `ecc-taste-dials` |
| UI polish / component design | `ui-design-expert` | `ecc-taste-dials` |
| Scroll storytelling / GSAP animation | `gsap-scroll-patterns` | `motion-accessibility` |
| Framer Motion / entrance/exit/stagger | `framer-motion-patterns` | `motion-accessibility` |
| Page transitions (Next.js) | `framer-motion-patterns` | `frontend-architecture-patterns` |
| Motion accessibility / WCAG compliance | `motion-accessibility` | `framer-motion-patterns`, `gsap-scroll-patterns` |
| 3D hero / product showcase / WebGL | `threejs-r3f-fundamentals` | `webgl-shader-basics` |
| Custom shaders / gradient backgrounds | `webgl-shader-basics` | `threejs-r3f-fundamentals` |
| Next.js project structure / routing | `nextjs-app-router-patterns` | `ecc-hydration-performance` |
| Performance optimization / budgets | `performance-engineering` | `ecc-hydration-performance` |
| Responsive layout implementation | `advanced-responsive-patterns` | `frontend-architecture-patterns` |
| SEO / metadata / structured data | `seo-metadata-patterns` | `nextjs-app-router-patterns` |
| Microinteractions & UI feedback | `microinteractions` | `ui-design-expert`, `framer-motion-patterns` |
| Codebase knowledge graph creation | `graphify` | `repo-analysis` |
| Web performance / font loading | `ecc-hydration-performance` | `react-performance-optimizations` |
| React performance tuning | `react-performance-optimizations` | — |
| Feature planning / specs | `spec-driven-build` | `repo-analysis` |
| Unknown codebase analysis | `repo-analysis` | — |
| Generating new skills / learning from links | `skill-generation-expert` | — |
| Video rendering (Remotion) | `huashu-video-rendering` | `remotion-*` suite |
| PDF/PPTX export | `huashu-deck-pdf-export` / `huashu-html-to-pptx-conversion` | — |
| Token efficiency / Context hygiene | `caveman-mode` | `rules/performance.md` |

---

## Deprecated Skills (DO NOT LOAD — Absorbed into Master Skills)
The following legacy skill names no longer exist as directories.
They were consolidated during the April 2026 registry normalization.

- ~~gsd-deliverable-verification~~ → absorbed into `spec-driven-build`
- ~~gsd-new-project-planning~~ → absorbed into `spec-driven-build`
- ~~gsd-parallel-wave-execution~~ → absorbed into `spec-driven-build`
- ~~gsd-security-enforcement~~ → absorbed into `backend-dev-guidelines`
- ~~gsd-xml-plan-generation~~ → absorbed into `spec-driven-build`
- ~~huashu-core-skill-prompt~~ → absorbed into `ui-design-expert`
- ~~huashu-test-prompt-evaluation~~ → retired
- ~~impeccable-color-contrast~~ → absorbed into `ui-design-expert`
- ~~impeccable-interaction-states~~ → absorbed into `ui-design-expert`
- ~~impeccable-motion-curves~~ → absorbed into `ui-design-expert`
- ~~impeccable-spatial-grids~~ → absorbed into `ui-design-expert`
- ~~impeccable-typography-system~~ → absorbed into `ui-design-expert`
- ~~pro-max-app-interface-patterns~~ → absorbed into `frontend-architecture-patterns`
- ~~pro-max-data-visualization~~ → absorbed into `frontend-architecture-patterns`
- ~~pro-max-landing-page-architecture~~ → absorbed into `frontend-architecture-patterns`
- ~~pro-max-react-performance-optimizations~~ → absorbed into `react-performance-optimizations`
- ~~pro-max-ux-guidelines~~ → absorbed into `frontend-architecture-patterns`
