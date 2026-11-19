---
type: "Reference"
title: "Where hooks are configured and how to disable"
description: "Hook scope by location (user, project, local, managed, plugin, skill, subagent), /hooks browser and disableAllHooks."
resource: "https://code.claude.com/docs/en/hooks-guide"
tags: [hooks, settings, scope, managed]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "~/.claude/settings.json"
  - ".claude/settings.json"
  - ".claude/settings.local.json"
  - "hooks/hooks.json"
  - "disableAllHooks"
  - "allowManagedHooksOnly"
  - "/hooks"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks-guide"
    resource: "https://code.claude.com/docs/en/hooks-guide"
    title: "Automate actions with hooks"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Where a hook is added sets its scope.

# How to use it

| Location | Scope | Shareable |
| --- | --- | --- |
| `~/.claude/settings.json` | All your projects | No |
| `.claude/settings.json` | Single project | Yes, can be committed |
| `.claude/settings.local.json` | Single project | No, gitignored when Claude Code saves a setting to it |
| Managed policy settings | Organization-wide | Yes, admin-controlled |
| Plugin `hooks/hooks.json` | While the plugin is enabled | Yes |
| Skill frontmatter | Rest of session once the skill is invoked | Yes |
| Subagent frontmatter | While that subagent runs | Yes |

`/hooks` browses all configured hooks by event. It does not list hooks from a skill not yet invoked in the session.

# Limits and defaults

`"disableAllHooks": true` disables hooks, using the value left after settings precedence (a project file can override yours); hooks from managed settings still run unless `disableAllHooks` is also set there. Edits to settings files are normally picked up by the file watcher; restart if not. If `/hooks` shows `Only hooks from managed settings run here`, `allowManagedHooksOnly` is set and user, project and local hooks do not run.
