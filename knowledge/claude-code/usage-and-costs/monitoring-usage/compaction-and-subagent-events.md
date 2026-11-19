---
type: "Reference"
title: "Compaction and subagent completed events"
description: "claude_code.compaction and claude_code.subagent_completed events for context compaction and subagent rollups."
resource: "https://code.claude.com/docs/en/monitoring-usage"
tags: [events, subagents, compaction, context]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "claude_code.compaction"
  - "claude_code.subagent_completed"
  - "pre_tokens"
  - "post_tokens"
  - "precompute_reuse"
  - "agent_type"
  - "agent.source"
  - "is_built_in"
  - "is_async"
  - "total_tokens"
  - "total_tool_uses"
  - "final_model"
  - "model_swapped"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "monitoring-usage"
    resource: "https://code.claude.com/docs/en/monitoring-usage"
    title: "Monitoring"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`claude_code.compaction` is logged when conversation compaction completes. `claude_code.subagent_completed` is logged when a subagent finishes and returns its result to the conversation that started it.

# How to use it

Compaction attributes: `trigger` (`auto`/`manual`), `success`, `duration_ms`, `pre_tokens`, `post_tokens` (approximate), `error`, `precompute_reuse` (set only for `manual`, or `auto` idle compaction in an interactive terminal; auto-compaction can prepare a summary in the background; `hit` = reused, `miss_custom_instructions`, `miss_hook`, `miss_not_ready` = why a fresh summary was computed).

Subagent attributes: `agent_type` (built-in and official-plugin names verbatim, others `custom` unless DETAILS), `agent.source` (`built-in`, `plugin`, or settings source such as `userSettings`, `projectSettings`), `is_built_in`, `is_async` (ran in the background), `total_tokens` (footprint of the final API request only: roughly the subagent's context size at completion, not a sum), `total_tool_uses` (across the whole run), `duration_ms`, `model` (model it was resolved to run), `final_model` (differs after a mid-run switch such as fallback), `model_swapped` (more than one model served), `plugin_id_hash`, `plugin.name`.

# Notes

For token or cost rollups by subagent use the token and cost counters filtered to `query_source` `"subagent"`; that category also counts agent-based hook requests, which emit no subagent event.
