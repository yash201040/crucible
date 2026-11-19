---
type: "Feature"
title: "Plugin monitors configuration"
description: "experimental.monitors declares persistent background commands that start at session start or when a named skill first runs."
resource: "https://code.claude.com/docs/en/plugins/manifest-reference"
tags: [plugins, monitors, background, experimental]
kind: "file"
maturity: "experimental"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "experimental.monitors"
  - "monitors/monitors.json"
  - "name"
  - "command"
  - "description"
  - "when"
  - "always"
  - "on-skill-invoke:<skill>"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-manifest-reference"
    resource: "https://code.claude.com/docs/en/plugins/manifest-reference"
    title: "Plugin manifest reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`experimental.monitors` takes a `.json` file path or the inline array; when omitted, Claude Code loads `monitors/monitors.json` if present. The `experimental` container holds keys whose manifest shape may still change. Each entry is a strict object. Monitors do not start with the `-p` flag.

# How to use it

| Field | Required | Description |
| :- | :- | :- |
| `name` | Yes | Identifier unique within the plugin |
| `command` | Yes | Shell command run as a persistent background process in the session working directory |
| `description` | Yes | Summary shown in the task panel and notification summaries |
| `when` | No | `"always"` (default): starts at session start and on plugin reload; `"on-skill-invoke:<skill>"`: starts the first time that skill runs |

Example: `{ "experimental": { "monitors": [ { "name": "deploy-status", "command": "\"${CLAUDE_PLUGIN_ROOT}\"/scripts/poll-deploy.sh", "description": "Deployment status changes", "when": "on-skill-invoke:deploy" } ] } }`.

# Limits and defaults

A monitor `command` cannot reference `${user_config.*}`; monitor processes do not receive `CLAUDE_PLUGIN_OPTION_<KEY>`, so the script must get values itself. Variables resolve in `command` but are not exported to the process.
