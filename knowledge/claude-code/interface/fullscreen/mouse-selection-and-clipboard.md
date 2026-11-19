---
type: "Feature"
title: "Fullscreen mouse, selection and clipboard"
description: "Click, scroll, select and copy behavior in fullscreen rendering, clipboard paths, and the env vars that turn mouse capture off."
resource: "https://code.claude.com/docs/en/fullscreen"
tags: [fullscreen, mouse, selection, clipboard, terminal]
kind: "mixed"
maturity: "research-preview"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "CLAUDE_CODE_DISABLE_MOUSE"
  - "CLAUDE_CODE_DISABLE_MOUSE_CLICKS"
  - "selection:clear"
  - "/config"
  - "Copy on select"
  - "/terminal-setup"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "fullscreen"
    resource: "https://code.claude.com/docs/en/fullscreen"
    title: "Fullscreen rendering"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Fullscreen rendering captures mouse events: click to place the prompt cursor, accept `/` or `@` suggestions, pick or toggle menu options, change a `/config` value (v2.1.271+), scroll menus with the wheel (v2.1.280+), scroll lists with a scrollbar (v2.1.281+; arrows and `↑ N more`/`↓ N more` rows v2.1.286+), expand collapsed tool results (a `!` command's output v2.1.257+; `Message from @<sender>` lines from teammates or agents), and open URLs and file paths with `Cmd`-click on macOS or `Ctrl`-click elsewhere. Click-drag selects (double-click word, triple-click line) and copies on mouse release (toggle Copy on select in `/config`).

# How to use it

- Manual copy with Copy on select off: `Ctrl+Shift+c` (and `Cmd+c` on kitty-protocol terminals). Shift plus arrows, `Shift+Home`/`Shift+End` extend a selection. `Esc` keeps the selection; `PgUp`, `PgDn`, `Ctrl+Home`, `Ctrl+End` and modified arrows keep it; other keys clear it; a key bound to `selection:clear` clears it.
- Clipboard path: `pbcopy` (macOS), `wl-copy` or `xclip`/`xsel` (Linux, also PRIMARY), PowerShell `Set-Clipboard` (Windows/WSL), tmux paste buffer, OSC 52 over SSH. iTerm2 blocks OSC 52 until enabled; `/terminal-setup` enables it. Native selection key: Terminal.app `Fn`, iTerm2 `Option`, most others `Shift`.
- `CLAUDE_CODE_DISABLE_MOUSE=1` opts out of mouse capture but keeps flicker-free rendering (keyboard scroll still works). `CLAUDE_CODE_DISABLE_MOUSE_CLICKS=1` keeps wheel scrolling but disables click, drag and hover; `CLAUDE_CODE_DISABLE_MOUSE` wins if both are set.

# Limits and defaults

- Linux/WSL file-path click needs a file manager exposing `org.freedesktop.FileManager1`; UNC paths render as plain text; Ghostty and Warp on macOS let a plain click open links; VS Code integrated terminal uses its own link handler.
- iTerm2 needs Settings > Profiles > Terminal > Enable mouse reporting.
