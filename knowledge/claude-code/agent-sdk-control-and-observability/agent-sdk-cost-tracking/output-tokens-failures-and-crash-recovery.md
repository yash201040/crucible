---
type: "Concept"
title: "Output tokens, failed runs and crash recovery"
description: "Per-step output_tokens is a placeholder, error results still carry cost, and a crash may zero the final result."
resource: "https://code.claude.com/docs/en/agent-sdk/cost-tracking"
tags: [cost, errors, crash-recovery, output-tokens]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "output_tokens"
  - "error_during_execution"
  - "error_max_budget_usd"
  - "usage"
  - "total_cost_usd"
  - "modelUsage"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-cost-tracking"
    resource: "https://code.claude.com/docs/en/agent-sdk/cost-tracking"
    title: "Track cost and usage"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

- Output tokens: each assistant message carries the `output_tokens` the API reported at `message_start`, a placeholder shared by every message from one API response. Read real output tokens from the result's `usage`, or `modelUsage` per model.
- Failed conversations: success and error results both include `usage` and `total_cost_usd` (optional in Python; check for `None`). Read cost from every result whatever its `subtype`.
- On some error results `usage` under-reports: after a session crash every cost field may be zeroed (`error_during_execution`); on `error_max_budget_usd`, `usage` omits the response that crossed the budget while `total_cost_usd` and `modelUsage` include it. Prefer `total_cost_usd` or `modelUsage`.

# How to use it

Crash recovery: when the Claude Code process crashes it emits a final `error_during_execution` result and exits (single-shot and streaming alike), possibly with zeroed `usage`, `total_cost_usd`, `modelUsage`.
1. Use the result of the turn before the crash (running total in streaming input mode). Not usable if the call was single-shot, the crash was on the first turn, or the previous turn was the `/clear` itself.
2. Otherwise sum assistant-message `usage`, counting each API response once (single-shot: all; streaming: those after the last result). This recovers only main-loop input and cache tokens, not subagent usage, output tokens or USD.
