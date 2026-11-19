---
type: "Concept"
title: "Command menu matching and hidden commands"
description: "How the / menu highlights, handles typos, omits unavailable commands and hides a few commands until typed in full."
resource: "https://code.claude.com/docs/en/commands#how-the-command-menu-matches-what-you-type"
tags: [slash-commands, menu, errors]
kind: "ui"
maturity: "unlabelled"
since: "2.1.236"
surfaces: [cli]
requires: ""
identifiers: []
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "commands"
    resource: "https://code.claude.com/docs/en/commands"
    title: "Commands"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Behavior of the `/` filtering menu.

# How to use it

- Highlighting (v2.1.236+): the top suggestion is highlighted only when the letters match a command name or alias from its start or from a word within it, ignoring `:`, `_`, `-`. `/adddir` highlights `/add-dir`; `/new` highlights `/clear` via its alias. `Enter` runs the highlighted one.
- After a typo nothing is highlighted; `Enter` submits the text as typed and reports Unknown command.
- Unavailable commands are left out of the menu; with no match the menu shows `No commands match "/name"`. Most return Unknown command when submitted; a few answer with their own availability message, and some answer with a message when organization policy disables them.
- Hidden commands such as `/heapdump` appear only once typed in full; a partial name never brings them in.
