# Antigravity OS — Technical Architecture

Global execution kernel for high-end software engineering.

## 1. DIRECTORY STRUCTURE

### `agents/`
- **Content:** Markdown personas (e.g., `planner.md`, `reviewer.md`).
- **Function:** Defines system role behavior, expertise, and tool prioritization. Linked via junction to allow `@agent` mentions in IDE.

### `commands/`
- **Content:** Technical logic for `/slash` commands.
- **Function:** Defines exact execution phases (PLANNING -> BUILD -> AUDIT). Reroutes high-level requests into structured workflows.

### `hooks/`
- **Content:** PowerShell and Bash scripts.
- **Function:** Git automation. `pre-commit` checks state sync. `lint-on-save` enforces code quality.

### `mcps/`
- **Content:** MCP server configurations.
- **Function:** Extends AI capabilities (Github, Linear, Filesystem, Memory) through standardized protocols.

### `prompts/`
- **Content:** `tools.md`.
- **Function:** Fine-grained instructions for internal tool usage (grep, multi-replace, etc).

### `rules/`
- **Content:** Domain-specific enforcement (e.g., `frontend.md`, `api.md`).
- **Function:** Binding constraints checked during the VERIFY phase. BANS anti-patterns (prop-drilling, raw SQL, etc).

### `scripts/`
- **Content:** `ag-init.ps1`.
- **Function:** The Master Linker. Runs in new projects to create junctions and seed project-local state.

### `skill-system/`
- **Content:** Maintenance guides and templates.
- **Function:** Logic for creating, importing, and updating skills without registry drift.

### `skills/`
- **Content:** The 17 Master Skills (e.g., `repo-analysis`, `ui-design-expert`).
- **Function:** Grounded knowledge bases. Loaded on-demand (Lazy Load) to provide specialized context for complex tasks.

### `workflows/`
- **Content:** Markdown wrappers for slash commands.
- **Function:** IDE-facing descriptions for the `/command` bridge.

---

## 2. CORE FILES

- **`AGENTS.md`**: The OS Constitution. Defines routing, complexity gate, and safety tiers.
- **`GEMINI.md`**: Force-injected authority rules (User Rules). Synchronized with kernel.
- **`settings.json`**: Machine-readable config for auto-execution and behavior flags.
- **`SKILLS_REGISTRY.json`**: Hard-coded list of active skills to prevent ghost loading.
- **`validate_agents.py`**: Integrity checker for the global registry.

---

## 3. STATE MANAGEMENT
- **`STATE.md`**: Project-root. Long-term tech memory.
- **`task.md`**: Project-root. Session tracker.
*The OS uses project-local state to prevent context leakage between different codebases.*

---
*Locked for Production. v2.1.*
