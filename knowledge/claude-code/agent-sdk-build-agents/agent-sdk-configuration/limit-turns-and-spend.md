---
type: "Limit"
title: "maxTurns and maxBudgetUsd caps"
description: "Turn and spend caps, their result subtypes, and how single-shot and streaming input handle hitting them."
resource: "https://code.claude.com/docs/en/agent-sdk/configuration"
tags: [limits, budget, max-turns, cost]
kind: "limit"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "maxTurns"
  - "max_turns"
  - "maxBudgetUsd"
  - "max_budget_usd"
  - "error_max_turns"
  - "error_max_budget_usd"
  - "/clear"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-configuration"
    resource: "https://code.claude.com/docs/en/agent-sdk/configuration"
    title: "Configure your agent"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`maxTurns` / `max_turns` caps turns; `maxBudgetUsd` / `max_budget_usd` caps spend. Both are off when unset. Hitting a cap ends the run with a result whose subtype is `error_max_turns` or `error_max_budget_usd`.

# How to use it

| Mode | Behavior on a cap result |
| - | - |
| Single-shot `query()` | SDK yields the cap result then raises; wrap in try to continue |
| Streaming input | session stays alive; max-turns count restarts for each queued message; budget accumulates across messages, so after spend reaches the cap later messages end with the same budget result; `/clear` restarts the budget |
| Streaming input in TypeScript | loop throws when the last response ends in an error result such as `error_max_turns`; wrap in try |

# Limits and defaults

- `maxTurns` `0` means no limit, same as unset.
- `maxBudgetUsd` `0` is rejected by the CLI at startup as an invalid amount and the session never runs.
- Subagent spend is covered in the agent-loop page (Turns and budget).
