---
type: "Reference"
title: "Keyboard focus, keys and hotkeys in panes and band"
description: "How a pane gets focus, what each key does while focused, hotkey and autoFocus props, and the Ctrl+X chords."
resource: "https://code.claude.com/docs/en/plugins/mods/interface"
tags: [mods, keyboard, focus, hotkeys]
kind: "ui"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop, ide]
requires: ""
identifiers:
  - "hotkey"
  - "autoFocus"
  - "focus: true"
  - "Ctrl+X then Tab"
  - "Ctrl+X then X"
  - "Ctrl+X then Ctrl+A"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-interface"
    resource: "https://code.claude.com/docs/en/plugins/mods/interface"
    title: "Draw in the interface with a mod"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A mod never reads the keyboard: Claude Code routes keys to the focused control's callback. Outside a digit hotkey on the band or an `action` binding, this happens only while the pane or band has focus; otherwise keys go to the prompt.

A pane gets focus when the mod opens it with `focus: true` from a command or press, when the user presses Ctrl+X then Tab, or when the user clicks it (terminal needs fullscreen rendering). `focus: true` is granted only while the prompt is empty and nothing else has focus.

# How to use it

| Key | Effect while focused |
| :- | :- |
| Tab | next control |
| Up/Down | move between controls; scroll when content overflows; in a terminal `Input` move between rows |
| Enter | press Button, submit Input, pick in Select |
| Button hotkey | presses it; while an `Input` has focus all printable keys go to the field |
| Page Up/Down, Home, End | scroll overflowing pane/band |
| Ctrl+X then arrow | resize pane (Left/Up more room, Right/Down give back; beside-transcript capped at 45% width) |
| Ctrl+X then X | close pane even from a focused field |
| Ctrl+X then Ctrl+A | collapse or expand the band (works from prompt too) |
| Esc | focus returns to prompt; with `closeOnEscape: true` also closes pane |

A mod cannot bind Tab or arrows. `hotkey` is one digit or one lowercase letter. `autoFocus: true` picks the first-focused control (accepts only `true`; does nothing in VS Code). Hotkey display: bracketed button in terminal shows `[ Add one ]` with no hotkey; `plain: true` shows `1: One`; Desktop shows a small key beside the label; VS Code shows the label and the hotkey does nothing.
