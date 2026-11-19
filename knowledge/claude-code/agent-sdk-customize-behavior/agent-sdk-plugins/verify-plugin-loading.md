---
type: "Feature"
title: "Verify plugins in the init message"
description: "Loaded plugins, plugin skills and commands show up in the system init message; plugin_errors explains a plugin that failed."
resource: "https://code.claude.com/docs/en/agent-sdk/plugins"
tags: [plugins, init-message, verification, troubleshooting]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "system"
  - "init"
  - "plugins"
  - "skills"
  - "slash_commands"
  - "plugin_errors"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-plugins"
    resource: "https://code.claude.com/docs/en/agent-sdk/plugins"
    title: "Plugins in the SDK"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The first stream message (`type: "system"`, `subtype: "init"`) reports what loaded. Because a missing plugin path is skipped silently, this message is how a program confirms a load.

# How to use it

| Field | Content |
| --- | --- |
| `plugins` | Array like `[{ name: "my-plugin", path: "/absolute/path/to/my-plugin" }]` |
| `skills` | Plugin skills with the plugin name as prefix, for example `["my-plugin:greet"]` |
| `slash_commands` | Built-ins plus plugin commands and skills, for example `["compact", "context", "my-plugin:custom-command", "my-plugin:greet"]` |
| `plugin_errors` | Reason a plugin failed to load; check it when the plugin is absent from `plugins` |

In Python the same fields are read from `message.data` of a `SystemMessage` with `subtype == "init"`.

# Notes

Plugin not loading checklist: path points to plugin root; `plugin.json` is valid JSON if present; directory readable; directory exists (a nonexistent path is skipped).
Skills not appearing checklist: invoke as `/plugin-name:skill-name`; check the `skills` list for the namespace; each skill needs `skills/<name>/SKILL.md`.
