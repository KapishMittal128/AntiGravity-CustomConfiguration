# Performance and Context Hygiene Rules

These are non-negotiable performance guidelines for managing LLM context budgets, ensuring optimal reasoning capacity, and preventing cognitive drift during long sessions.

## Context Hygiene Rules (The 40% Rule)

1. **Reasoning Optimization**:
   - LLM reasoning capability peaks when context usage is kept **below 40%** of the token window. Beyond 60%, reasoning accuracy and instruction adherence degrade significantly.

2. **Proactive Compaction & State Sync**:
   - If estimated session context exceeds **60%**, the active agent must immediately dump all current architectural truth, key decisions, and next steps to the project root `STATE.md` and `task.md`.
   - The agent must then suggest that the user run `/compact` (or manually start a fresh context session) to clear the active conversation history and restore a clean context footprint.

3. **Phase Threshold Evaluation**:
   - Before transitioning into any major execution phase (`PLANNING`, `BUILD`, `AUDIT`, `SHIP`), the active agent must estimate the context load.
   - If the context size is approaching the 60% limit, the agent must output a clear warning to the user before editing files or running commands.

4. **Preserving Headroom**:
   - Favor concise, factual checkpoint summaries and structured markdown diffs over long inline conversational explanations. 
   - Keep dialogue minimal and technical to maximize active token headroom for core code reasoning.
