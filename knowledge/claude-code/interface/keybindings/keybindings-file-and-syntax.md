---
type: "Feature"
title: "keybindings.json, contexts and keystroke syntax"
description: "Config file structure, binding contexts, keystroke syntax, chords, unbinding, reserved shortcuts and validation."
resource: "https://code.claude.com/docs/en/keybindings"
tags: [keybindings, configuration, shortcuts, chords, contexts]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "/keybindings"
  - "~/.claude/keybindings.json"
  - "$schema"
  - "$docs"
  - "bindings"
  - "context"
  - "vimInsertModeRemaps"
  - "--debug"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "keybindings"
    resource: "https://code.claude.com/docs/en/keybindings"
    title: "Customize keyboard shortcuts"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`/keybindings` creates or opens `~/.claude/keybindings.json`: an object with optional `$schema` (`https://www.schemastore.org/claude-code-keybindings.json`), optional `$docs`, and a `bindings` array of blocks `{ "context": ..., "bindings": { "<keys>": "<action>" | null } }`. Changes are detected and applied without restart.

# How to use it

Contexts: `Global`, `Chat`, `Autocomplete`, `Settings`, `Confirmation`, `Tabs`, `Help`, `Transcript`, `HistorySearch`, `Task`, `ThemePicker`, `Attachments`, `Footer`, `MessageSelector`, `DiffDialog`, `DiffPanel`, `ModelPicker`, `EffortSlider`, `Select`, `Plugin`, `AbovePrompt`, `AbovePromptInput`, `AbovePromptSelect`, `Pane`, `PaneField`, `Agents`, `Scroll`. (A `Doctor` context and `doctor:fix` action existed before v2.1.205.)

Actions use `namespace:action`. `command:<name>` runs a slash command (example `"meta+g": "command:compact"` in `Chat`).

Syntax: modifiers joined with `+`: `ctrl`/`control`, `shift`, `alt`/`opt`/`option`/`meta`, `cmd`/`command`/`super`/`win` (cmd group only in terminals reporting Super, such as Kitty protocol or xterm `modifyOtherKeys`). Names are case-insensitive (`shift+k` for Shift plus letter). Special keys: `escape`/`esc`, `enter`/`return`, `tab`, `space`, arrows, `pageup`, `pagedown`, `home`, `end`, `backspace`, `delete`, `wheelup`, `wheeldown`. Chords are space-separated (`ctrl+k ctrl+s`), each keystroke within 3 seconds. Use Latin names for Ctrl shortcuts on non-Latin layouts (US-position matching needs Kitty protocol reporting).

Unbind with `null`; a chord prefix is reserved while any chord on it exists in an active context. Default `ctrl+x` chords by context: `Chat` (`ctrl+x ctrl+k`, `ctrl+x ctrl+e`, `ctrl+x enter` v2.1.247+, `ctrl+x ctrl+a` and `ctrl+x tab` v2.1.260+, `ctrl+x ctrl+s` v2.1.275+, `ctrl+x ctrl+=`, `ctrl+x ctrl+-`, `ctrl+x ctrl+_`, `ctrl+x =`, `ctrl+x -`), `Task` (`ctrl+x ctrl+b`), `DiffPanel` (`ctrl+x b` v2.1.260+), `Pane` (`ctrl+x left/right/up/down/x`), `PaneField` (`ctrl+x x`).

# Limits and defaults

- Reserved (cannot rebind): Ctrl+C (interrupt), Ctrl+D (exit), Ctrl+M (Enter), Ctrl+[ (Escape; Kitty protocol needs v2.1.242+), Ctrl+I (Tab), Ctrl+H (backspace byte; see `CLAUDE_CODE_BS_AS_CTRL_BACKSPACE`), Caps Lock.
- Terminal conflicts: Ctrl+B (tmux prefix), Ctrl+A (GNU screen), Ctrl+Z (suspend).
- In a dialog or panel text field, printable keys without Ctrl, Alt or Cmd go to the field, not bindings; at the main prompt every key is matched first.
- Vim mode: keybindings and vim run independently; Escape switches INSERT to NORMAL, not `chat:cancel`; vim keys are not remappable here (use `vimInsertModeRemaps`). To cancel a question from the `Other` row in one press, bind a Ctrl/Alt key to `select:cancel` in `Select` (not effective in screen reader mode or multi-select).
- Validation warnings go to the debug log (`--debug`): invalid JSON, misspelled modifiers (binding ignored), `ctrl+ k` with a space (read as a chord), invalid contexts, unknown actions (binding skipped, default stays), reserved conflicts, duplicates.
