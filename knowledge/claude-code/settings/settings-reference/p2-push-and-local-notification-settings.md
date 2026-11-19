---
type: "Reference"
title: "Notification and recap settings"
description: "Settings for mobile push notifications, local notification channel and the away summary recap."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [settings, notifications, push, remote-control]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli, mobile]
requires: "Remote Control connected for push in a local session"
identifiers:
  - "agentPushNotifEnabled"
  - "inputNeededNotifEnabled"
  - "preferredNotifChannel"
  - "awaySummaryEnabled"
  - "CLAUDE_CODE_ENABLE_AWAY_SUMMARY"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Any-file keys for how Claude Code reaches you when it is done or needs input.

# How to use it

| Name | Type / values | Default | What it does |
| :- | :- | :- | :- |
| `agentPushNotifEnabled` | Boolean | `false` | Claude may push to your phone when it decides it is worth it (for example a long task finished). In a local session only while Remote Control is connected. `/config`: Push when Claude decides. Not enough alone; follow Mobile push notifications setup. Sessions under a `claude remote-control` server follow the value saved to your account instead |
| `inputNeededNotifEnabled` | Boolean | `false` | Push when a permission prompt or question awaits input; local sessions only while Remote Control is connected. `/config`: Push when actions required |
| `preferredNotifChannel` | `"auto"`, `"terminal_bell"`, `"iterm2"`, `"iterm2_with_bell"`, `"kitty"`, `"ghostty"`, `"notifications_disabled"` | `"auto"` | Local notification on task completion or prompt. `auto`: desktop notification when iTerm2, Ghostty or Kitty detected; bell in Terminal.app only if its audible bell is off; nothing elsewhere. Mod notifications use the same setting. `/config`: Local notifications |
| `awaySummaryEnabled` | Boolean | unset (on) | One-line recap after a few minutes away; never shown in non-interactive mode. `CLAUDE_CODE_ENABLE_AWAY_SUMMARY` overrides per session in either direction |

# Notes

The first two also read an older value from `~/.claude.json`, as does `preferredNotifChannel`.
