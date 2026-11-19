---
type: "Reference"
title: "Agent tool input and response fields"
description: "tool_input for the Agent tool and the run telemetry a PostToolUse hook gets back, including async_launched and SubagentHandback notes."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, subagents, agent-tool, telemetry]
kind: "tool"
maturity: "unlabelled"
since: "2.1.271"
surfaces: [cli, headless]
requires: ""
identifiers:
  - "Agent"
  - "subagent_type"
  - "status"
  - "agentId"
  - "content"
  - "resolvedModel"
  - "modelsUsed"
  - "totalTokens"
  - "totalDurationMs"
  - "totalToolUseCount"
  - "usage"
  - "async_launched"
  - "outputFile"
  - "SubagentHandback"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The `Agent` tool spawns a subagent. Its `tool_input` has `prompt` (task), `description` (short), `subagent_type` (e.g. `"Explore"`) and optional `model` alias override. When a foreground Agent call completes, a PostToolUse hook receives the result and run telemetry in `tool_response`.

# How to use it

| Field | Description |
| :- | :- |
| `status` | `"completed"` (foreground) or `"async_launched"` (background) |
| `agentId` | Subagent run identifier |
| `content` | Final text blocks; for a subagent reporting via `SubagentHandback`, a short note about the hand-back instead |
| `resolvedModel` | Model the subagent started on (may differ from requested, e.g. when `availableModels` or another override applies) |
| `modelsUsed` | Models in order, consecutive repeats collapsed; set only when swapped mid-run |
| `totalTokens` | Tokens from the final API request only (input, output, cache combined), not the run total |
| `totalDurationMs` | Wall-clock duration |
| `totalToolUseCount` | Tool calls made |
| `usage` | Per-type breakdown of the final request: `input_tokens`, `output_tokens`, `cache_creation_input_tokens`, `cache_read_input_tokens` |

For token and cost rollups across subagents use the token and cost counters filtered to `query_source` `"subagent"`, since `totalTokens` and `usage` cover only the final request.

# Limits and defaults

- Background launches return when the task moves to the background (including a foreground task Claude Code backgrounds mid-run): no usage fields; the response has `status: "async_launched"`, `agentId`, `description`, `prompt`, `outputFile`, `resolvedModel` (the model in use at backgrounding).
- From v2.1.271, a subagent running with the `SubagentHandback` tool (provided in auto mode) delivers its report through that tool. To read it, match a `PreToolUse` or `PostToolUse` hook on `SubagentHandback` and read `tool_input.message`.
