---
type: "Reference"
title: "Spinner tips, verbs and status line"
description: "Settings for spinner tips, spinner verbs and the custom status line command."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [settings, spinner, status-line, tips]
kind: "setting"
maturity: "unlabelled"
since: "2.1.247"
surfaces: [cli]
requires: ""
identifiers:
  - "spinnerTipsEnabled"
  - "spinnerTipsOverride"
  - "spinnerTipsOverride.tips"
  - "spinnerTipsOverride.tipsFile"
  - "spinnerTipsOverride.label"
  - "spinnerTipsOverride.excludeDefault"
  - "spinnerVerbs"
  - "statusLine"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Keys controlling the text on the spinner line and the status line below the prompt.

# How to use it

| Name | Type | Default | What it does |
| :- | :- | :- | :- |
| `spinnerTipsEnabled` | Boolean | `true` | `false` hides all spinner tips, yours included. `/config`: Show tips |
| `spinnerTipsOverride` | object: `tips`, `tipsFile`, `label`, `excludeDefault` | unset | Add or replace tips |
| `spinnerVerbs` | object: `verbs` array, `mode` `"append"` or `"replace"` | unset | Add to or replace the rotating verb list; `"replace"` with an empty array keeps built-ins |
| `statusLine` | object: `type: "command"`, `command`, optional `padding` (chars), `refreshInterval` (seconds, min `1`), `hideVimModeIndicator` (Boolean) | unset | Custom status line command; example reads `model.display_name` and `context_window.used_percentage` with `jq` |

Tip entries: plain string or object `{ id, text, cooldownSessions, priority }`.

| Field | Required | Rule |
| :- | :- | :- |
| `id` | yes | up to 64 of letters, digits, `.`, `_`, `-`; keys show history; first of duplicate ids wins |
| `text` | yes | one line, up to 500 characters |
| `cooldownSessions` | no | `0` to `1000`, default `0` |
| `priority` | no | `-10` to `10`, default `0` |

# Limits and defaults

- Max 200 tips across `tips` and `tipsFile`; invalid entries dropped with a debug warning.
- `tipsFile`: absolute or `~/` path to a JSON array (or object with `tips`), up to 256 KB, read once per process; cannot be set through server-managed settings.
- `label`: up to 40 characters, default `Tip`; project and local tips always use `Tip`.
- Tip objects, `tipsFile`, `label` need v2.1.247+; from project and local settings only plain strings are read.
- Multiple files: tips from all combine; `tipsFile`, `label`, `excludeDefault` come from the highest-precedence of managed, `--settings`, user.
- `excludeDefault: true` hides built-ins but falls back to them if none of yours load.
- `statusLine` scope is any file, but when `allowManagedHooksOnly` is on or `disableAllHooks` is set outside managed settings, only the managed value runs.
