---
type: "Guide"
title: "Typed input with a list of rows (notes pane)"
description: "Pattern for an Input plus a per-item row list with delete buttons, saved to $.store, with a key per row button."
resource: "https://code.claude.com/docs/en/plugins/mods/interface"
tags: [mods, input, list, store]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "label"
  - "placeholder"
  - "value"
  - "submitLabel"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-interface"
    resource: "https://code.claude.com/docs/en/plugins/mods/interface"
    title: "Draw in the interface with a mod"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A notes pane: an `Input` (`onSubmit` adds a trimmed non-empty note, `onInput` fires on every change) above one `Box` row per note holding a delete `Button` (`label: 'x'`, `plain: true`, key `'delete-' + i`) and the note's `Text`. Callbacks change the list, call `redraw`, and save to `$.store`.

| Prop | Meaning |
| :- | :- |
| `label` | text before the field; terminal adds `: ` |
| `placeholder` | dim text while empty |
| `value` | starting text |
| `submitLabel` | word after `⏎` |

# Notes

Delete via Tab to the `x` button then Enter; `x` is a label, not a hotkey. The example saves but does not load notes; read them in `session.start` to restore.
