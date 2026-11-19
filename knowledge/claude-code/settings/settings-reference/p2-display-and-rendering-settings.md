---
type: "Reference"
title: "Display, rendering and transcript settings"
description: "Settings for theme, renderer, transcript view, time format, scrolling, motion and screen-reader output."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [settings, interface, rendering, accessibility]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "autoScrollEnabled"
  - "axScreenReader"
  - "maxProseWidth"
  - "prefersReducedMotion"
  - "syntaxHighlightingDisabled"
  - "terminalProgressBarEnabled"
  - "terminalTitleFromRename"
  - "theme"
  - "timeFormat"
  - "timeZone"
  - "tui"
  - "verbose"
  - "viewMode"
  - "wheelScrollAccelerationEnabled"
  - "showTurnDuration"
  - "--ax-screen-reader"
  - "CLAUDE_AX_SCREEN_READER"
  - "CLAUDE_CODE_NO_FLICKER"
  - "CLAUDE_CODE_DISABLE_ALTERNATE_SCREEN"
  - "CLAUDE_CODE_DISABLE_TERMINAL_TITLE"
  - "--verbose"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Interface keys that change how the terminal UI looks. Scope is any settings file unless noted.

# How to use it

| Name | Type / values | Default | What it does |
| :- | :- | :- | :- |
| `autoScrollEnabled` | Boolean | `true` | Follow new output to the bottom in fullscreen rendering |
| `axScreenReader` | Boolean | unset (off) | Flat, border-free, animation-free output using the classic renderer (the `tui` key has no effect then). User or managed scope, or `--settings`; ignored in project and local settings. `--ax-screen-reader` beats `CLAUDE_AX_SCREEN_READER`, both beat the key. Attached background sessions still render fullscreen |
| `maxProseWidth` | whole number of columns, min `40` | unset | Wrap prose (paragraphs, headings, lists, blockquotes) at this width; tables and code keep full width. Needs v2.1.282+. Other values ignored |
| `prefersReducedMotion` | Boolean | `false` | Reduce spinner, shimmer, flash animations. `/config`: Reduce motion |
| `syntaxHighlightingDisabled` | Boolean | `false` | Plain text in diffs, code blocks, file previews |
| `terminalProgressBarEnabled` | Boolean | `true` | Report progress to the terminal tab; stays on while background subagents or dynamic workflows run. Works in ConEmu, Ghostty 1.2.0+, iTerm2 3.6.6+ |
| `terminalTitleFromRename` | Boolean | `true` | `false` keeps the generated tab title after `/rename` or `--name`; the name still works for `/resume`. To stop title updates entirely set `CLAUDE_CODE_DISABLE_TERMINAL_TITLE=1` |
| `theme` | `"auto"`, `"dark"`, `"light"`, `"dark-daltonized"`, `"light-daltonized"`, `"dark-ansi"`, `"light-ansi"`, `"custom:<slug>"`, `"custom:<plugin-name>:<slug>"` | `"dark"` | Colour theme; custom themes live in `~/.claude/themes/` or a plugin |
| `timeFormat` | `"auto"`, `"12-hour"`, `"24-hour"`, `"24-hour-utc"`, or a strftime pattern containing `%` | `"auto"` | Format of times such as "done 6:05 PM" and transcript timestamps. Needs v2.1.257+. `/config` offers presets only |
| `timeZone` | IANA zone name | unset (system zone) | Zone for those times; ignored with `24-hour-utc`; unknown names fall back to system. Needs v2.1.257+ |
| `tui` | `"default"` (classic) or `"fullscreen"` (alt-screen, virtualized scrollback) | unset (auto-picked) | Renderer; `/tui fullscreen` or `/tui default` writes it. `CLAUDE_CODE_NO_FLICKER=1` forces fullscreen; `=0` or `CLAUDE_CODE_DISABLE_ALTERNATE_SCREEN=1` forces off (off wins if both set). Classic is kept under tmux `-CC` or SSH to Windows unless `CLAUDE_CODE_NO_FLICKER=1`. Background sessions from agent view always use fullscreen |
| `verbose` | Boolean | `false` | Show full tool input/output inline; `--verbose` overrides for a session |
| `viewMode` | `"default"`, `"verbose"`, `"focus"` | unset | Starting transcript view; overrides `verbose` and sticky `/focus`. Focus view needs fullscreen renderer |
| `wheelScrollAccelerationEnabled` | Boolean | `true` | Accelerated wheel scrolling in fullscreen |
| `showTurnDuration` | Boolean | `true` | Show turn duration after each response (for example "Cooked for 1m 6s"). Old `~/.claude.json` value applies if no settings file sets it |

# Notes

Several keys fall back to an older value in `~/.claude.json` when no settings file sets them (`theme`, `verbose`, `terminalProgressBarEnabled`, `showTurnDuration`).
