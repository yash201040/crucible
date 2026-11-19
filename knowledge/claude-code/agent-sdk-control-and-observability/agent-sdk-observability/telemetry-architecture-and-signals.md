---
type: "Concept"
title: "How SDK telemetry flows and its signals"
description: "The SDK emits no telemetry itself; the bundled CLI exports metrics, log events and beta traces over OTLP using env var configuration."
resource: "https://code.claude.com/docs/en/agent-sdk/observability"
tags: [opentelemetry, telemetry, otlp, environment]
kind: "mixed"
maturity: "beta"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "OTEL_METRICS_EXPORTER"
  - "OTEL_LOGS_EXPORTER"
  - "OTEL_TRACES_EXPORTER"
  - "CLAUDE_CODE_ENHANCED_TELEMETRY_BETA"
  - "ClaudeAgentOptions.env"
  - "options.env"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-observability"
    resource: "https://code.claude.com/docs/en/agent-sdk/observability"
    title: "Observability with OpenTelemetry"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The Agent SDK runs the Claude Code CLI as a child process over a local pipe. The CLI has built-in OpenTelemetry instrumentation; the SDK produces no telemetry of its own and only passes configuration through, and the CLI exports straight to your collector. Data goes to any OTLP backend.

# How to use it

Configuration is environment variables, set either in the process environment (recommended for production; every `query()` picks them up) or per call in `ClaudeAgentOptions.env` / `options.env` (when different agents need different settings). Python merges `env` over the inherited environment; TypeScript `env` replaces it, so include `...process.env`.

| Signal | Contains | Enable with |
| - | - | - |
| Metrics | counters for tokens, cost, sessions, lines of code, tool decisions | `OTEL_METRICS_EXPORTER` |
| Log events | records for each prompt, API request, API error, tool result | `OTEL_LOGS_EXPORTER` |
| Traces (beta) | spans for each interaction, model request, tool call, hook | `OTEL_TRACES_EXPORTER` plus `CLAUDE_CODE_ENHANCED_TELEMETRY_BETA=1` |

Each signal has its own switch and exporter. The full metric, event and attribute lists are in the Monitoring reference.
