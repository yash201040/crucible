---
type: "Reference"
title: "Gallery: Button, Input and Select controls"
description: "Usage of the Button, Input (single and multi-line) and Select controls, their focus behavior and keys in the terminal."
resource: "https://code.claude.com/docs/en/plugins/mods/gallery"
tags: [mods, controls, input, button, select]
kind: "ui"
maturity: "unlabelled"
since: "2.1.301"
surfaces: [cli, desktop, ide]
requires: ""
identifiers:
  - "Button"
  - "Input"
  - "Select"
  - "onPress"
  - "onSubmit"
  - "onInput"
  - "onSelect"
  - "submitLabel"
  - "rows"
  - "plain: true"
  - "hotkey"
  - "focus: true"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-gallery"
    resource: "https://code.claude.com/docs/en/plugins/mods/gallery"
    title: "Interface gallery for mods"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Controls take focus: the user moves between them with Tab. Open a pane with `focus: true` to request keyboard focus; typed letters reach an `Input` once it has focus.

- `Button({ key, label, hotkey, plain, dimColor, onPress })`: default form draws in brackets; `plain: true` draws `n: Next` with the hotkey colored; focused button draws in inverse video.
- `Input({ key, label, placeholder, value, submitLabel, rows, onSubmit })`: one line by default; runs `onSubmit` on Enter; focused shows bold label, cursor, and `⏎` plus `submitLabel`.
- `Select({ key, label, value, options: [{ value, label }], onSelect })`: shows the current option closed; list opens to pick; `onSelect` gets the option's `value`.

# Limits and defaults

- `rows` of 2 or more makes a multi-line `Input`. Drawn in the terminal and Desktop app; in the VS Code extension the field holds one line. Requires v2.1.301 or later (earlier: one line).
- The field takes its set rows even when empty, up to the pane or band height; longer text scrolls while focused.
- Terminal: Enter submits; new line via backslash then Enter, or Shift+Enter where the emulator supports it; Up/Down move between rows and from first/last row to the previous/next control.
- `onSubmit` and `onInput` receive the whole text with lines joined by `\n`.
