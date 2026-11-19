---
type: "Reference"
title: "Fullscreen scrolling, auto-follow and scroll speed"
description: "Scroll keys, jump-to-bottom button, auto-scroll setting, CLAUDE_CODE_SCROLL_SPEED, /scroll-speed and JetBrains terminal behavior."
resource: "https://code.claude.com/docs/en/fullscreen"
tags: [fullscreen, scrolling, auto-follow, scroll-speed, keybindings]
kind: "mixed"
maturity: "research-preview"
since: "2.1.174"
surfaces: [cli]
requires: ""
identifiers:
  - "CLAUDE_CODE_SCROLL_SPEED"
  - "/scroll-speed"
  - "wheelScrollAccelerationEnabled"
  - "autoScrollEnabled"
  - "scroll:bottom"
  - "/focus"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "fullscreen"
    resource: "https://code.claude.com/docs/en/fullscreen"
    title: "Fullscreen rendering"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

In-app scrolling for fullscreen rendering. Scrolling up pauses auto-follow; a `Jump to bottom` button (with a count like `3 new messages`) appears; clicking it, `Ctrl+End`, or scrolling to the bottom resumes. A dim header shows the latest prompt above the view (click to jump). After resuming a compacted session, scrolling stops at the `Conversation compacted` row.

# How to use it

| Key | Action |
| :- | :- |
| `PgUp` / `PgDn` | Half a screen |
| `Ctrl+Home` | Start of conversation |
| `Ctrl+End` | Latest message, re-enable auto-follow |
| Mouse wheel | A few lines |

Transcript mode (`Ctrl+o`) keys: `/` search, `n`/`N`, `j`/`k`, `g`/`G`, `{`/`}` (prompt), `Ctrl+u`/`Ctrl+d`, `Ctrl+b`/`Ctrl+f`, `Space`/`b`, exit with `Ctrl+o`, `Esc` or `q`. On MacBook keyboards use `Fn`+arrows; `Ctrl+Fn+→` does not reach Claude Code, so rebind `scroll:bottom` or use the button/wheel.

Scroll speed: `CLAUDE_CODE_SCROLL_SPEED` multiplies base distance (positive up to 20; `3` matches vim; fractions like `0.25` allowed). `/scroll-speed` dialog (arrows adjust, `r` reset, `Enter` saves; maximum 10, whole steps up to 10, quarter steps down to 0.25 on capable terminals) persists to `~/.claude/settings.json`; not available in the JetBrains IDE terminal. `wheelScrollAccelerationEnabled: false` (v2.1.174+) turns off wheel acceleration. Auto-scroll can be turned off in `/config` (`autoScrollEnabled`).

# Limits and defaults

JetBrains terminal: Claude Code ignores `CLAUDE_CODE_SCROLL_SPEED` and applies its own handling; 2025.2 has scroll bugs that are mitigated automatically; upgrade to 2025.3+ is recommended.
