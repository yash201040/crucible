---
type: "Reference"
title: "Permission update entries"
description: "The array format used by updatedPermissions and permission_suggestions: types, fields, modes and destinations."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, permissions, settings, reference]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "addRules"
  - "replaceRules"
  - "removeRules"
  - "setMode"
  - "addDirectories"
  - "removeDirectories"
  - "destination"
  - "session"
  - "localSettings"
  - "projectSettings"
  - "userSettings"
  - "toolName"
  - "ruleContent"
  - "default"
  - "auto"
  - "acceptEdits"
  - "dontAsk"
  - "bypassPermissions"
  - "plan"
  - "manual"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`updatedPermissions` (hook output) and `permission_suggestions` (hook input) share one array of entry objects. Each has a `type` fixing its other fields and a `destination` saying where the change is stored.

# How to use it

| `type` | Fields | Effect |
| :- | :- | :- |
| `addRules` | `rules`, `behavior`, `destination` | Add rules; `rules` = array of `{toolName, ruleContent?}`; `behavior` is `allow`, `deny` or `ask` |
| `replaceRules` | `rules`, `behavior`, `destination` | Replace all rules of that behavior at the destination |
| `removeRules` | `rules`, `behavior`, `destination` | Remove matching rules |
| `setMode` | `mode`, `destination` | Change permission mode: `default`, `auto`, `acceptEdits`, `dontAsk`, `bypassPermissions`, `plan`, `manual` (alias for `default`) |
| `addDirectories` | `directories`, `destination` | Add working directories |
| `removeDirectories` | `directories`, `destination` | Remove working directories |

| `destination` | Writes to |
| :- | :- |
| `session` | In memory only, dropped at session end |
| `localSettings` | `.claude/settings.local.json` |
| `projectSettings` | `.claude/settings.json` |
| `userSettings` | `~/.claude/settings.json` |

Rule mapping: `Bash(npm test)` is `{ "toolName": "Bash", "ruleContent": "npm test" }`; `Bash` or `Bash(*)` is `{ "toolName": "Bash" }`; `mcp__github__get_issue` is `{ "toolName": "mcp__github__get_issue" }`. Leave `ruleContent` out of an allow rule for an MCP tool or it matches no call. A hook can echo one of the received suggestions as its own `updatedPermissions`.

# Limits and defaults

- `setMode` with `bypassPermissions` takes effect only if the session launched with bypass mode already available (`--dangerously-skip-permissions`, `--permission-mode bypassPermissions`, `--allow-dangerously-skip-permissions`, or `permissions.defaultMode: "bypassPermissions"` in user, `--settings` or managed settings). Otherwise a no-op; also a no-op when `permissions.disableBypassPermissionsMode` disables it or the session starts in restricted mode.
- `bypassPermissions` is never persisted as `defaultMode` regardless of destination.
