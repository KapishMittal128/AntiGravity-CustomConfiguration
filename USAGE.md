# Antigravity OS — Professional Usage & Prompting Guide

This guide provides high-fidelity strategies for utilizing Antigravity OS to its maximum potential. Whether starting a new project from scratch or maintaining a legacy system, these workflows ensure rigorous, production-grade output.

---

## 1. Project Initialization & The Authority Gate

### How it works
The `scripts/ag-init.ps1` script creates a **Junction Link** (`.agents/`). 
1. **Detection:** When an AI agent (like Gemini, Claude, or ChatGPT) reads the workspace, it sees the `.agents/` directory.
2. **Authority:** The presence of `AGENTS.md` inside that directory triggers a "Global Rule" in the AI's internal logic. It realizes it is no longer a general assistant but a **Component of Antigravity OS**.
3. **Execution:** It will immediately prioritize Section 0 (Complexity Gate) and apply the 17 Master Skills.

### Initialization Workflow
1. Create your project folder.
2. Run: `powershell -ExecutionPolicy Bypass -File C:\Users\Kapish\.antigravity\ag-init.ps1`.
3. Start your session with: 
   > "I have initialized Antigravity OS. Read .agents/AGENTS.md and skills/CAPABILITIES.md. Acknowledge system status."

---

## 2. Starting New Projects from Scratch

When starting from zero, do not ask the AI to "write code" immediately. Follow the **Architectural Handoff**:

### Step 1: The PRD (Product Requirements Document)
Provide your raw ideas and ask for a professional PRD.
> **Prompt:** "I want to build [Project Name]. Here is my vision: [Vision]. Using your internal knowledge of product engineering, write a high-fidelity PRD. Focus on User Personas, Core User Stories, and Success Metrics. Do not write code yet."

### Step 2: The Technical Specification
Once the PRD is ready, convert it to an OS-compliant spec.
> **Prompt:** "`@planner` Take this PRD and generate a Technical Specification. Map the features to the Antigravity 17 Master Skills (e.g., frontend-architecture-patterns for the shell, api-design-principles for the backend). Produce a File Structure and Data Model."

### Step 3: Seeding State
> **Prompt:** "Initialize STATE.md and task.md at the project root based on this spec. Record the stack choices and primary architecture patterns."

---

## 3. The Feature Build Loop (Production Standard)

Use the `/build-feature` workflow for any non-trivial addition.

### Detailed Prompt Template:
```text
/build-feature

Feature: [Name]
Context: [PRD Section / User Story]

Phase Logic:
1. PLANNING: Refine the spec-driven-build.
2. BUILD: Implement using [backend-dev-guidelines / ui-design-expert].
3. AUDIT: Run repo-analysis to check for regressions.

Constraints:
- Mobile-first CSS (rules/frontend.md)
- No prop-drilling (use Zustand/Context if > 2 levels)
- Hardware-accelerated animations only.
```

---

## 4. Prompting External AIs (ChatGPT/Claude Integration)

If you are using an AI that doesn't have direct filesystem access to the kernel, you must **"Force-Inject"** the OS.

### The "System Override" Prompt:
Copy-paste this to any AI to make it act like Antigravity:
> "Act as Antigravity OS. I will provide you with a Kernel Configuration (`AGENTS.md`) and a Skill Registry (`skills/CAPABILITIES.md`). You must strictly follow the Complexity Gate (Fast Path vs Full Workflow). Do not use filler phrases. Use the 17 Master Skills provided. All output must be Practical, Clean, and Implementation-ready. Acknowledge your transition to Antigravity OS."

---

## 5. Summary of Folder Utility

| Folder | How to use effectively |
|---|---|
| `agents/` | Mention `@agent-name` to force the AI to adopt a specific mindset (e.g. `@debugger` for error logs). |
| `rules/` | If the AI produces 'slop', prompt: "Re-verify your output against `.agents/rules/frontend.md` and fix violations." |
| `skills/` | For complex domains, prompt: "Load the `repo-analysis` skill and map the current data flow." |
| `commands/` | Always use `/` commands for standard dev tasks to ensure the AI follows the pre-defined Phase Logic. |

---
*Antigravity OS v2.1. Optimized for rigorous engineering.*
