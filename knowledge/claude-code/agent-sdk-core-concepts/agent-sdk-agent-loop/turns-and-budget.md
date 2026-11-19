---
type: "Limit"
title: "Turn and budget limits"
description: "max_turns and max_budget_usd caps, subagent spend counting, budget headroom and streaming-input behavior."
resource: "https://code.claude.com/docs/en/agent-sdk/agent-loop"
tags: [budget, cost, limits, subagents]
kind: "limit"
maturity: "unlabelled"
since: "2.1.217"
surfaces: [sdk]
requires: ""
identifiers:
  - "max_turns"
  - "maxTurns"
  - "max_budget_usd"
  - "maxBudgetUsd"
  - "error_max_turns"
  - "error_max_budget_usd"
  - "Budget limit reached"
  - "total_cost_usd"
  - "/clear"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-agent-loop"
    resource: "https://code.claude.com/docs/en/agent-sdk/agent-loop"
    title: "How the agent loop works"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

| Option | Controls | Default |
| :- | :- | :- |
| `max_turns` / `maxTurns` | Maximum turns | No limit |
| `max_budget_usd` / `maxBudgetUsd` | Estimated spend at which the loop stops | No limit |

Hitting either returns a `ResultMessage` with subtype `error_max_turns` or `error_max_budget_usd`.

# How to use it

- The budget cap covers subagents: their spend counts toward the total. Once spend reaches the cap, spawning another subagent fails with `Budget limit reached` and Claude Code stops background subagents still running. These cap-enforcement behaviors need Claude Code v2.1.217 or later.
- With streaming input: a message queued when a turn ends at max turns stays queued and starts a new turn, and the max-turns count restarts. The budget total keeps accumulating across messages; once spend reaches `maxBudgetUsd`, later messages end with `error_max_budget_usd`. `/clear` restarts the budget.

# Limits and defaults

Budget headroom: spend is compared with the cap after model responses arrive (cost comes from returned token usage). The response that reaches the cap still completes and counts toward `total_cost_usd`, so spend can exceed the cap by up to one response plus what still-running subagents spend before they stop. Leave headroom.
