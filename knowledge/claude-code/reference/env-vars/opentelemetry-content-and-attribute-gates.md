---
type: "Reference"
title: "OpenTelemetry content capture and attribute variables"
description: "Variables that decide whether prompts, responses, tool details, raw API bodies and managed settings appear in telemetry, and which attributes tag metrics."
resource: "https://code.claude.com/docs/en/env-vars"
tags: [opentelemetry, privacy, attributes, monitoring]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "OTEL_LOG_USER_PROMPTS"
  - "OTEL_LOG_ASSISTANT_RESPONSES"
  - "OTEL_LOG_TOOL_CONTENT"
  - "OTEL_LOG_TOOL_DETAILS"
  - "OTEL_LOG_RAW_API_BODIES"
  - "OTEL_LOG_MANAGED_SETTINGS"
  - "OTEL_METRICS_INCLUDE_ACCOUNT_UUID"
  - "OTEL_METRICS_INCLUDE_ENTRYPOINT"
  - "OTEL_METRICS_INCLUDE_REPOSITORY"
  - "OTEL_METRICS_INCLUDE_RESOURCE_ATTRIBUTES"
  - "OTEL_METRICS_INCLUDE_SESSION_ID"
  - "OTEL_METRICS_INCLUDE_VERSION"
  - "OTEL_RESOURCE_INCLUDE_HOST"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "env-vars"
    resource: "https://code.claude.com/docs/en/env-vars"
    title: "Environment variables"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Opt-in content gates (off by default to protect sensitive data) and attribute toggles for metrics and events. The `OTEL_LOG_*` gates and `OTEL_RESOURCE_INCLUDE_HOST` are set in the shell, user settings or managed settings and are ignored in project and local settings (apart from off values).

# How to use it

| Variable | Default | What it does |
| :- | :- | :- |
| `OTEL_LOG_USER_PROMPTS` | redacted | `1` includes user prompt text in traces and logs. |
| `OTEL_LOG_ASSISTANT_RESPONSES` | follows `OTEL_LOG_USER_PROMPTS` | `1` includes response text on `assistant_response` log events; `0` keeps responses redacted even when prompts are logged. Requires v2.1.193+. |
| `OTEL_LOG_TOOL_CONTENT` | off | `1` includes tool content in the `tool.output` span event (needs tracing); span attributes use their own gates. |
| `OTEL_LOG_TOOL_DETAILS` | off | `1` includes tool input arguments, MCP server names, user-authored workflow names, raw tool error strings, the refusal `category` on `api_refusal` events, real agent, skill, plugin and MCP server names on cost and token metrics, and other tool details. |
| `OTEL_LOG_RAW_API_BODIES` | off | Emits Messages API request and response JSON as `api_request_body` and `api_response_body` log events. `1` = inline bodies truncated at the content limit (60 KB default via `CLAUDE_CODE_OTEL_CONTENT_MAX_LENGTH`); `file:<dir>` writes untruncated bodies to disk and emits a `body_ref` path. Bodies include the whole conversation history. |
| `OTEL_LOG_MANAGED_SETTINGS` | off | `1` adds redacted managed settings and a SHA-256 digest of the pre-redaction settings to `managed_settings_resolved` log events. Project or local settings do not turn it on. Requires v2.1.274+. |
| `OTEL_METRICS_INCLUDE_ACCOUNT_UUID` | included | `false` excludes account UUID from metric and event attributes. |
| `OTEL_METRICS_INCLUDE_ENTRYPOINT` | excluded | `true` includes the session entrypoint. Added in v2.1.152. |
| `OTEL_METRICS_INCLUDE_REPOSITORY` | excluded | `true` tags metrics and events with `vcs.*` repository attributes. Requires v2.1.269+. |
| `OTEL_METRICS_INCLUDE_RESOURCE_ATTRIBUTES` | included | As of v2.1.161 `OTEL_RESOURCE_ATTRIBUTES` keys attach to metric datapoint labels; `false` excludes them. |
| `OTEL_METRICS_INCLUDE_SESSION_ID` | included | `false` excludes session ID. |
| `OTEL_METRICS_INCLUDE_VERSION` | excluded | `true` includes the Claude Code version. |
| `OTEL_RESOURCE_INCLUDE_HOST` | excluded | `1` adds `host.name` and `host.id` resource attributes. Requires v2.1.326+. |
