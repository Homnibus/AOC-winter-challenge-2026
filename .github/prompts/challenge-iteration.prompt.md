---
description: "Generate an actionable Codingame iteration plan from league feedback, replays, and known bugs."
agent: "ask"
---

Create a compact, high-impact iteration plan for this Codingame bot.

Inputs:

- Current league level:
- Latest observed failures:
- Performance concerns:
- Constraints from game rules:
- Optional replay notes / seeds:
- Current strategy summary:
- Current test gaps:

If key inputs are missing, state assumptions explicitly before proposing changes.

Planning rules:

- Focus on the smallest safe change with highest expected impact.
- Prefer deterministic behavior over risky complexity.
- Keep per-turn runtime bounded and predictable.
- Propose changes that are easy to test and rollback.
- Do not claim performance gains without a verification method.

Required output:

1. Objective: one sentence.
2. Assumptions: only if needed.
3. Candidate hypotheses (max 3):
   - hypothesis
   - expected impact
   - risk
   - runtime cost
4. Selected hypothesis: explain why it wins on impact/risk ratio.
5. Minimal implementation plan:
   - exact files to change
   - behavior delta
   - fallback behavior
6. Tests to add/update:
   - regression case
   - edge case
   - expected assertions
7. Validation checklist:
   - local checks to run
   - measurable success signal
8. Rollback criteria: when to revert this iteration.
9. Commit message suggestions (max 3).

Output format constraints:

- Keep response under 220 lines.
- Use concise bullets.
- No generic advice; all points must be action-ready.
