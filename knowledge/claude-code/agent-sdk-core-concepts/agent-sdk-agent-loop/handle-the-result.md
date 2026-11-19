---
type: "Reference"
title: "Result subtypes and stop_reason"
description: "ResultMessage subtypes, which fields every result carries, crash behavior and how errors raise from query()."
resource: "https://code.claude.com/docs/en/agent-sdk/agent-loop"
tags: [result, errors, cost, stop-reason]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "success"
  - "error_max_turns"
  - "error_max_budget_usd"
  - "error_during_execution"
  - "error_max_structured_output_retries"
  - "total_cost_usd"
  - "usage"
  - "model_usage"
  - "modelUsage"
  - "num_turns"
  - "session_id"
  - "stop_reason"
  - "end_turn"
  - "max_tokens"
  - "refusal"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-agent-loop"
    resource: "https://code.claude.com/docs/en/agent-sdk/agent-loop"
    title: "How the agent loop works"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

| Subtype | What happened | `result` field |
| :- | :- | :-: |
| `success` | Finished normally | Yes |
| `error_max_turns` | Hit `maxTurns` | No |
| `error_max_budget_usd` | Hit `maxBudgetUsd` | No |
| `error_during_execution` | Error interrupted the loop (e.g. cancelled request) | No |
| `error_max_structured_output_retries` | No valid structured output within retry limit (every attempt failed validation, or a model fallback retracted completed output with no successful retry) | No |

The `result` text exists only on `success`; check subtype first.

# How to use it

All subtypes carry `total_cost_usd`, `usage`, `num_turns`, `session_id`. `usage` covers only the main loop; use `modelUsage` / `model_usage` for whole-tree token and cost accounting. In Python `total_cost_usd`, `usage`, `model_usage` are optional, so check for `None`.

`stop_reason` (`string | null` / `str | None`): `end_turn`, `max_tokens`, `refusal`. On loop-produced errors it carries the last assistant response's value; after a crash it is `null`. Detect refusals with `stop_reason == "refusal"`.

# Limits and defaults

- After a session crash the final result is `error_during_execution`, cost fields may be zeroed, `stop_reason` `null`, and the process exits.
- A single-shot `query()` yields the final result then raises an error (e.g. `Reached maximum number of turns`); the process exits nonzero. A streaming input session stays alive (except after a crash); in TypeScript the loop throws when the last response ends in an error result.
