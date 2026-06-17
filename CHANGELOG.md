# Changelog

## [2.6.0] - 2026-06-17
### Fixed
- Fixed `/brainstorm` slash command with hard system constraint in AGENTS.md Section 6A (forces model to read workflow file before executing)
- Fixed `.agents/workflows/brainstorm.md` path reference that caused `validate_agents.py` to fail
- Cleaned all remnant references to deleted specialist agents (forge/bastion/oracle) from AGENTS.md routing tables and STATE.md

### Added
- Built context scaffold protocol: `STATE.md` (strategic truth) and `task.md` (tactical execution) templates with project-local scaffolding via `.agents/scripts/ag-init.ps1`
- Added `/brainstorm`, `/execute-plan`, `/write-plan` workflows to the slash command bridge

### Changed
- Evaluated and reverted specialist agents (forge/bastion/oracle) after analysis confirmed the original 6-agent system (planner/debugger/frontend/backend/ai-engineer/reviewer) is superior
- Synchronized all stale counts and version numbers across CAPABILITIES.md, USAGE.md, and evaluation.md

## [2.5.0] - 2026-04-29
### Added
- Added PowerShell hook equivalents for pre-commit, state sync, and lint-on-save
- Switched settings and docs to PowerShell-first enforcement on Windows
- Kept legacy `.sh` hooks as compatibility fallbacks

## [2.4.0] - 2026-04-28
### Added
- Added `validate_agents.py` for structural and reference integrity checks
- Wired validator execution into the pre-commit hook path and settings
- Added `implementation_plan.md` as a real planning artifact target

## [2.3.0] - 2026-04-28
### Changed
- Compressed non-skill docs into a cleaner authority structure
- Replaced long overlapping evaluation text with a concise current-state snapshot
- Recast `versionperformance.md` as a historical benchmark note

## [2.2.0] - 2026-04-28
### Fixed
- Runtime consistency patch: standardized on `.agents/skills/RUNTIME_CONTROL.md`
- Repaired the missing `repo-analysis` skill
- Aligned MCP activation packs with installed MCP docs

### Changed
- Normalized all 39 live skills to the same template with YAML frontmatter
- Reduced doc drift between support docs and real filesystem state

## [2.1.0] - 2026-05-30
### Added
- Added **skill-generation-expert** as a Tier 1 global skill to dynamically distill web URLs and documentation into new permanent Antigravity skills.

## [2.0.0] - 2026-04-29
### Added
- Integrated **Taste-Skill** as the master aesthetic filter (`design-taste-frontend`).
- Embedded **30+ Industry Palettes** into `impeccable-color-contrast`.
- Embedded **30+ Landing Patterns** into `pro-max-landing-page-architecture`.
- Embedded **Modular Scale Tables** into `impeccable-typography-system`.
- Added **Bauhaus and Glassmorphism** definitions to `pro-max-app-interface-patterns`.

### Changed
- Refactored all 25 skills to use real file-backed logic from cloned repos.
- Combined redundant Remotion metadata skills to make room for Taste-Skill.
- Strictly enforced the **Anti-Slop** rules (No Inter, No AI Purple).

