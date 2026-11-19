---
type: "Reference"
title: "Button rules: action, hotkeys, variant, role, children"
description: "Extra Button behavior: keybinding action, digit hotkeys on the band, hotkey conflicts, variant and role values, and children."
resource: "https://code.claude.com/docs/en/plugins/mods/reference"
tags: [mods, button, hotkey, keybindings]
kind: "ui"
maturity: "unlabelled"
since: "2.1.295"
surfaces: [cli, desktop, ide]
requires: ""
identifiers:
  - "action"
  - "hotkey"
  - "variant"
  - "role"
  - "dismiss"
  - "primary"
  - "secondary"
  - "children"
  - "autoFocus"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-reference"
    resource: "https://code.claude.com/docs/en/plugins/mods/reference"
    title: "Mods reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

- `action`: names one of Claude Code's keybinding actions; the user's binding presses the button when it is a chord or a modified key.
- Digit hotkeys on the band: a digit `hotkey` on a band button also fires when the user types that digit alone into an empty prompt and pauses.
- Collapsed band: neither an `action` binding nor a hotkey presses a button in it.
- Two buttons on one hotkey in one drawing: the later one gets it.
- `variant`: `primary` or `secondary`; any other value throws. A terminal `primary` button draws in the accent color unless `plain`.
- `role`: `dismiss` marks a close button; any other value throws. Do the closing in `onPress`. In a band with text and a row of buttons, Desktop can draw the first `dismiss` button as its own close control; the terminal ignores `role`.
- `autoFocus` accepts only `true` on any control; omit to leave it off.

# How to use it

`children` (strings and `Text` elements only; any other element is refused) may replace `label`. `label` names the button and defaults to the children's text; give a button with non-single-string children a `key` or `label`. Terminal: children draw where the label would, and a press anywhere counts as one press (each list row can be one button). Desktop and VS Code draw the `label`.

# Limits and defaults

A `Button` with children other than a single string needs v2.1.295+.
