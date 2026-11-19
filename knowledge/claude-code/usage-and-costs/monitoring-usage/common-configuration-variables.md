---
type: "Reference"
title: "Common OpenTelemetry configuration variables"
description: "Exporters, endpoints, protocols, headers, intervals, content-logging gates and limits shared by metrics, logs and traces."
resource: "https://code.claude.com/docs/en/monitoring-usage"
tags: [telemetry, env-vars, otlp, content-logging]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "CLAUDE_CODE_ENABLE_TELEMETRY"
  - "OTEL_METRICS_EXPORTER"
  - "OTEL_LOGS_EXPORTER"
  - "OTEL_EXPORTER_OTLP_PROTOCOL"
  - "OTEL_EXPORTER_OTLP_ENDPOINT"
  - "OTEL_EXPORTER_OTLP_METRICS_PROTOCOL"
  - "OTEL_EXPORTER_OTLP_METRICS_ENDPOINT"
  - "OTEL_EXPORTER_OTLP_LOGS_PROTOCOL"
  - "OTEL_EXPORTER_OTLP_LOGS_ENDPOINT"
  - "OTEL_EXPORTER_OTLP_HEADERS"
  - "OTEL_EXPORTER_OTLP_METRICS_HEADERS"
  - "OTEL_EXPORTER_OTLP_LOGS_HEADERS"
  - "OTEL_METRIC_EXPORT_INTERVAL"
  - "OTEL_LOGS_EXPORT_INTERVAL"
  - "OTEL_LOG_USER_PROMPTS"
  - "OTEL_LOG_ASSISTANT_RESPONSES"
  - "OTEL_LOG_TOOL_DETAILS"
  - "OTEL_LOG_TOOL_CONTENT"
  - "OTEL_LOG_MANAGED_SETTINGS"
  - "OTEL_LOG_RAW_API_BODIES"
  - "CLAUDE_CODE_OTEL_CONTENT_MAX_LENGTH"
  - "OTEL_RESOURCE_INCLUDE_HOST"
  - "OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE"
  - "CLAUDE_CODE_OTEL_HEADERS_HELPER_DEBOUNCE_MS"
  - "OTEL_ATTRIBUTE_VALUE_LENGTH_LIMIT"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "monitoring-usage"
    resource: "https://code.claude.com/docs/en/monitoring-usage"
    title: "Monitoring"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Variables that configure exporters, endpoints and export behaviour for all deployments. A per-signal endpoint or protocol variable overrides the generic one for that signal; a per-signal headers variable is merged with `OTEL_EXPORTER_OTLP_HEADERS`. For `http/protobuf` and `http/json`, each export request carries a `Content-Length` header.

# How to use it

| Name | Kind | Default | What it does |
| - | - | - | - |
| `CLAUDE_CODE_ENABLE_TELEMETRY` | env var | off | Required switch; `1` enables |
| `OTEL_METRICS_EXPORTER` | env var | none set | Comma-separated: `console`, `otlp`, `prometheus`, `none` |
| `OTEL_LOGS_EXPORTER` | env var | none set | Comma-separated: `console`, `otlp`, `none` |
| `OTEL_EXPORTER_OTLP_PROTOCOL` | env var | `http/protobuf` for a valid http(s) endpoint (default needs v2.1.323+) | `grpc`, `http/json`, `http/protobuf`; set `grpc` for e.g. `http://localhost:4317` |
| `OTEL_EXPORTER_OTLP_ENDPOINT` | env var | | Collector endpoint for all signals |
| `OTEL_EXPORTER_OTLP_METRICS_PROTOCOL` / `_ENDPOINT` | env var | | Metrics overrides (`http://localhost:4318/v1/metrics`) |
| `OTEL_EXPORTER_OTLP_LOGS_PROTOCOL` / `_ENDPOINT` | env var | | Logs overrides (`http://localhost:4318/v1/logs`) |
| `OTEL_EXPORTER_OTLP_HEADERS` | env var | | Auth headers, e.g. `Authorization=Bearer token` |
| `OTEL_EXPORTER_OTLP_METRICS_HEADERS`, `OTEL_EXPORTER_OTLP_LOGS_HEADERS` | env var | | Per-signal headers merged with the general ones |
| `OTEL_METRIC_EXPORT_INTERVAL` | env var | 60000 ms | Metrics export interval |
| `OTEL_LOGS_EXPORT_INTERVAL` | env var | 5000 ms | Logs export interval |
| `OTEL_LOG_USER_PROMPTS` | env var | disabled | `1` logs prompt content |
| `OTEL_LOG_ASSISTANT_RESPONSES` | env var | disabled; falls back to `OTEL_LOG_USER_PROMPTS` when unset | `1` logs response text on `assistant_response`; `0` keeps it redacted |
| `OTEL_LOG_TOOL_DETAILS` | env var | disabled | Logs tool parameters and input in tool events and span attributes (Bash commands, MCP server/tool names, skill names, user-authored workflow names, tool input); also real command names on `user_prompt` and real agent, skill, plugin, MCP names on cost and token counters. Desktop built-in servers emit `mcp_server_name`/`mcp_tool_name` regardless (v2.1.214+) |
| `OTEL_LOG_TOOL_CONTENT` | env var | disabled | Logs tool content in the `tool.output` span event; requires tracing |
| `OTEL_LOG_MANAGED_SETTINGS` | env var | disabled | Adds redacted managed settings and a SHA-256 digest to `managed_settings_resolved`; project/local settings values do not enable it; v2.1.274+ |
| `OTEL_LOG_RAW_API_BODIES` | env var | disabled | `1` inline bodies (truncated at content limit) or `file:<dir>` untruncated on disk with `body_ref`; implies consent to prompts, tool details and tool content |
| `CLAUDE_CODE_OTEL_CONTENT_MAX_LENGTH` | env var | 61440 UTF-16 code units (60 KB) | Max length of content-bearing attributes, truncation marker included; a lower `OTEL_ATTRIBUTE_VALUE_LENGTH_LIMIT` (or its logrecord/span variants) wins |
| `OTEL_RESOURCE_INCLUDE_HOST` | env var | disabled | Adds `host.name`/`host.id`; v2.1.326+ |
| `OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE` | env var | `delta` | `delta` or `cumulative` |
| `CLAUDE_CODE_OTEL_HEADERS_HELPER_DEBOUNCE_MS` | env var | 1740000 ms (29 min) | Refresh interval for dynamic headers |

# Notes

See [mTLS](./mtls-authentication.md), [cardinality control](./metrics-cardinality-control.md) and [dynamic headers](./dynamic-headers.md).
