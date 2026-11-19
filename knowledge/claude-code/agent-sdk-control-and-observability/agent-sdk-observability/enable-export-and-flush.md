---
type: "Guide"
title: "Enable telemetry export and flush timing"
description: "Turn on CLAUDE_CODE_ENABLE_TELEMETRY with an OTLP exporter, avoid console, surface export errors, and shorten export intervals."
resource: "https://code.claude.com/docs/en/agent-sdk/observability"
tags: [opentelemetry, otlp, export, flush]
kind: "env_var"
maturity: "unlabelled"
since: "2.1.179"
surfaces: [sdk]
requires: "CLAUDE_CODE_OTEL_DIAG_STDERR needs Claude Code v2.1.179 or later"
identifiers:
  - "CLAUDE_CODE_ENABLE_TELEMETRY"
  - "OTEL_EXPORTER_OTLP_PROTOCOL"
  - "OTEL_EXPORTER_OTLP_ENDPOINT"
  - "OTEL_EXPORTER_OTLP_HEADERS"
  - "CLAUDE_CODE_OTEL_DIAG_STDERR"
  - "OTEL_METRIC_EXPORT_INTERVAL"
  - "OTEL_LOGS_EXPORT_INTERVAL"
  - "OTEL_TRACES_EXPORT_INTERVAL"
  - "stderr"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-observability"
    resource: "https://code.claude.com/docs/en/agent-sdk/observability"
    title: "Observability with OpenTelemetry"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Telemetry is off until `CLAUDE_CODE_ENABLE_TELEMETRY=1` is set and at least one exporter chosen.

# How to use it

Typical env: `CLAUDE_CODE_ENABLE_TELEMETRY=1`, `CLAUDE_CODE_ENHANCED_TELEMETRY_BETA=1` (traces only), `OTEL_TRACES_EXPORTER=otlp`, `OTEL_METRICS_EXPORTER=otlp`, `OTEL_LOGS_EXPORTER=otlp`, `OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf`, `OTEL_EXPORTER_OTLP_ENDPOINT=http://collector.example.com:4318`, `OTEL_EXPORTER_OTLP_HEADERS=Authorization=Bearer your-token`. Verify by checking collector logs after a task.

| Variable | Default | What it does |
| - | - | - |
| `OTEL_METRIC_EXPORT_INTERVAL` | 60 seconds | metrics export interval (ms) |
| `OTEL_LOGS_EXPORT_INTERVAL` | 5 seconds | logs interval; example sets `1000` |
| `OTEL_TRACES_EXPORT_INTERVAL` | 5 seconds | traces interval; example sets `1000` |
| `CLAUDE_CODE_OTEL_DIAG_STDERR=1` | off | surfaces exporter diagnostics, read through the SDK's `stderr` callback (Python) or `stderr` option (TypeScript) |

# Limits and defaults

- Export errors fail silently by default: an unreachable or rejecting endpoint drops telemetry and the agent still runs.
- Do not use the `console` exporter in the SDK: it writes to standard output, which is the SDK's message channel. Point `OTEL_EXPORTER_OTLP_ENDPOINT` at a local collector to inspect locally.
- On clean exit the CLI tries to flush, bounded by a short timeout, so spans can drop if the collector is slow; if the process is killed, buffered data is lost. Lower the intervals for short-lived calls.
