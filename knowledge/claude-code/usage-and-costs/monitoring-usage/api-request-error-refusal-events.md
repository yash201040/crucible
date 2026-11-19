---
type: "Reference"
title: "API request, error, refusal and retry events"
description: "claude_code.api_request, api_error, api_refusal and api_retries_exhausted events with cost, token, effort and refusal fields."
resource: "https://code.claude.com/docs/en/monitoring-usage"
tags: [events, api, cost, refusals, retries]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "claude_code.api_request"
  - "claude_code.api_error"
  - "claude_code.api_refusal"
  - "claude_code.api_retries_exhausted"
  - "cost_usd"
  - "cost_usd_micros"
  - "cache_creation_5m_tokens"
  - "cache_creation_1h_tokens"
  - "attempt"
  - "status_code"
  - "server_fallback_hop"
  - "has_category"
  - "has_explanation"
  - "category"
  - "total_attempts"
  - "total_retry_duration_ms"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "monitoring-usage"
    resource: "https://code.claude.com/docs/en/monitoring-usage"
    title: "Monitoring"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Per-request events for cost, failure, refusal and retry analysis.

# How to use it

`claude_code.api_request` (each API request): `model`, `cost_usd` (estimate), `cost_usd_micros` (integer millionths of a dollar), `duration_ms`, `input_tokens` (excludes cache), `output_tokens`, `cache_read_tokens`, `cache_creation_tokens`, `cache_creation_5m_tokens` and `cache_creation_1h_tokens` (0 when the API does not report them; v2.1.300+), `request_id`, `client_request_id`, `speed` (`fast`/`normal`), `query_source`, `effort`, plus `agent.name`, `skill.name`, `plugin.name`, `marketplace.name`, `mcp_server.name`, `mcp_tool.name` attribution (a third-party mod's `$.model` call shows `marketplace.name` as `third-party` unless DETAILS).

`claude_code.api_error` (failed request): `model`, `error`, `status_code` (absent for non-HTTP errors), `duration_ms`, `attempt` (including the first), `request_id`, `client_request_id`, `speed`, `query_source`, `effort`, attribution attributes.

`claude_code.api_refusal` (response with `stop_reason: "refusal"`, which arrives on a successful stream so `api_error` does not fire): `model`, `request_id`, `query_source`, `speed`, `attempt` (first is 1), `effort`, `server_fallback_hop` (true when the API's server-side model fallback already retried this refusal on another model; a turn can emit a true hop event and a later false final event), `has_category` (true for `stop_details.category` of `cyber`, `bio`, `frontier_llm`, `reasoning_extraction`; absent on hops), `has_explanation` (absent on hops), `category` (only with DETAILS and `has_category` true), attribution attributes.

`claude_code.api_retries_exhausted` (once, alongside the final `api_error`, when a request fails after more than one attempt): `model`, `error`, `status_code`, `total_attempts`, `total_retry_duration_ms`, `speed`.

# Notes

Retry detection details: see [retry exhaustion](./interpreting-usage-and-cost-data.md).
