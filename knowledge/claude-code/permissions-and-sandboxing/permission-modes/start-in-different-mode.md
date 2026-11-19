---
type: "Guide"
title: "Set the starting permission mode"
description: "Where to set permissions.defaultMode per scope (session, machine, project, organization) and what each honors."
resource: "https://code.claude.com/docs/en/permission-modes"
tags: [permissions, settings, defaultmode, managed-settings]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli, ide]
requires: ""
identifiers:
  - "permissions.defaultMode"
  - "permissions.disableAutoMode"
  - "~/.claude/settings.json"
  - ".claude/settings.json"
  - "--permission-mode"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permission-modes"
    resource: "https://code.claude.com/docs/en/permission-modes"
    title: "Choose a permission mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The starting mode can be set for one session, a machine, a project or an organization. When several files set `permissions.defaultMode`, settings precedence decides, so a project or managed value outranks `~/.claude/settings.json`.

# How to use it

| Scope | How |
| :- | :- |
| One session | `claude --permission-mode default` |
| Every terminal session on this machine | `permissions.defaultMode` in `~/.claude/settings.json` |
| Every terminal session in one project | `permissions.defaultMode` in the project's `.claude/settings.json`; terminal sessions honor every value except `auto` and `bypassPermissions`; VS Code does not read project settings for this |
| Whole organization | `permissions.defaultMode` in managed settings (people can still switch to auto). To remove auto entirely set `permissions.disableAutoMode` to `"disable"` |

```json
{ "permissions": { "defaultMode": "default" } }
```

The next session shows `⏸ manual mode on` in the status bar.
