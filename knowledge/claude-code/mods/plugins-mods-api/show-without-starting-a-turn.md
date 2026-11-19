---
type: "Reference"
title: "Mod UI output calls: status, toast, log, notify"
description: "Four $.ui calls show text without starting a turn; only $.ui.notify answers with isSent and a reason."
resource: "https://code.claude.com/docs/en/plugins/mods/api"
tags: [mods, ui, notifications, preferrednotifchannel]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [cli, ide]
requires: ""
identifiers:
  - "$.ui.status"
  - "$.ui.toast"
  - "$.ui.log"
  - "$.ui.notify"
  - "preferredNotifChannel"
  - "terminal_bell"
  - "notifications_disabled"
  - "plugin_notification"
  - "Notification"
  - "turn.complete"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-api"
    resource: "https://code.claude.com/docs/en/plugins/mods/api"
    title: "Use the mods API"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A background job can show the user something without starting a turn.

# How to use it

| Call | What the user sees |
| :- | :- |
| `$.ui.status(text)` | One line under the prompt until changed, starting with `⚠` and the mod's name |
| `$.ui.toast(text)` | Toast with mod's name, gone after seconds (top-right box in fullscreen rendering; one line under the prompt in classic) |
| `$.ui.log(text)` | Dim transcript line Claude does not read, starting with `●` and the mod's name |
| `$.ui.notify(text)` | Terminal notification via the user's `preferredNotifChannel`; mod's name is the title unless a non-empty `{ title }` is passed |

`$.ui.notify` resolves to `{ isSent: true, channel }` (`channel` such as `kitty` or `terminal_bell`; `terminal_bell` rings the bell and shows no text) or `{ isSent: false, reason }`:

| `reason` | Meaning |
| :- | :- |
| `disabled` | setting is `notifications_disabled` |
| `no-channel` | setting is `auto` and the terminal has none Claude Code can use |
| `no-surface` | no terminal: `-p` run, Agent SDK, desktop app, VS Code extension, cloud session; also calls before session start or during exit |
| `refused` | another mod's `ui.notify` hook answered without sending |

# Limits and defaults

- It rejects when `text` is not a string, another mod's hook returns `{ deny }`, or the terminal write fails.
- A mod cannot choose the channel; Claude Code does not rate-limit mod notifications.
- The user's `Notification` hooks run with type `plugin_notification`, even for `disabled` and `no-surface`; none run before session start or during exit. The calling hook is left out of that run.
- `isSent: true` means sent, not seen.
- In the VS Code extension, status lines and toasts show above the prompt box and log lines in the conversation.
