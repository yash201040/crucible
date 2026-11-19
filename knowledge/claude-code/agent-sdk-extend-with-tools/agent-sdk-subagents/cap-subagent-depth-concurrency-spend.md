---
type: "Limit"
title: "Cap subagent depth, concurrency and spend"
description: "CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH (3), CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS (20) and maxBudgetUsd bound a tree of subagents."
resource: "https://code.claude.com/docs/en/agent-sdk/subagents"
tags: [subagents, limits, budget, concurrency]
kind: "limit"
maturity: "unlabelled"
since: "2.1.219"
surfaces: [sdk]
requires: "TypeScript SDK v0.3.219 or Python SDK v0.2.127 and later (bundling Claude Code v2.1.219 or later)"
identifiers:
  - "CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH"
  - "CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS"
  - "maxBudgetUsd"
  - "max_budget_usd"
  - "total_cost_usd"
  - "error_max_budget_usd"
  - "Concurrent subagent limit reached"
  - "Budget limit reached"
  - "env"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-subagents"
    resource: "https://code.claude.com/docs/en/agent-sdk/subagents"
    title: "Subagents in the SDK"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude decides itself when and how many subagents to spawn; each makes its own API requests counted toward the query's `total_cost_usd`, and subagents can spawn subagents, so one prompt can grow into a tree. Three caps bound it. On earlier releases some limits are missing or default differently.

# How to use it

| Limit | Set with | Default | At the limit |
| --- | --- | --- | --- |
| Depth | `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` | `3` layers below the main agent; `1` stops subagents spawning their own | Bottom-layer subagent cannot spawn and does the work itself |
| Concurrency | `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` | `20` running at once, counting every Agent-tool subagent | Refuses to spawn, returning `Concurrent subagent limit reached`, until the count drops; sessions with ultracode active are never refused |
| Spend | `maxBudgetUsd` (TS) / `max_budget_usd` (Python) | No limit; counts the call's spend including subagents | Refuses further spawns with `Budget limit reached`, stops running background subagents, and ends the query with result subtype `error_max_budget_usd` |

Set depth and concurrency as environment variables via the `env` option; spend is a query option. `env` differs by SDK: TypeScript replaces the subprocess environment (spread `process.env` to keep `PATH`); Python merges it into the inherited environment.

Outcomes: under the cap, `success` plus estimated cost; at the spend cap, `error_max_budget_usd` with cost at or above the cap and the error handler runs; at the concurrency limit, a `tool_result` block with `Concurrent subagent limit reached` appears in the stream and goes to Claude.

# Notes

Opus 5 delegates more readily than earlier models, so these limits matter most there. With the `claude_code` system prompt preset and an Opus 5 model, Claude Code adds a line telling Claude not to call the Agent tool unless asked (the tool stays available). With a custom or absent `systemPrompt` that line is absent; add the delegation instruction from the Opus 5 prompting guide. Prompts only steer Claude; the limits are enforced regardless.
