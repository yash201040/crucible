---
type: "Reference"
title: "Open and close a pane ($.ui.open fields)"
description: "$.ui.open fields, the true-only flags, immediate commands and when a mod-initiated pane waits for a wider terminal."
resource: "https://code.claude.com/docs/en/plugins/mods/interface"
tags: [mods, pane, ui-open, terminal-width]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [cli, ide]
requires: ""
identifiers:
  - "$.ui.open"
  - "$.ui.close"
  - "id"
  - "title"
  - "focus"
  - "closeOnEscape"
  - "holdToasts"
  - "rows"
  - "columns"
  - "immediate: true"
  - "isPlaced"
  - "$.ui.toast"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-interface"
    resource: "https://code.claude.com/docs/en/plugins/mods/interface"
    title: "Draw in the interface with a mod"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`await $.ui.open({ id: 'hello-tabs', title: 'Hello tabs', focus: true })` opens a pane; `await $.ui.close({ id })` closes it. If another mod has a pane open with that `id`, the call rejects.

# How to use it

| Field | What it does |
| :- | :- |
| `title` | Tab label when more than one pane is open |
| `focus` | Requests keyboard focus |
| `closeOnEscape` | Esc closes the pane |
| `holdToasts` | Terminal: holds toasts while this pane is showing (for dialogs the user answers and leaves; also holds other mods' toasts and Claude Code's short notifications) |
| `rows` | Height asked for above the prompt; default a third of the space |
| `columns` | Width asked for beside the transcript, at most 45% of terminal width; a width the user resized to applies instead, same 45% cap |

`focus`, `closeOnEscape`, `holdToasts` accept only `true`; passing `false` throws (`ui.open: focus is true or left out`). Add the field conditionally. VS Code ignores `rows` and `columns`. To let a command open a pane while Claude works, register it with `immediate: true`; otherwise a command typed during a turn waits for the turn to end.

# Limits and defaults

A pane opened without being asked does not appear in a narrow terminal. Opened by a user action: any width. Opened by the mod itself (timer, `turn.start`): only from 144 columns, or 110 after the user has opened it once. `$.ui.open` resolves `{ isPlaced: true }` or `isPlaced: false` with a `reason`; the waiting pane appears when the user opens it or widens the terminal. Use `$.ui.toast('...')` to announce availability.
