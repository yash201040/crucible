---
type: "Reference"
title: "Organization plugin controls and telemetry"
description: "What managed settings can enforce for plugins and how plugin names appear in OpenTelemetry events and the Analytics API."
resource: "https://code.claude.com/docs/en/plugins/security"
tags: [plugins, managed-settings, telemetry, otel]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "--plugin-dir"
  - "--plugin-url"
  - "CLAUDE_CODE_PLUGIN_DIRS"
  - "syncClaudeAiPlugins"
  - "allowedChannelPlugins"
  - "OTEL_LOG_TOOL_DETAILS"
  - "plugin.name"
  - "marketplace.name"
  - "plugin.scope"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-security"
    resource: "https://code.claude.com/docs/en/plugins/security"
    title: "Plugin security and trust"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Controls an administrator can enforce through managed settings, and what plugin names telemetry reports.

# How to use it

Managed settings can: allowlist or blocklist marketplace sources; force-enable plugins; turn off `--plugin-dir`, `--plugin-url` and the `CLAUDE_CODE_PLUGIN_DIRS` variable; limit hooks to those from managed settings and force-enabled plugins; stop plugins from members' claude.ai accounts loading with `syncClaudeAiPlugins`. The control matrix on the org page says what each key covers.

Telemetry (OpenTelemetry events):

| Item | Behavior |
| :- | :- |
| Plugin loaded event | Official-tier names reported as is; community and third-party `plugin.name` and `marketplace.name` are the literal `third-party` unless `OTEL_LOG_TOOL_DETAILS=1` |
| `plugin.scope` | Still reports origin, e.g. `org` for managed-settings plugins, `user-local` for other third-party plugins |
| Plugin installed event | Without `OTEL_LOG_TOOL_DETAILS=1`, name fields for non-official plugins are omitted (not `third-party`) |
| Claude Code Analytics API | Official and community plugins by name; every other plugin as `third-party` |
