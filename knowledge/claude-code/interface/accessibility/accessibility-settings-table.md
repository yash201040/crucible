---
type: "Reference"
title: "Accessibility options: magnifier, motion, themes, bell"
description: "Flag, env var and setting names for screen readers, magnifiers, reduced motion, colorblind themes and terminal bell."
resource: "https://code.claude.com/docs/en/accessibility"
tags: [accessibility, settings, magnifier, reduced-motion, themes]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "CLAUDE_CODE_ACCESSIBILITY"
  - "prefersReducedMotion"
  - "theme"
  - "dark-daltonized"
  - "light-daltonized"
  - "/theme"
  - "preferredNotifChannel"
  - "terminal_bell"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "accessibility"
    resource: "https://code.claude.com/docs/en/accessibility"
    title: "Use Claude Code with a screen reader"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Non-screen-reader accessibility controls (see [screen reader mode](./screen-reader-mode.md) for the flag, variable and setting of that mode).

# How to use it

| Option | Kind | What it changes |
| :- | :- | :- |
| `CLAUDE_CODE_ACCESSIBILITY` | env var | Set to `1` for a visible terminal cursor for magnifiers such as macOS Zoom; follows the input caret and (v2.1.218+) the highlighted row in menus like `/config` and `/plugin` |
| `prefersReducedMotion` | setting | `true` reduces or removes spinners, shimmer and animations |
| `theme` | setting | Colors, including colorblind-friendly `dark-daltonized` and `light-daltonized`; also `/theme` |
| `preferredNotifChannel` | setting | `"terminal_bell"` gives a bell outside screen reader mode when Claude is waiting |

# Notes

Issues go to the Claude Code GitHub tracker; include OS, terminal, and assistive technology name and version.
