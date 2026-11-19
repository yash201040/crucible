---
type: "Concept"
title: "Cost totals in streaming input mode"
description: "Which result fields are per-turn or running totals in streaming input, and how /clear, /reset and /new reset them."
resource: "https://code.claude.com/docs/en/agent-sdk/cost-tracking"
tags: [streaming-input, cost, reset, accounting]
kind: "behavior"
maturity: "unlabelled"
since: "0.2.137"
surfaces: [sdk]
requires: "Streaming input mode"
identifiers:
  - "usage"
  - "total_cost_usd"
  - "modelUsage"
  - "model_usage"
  - "/clear"
  - "/reset"
  - "/new"
  - "SDKConversationResetMessage"
  - "ConversationResetMessage"
  - "maxBudgetUsd"
  - "max_budget_usd"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-cost-tracking"
    resource: "https://code.claude.com/docs/en/agent-sdk/cost-tracking"
    title: "Track cost and usage"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

In streaming input mode one `query()` call carries many user turns and each emits a result message. Field scope differs:
- `usage`: only that turn, and only the main agent loop (not subagents).
- `total_cost_usd` and `modelUsage` / `model_usage`: running total for the whole call so far, plus spend restored when the call resumed a session.

# How to use it

If the app never sends `/clear`, `/reset` or `/new`, read the latest result for call totals; do not sum. Those three commands restart the running totals (nothing else does inside a call). Then: the reset turn's own result covers only what ran since the reset and carries a new `session_id`; later results count from the reset; the last result before each reset holds the total since the previous reset. To total the whole call, add the last result before each reset to the final result.

Detect resets from the stream: TypeScript emits `SDKConversationResetMessage`; Python emits `ConversationResetMessage`. Before Python SDK v0.2.137 the iterator dropped it, so count resets yourself from the `/clear` turns you send.

`maxBudgetUsd` / `max_budget_usd` counts only the call's own spend: restored session totals do not count, and a `/clear` starts the budget over.
