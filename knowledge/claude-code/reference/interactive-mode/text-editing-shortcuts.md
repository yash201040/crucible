---
type: "Reference"
title: "Text editing shortcuts and word boundaries"
description: "Readline-style editing keys in the prompt and how word boundaries are defined for them."
resource: "https://code.claude.com/docs/en/interactive-mode"
tags: [keyboard, editing, readline, prompt]
kind: "ui"
maturity: "unlabelled"
since: "2.1.261"
surfaces: [cli]
requires: ""
identifiers:
  - "Ctrl+A"
  - "Ctrl+E"
  - "Ctrl+K"
  - "Ctrl+U"
  - "Ctrl+W"
  - "Ctrl+Y"
  - "Alt+Y"
  - "Alt+B"
  - "Alt+F"
  - "Alt+D"
  - "Ctrl+_"
  - "Ctrl+Shift+-"
  - "keybindingFlavor"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "interactive-mode"
    resource: "https://code.claude.com/docs/en/interactive-mode"
    title: "Interactive mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Editing keys for the prompt input, plus the rule for what counts as a word.

# How to use it

| Shortcut | Action |
| :- | :- |
| `Ctrl+A` / `Ctrl+E` | Start / end of current logical line |
| `Ctrl+K` | Delete to end of line (stored for paste) |
| `Ctrl+U` | Delete to line start; repeat clears across lines. `Cmd+Backspace` maps to it on macOS terminals |
| `Ctrl+W` | Delete back to previous whitespace (removes a whole path or `--flag=value`) |
| `Ctrl+Y` | Paste last deleted text |
| `Alt+Y` after `Ctrl+Y` | Cycle paste history |
| `Alt+B` / `Alt+F` | Back / forward one word |
| `Alt+D` | Delete to end of word |
| `Ctrl+_` or `Ctrl+Shift+-` | Undo last input edit |

# Limits and defaults

Word shortcuts (`Alt+B`, `Alt+F`, `Alt+D`, `Option+Delete`, `Ctrl+Backspace`) treat a word as a run of letters and digits, so `_ . /` separate words. `Ctrl+W` ignores punctuation. These readline conventions apply from v2.1.261; the `keybindingFlavor` setting that enabled them earlier is deprecated and has no effect. These shortcuts cannot be remapped in the keybindings file.
