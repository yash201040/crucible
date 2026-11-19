---
type: "Guide"
title: "Worked example: a pane with tabs and a counter"
description: "Builds a /hello-tabs mod whose pane has two tabs and a persisted counter, showing the render cycle of callback, state change and invalidate."
resource: "https://code.claude.com/docs/en/plugins/mods/interface"
tags: [mods, pane, tutorial, render-cycle]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "/hello-tabs"
  - "claude --plugin-dir ./hello-tabs"
  - "$.ui.invalidate"
  - "$.store.get"
  - "$.store.set"
  - "$.store.delete"
  - "closeOnEscape"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-interface"
    resource: "https://code.claude.com/docs/en/plugins/mods/interface"
    title: "Draw in the interface with a mod"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A mod `hello-tabs` (manifest plus `hooks/hooks.json` with `"modules": ["./register.js"]`) adds `/hello-tabs`, which opens a pane with two tab buttons (hotkeys `1`, `2`) and, on tab two, an "Add one" button (hotkey `a`) beside `Count: n`.

# How to use it

Three hooks in `register.js`: `session.start` registers the command and loads the saved count from `$.store`; `command.run` (matcher `{ command: 'hello-tabs' }`) calls `$.ui.open({ id, title, focus: true, closeOnEscape: true })` and returns `{}` (opening draws nothing by itself; Claude Code then fires `ui.render`); `ui.render` with `{ component: 'Pane' }` returns the element tree from `tab` and `count`, ignoring other mods' panes by `e.requestId`.

Render cycle: a button's `onPress` changes a variable and calls `$.ui.invalidate('ui.render')`; Claude Code reruns the hook, which builds a new tree. Run with `claude --plugin-dir ./hello-tabs`; the count persists across restarts via `$.store`. `$.store.delete('count')` clears it.
