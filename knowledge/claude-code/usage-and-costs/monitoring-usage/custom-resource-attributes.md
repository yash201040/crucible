---
type: "Feature"
title: "Custom attributes via OTEL_RESOURCE_ATTRIBUTES"
description: "Add team or cost-center attributes to all metrics and events; strict formatting rules apply."
resource: "https://code.claude.com/docs/en/monitoring-usage"
tags: [telemetry, resource-attributes, multi-team, formatting]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "OTEL_RESOURCE_ATTRIBUTES"
  - "OTEL_METRICS_INCLUDE_RESOURCE_ATTRIBUTES"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "monitoring-usage"
    resource: "https://code.claude.com/docs/en/monitoring-usage"
    title: "Monitoring"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Comma-separated key=value pairs that label every metric datapoint and event record, and are also sent in the OTLP resource block. Use them to filter by team, track cost per cost center, build team dashboards or alerts. Custom keys never override standard attributes such as `user.id` or `session.id` (built-in value kept), except the `vcs.*` repository attributes.

# How to use it

```bash
export OTEL_RESOURCE_ATTRIBUTES="department=engineering,team.id=platform,cost_center=eng-123"
```

Format rules: no spaces in values (`org.name=My Company` is invalid; use `Johns_Organization` or `JohnsOrganization`); only US-ASCII excluding control characters, whitespace, double quotes, commas, semicolons, backslashes; other characters percent-encoded (`John%27s%20Organization`), and `=` inside a value written `%3D`; quotes do not escape spaces. Claude Code does not expand shell syntax in values.

# Notes

Every custom key becomes a label on every metric series, so high-cardinality values raise storage cost. Set `OTEL_METRICS_INCLUDE_RESOURCE_ATTRIBUTES=false` to keep them in the resource block only.
