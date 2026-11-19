---
type: "Feature"
title: "Terminal bell, notifications and session status"
description: "How Claude Code signals that it finished or needs permission: preferredNotifChannel, Notification hooks, and OSC 7501 session status."
resource: "https://code.claude.com/docs/en/terminal-config"
tags: [notifications, bell, hooks, osc-7501]
kind: "setting"
maturity: "unlabelled"
since: "2.1.295"
surfaces: [cli]
requires: "OSC 7501 status needs Claude Code v2.1.295 or later and a terminal that implements it"
identifiers:
  - "preferredNotifChannel"
  - "terminal_bell"
  - "auto"
  - "iterm2"
  - "kitty"
  - "ghostty"
  - "Notification"
  - "CLAUDE_CODE_DISABLE_TERMINAL_TITLE"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "terminal-config"
    resource: "https://code.claude.com/docs/en/terminal-config"
    title: "Configure your terminal for Claude Code"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

When Claude finishes or pauses for a permission prompt while you appear away, it fires a notification event. Defaults: Ghostty, Kitty and iTerm2 (when detected) get a desktop notification (iTerm2 only after its alert settings are on); Apple Terminal gets a silent bell character only if "Audible bell" is off in the profile; other terminals get nothing.

# How to use it

Set `preferredNotifChannel` in settings: `"terminal_bell"` sends the bell character regardless of terminal; default `"auto"`. Over SSH outside tmux keep `"auto"`; before v2.1.326 set `"iterm2"`, `"kitty"` or `"ghostty"` on the machine running Claude Code. iTerm2 needs Settings > Profiles > Terminal > "Notification Center Alerts" and "Send escape sequence-generated alerts". Inside tmux enable `allow-passthrough` (a pane in a window you are not viewing sends none; tmux older than 3.3 lacks the option).

A `Notification` hook runs alongside the built-in notification, for a sound or custom command:

```json
{ "hooks": { "Notification": [ { "hooks": [ { "type": "command", "command": "afplay /System/Library/Sounds/Glass.aiff" } ] } ] } }
```

# Limits and defaults

Terminals implementing the OSC 7501 Program Status Protocol can show whether each interactive session is working, waiting or done; nothing to enable. It needs v2.1.295+, is not available inside tmux (Claude Code checks tmux for support, `allow-passthrough` has no effect), does not apply to background sessions (agent view shows status instead), and is skipped when `CLAUDE_CODE_DISABLE_TERMINAL_TITLE=1`. Such terminals do not get the status glyph in the tab title.
