---
type: "Guide"
title: "Telemetry from cloud sessions and Claude Tag"
description: "Where to set telemetry variables for cloud sessions, network reachability, and how to tell cloud and Claude Tag sessions apart."
resource: "https://code.claude.com/docs/en/monitoring-usage"
tags: [telemetry, cloud-sessions, claude-tag, attribution]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cloud, web]
requires: ""
identifiers:
  - "CLAUDE_CODE_REMOTE_SESSION_ID"
  - "ccr.session.id"
  - "OTEL_METRICS_INCLUDE_ENTRYPOINT"
  - "claude-in-slack"
  - "OTEL_RESOURCE_ATTRIBUTES"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "monitoring-usage"
    resource: "https://code.claude.com/docs/en/monitoring-usage"
    title: "Monitoring"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Cloud sessions (including Claude Tag channel sessions) run in cloud environments, so device-side managed settings do not configure them.

# How to use it

Set `CLAUDE_CODE_ENABLE_TELEMETRY` and the `OTEL_*` variables in one of two places:
- Server-managed settings `env` block: reaches cloud sessions other than Claude Tag channel sessions (Claude Tag and Cowork sessions do not receive server-managed settings).
- A cloud environment's environment variables: affects only sessions in that environment; the route that reaches Claude Tag sessions.

Do not put credentials (e.g. a collector token in `OTEL_EXPORTER_OTLP_HEADERS`) in environment variables: anyone using the environment can read them, and a network secret does not help because Claude Code's telemetry export never gets the secret. If a credential is needed, configure the export entirely via server-managed settings.

The collector domain must be reachable under the environment's network access level; add it to the environment's allowlist (no server-managed setting adds domains). For Claude Tag channels change the shared environment set as default or pinned to the channel.

Attribution: metrics and events carry `session.id`, `ccr.session.id` (value of `CLAUDE_CODE_REMOTE_SESSION_ID`) and `organization.id`; group by `ccr.session.id` to tell cloud sessions apart. Set `OTEL_METRICS_INCLUDE_ENTRYPOINT=true` to get `app.entrypoint` = `claude-in-slack` for Claude Tag sessions. Add custom attributes with `OTEL_RESOURCE_ATTRIBUTES` where the other `OTEL_*` variables are set; exporting it in the environment's setup script does not reach Claude Code.

# Notes

In Claude Tag channel sessions Claude works as the organization's shared identity, so do not rely on `user.*` attributes to identify who tagged Claude.
