---
type: "Guide"
title: "Quick start for OpenTelemetry export"
description: "Turn on OTel export with environment variables, choose exporters and verify that data arrives."
resource: "https://code.claude.com/docs/en/monitoring-usage"
tags: [telemetry, opentelemetry, setup, otlp]
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
  - "OTEL_EXPORTER_OTLP_HEADERS"
  - "claude --debug-file <path>"
  - "claude_code.session.count"
  - "claude_code.user_prompt"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "monitoring-usage"
    resource: "https://code.claude.com/docs/en/monitoring-usage"
    title: "Monitoring"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude Code exports usage, cost and tool activity through OpenTelemetry (OTel): metrics as time series, events through the logs/events protocol, and optionally distributed traces (beta). Everything is configured with environment variables. For the Claude API or Managed Agents the page points to a separate OpenTelemetry page on platform.claude.com.

# How to use it

```bash
export CLAUDE_CODE_ENABLE_TELEMETRY=1
export OTEL_METRICS_EXPORTER=otlp      # otlp, prometheus, console, none
export OTEL_LOGS_EXPORTER=otlp         # otlp, console, none
export OTEL_EXPORTER_OTLP_PROTOCOL=grpc
export OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317
export OTEL_EXPORTER_OTLP_HEADERS="Authorization=Bearer your-token"
export OTEL_METRIC_EXPORT_INTERVAL=10000   # debugging; default 60000
export OTEL_LOGS_EXPORT_INTERVAL=5000      # default 5000
claude
```

Both exporters are optional; configure only what you need.

- Verify metrics: look for `claude_code.session.count` (emitted at session start).
- Verify logs only: submit a prompt and look for the `claude_code.user_prompt` event.
- If nothing arrives: run `claude --debug-file <path>`. Exporter failures appear as `[3P telemetry]` errors (3P = third-party). Lines prefixed `[Anthropic telemetry]` belong to Anthropic's separate operational telemetry and are not a problem with your setup.

# Notes

Telemetry export to your own backend is opt-in. Full option details are in the OpenTelemetry exporter specification. See [common variables](./common-configuration-variables.md).
