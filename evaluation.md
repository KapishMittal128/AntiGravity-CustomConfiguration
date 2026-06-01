# evaluation.md — Antigravity OS Current-State Snapshot

**Current Version:** v2.5.0  
**Last Updated:** 2026-04-28

This file is a concise assessment of the current `.agents` operating system.
It is not a policy source. `AGENTS.md`, `.agents/skills/RUNTIME_CONTROL.md`, and `.agents/skills/SYSTEM_ORCHESTRATION.md` remain authoritative.

---

## 1. Current Shape

Antigravity is now a compact operating layer with:
- one top-level policy file: `AGENTS.md`
- one runtime control file: `.agents/skills/RUNTIME_CONTROL.md`
- one orchestration file: `.agents/skills/SYSTEM_ORCHESTRATION.md`
- one routing index: `.agents/skills/CAPABILITIES.md`
- one normalized live skill library: 40 skills
- one machine-readable config mirror: `settings.json`

The system is substantially leaner and more internally consistent than the earlier mixed-format state.
It now also includes a mechanical validator for the `.agents` operating system itself.
It now defaults to Windows-native PowerShell hooks instead of requiring a Unix shell for core enforcement.

---

## 2. What Is Strong

- **Complexity routing is explicit.** Fast Path vs Full Workflow is clearly defined in `AGENTS.md`.
- **Runtime authority is singular.** `.agents/skills/RUNTIME_CONTROL.md` now owns checkpoints, lockouts, and state behavior.
- **Skill quality is normalized.** All live skills share the same metadata and section structure.
- **Command safety is explicit.** Command tiers and hook guidance are aligned.
- **State continuity exists but is bounded.** `STATE.md` records durable truth; `task.md` tracks the current frontier.
- **The OS can validate itself.** `validate_agents.py` checks structure, references, inventory drift, and config alignment.
- **Windows enforcement is first-class.** PowerShell hook equivalents now exist for pre-commit, state sync, and lint-on-save behavior.

---

## 3. What Was Cleaned Up

- Removed runtime-reference drift by standardizing on `.agents/skills/RUNTIME_CONTROL.md`
- Added compatibility aliases for legacy filenames
- Repaired the missing `repo-analysis` skill
- Normalized all 25 live skills to the same template
- Aligned MCP activation packs with installed MCP docs
- Reduced doc drift between support docs and real filesystem state
- Added `validate_agents.py` and wired it into the pre-commit hook path
- Converted hook configuration to PowerShell-first execution on Windows

---

## 4. Remaining Weak Spots

- **Policy surface is still text-heavy.** The OS is clearer than before, but `AGENTS.md` remains dense.
- **Enforcement is partly social.** Many guarantees still rely on instruction-following rather than hard mechanical locks.
- **Historical support docs can stale again.** `evaluation.md` and `versionperformance.md` must stay concise or they will reintroduce overlap.
- **Validator scope is only local-file integrity.** It does not yet test behavioral correctness of every rule.
- **Global copy drift remains possible.** If you edit the source `.agents` workspace, you still need to refresh the global copy manually or via your install workflow.

---

## 5. Practical Verdict

This `.agents` folder is now a strong reusable Antigravity workspace OS:
- good enough to use seriously
- much easier to maintain than before
- still best when treated as an operational ruleset, not a magical autopilot

If you keep one mental model, keep this:

`AGENTS.md` decides policy.  
`.agents/skills/RUNTIME_CONTROL.md` decides runtime behavior.  
`.agents/skills/SYSTEM_ORCHESTRATION.md` decides multi-skill flow.  
`.agents/skills/CAPABILITIES.md` decides which skill to reach for.

---

## 6. Changelog

- **v2.5.0**
  - Added PowerShell hook equivalents for pre-commit, state sync, and lint-on-save
  - Switched settings and docs to PowerShell-first enforcement on Windows
  - Kept legacy `.sh` hooks as compatibility fallbacks
- **v2.4.0**
  - Added `validate_agents.py` for structural and reference integrity checks
  - Wired validator execution into the pre-commit hook path and settings
  - Added `implementation_plan.md` as a real planning artifact target
- **v2.3.0**
  - Compressed non-skill docs into a cleaner authority structure
  - Replaced long overlapping evaluation text with a concise current-state snapshot
  - Recast `versionperformance.md` as a historical benchmark note
- **v2.2.1**
  - Runtime consistency patch
  - Skill inventory repair
  - Skill normalization across 25 live skills
