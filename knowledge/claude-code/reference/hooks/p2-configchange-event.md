---
type: "Feature"
title: "ConfigChange hook event"
description: "Fires when a settings, managed policy or skill file changes mid-session; can block non-policy changes."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, configchange, settings, audit]
kind: "hook"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "ConfigChange"
  - "user_settings"
  - "project_settings"
  - "local_settings"
  - "policy_settings"
  - "skills"
  - "managed-settings.json"
  - "managed-settings.d/"
  - "wslInheritsWindowsSettings"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Runs when a settings file, a managed policy file or a skill file changes during a session. Use to audit changes, enforce policy or block unauthorized edits. For managed policy it runs only when `managed-settings.json` or a file in `managed-settings.d/` changes.

# How to use it

| Matcher | Fires when |
| :- | :- |
| `user_settings` | `~/.claude/settings.json` changes |
| `project_settings` | `.claude/settings.json` changes |
| `local_settings` | `.claude/settings.local.json` changes |
| `policy_settings` | `managed-settings.json` or a file in `managed-settings.d/` changes |
| `skills` | A skill file in `.claude/skills/` changes |

Input adds `source` and optional `file_path`. Block with exit 2 or `{"decision": "block"}`; the new settings are then not applied to the running session. `reason` is accepted but never shown.

# Limits and defaults

- `policy_settings` changes cannot be blocked; hooks fire (for logging) but a block is ignored.
- Not run for: rules saved via "Yes, and don't ask again", `/permissions` or `/model` in the saving session (other open sessions loading the same file do run hooks); server-managed settings arrival or refresh, macOS managed preferences, Windows registry policy; on WSL with `wslInheritsWindowsSettings`, a changed Windows-side managed file picked up by policy poll.
- A blocked change surfaces no message to user or Claude; only a debug-log line. `systemMessage` and `continue` are discarded.
