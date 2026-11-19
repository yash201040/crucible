---
type: "Guide"
title: "Reduce tokens: thinking and subagents"
description: "Lower extended-thinking cost with effort levels or MAX_THINKING_TOKENS, and delegate verbose work to cheaper subagents."
resource: "https://code.claude.com/docs/en/costs"
tags: [thinking, effort, subagents, max-thinking-tokens, cost]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: "Fixed-budget models for MAX_THINKING_TOKENS"
identifiers:
  - "MAX_THINKING_TOKENS"
  - "/effort"
  - "/model"
  - "/config"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "costs"
    resource: "https://code.claude.com/docs/en/costs"
    title: "Manage costs effectively"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Extended thinking is on by default; thinking tokens are billed as output tokens and the default budget can be tens of thousands of tokens per request depending on the model.

# How to use it

- Lower the effort level with `/effort` or in `/model`, or disable thinking in `/config`.
- On models with a fixed thinking budget set `MAX_THINKING_TOKENS`, e.g. `MAX_THINKING_TOKENS=8000`. Adaptive-reasoning models ignore nonzero budgets; use effort levels there.
- Delegate verbose work (tests, docs fetching, log processing) to subagents so only a summary returns to the main conversation. Subagent requests still draw on your usage; choose a smaller model for a subagent or run every subagent on one model.

# Limits and defaults

- Thinking cannot be turned off on Opus 5.5, Sonnet 5.5, Haiku 5.5 or the Fable models; they always use extended thinking.
