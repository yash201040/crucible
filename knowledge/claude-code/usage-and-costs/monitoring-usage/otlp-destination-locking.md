---
type: "Feature"
title: "How managed settings lock the OTLP destination"
description: "When managed settings set OTLP variables, Claude Code removes conflicting developer-set endpoint, protocol and credential variables at startup."
resource: "https://code.claude.com/docs/en/monitoring-usage"
tags: [telemetry, managed-settings, otlp, security]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.217"
surfaces: [cli, desktop]
requires: "Exporter selectors rule: Claude Code v2.1.223 or later; launcher pinning: v2.1.251 or later"
identifiers:
  - "OTEL_EXPORTER_OTLP_ENDPOINT"
  - "OTEL_EXPORTER_OTLP_PROTOCOL"
  - "OTEL_EXPORTER_OTLP_HEADERS"
  - "OTEL_EXPORTER_OTLP_CLIENT_KEY"
  - "OTEL_EXPORTER_OTLP_CLIENT_CERTIFICATE"
  - "OTEL_TRACES_EXPORTER"
  - "BETA_TRACING_ENDPOINT"
  - "otelHeadersHelper"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "monitoring-usage"
    resource: "https://code.claude.com/docs/en/monitoring-usage"
    title: "Monitoring"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

When an `OTEL_EXPORTER_OTLP_*` variable is set in managed settings, Claude Code removes conflicting developer-set variables at startup and writes a warning to the debug log. This changes where telemetry goes, not what is collected.

# How to use it

| Managed variable set | Developer-set variables removed |
| - | - |
| `OTEL_EXPORTER_OTLP_ENDPOINT` | every per-signal endpoint |
| `OTEL_EXPORTER_OTLP_PROTOCOL` | every per-signal protocol |
| `OTEL_EXPORTER_OTLP_HEADERS`, `OTEL_EXPORTER_OTLP_CLIENT_KEY`, `OTEL_EXPORTER_OTLP_CLIENT_CERTIFICATE` | per-signal versions of that variable, plus every endpoint variable (generic and per-signal) |
| `OTEL_METRICS_EXPORTER`, `OTEL_LOGS_EXPORTER`, `OTEL_TRACES_EXPORTER` (beta) | none: normal per-key precedence, so a developer can still disable a signal or switch to console. Set them in managed settings to lock them. `OTEL_LOGS_EXPORTER` follows the telemetry unit across admin sources; the other two merge per key. Requires v2.1.223+ |

- Per-signal variables set in managed settings itself are not removed, so one signal can be routed to a different collector (as in the SIEM example). A per-signal credential set there removes the developer-set endpoint for that signal.
- Detailed beta tracing exports logs and traces to `BETA_TRACING_ENDPOINT`. Claude Code removes a developer-set `BETA_TRACING_ENDPOINT` when managed settings decide either signal's destination: a generic or logs/traces endpoint or credential, an `otelHeadersHelper`, a logs or traces selector of `none`, `console` or empty, or `CLAUDE_CODE_ENABLE_TELEMETRY` turned off. A metrics-only endpoint or credential does not remove it. Before v2.1.251 a developer-set `BETA_TRACING_ENDPOINT` could redirect those exports.
- When the desktop app or a self-hosted environment runner launches Claude Code and names an OTLP endpoint in the environment it provides, the same pinning applies; variables the launcher itself set are not removed. Requires v2.1.251 or later.

# Notes

Before v2.1.217 every variable followed per-key precedence independently, so a per-signal endpoint in user settings or the shell redirected that signal away from the managed collector.
