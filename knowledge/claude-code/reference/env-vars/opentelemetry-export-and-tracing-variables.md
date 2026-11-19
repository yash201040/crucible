---
type: "Reference"
title: "OpenTelemetry export, limits and tracing variables"
description: "Variables that enable OpenTelemetry export, set exporter, flush and shutdown timeouts, content length, trace propagation and detailed beta tracing."
resource: "https://code.claude.com/docs/en/env-vars"
tags: [opentelemetry, monitoring, tracing, metrics]
kind: "env_var"
maturity: "beta"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "CLAUDE_CODE_ENABLE_TELEMETRY"
  - "OTEL_METRICS_EXPORTER"
  - "OTEL_LOGS_EXPORTER"
  - "OTEL_EXPORTER_OTLP_ENDPOINT"
  - "OTEL_EXPORTER_OTLP_PROTOCOL"
  - "OTEL_EXPORTER_OTLP_HEADERS"
  - "OTEL_METRIC_EXPORT_INTERVAL"
  - "OTEL_RESOURCE_ATTRIBUTES"
  - "CLAUDE_CODE_OTEL_CONTENT_MAX_LENGTH"
  - "CLAUDE_CODE_OTEL_DIAG_STDERR"
  - "CLAUDE_CODE_OTEL_FLUSH_TIMEOUT_MS"
  - "CLAUDE_CODE_OTEL_HEADERS_HELPER_DEBOUNCE_MS"
  - "CLAUDE_CODE_OTEL_SHUTDOWN_TIMEOUT_MS"
  - "OTEL_ATTRIBUTE_VALUE_LENGTH_LIMIT"
  - "OTEL_LOGRECORD_ATTRIBUTE_VALUE_LENGTH_LIMIT"
  - "OTEL_SPAN_ATTRIBUTE_VALUE_LENGTH_LIMIT"
  - "BETA_TRACING_ENDPOINT"
  - "ENABLE_BETA_TRACING_DETAILED"
  - "CLAUDE_CODE_PROPAGATE_TRACEPARENT"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "env-vars"
    resource: "https://code.claude.com/docs/en/env-vars"
    title: "Environment variables"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

OpenTelemetry configuration for watching many sessions. The "beta" label here applies to the detailed tracing variables (the docs call them "detailed beta tracing", Traces (beta)); the rest are unlabelled. Setting rules: set export-enabling variables and destinations in the shell, user settings or managed settings; Claude Code ignores them in project and local settings apart from off values. `OTEL_RESOURCE_ATTRIBUTES` and interval, timeout and compression variables such as `OTEL_METRIC_EXPORT_INTERVAL` still apply from project and local settings. See the monitoring-usage page for details.

# How to use it

| Variable | What it does |
| :- | :- |
| `CLAUDE_CODE_ENABLE_TELEMETRY` | `1` enables OpenTelemetry collection for metrics and logging; required before configuring exporters. |
| `OTEL_METRICS_EXPORTER`, `OTEL_LOGS_EXPORTER`, `OTEL_EXPORTER_OTLP_ENDPOINT`, `OTEL_EXPORTER_OTLP_PROTOCOL`, `OTEL_EXPORTER_OTLP_HEADERS`, `OTEL_METRIC_EXPORT_INTERVAL`, `OTEL_RESOURCE_ATTRIBUTES` | Standard OpenTelemetry exporter variables, also supported (with signal-specific variants). |
| `CLAUDE_CODE_OTEL_CONTENT_MAX_LENGTH` | Max length of content-bearing attributes (responses, tool content, system prompts, raw API bodies), marker included, in UTF-16 code units (default 61440 = 60 KB). Requires v2.1.214+. |
| `OTEL_ATTRIBUTE_VALUE_LENGTH_LIMIT` | Standard SDK limit; Claude Code caps content attributes at the smaller of this and `CLAUDE_CODE_OTEL_CONTENT_MAX_LENGTH`. The `OTEL_LOGRECORD_ATTRIBUTE_VALUE_LENGTH_LIMIT` and `OTEL_SPAN_ATTRIBUTE_VALUE_LENGTH_LIMIT` variants are read the same way; the smallest set value applies to all signals. Requires v2.1.214+. |
| `CLAUDE_CODE_OTEL_DIAG_STDERR` | `1` writes exporter diagnostic errors to stderr (otherwise only with `--debug`, so a Prometheus port collision fails silently). Requires v2.1.179+. |
| `CLAUDE_CODE_OTEL_FLUSH_TIMEOUT_MS` | Flush timeout for pending spans (default 5000). |
| `CLAUDE_CODE_OTEL_HEADERS_HELPER_DEBOUNCE_MS` | Refresh interval for dynamic OpenTelemetry headers (default 1740000 = 29 minutes). |
| `CLAUDE_CODE_OTEL_SHUTDOWN_TIMEOUT_MS` | Exporter shutdown timeout (default 2000); increase if metrics are dropped at exit. |
| `BETA_TRACING_ENDPOINT` | OTLP/HTTP endpoint for detailed beta tracing; with `ENABLE_BETA_TRACING_DETAILED=1`, logs and traces go there instead of the configured exporters. Ignored in project and local settings. |
| `ENABLE_BETA_TRACING_DETAILED` | `1` (plus `BETA_TRACING_ENDPOINT`) turns on detailed beta tracing with content-bearing span attributes and the `claude_code.hook` span. Interactive CLI sessions also require the organization to be allowlisted for the beta. Ignored in project and local settings. |
| `CLAUDE_CODE_PROPAGATE_TRACEPARENT` | `1` propagates W3C trace context when `ANTHROPIC_BASE_URL` is a custom proxy: `traceparent` header on model and HTTP MCP requests, `TRACEPARENT` env var for Bash, PowerShell and hook subprocesses. By default only on direct Anthropic API connections. Added in v2.1.152. |
