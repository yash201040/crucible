---
type: "Reference"
title: "Terminal rendering, accessibility and display variables"
description: "Variables for fullscreen rendering, mouse and scrolling, screen reader mode, cursor, color, hyperlinks, terminal title and demo mode."
resource: "https://code.claude.com/docs/en/env-vars"
tags: [terminal, accessibility, fullscreen, rendering]
kind: "env_var"
maturity: "research-preview"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "CLAUDE_CODE_NO_FLICKER"
  - "CLAUDE_CODE_DISABLE_ALTERNATE_SCREEN"
  - "CLAUDE_CODE_ALT_SCREEN_FULL_REPAINT"
  - "CLAUDE_CODE_DISABLE_MOUSE"
  - "CLAUDE_CODE_DISABLE_MOUSE_CLICKS"
  - "CLAUDE_CODE_DISABLE_VIRTUAL_SCROLL"
  - "CLAUDE_CODE_SCROLL_SPEED"
  - "CLAUDE_AX_SCREEN_READER"
  - "CLAUDE_AX_PREPARK_MS"
  - "CLAUDE_AX_STARTUP_QUIET_MS"
  - "CLAUDE_CODE_ACCESSIBILITY"
  - "CLAUDE_CODE_NATIVE_CURSOR"
  - "CLAUDE_CODE_FORCE_STRIKETHROUGH"
  - "CLAUDE_CODE_FORCE_SYNC_OUTPUT"
  - "CLAUDE_CODE_FORCE_TERMINAL_IMAGES"
  - "FORCE_HYPERLINK"
  - "CLAUDE_CODE_HIDE_CWD"
  - "CLAUDE_CODE_TMUX_TRUECOLOR"
  - "CLAUDE_CODE_SYNTAX_HIGHLIGHT"
  - "CLAUDE_CODE_BS_AS_CTRL_BACKSPACE"
  - "CLAUDE_CODE_DISABLE_TERMINAL_TITLE"
  - "CLAUDE_CODE_NONBLOCKING_STDOUT"
  - "CLAUDE_CODE_YOU_SHOULD_KNOW_DEBUG"
  - "IS_DEMO"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "env-vars"
    resource: "https://code.claude.com/docs/en/env-vars"
    title: "Environment variables"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Interface-only variables. The "research preview" label applies to fullscreen rendering (`CLAUDE_CODE_NO_FLICKER`); the rest are unlabelled.

# How to use it

| Variable | What it does |
| :- | :- |
| `CLAUDE_CODE_NO_FLICKER` | `1` enables fullscreen rendering (research preview; reduces flicker, keeps memory flat in long conversations). Overrides the `tui` setting; also `/tui fullscreen`. |
| `CLAUDE_CODE_DISABLE_ALTERNATE_SCREEN` | `1` disables fullscreen rendering for the classic renderer (native scrollback, `Cmd+f`, tmux copy mode). Beats `CLAUDE_CODE_NO_FLICKER` and `tui`; also `/tui default`. Does not apply to background sessions opened from agent view (always fullscreen). |
| `CLAUDE_CODE_ALT_SCREEN_FULL_REPAINT` | `1` repaints the whole screen every frame in fullscreen rendering (fixes stale text). Enabled automatically for background sessions and agent view on Windows. |
| `CLAUDE_CODE_DISABLE_MOUSE` | `1` disables mouse tracking in fullscreen; PgUp and PgDn still scroll. Beats the clicks variable. |
| `CLAUDE_CODE_DISABLE_MOUSE_CLICKS` | `1` disables click, drag and hover handling but keeps wheel scrolling. Requires v2.1.195+. |
| `CLAUDE_CODE_DISABLE_VIRTUAL_SCROLL` | `1` renders every transcript message (fixes blank regions when scrolling). |
| `CLAUDE_CODE_SCROLL_SPEED` | Wheel multiplier, any positive value up to 20 (fractions such as `0.5` allowed; `3` matches vim). Ignored in the JetBrains terminal. |
| `CLAUDE_AX_SCREEN_READER` | `1` screen-reader friendly output (flat text, no borders or animations); `0` forces it off even when `axScreenReader` is `true`. `--ax-screen-reader` takes precedence. Ignored in project and local settings. Requires v2.1.181+. |
| `CLAUDE_AX_PREPARK_MS` | Screen reader mode: ms before writing a new or changed line (default `0`; before v2.1.287 `50`; capped at `5000`). Ignored in project and local settings. Requires v2.1.233+. |
| `CLAUDE_AX_STARTUP_QUIET_MS` | Screen reader mode: ms to hold the first render after the startup line (default `3000`; `0` renders immediately; capped at `600000`; first keystroke ends the hold). Ignored in project and local settings. Requires v2.1.217+. |
| `CLAUDE_CODE_ACCESSIBILITY` | `1` keeps the native terminal cursor visible and disables the inverted-text cursor (for screen magnifiers). |
| `CLAUDE_CODE_NATIVE_CURSOR` | `1` shows the terminal's own cursor at the input caret; `0` reads like unset. |
| `CLAUDE_CODE_FORCE_STRIKETHROUGH` | `1` forces `~~text~~` strikethrough when undetected (for example over SSH). Requires v2.1.186+. |
| `CLAUDE_CODE_FORCE_SYNC_OUTPUT` | `1` forces DEC private mode 2026 synchronized output when undetected; no effect under tmux; does not change the renderer. |
| `CLAUDE_CODE_FORCE_TERMINAL_IMAGES` | `1` draws mod `Image` elements as pictures on terminals with kitty graphics Unicode placeholders that still show the dimmed alt text. |
| `FORCE_HYPERLINK` | `1` enables OSC 8 hyperlinks when undetected; `0`, `false`, `no`, `off` render all as plain text (before v2.1.314 those false values enabled them). |
| `CLAUDE_CODE_HIDE_CWD` | `1` hides the working directory in the startup logo. |
| `CLAUDE_CODE_TMUX_TRUECOLOR` | Presence-only: any non-empty value (even `0` or `false`) allows 24-bit color in tmux; unset restores the 256-color clamp. Needs `set -ga terminal-overrides ',*:Tc'` in `~/.tmux.conf`. |
| `CLAUDE_CODE_SYNTAX_HIGHLIGHT` | `false` disables syntax highlighting in diff output (the `syntaxHighlightingDisabled` setting also covers code blocks and previews). |
| `CLAUDE_CODE_BS_AS_CTRL_BACKSPACE` | `0` reads `0x08` (`^H`) as plain Backspace, `1` as Ctrl+Backspace. Default Ctrl+Backspace on Windows (except `TERM_PROGRAM=mintty` or `TERM=cygwin`), Backspace on macOS and Linux. |
| `CLAUDE_CODE_DISABLE_TERMINAL_TITLE` | `1` disables terminal title updates, skips the small/fast-model request that generates a session title, and turns off status reports to the terminal. |
| `CLAUDE_CODE_NONBLOCKING_STDOUT` | `1` writes through a second non-blocking file descriptor so a stalled terminal (paused tmux control-mode pane, stalled SSH) cannot freeze Claude Code. macOS, Linux, WSL, when stdout is a terminal. Requires v2.1.261+. |
| `CLAUDE_CODE_YOU_SHOULD_KNOW_DEBUG` | `1` shows above the prompt a line per each of the last three You should know mod checks. Requires v2.1.287+. |
| `IS_DEMO` | Presence-only: any non-empty value (even `0` or `false`) enables demo mode (hides email and organization from header and `/status`, skips onboarding). |
