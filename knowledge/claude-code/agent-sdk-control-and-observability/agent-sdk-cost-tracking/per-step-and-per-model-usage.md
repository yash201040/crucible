---
type: "Feature"
title: "Per-step and per-model usage breakdown"
description: "Deduplicate assistant messages by ID for step input tokens, and read modelUsage for per-model cost with a costBasis field."
resource: "https://code.claude.com/docs/en/agent-sdk/cost-tracking"
tags: [usage, per-model, tokens, cost-basis]
kind: "api"
maturity: "unlabelled"
since: "2.1.246"
surfaces: [sdk]
requires: "costBasis needs Claude Code v2.1.246 or later"
identifiers:
  - "modelUsage"
  - "costBasis"
  - "costUSD"
  - "inputTokens"
  - "outputTokens"
  - "cacheReadInputTokens"
  - "cacheCreationInputTokens"
  - "parent_tool_use_id"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-cost-tracking"
    resource: "https://code.claude.com/docs/en/agent-sdk/cost-tracking"
    title: "Track cost and usage"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Per-step usage: parallel tool calls produce several assistant messages with the same `id` and identical usage; track seen IDs and count each once. Skip subagent messages by checking `parent_tool_use_id`. Deduplicated per-step values are accurate for input and cache tokens, but per-step `output_tokens` is a placeholder.

Per-model: the result's `modelUsage` maps model name to token counts and cost (fields `costUSD`, `inputTokens`, `outputTokens`, `cacheReadInputTokens`, `cacheCreationInputTokens`). Useful when running several models, for example Haiku for subagents and Opus for the main agent. Python equivalents: `AssistantMessage.usage`, `AssistantMessage.message_id`, `ResultMessage.model_usage`.

# Limits and defaults

Each `modelUsage` entry's `costBasis` says which price table priced that model's latest request: `list` (list price), `managed` (a `modelPricing` table) or `unknown` (neither matched the model ID). Requires Claude Code v2.1.246 or later.
