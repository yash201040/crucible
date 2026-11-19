---
type: "Guide"
title: "Terminal rendering, scrolling and clipboard issues"
description: "Fixes for garbled text, stray control characters, scroll speed, sandboxed clipboard tools and OSC 52 over SSH."
resource: "https://code.claude.com/docs/en/troubleshooting"
tags: [terminal, clipboard, scrolling, sandbox, ssh]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.301"
surfaces: [cli]
requires: ""
identifiers:
  - "/terminal-setup"
  - "/scroll-speed"
  - "/tui default"
  - "/copy"
  - "CLAUDE_CODE_SCROLL_SPEED"
  - "CLAUDE_CODE_DISABLE_MOUSE"
  - "terminal.integrated.gpuAcceleration"
  - "sandbox.excludedCommands"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "troubleshooting"
    resource: "https://code.claude.com/docs/en/troubleshooting"
    title: "Troubleshooting"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Fixes for terminal-related display and clipboard problems.

# How to use it

- Garbled glyphs in the VS Code, Cursor or Devin Desktop integrated terminal: run `/terminal-setup` to set `terminal.integrated.gpuAcceleration` to `"off"`.
- Stray `>0q` at startup or `>4m` after exit come from VTE libraries older than 0.53; update to Claude Code v2.1.301 or later, which skips both sequences on such terminals. `echo $VTE_VERSION` below `5300` means an old library.
- Fullscreen rendering mouse wheel: `/scroll-speed` or `CLAUDE_CODE_SCROLL_SPEED` raise lines per notch (neither works in the JetBrains IDE terminal). PgUp/PgDn scroll half a screen; `/tui default` switches to the classic renderer with native scrollback.
- With sandboxing on, `pbcopy`, `xclip`, `wl-copy` can fail inside sandboxed Bash; use `/copy` instead (writes from the Claude Code process, can copy a single code block, also writes a file and prints its path). Adding `pbcopy *`, `wl-copy *` or `xclip *` to `excludedCommands` does not take such a piped call out of the sandbox on its own.
- Over SSH, `/copy` and fullscreen selection send OSC 52; iTerm2 needs Settings > General > Selection > Applications in terminal may access clipboard; macOS Terminal.app does not support it. Alternatives: hold the native-selection key (`Fn` in Terminal.app, `Option` in iTerm2) or set `CLAUDE_CODE_DISABLE_MOUSE=1` on the remote machine.

# Notes

None of these affect headless runs.
