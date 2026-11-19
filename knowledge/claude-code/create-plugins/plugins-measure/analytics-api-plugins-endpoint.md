---
type: "Feature"
title: "Analytics API plugins endpoint"
description: "GET /v1/organizations/analytics/plugins returns per-plugin per-day install and invocation counts for Enterprise organizations, without an exporter."
resource: "https://code.claude.com/docs/en/plugins/measure"
tags: [plugins, analytics-api, enterprise, usage]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop, web]
requires: "Enterprise plan; API key with read:analytics scope created by a Primary Owner"
identifiers:
  - "GET /v1/organizations/analytics/plugins"
  - "read:analytics"
  - "third-party"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-measure"
    resource: "https://code.claude.com/docs/en/plugins/measure"
    title: "Measure plugin cost and usage"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

On the Enterprise plan, `GET /v1/organizations/analytics/plugins` answers which plugins the organization installs and invokes, from Anthropic's records. It returns per-plugin, per-day install and invocation counts across Claude Code and Cowork, groupable by user, RBAC group, or product.

# How to use it

Authenticate with an API key that has the `read:analytics` scope, created by a Primary Owner (see Access data programmatically on the analytics page). Parameters and response fields are on the endpoint reference.

# Notes

Plugin activity that reaches Anthropic without a plugin name appears in one aggregate `third-party` row.
