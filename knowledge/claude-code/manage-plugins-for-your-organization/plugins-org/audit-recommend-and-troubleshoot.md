---
type: "Guide"
title: "Plugin audit, suggestions and policy troubleshooting"
description: "OpenTelemetry events and the Analytics API for plugin usage, the suggestion allowlist key, and checks when plugin policy misbehaves."
resource: "https://code.claude.com/docs/en/plugins/org"
tags: [plugins, audit, telemetry, analytics, troubleshooting]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, cloud]
requires: "Analytics API needs the Enterprise plan"
identifiers:
  - "claude_code.plugin_installed"
  - "claude_code.plugin_loaded"
  - "OTEL_LOG_TOOL_DETAILS"
  - "GET /v1/organizations/analytics/plugins"
  - "pluginSuggestionMarketplaces"
  - "/status"
  - "claude plugin list"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-org"
    resource: "https://code.claude.com/docs/en/plugins/org"
    title: "Manage Claude Code plugins for your organization"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Ways to see what a fleet installs and runs, and to debug policy.

# How to use it

- OpenTelemetry: `claude_code.plugin_installed` (each install) and `claude_code.plugin_loaded` (each enabled plugin at session start). Third-party plugin and marketplace names are redacted or omitted unless `OTEL_LOG_TOOL_DETAILS=1`.
- Analytics API (Enterprise plan): `GET /v1/organizations/analytics/plugins` returns per-plugin per-day install and invocation counts across Claude Code and Cowork, groupable by user or RBAC group. Activity without a plugin name appears in one aggregate `third-party` row.
- Suggestions: marketplace plugins can be suggested only if the marketplace is listed in `pluginSuggestionMarketplaces`, registered, and its source is declared in the same policy. In a cloud session conversation, Claude can suggest plugins regardless of this key.
- Troubleshooting: a `managed-settings.json` that is not valid JSON makes Claude Code refuse to start with an error naming the file; a file with one invalid entry keeps the rest. Run `/status` and look for `Enterprise managed settings` in `Setting sources`. A user-disabled plugin that still loads shows `Disabled in ~/.claude/settings.json but still loads` with the overriding source (for example a managed `enabledPlugins`).

# Notes

Read the plugin security page before approving a marketplace.
