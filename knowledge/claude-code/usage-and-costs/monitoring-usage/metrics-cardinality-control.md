---
type: "Reference"
title: "Metrics cardinality control"
description: "Environment variables that include or drop attributes on metrics and events to manage cardinality."
resource: "https://code.claude.com/docs/en/monitoring-usage"
tags: [telemetry, cardinality, attributes, env-vars]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "OTEL_METRICS_INCLUDE_SESSION_ID"
  - "OTEL_METRICS_INCLUDE_VERSION"
  - "OTEL_METRICS_INCLUDE_ACCOUNT_UUID"
  - "OTEL_METRICS_INCLUDE_ENTRYPOINT"
  - "OTEL_METRICS_INCLUDE_RESOURCE_ATTRIBUTES"
  - "OTEL_METRICS_INCLUDE_REPOSITORY"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "monitoring-usage"
    resource: "https://code.claude.com/docs/en/monitoring-usage"
    title: "Monitoring"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Switches that decide which attributes appear on metrics and events. Lower cardinality means better performance and lower storage cost but less granular analysis.

# How to use it

| Variable | Attribute(s) controlled | Default |
| - | - | - |
| `OTEL_METRICS_INCLUDE_SESSION_ID` | `session.id` and cloud sessions' `ccr.session.id` | `true` |
| `OTEL_METRICS_INCLUDE_VERSION` | `app.version` | `false` |
| `OTEL_METRICS_INCLUDE_ACCOUNT_UUID` | `user.account_uuid`, `user.account_id` | `true` |
| `OTEL_METRICS_INCLUDE_ENTRYPOINT` | `app.entrypoint` | `false` |
| `OTEL_METRICS_INCLUDE_RESOURCE_ATTRIBUTES` | keys from `OTEL_RESOURCE_ATTRIBUTES` on datapoints and events | `true` |
| `OTEL_METRICS_INCLUDE_REPOSITORY` | `vcs.*` repository attributes (v2.1.269+) | `false` |
