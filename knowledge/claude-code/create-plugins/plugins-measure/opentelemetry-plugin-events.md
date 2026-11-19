---
type: "Reference"
title: "OpenTelemetry events for plugins"
description: "Events and attributes that answer plugin install, load, skill activation, hook and cost questions, and how names are redacted."
resource: "https://code.claude.com/docs/en/plugins/measure"
tags: [plugins, telemetry, opentelemetry, cost]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "claude_code.plugin_installed"
  - "claude_code.plugin_loaded"
  - "claude_code.skill_activated"
  - "claude_code.hook_plugin_metrics"
  - "plugin.name"
  - "marketplace.name"
  - "plugin_id_hash"
  - "skill.name"
  - "OTEL_LOG_TOOL_DETAILS"
  - "third-party"
  - "custom_skill"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-measure"
    resource: "https://code.claude.com/docs/en/plugins/measure"
    title: "Measure plugin cost and usage"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Once an exporter is configured, Claude Code sends these events to your backend.

| Question | Event or attribute |
| :- | :- |
| Which plugins get installed | `claude_code.plugin_installed`, one per install |
| Which plugins are active in how many sessions | `claude_code.plugin_loaded`, one per enabled plugin at session start |
| Which skills activate and which plugin owns them | `claude_code.skill_activated`, with `plugin.name` and `marketplace.name` for plugin skills |
| What a plugin's hooks report | `claude_code.hook_plugin_metrics`, only for hooks in official-marketplace plugins |
| Plugin API spend | `plugin.name` and `marketplace.name` on the cost counter, set when the active skill or subagent belongs to a plugin |

# Limits and defaults

Official-marketplace plugins report names verbatim; every other plugin, including your org's own marketplace, is redacted or omitted by default (decided by trust tier). Set `OTEL_LOG_TOOL_DETAILS=1` on exporting machines (for example in the `env` block of managed settings) for real names:

| Event | Default | With `OTEL_LOG_TOOL_DETAILS=1` |
| :- | :- | :- |
| `plugin_loaded` | `plugin.name` and `marketplace.name` are literal `third-party` | Real names |
| `plugin_installed`, `skill_activated` | names omitted; `skill.name` is `custom_skill` on `skill_activated` | Real names |
| Cost counter | `plugin.name` is `third-party`; `marketplace.name` absent | Real `plugin.name`; `marketplace.name` still absent |

`plugin_id_hash` on `plugin_loaded` still identifies each plugin by default.
