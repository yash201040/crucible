---
type: "Reference"
title: "Result cost fields and subagent coverage"
description: "total_cost_usd and modelUsage include subagent spend while usage excludes it; background subagents are awaited before the result."
resource: "https://code.claude.com/docs/en/agent-sdk/cost-tracking"
tags: [subagents, cost, usage, result-message]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "total_cost_usd"
  - "usage"
  - "modelUsage"
  - "model_usage"
  - "duration_api_ms"
  - "SDKResultMessage"
  - "ResultMessage"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-cost-tracking"
    resource: "https://code.claude.com/docs/en/agent-sdk/cost-tracking"
    title: "Track cost and usage"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The result message (`SDKResultMessage` in TypeScript, `ResultMessage` in Python) marks the end of the agent loop and carries `total_cost_usd`, the cumulative estimated cost across all steps in that call (including earlier session spend on a resumed call). In Python the field is optional: check for `None`. Success and error results both carry it, though the final result of a session crash may carry it zeroed.

# How to use it

| Field | Subagent activity |
| - | - |
| `usage` | Excluded; counts only the top-level agent loop |
| `total_cost_usd` | Included |
| `modelUsage` / `model_usage` | Included, broken down by model |

Use `modelUsage` / `model_usage` for whole-tree token accounting; `usage` undercounts once subagents nest. To bound subagent spend, use the depth, concurrency and spend limits on the subagents page.

# Notes

In single message input mode, Claude Code waits for background subagents still running at the end of the final turn (up to the cap in the headless page, background tasks at exit) before emitting the result; `total_cost_usd`, `duration_api_ms` and `modelUsage` include that wait. In a single-shot `query()`, an error result is yielded and then the call throws; connection or process failures yield no result.
