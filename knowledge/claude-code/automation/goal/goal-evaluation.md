---
type: "Concept"
title: "How /goal evaluation and cost work"
description: "Verdicts of the evaluator model, the no-progress stop, and which model evaluates and bills."
resource: "https://code.claude.com/docs/en/goal"
tags: [goal, evaluator, haiku, cost]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "ANTHROPIC_DEFAULT_HAIKU_MODEL"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "goal"
    resource: "https://code.claude.com/docs/en/goal"
    title: "Keep Claude working toward a goal"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`/goal` wraps a session-scoped prompt-based Stop hook. When Claude finishes a turn, Claude Code sends the condition and the conversation so far to your configured small fast model, which returns one verdict with a short reason:

- **Not yet met**: Claude keeps working, using the reason as guidance.
- **Met**: goal cleared, an achieved entry recorded.
- **Impossible**: goal cleared, a failed entry recorded with the reason; no manual clear needed.

If Claude answers the evaluator without progress (no tool use for several turns in a row), Claude Code stops the loop, prints a warning and returns control with the goal still set; evaluation resumes after your next prompt. The underlying cap is the Stop hook block cap.

# How to use it

To evaluate on a different model set `ANTHROPIC_DEFAULT_HAIKU_MODEL`. Warning: Claude Code reads it wherever it uses the small fast model, so it also resolves the `haiku` alias to that model and runs session title generation and some other background tasks on it.

# Limits and defaults

The evaluator runs on the provider your session uses. It calls no tools, so it judges only what Claude surfaced. Evaluation tokens bill on the provider's small fast model and are typically negligible versus main-turn spend.
