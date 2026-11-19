---
type: "Concept"
title: "Backends, service resource attributes and privacy defaults"
description: "Backend choices per signal, resource attributes on all exports, ROI guide, Bedrock monitoring pointer and what is collected by default."
resource: "https://code.claude.com/docs/en/monitoring-usage"
tags: [telemetry, privacy, resource-attributes, backends]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop]
requires: ""
identifiers:
  - "service.name"
  - "service.version"
  - "os.type"
  - "os.version"
  - "host.arch"
  - "wsl.version"
  - "claude-code"
  - "claude-code-desktop"
  - "OTEL_LOG_USER_PROMPTS"
  - "OTEL_LOG_ASSISTANT_RESPONSES"
  - "OTEL_LOG_TOOL_DETAILS"
  - "OTEL_LOG_TOOL_CONTENT"
  - "OTEL_LOG_RAW_API_BODIES"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "monitoring-usage"
    resource: "https://code.claude.com/docs/en/monitoring-usage"
    title: "Monitoring"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Backend guidance: metrics suit time-series databases (rates), columnar stores (complex queries, unique users) or observability platforms; events/logs suit log aggregation, columnar stores or platforms; traces need a distributed tracing backend. For DAU/WAU/MAU consider backends with efficient unique-value queries.

Resource attributes on all exports: `service.name` (`claude-code` for terminal; `claude-code-desktop` for local Code tab sessions, so add it to filters), `service.version`, `os.type`, `os.version`, `host.arch`, optional `host.name`/`host.id`, `wsl.version` (WSL only). Meter name `com.anthropic.claude_code`.

# How to use it

Privacy defaults: export is opt-in and goes only to the backend you configure (Anthropic's separate operational telemetry is covered on the data usage page). Raw file contents and code snippets are not in metrics or events by default. `user.email` (OAuth) goes only to your endpoint. Prompt content is off (only length) until `OTEL_LOG_USER_PROMPTS=1`; then `user_prompt` carries both `prompt` and `prompt_text`, so a collector rule must delete both (an `attributes` processor with `delete` actions for keys `prompt` and `prompt_text`), and the `claude_code.interaction` span carries `user_prompt`. Response text is off until `OTEL_LOG_ASSISTANT_RESPONSES=1` (falls back to the prompt flag; set `0` to keep responses redacted). Tool parameters off until `OTEL_LOG_TOOL_DETAILS=1` (adds `tool_parameters`, `tool_input` with values over 512 chars truncated and about 4K total, `command_name` for custom/plugin/MCP commands, real names on counters, span `file_path`). Tool content off in spans until `OTEL_LOG_TOOL_CONTENT=1`. Raw API bodies off until `OTEL_LOG_RAW_API_BODIES` (ignored in project/local settings; implies consent to all other content flags; thinking content always redacted).

# Notes

ROI guide: a separate repository (claude-code-monitoring-guide) provides Docker Compose, Prometheus and OTel setups and report templates integrated with tools like Linear. A separate guidance repository exists for monitoring Claude Code on Amazon Bedrock.
