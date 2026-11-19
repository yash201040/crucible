---
type: "Reference"
title: "Callbacks and keys for Button, Input, Select"
description: "Control callbacks, which controls need a key, and how ui.press, ui.input and ui.select let other mods observe them."
resource: "https://code.claude.com/docs/en/plugins/mods/interface"
tags: [mods, callbacks, keys, controls]
kind: "ui"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop, ide]
requires: ""
identifiers:
  - "onPress"
  - "onSubmit"
  - "onInput"
  - "onSelect"
  - "options"
  - "key"
  - "ui.press"
  - "ui.input"
  - "ui.select"
  - "$.prompt.submit"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-interface"
    resource: "https://code.claude.com/docs/en/plugins/mods/interface"
    title: "Draw in the interface with a mod"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

| Control | Callback |
| :- | :- |
| `Button` | `onPress(e)`; `e.surface` is the app the press came from |
| `Input` | `onSubmit(value)` and `onInput(value)` |
| `Select` | `onSelect(value)`; `options` is a list of at least one `{ value, label }` with unique values |

# How to use it

Give every `Input` and `Select` a `key`. A `Button` may omit it when it has a `label` or one string child (key is then that text). Tests press or type into controls by key. Claude Code fires `ui.press`, `ui.input` or `ui.select` with the key in `e.element` before running the callback; another mod's hook (with a `plugin` matcher) can see typed text, change it, or stop your callback. The mods API gives other mods no method to press your buttons. Messages `needs a key` or `is drawn twice` point to troubleshooting.

# Notes

Submitting an `Input` does not start a turn unless the callback calls `$.prompt.submit`. Keeping the same `value` across redraws preserves what the user is typing; a different `value` replaces it.
