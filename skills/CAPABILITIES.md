# CAPABILITIES.md — Live Skill Routing Index

This file is a machine-readable index of all available skills in the Antigravity OS.
It is used by the system to identify which skills can be loaded for a given task.

## Available Skills (21 Master Skills — Consolidated Registry)

### TIER 1 — Production Safe
- `api-design-principles`
- `backend-dev-guidelines` *(Tier 1 for CRUD; Tier 2 under distributed/ORM constraints)*
- `caveman-mode`
- `repo-analysis`
- `spec-driven-build`
- `testing-quality-engineering`
- `devops-deployment-automation`

### TIER 2 — Conditional (Validation Required Before Output)
- `frontend-architecture-patterns`
- `ui-design-expert`
- `modern-database-orchestration`
- `ai-rag-architectures`

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
| Database schema + ORM work | `modern-database-orchestration` | `backend-dev-guidelines` |
| Docker / CI/CD / Deployment | `devops-deployment-automation` | — |
| RAG / Vector search / Embeddings | `ai-rag-architectures` | — |
| REST/GraphQL API design | `api-design-principles` | `backend-dev-guidelines` |
| Backend service logic | `backend-dev-guidelines` | `testing-quality-engineering` |
| Frontend page architecture | `frontend-architecture-patterns` | `ui-design-expert` |
| UI polish / component design | `ui-design-expert` | — |
| React performance tuning | `react-performance-optimizations` | — |
| Feature planning / specs | `spec-driven-build` | `repo-analysis` |
| Unknown codebase analysis | `repo-analysis` | — |
| Video rendering (Remotion) | `huashu-video-rendering` | `remotion-*` suite |
| PDF/PPTX export | `huashu-deck-pdf-export` / `huashu-html-to-pptx-conversion` | — |
| Token efficiency | `caveman-mode` | — |

---

## Deprecated Skills (DO NOT LOAD — Absorbed into Master Skills)
The following legacy skill names no longer exist as directories.
They were consolidated during the April 2026 registry normalization.

- ~~`gsd-deliverable-verification`~~ → absorbed into `spec-driven-build`
- ~~`gsd-new-project-planning`~~ → absorbed into `spec-driven-build`
- ~~`gsd-parallel-wave-execution`~~ → absorbed into `spec-driven-build`
- ~~`gsd-security-enforcement`~~ → absorbed into `backend-dev-guidelines`
- ~~`gsd-xml-plan-generation`~~ → absorbed into `spec-driven-build`
- ~~`huashu-core-skill-prompt`~~ → absorbed into `ui-design-expert`
- ~~`huashu-test-prompt-evaluation`~~ → retired
- ~~`impeccable-color-contrast`~~ → absorbed into `ui-design-expert`
- ~~`impeccable-interaction-states`~~ → absorbed into `ui-design-expert`
- ~~`impeccable-motion-curves`~~ → absorbed into `ui-design-expert`
- ~~`impeccable-spatial-grids`~~ → absorbed into `ui-design-expert`
- ~~`impeccable-typography-system`~~ → absorbed into `ui-design-expert`
- ~~`pro-max-app-interface-patterns`~~ → absorbed into `frontend-architecture-patterns`
- ~~`pro-max-data-visualization`~~ → absorbed into `frontend-architecture-patterns`
- ~~`pro-max-landing-page-architecture`~~ → absorbed into `frontend-architecture-patterns`
- ~~`pro-max-react-performance-optimizations`~~ → absorbed into `react-performance-optimizations`
- ~~`pro-max-ux-guidelines`~~ → absorbed into `frontend-architecture-patterns`
