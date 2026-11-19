---
type: "Guide"
title: "Interpreting usage, cost and retry data"
description: "How to analyze tokens, cost, retries and tool events, and how Claude Code's input tokens map to GenAI conventions."
resource: "https://code.claude.com/docs/en/monitoring-usage"
tags: [cost, usage, analysis, retries]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "CLAUDE_CODE_MAX_RETRIES"
  - "CLAUDE_CODE_RETRY_WATCHDOG"
  - "gen_ai.usage.input_tokens"
  - "gen_ai.usage.cache_read.input_tokens"
  - "gen_ai.usage.cache_write.input_tokens"
  - "gen_ai.usage.cache_creation.input_tokens"
  - "OTEL_METRICS_INCLUDE_ENTRYPOINT"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "monitoring-usage"
    resource: "https://code.claude.com/docs/en/monitoring-usage"
    title: "Monitoring"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Guidance for turning exported data into answers.

# How to use it

- Usage: break `claude_code.token.usage` down by token `type`, user, team, model, `skill.name`, `plugin.name`, `agent.name`. `claude_code.lines_of_code.count` by model; commits and PRs for workflow impact. To compare active users per surface set `OTEL_METRICS_INCLUDE_ENTRYPOINT=true` and count distinct `user.account_uuid` per `app.entrypoint` on `user_prompt` events (or on token usage if metrics only). `claude_code.session.count` rises without adding active users when one person starts many sessions or a session gets no prompt. `user.account_uuid` does not identify people in Claude Tag sessions and is missing without a Claude account.
- Cost: `claude_code.cost.usage` for trends, high-usage sessions, and spend by skill, plugin or subagent type. Cost metrics are approximations.
- Segmentation and alerts: cost spikes, unusual token consumption, high session volume per user. `model` is on `token.usage`, `cost.usage`, `lines_of_code.count`. Per-model commits can only be approximated by joining on `session.id`; filter the cost side to `query_source` `"main"`.
- Retry exhaustion: Claude Code retries internally and emits one `api_error` only after giving up (intermediate attempts are not events). `CLAUDE_CODE_MAX_RETRIES` defaults to 10 and is capped at 15; with `CLAUDE_CODE_RETRY_WATCHDOG` set the default is higher and there is no cap. On exhaustion `attempt` is at most limit plus one (11 by default); a lower value can still mean exhaustion because `attempt` restarts at 1 after each re-issue following a streaming failure. To tell a recovered session from a stalled one, group by `session.id` and look for a later `api_request`.
- Events: tool result events give frequent tools, success rates, durations, error patterns; request durations for bottlenecks.

# Notes

GenAI mapping: Claude Code does not set `gen_ai.usage.*`. Its input counts (span/event `input_tokens`, token metric type `input`) exclude cache. For the convention's `gen_ai.usage.input_tokens` add `input_tokens` + `cache_read_tokens` + `cache_creation_tokens` (or types `input`, `cacheRead`, `cacheCreation`). `cache_read_tokens` maps to `gen_ai.usage.cache_read.input_tokens`; `cache_creation_tokens` to `gen_ai.usage.cache_write.input_tokens` (older conventions: `gen_ai.usage.cache_creation.input_tokens`).
