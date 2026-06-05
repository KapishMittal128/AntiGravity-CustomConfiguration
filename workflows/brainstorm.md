# Command: /brainstorm

## Purpose

Generates a wide range of creative and technical solutions for a given problem. Moves from divergent thinking (many ideas) to convergent selection (best path).

---

## Execution Workflow

### Phase 1: Divergent Ideation
1. Generate 3-5 distinct architectural or technical approaches.
2. For each approach, list:
   - Key mechanism
   - Unique advantage
   - Potential drawback

### Phase 2: Critical Evaluation
1. Compare the ideas against the project's current constraints (from `STATE.md`).
2. Identify which approach is "Optimal," which is "Fastest," and which is "Most Robust."

### Phase 3: Convergent Recommendation
1. Select the single best path.
2. Provide a high-level summary of why it was chosen.
3. Ask the user for approval to proceed to `/write-plan`.

---

## Constraints
- Do not provide generic advice.
- Every idea must be actionable within the current tech stack.
- Do not spend more than one pass on ideation unless the user asks for more.
