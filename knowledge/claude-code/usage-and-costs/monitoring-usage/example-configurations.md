---
type: "Guide"
title: "Example telemetry configurations"
description: "Ready-made environment variable sets for console, OTLP gRPC, Prometheus, multi-exporter, split endpoints, metrics-only and logs-only."
resource: "https://code.claude.com/docs/en/monitoring-usage"
tags: [telemetry, examples, prometheus, otlp]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "OTEL_METRICS_EXPORTER=console,otlp"
  - "http://localhost:9464/metrics"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "monitoring-usage"
    resource: "https://code.claude.com/docs/en/monitoring-usage"
    title: "Monitoring"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Complete scenario configurations. All start with `CLAUDE_CODE_ENABLE_TELEMETRY=1`; confirm with `claude_code.session.count`.

# How to use it

| Scenario | Variables |
| - | - |
| Console debugging | `OTEL_METRICS_EXPORTER=console`, `OTEL_METRIC_EXPORT_INTERVAL=1000` |
| OTLP gRPC | `OTEL_METRICS_EXPORTER=otlp`, `OTEL_EXPORTER_OTLP_PROTOCOL=grpc`, `OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317` |
| Prometheus | `OTEL_METRICS_EXPORTER=prometheus` (scraped from `http://localhost:9464/metrics`) |
| Multiple exporters | `OTEL_METRICS_EXPORTER=console,otlp`, `OTEL_EXPORTER_OTLP_PROTOCOL=http/json` |
| Different backends | metrics `http/protobuf` to `http://metrics.example.com:4318/v1/metrics`; logs `grpc` to `http://logs.example.com:4317` via the per-signal variables |
| Metrics only | `OTEL_METRICS_EXPORTER=otlp` and no logs exporter |
| Logs/events only | `OTEL_LOGS_EXPORTER=otlp` and no metrics exporter |

# Limits and defaults

On a self-hosted environment the session binds port 9464 only at the runner's default capacity of one; at higher capacity the runner re-exposes session counters and gauges on its own `/metrics` endpoint.
