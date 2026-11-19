---
type: "Guide"
title: "Example: personal settings.json"
description: "A developer's ~/.claude/settings.json setting model, per-model effort, vim mode, theme, status line, notification channel, allow rules, update channel, cleanup."
resource: "https://code.claude.com/docs/en/settings-example"
tags: [settings, example, user-settings, model]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "model"
  - "modelSettings"
  - "effortLevel"
  - "editorMode"
  - "theme"
  - "statusLine"
  - "statusLine.type"
  - "statusLine.command"
  - "statusLine.padding"
  - "spinnerTipsEnabled"
  - "preferredNotifChannel"
  - "permissions.allow"
  - "autoUpdatesChannel"
  - "cleanupPeriodDays"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-example"
    resource: "https://code.claude.com/docs/en/settings-example"
    title: "Example settings files"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

One developer's personal file for `~/.claude/settings.json`, applying to every project. Each page example has a copyable JSON tab and a commented tab; real settings files accept no comments. None is a recommended baseline; values come from the settings reference.

# How to use it

| Key | Example value | Effect |
| :- | :- | :- |
| `model` | `"claude-sonnet-5"` | start every session on Sonnet 5 |
| `modelSettings` | `{"claude-sonnet-5": {"effortLevel": "xhigh"}}` | effort above Sonnet 5's default `high`; `/effort` saves a level per model, `--effort` sets one session |
| `editorMode` | `"vim"` | vim keybindings in prompt |
| `theme` | `"light-daltonized"` | colorblind-friendly light theme |
| `statusLine` | `{"type": "command", "command": "jq -r '...'", "padding": 2}` | status line showing model display name and `context_window.used_percentage` |
| `spinnerTipsEnabled` | `false` | hide spinner tips |
| `preferredNotifChannel` | `"terminal_bell"` | bell for finished task or waiting prompt |
| `permissions.allow` | `["Bash(git diff *)", "Read(~/.zshrc)"]` | no prompt for those |
| `autoUpdatesChannel` | `"stable"` | stable release channel |
| `cleanupPeriodDays` | `20` | delete session transcripts and local session data older than 20 days |
