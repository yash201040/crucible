---
type: "Feature"
title: "Test a drawing with ui.mount"
description: "$.ui.mount draws a render site through the mod's ui.render hook and returns a handle with press, input, select, find, keepsBeneath and unmount."
resource: "https://code.claude.com/docs/en/plugins/mods/test"
tags: [mods, testing, ui, render]
kind: "api"
maturity: "unlabelled"
since: "2.1.321"
surfaces: [cli, desktop]
requires: ""
identifiers:
  - "$.ui.mount"
  - "surface"
  - "press({ key })"
  - "input({ key, text })"
  - "select({ key, value })"
  - "keepsBeneath()"
  - "find({ key })"
  - "find({ type, text })"
  - "unmount()"
  - "kind: 'change'"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-test"
    resource: "https://code.claude.com/docs/en/plugins/mods/test"
    title: "Test a mod"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A test can draw one of the mod's render sites, then press, type into and find elements. `$.ui.mount` draws the site through the mod's `ui.render` hook and returns a handle. Set `surface` (for example `'terminal'` or `'desktop'`) to cover several apps in one test. Pass `props` as Claude Code would for that site (the render-sites table in the mods reference lists them).

# How to use it

Mount arguments in the documented example: `plugin`, `component` (e.g. `'Pane'`), `requestId`, `viewport: { columns, rows }`, `props` (`title`, `isFocused`, `bodyColumns`, `placement`, `scroll`, `view`), and `surface`.

| Handle method | What it does |
| :- | :- |
| `press({ key: 'more' })` | Presses the `Button` with that key |
| `input({ key: 'new-note', text: 'buy milk' })` | Types into the `Input` with that key and presses Enter; add `kind: 'change'` to type without submitting; for a field with `rows` text may hold `\n` |
| `select({ key: 'size', value: 'large' })` | Picks the option in the `Select` with that key |
| `keepsBeneath()` | With no `ui.render` stub: `true` when the drawing includes what `next(e)` returned, `false` when the hook left it out. With a stub, use `find`. Requires Claude Code v2.1.321 or later |
| `find({ key })` or `find({ type: 'Text', text: 'Count: 2' })` | First matching element as `{ type, props, children }` or `undefined`; `text` is a string or regex |
| `unmount()` | Removes the drawing |

Each method resolves after the handler finishes.

# Limits and defaults

The test does not check how the app paints a tree; an element tree invalid for the named `surface` is caught by using `find` for an element your hook adds. Check new layouts in a real session too. Mounts in one test share the same loaded module, so state (e.g. a saved count) carries across surfaces.
