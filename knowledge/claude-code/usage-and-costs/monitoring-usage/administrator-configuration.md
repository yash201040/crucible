---
type: "Feature"
title: "Administrator configuration of telemetry"
description: "Set OTel variables for all users via managed settings; repository settings cannot enable telemetry; OTEL_* variables are not passed to subprocesses."
resource: "https://code.claude.com/docs/en/monitoring-usage"
tags: [telemetry, managed-settings, admin, security]
kind: "setting"
maturity: "unlabelled"
since: "2.1.223"
surfaces: [cli, desktop]
requires: ""
identifiers:
  - "env"
  - ".claude/settings.json"
  - ".claude/settings.local.json"
  - "~/.claude/settings.json"
  - "--settings"
  - "/status"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "monitoring-usage"
    resource: "https://code.claude.com/docs/en/monitoring-usage"
    title: "Monitoring"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Administrators put the telemetry variables in the `env` block of the managed settings file so every user exports to the same collector.

# How to use it

```json
{ "env": {
  "CLAUDE_CODE_ENABLE_TELEMETRY": "1",
  "OTEL_METRICS_EXPORTER": "otlp",
  "OTEL_LOGS_EXPORTER": "otlp",
  "OTEL_EXPORTER_OTLP_PROTOCOL": "grpc",
  "OTEL_EXPORTER_OTLP_ENDPOINT": "http://collector.example.com:4317",
  "OTEL_EXPORTER_OTLP_HEADERS": "Authorization=Bearer example-token" } }
```

- Claude Desktop Code tab sessions read managed settings from the sources that reach each kind of Desktop session. The Cowork OpenTelemetry form in the admin console (Data and privacy settings, Monitoring) applies to Cowork sessions only; neither the terminal CLI nor the Code tab exports to a collector set there.
- Claude Code ignores the OpenTelemetry exporter variables in a repository's `.claude/settings.json` and `.claude/settings.local.json`, so a repository cannot turn telemetry on, choose its destination or capture content. Set them in managed settings, or in the shell or `~/.claude/settings.json`.
- A repository can still turn a signal off by setting its exporter selector (for example `OTEL_LOGS_EXPORTER`) to `none`, unless managed settings, a `--settings` file or the launch environment sets that variable.
- Claude Code does not pass `OTEL_*` variables to subprocesses it spawns: the Bash tool, hooks, MCP servers and language servers. An instrumented app run through Bash must get its own exporter variables in the command.

# Limits and defaults

Locking behaviour (v2.1.223 and later for exporter selectors): see [OTLP destination locking](./otlp-destination-locking.md).
