---
type: "Feature"
title: "Distributed traces (beta)"
description: "Span tracing linking each prompt to its API requests, tools and subagents, with W3C trace-context propagation."
resource: "https://code.claude.com/docs/en/monitoring-usage"
tags: [telemetry, tracing, traceparent, beta]
kind: "env_var"
maturity: "beta"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "CLAUDE_CODE_ENHANCED_TELEMETRY_BETA"
  - "ENABLE_ENHANCED_TELEMETRY_BETA"
  - "OTEL_TRACES_EXPORTER"
  - "OTEL_EXPORTER_OTLP_TRACES_PROTOCOL"
  - "OTEL_EXPORTER_OTLP_TRACES_ENDPOINT"
  - "OTEL_EXPORTER_OTLP_TRACES_HEADERS"
  - "OTEL_TRACES_EXPORT_INTERVAL"
  - "TRACEPARENT"
  - "TRACESTATE"
  - "traceparent"
  - "traceresponse"
  - "CLAUDE_CODE_PROPAGATE_TRACEPARENT"
  - "ANTHROPIC_BASE_URL"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "monitoring-usage"
    resource: "https://code.claude.com/docs/en/monitoring-usage"
    title: "Monitoring"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Tracing exports spans linking each user prompt to the API requests and tool executions it triggers, so a request reads as one trace. It is off by default and labelled beta.

# How to use it

Set `CLAUDE_CODE_ENABLE_TELEMETRY=1` and `CLAUDE_CODE_ENHANCED_TELEMETRY_BETA=1` (`ENABLE_ENHANCED_TELEMETRY_BETA` also accepted), then `OTEL_TRACES_EXPORTER` (`console`, `otlp`, `none`). Traces reuse the common OTLP endpoint, protocol, headers and mTLS settings.

| Name | Default | What it does |
| - | - | - |
| `OTEL_EXPORTER_OTLP_TRACES_PROTOCOL` | | Overrides `OTEL_EXPORTER_OTLP_PROTOCOL` |
| `OTEL_EXPORTER_OTLP_TRACES_ENDPOINT` | | Overrides the endpoint (`http://localhost:4318/v1/traces`) |
| `OTEL_EXPORTER_OTLP_TRACES_HEADERS` | | Merged with general headers |
| `OTEL_TRACES_EXPORT_INTERVAL` | 5000 ms | Span batch interval |
| `CLAUDE_CODE_PROPAGATE_TRACEPARENT` | off | `1` to propagate trace context through a custom `ANTHROPIC_BASE_URL` proxy |

- Spans redact prompt text, tool input details and tool content by default; `OTEL_LOG_USER_PROMPTS=1`, `OTEL_LOG_TOOL_DETAILS=1`, `OTEL_LOG_TOOL_CONTENT=1` include them.
- With tracing active, Bash and PowerShell subprocesses inherit `TRACEPARENT` (W3C context of the active tool span). Model requests (when connected directly to the Anthropic API) carry a `traceparent` header set to the `claude_code.llm_request` span context, and the API's `traceresponse` header is recorded as a span link; outbound HTTP MCP requests carry `traceparent` too. Not sent to third-party providers, and by default only when `ANTHROPIC_BASE_URL` is unset or points at the Anthropic API (the subprocess `TRACEPARENT` follows the same switch).
- In Agent SDK and `-p` sessions, Claude Code reads `TRACEPARENT` and `TRACESTATE` from its environment at each interaction span, so an embedding process can parent Claude Code's spans under its own trace. Interactive sessions ignore inbound `TRACEPARENT`.
- In those sessions each OTLP event log record also carries `trace_id` and `span_id` joining it to the caller's trace, even with no traces exporter configured. A record emitted during an interaction carries that span's IDs; with no active interaction it carries the inbound `TRACEPARENT` IDs.

# Notes

See [span hierarchy and attributes](./span-hierarchy-and-attributes.md) and [detailed beta tracing](./detailed-beta-tracing.md).
