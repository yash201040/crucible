---
type: "Guide"
title: "Fullscreen rendering, paste handling and Vim mode"
description: "Fixes for flicker, how large pastes are collapsed and cached, response width cap, and Vim editing mode for the prompt."
resource: "https://code.claude.com/docs/en/terminal-config"
tags: [fullscreen, paste, vim, rendering]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "/tui fullscreen"
  - "CLAUDE_CODE_NO_FLICKER"
  - "CLAUDE_CODE_FORCE_SYNC_OUTPUT"
  - "maxProseWidth"
  - "editorMode"
  - "vimInsertModeRemaps"
  - "~/.claude/paste-cache/"
  - "cleanupPeriodDays"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "terminal-config"
    resource: "https://code.claude.com/docs/en/terminal-config"
    title: "Configure your terminal for Claude Code"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Display and input tweaks for the interactive CLI.

# How to use it

- Fullscreen rendering: run `/tui fullscreen` (saves preference, relaunches the conversation intact) or start with `CLAUDE_CODE_NO_FLICKER=1` (also settable via the `env` settings key). Scrolling then uses mouse or PageUp inside Claude Code. In screen reader mode it does not apply and `/tui fullscreen` prints an explanation (except attached background sessions, which always render as plain scrolling text).
- If only flicker is the problem and the terminal supports synchronized output but is not auto-detected (e.g. Emacs `eat`), set `CLAUDE_CODE_FORCE_SYNC_OUTPUT=1`.
- `maxProseWidth` in settings wraps prose at a set column count in wide terminals.
- Vim mode: `/config` > Editor mode, or `editorMode` set to `"vim"`; set back to `normal` to turn off. Subset of NORMAL/VISUAL motions. Vim motions are not remappable via keybindings; map two-key INSERT sequences such as `jj` to Escape with `vimInsertModeRemaps`. Enter still submits in INSERT mode; use `o`/`O` in NORMAL or Ctrl+J for a newline.

# Limits and defaults

Pastes over 800 characters or more than three lines collapse to a placeholder like `[Pasted text #1 +120 lines]` while the full content is still sent. Claude is told pasted text may contain instructions you did not write and follows them only where your typed message asks. Invisible Unicode characters are removed on Enter. The VS Code integrated terminal can drop characters from very large pastes; use a file instead.

# Notes

- Content behind placeholders is kept under `~/.claude/paste-cache/`, so recalled history prompts resend it, even in later sessions. Files older than `cleanupPeriodDays` are deleted; a prompt referencing missing paste has the placeholder removed with a notification, or the submission is cancelled for shell-mode / `/` commands and prompts that would be left empty.
- Deleting a range reaching into a placeholder with Ctrl+W, Ctrl+K or vim `df]` removes it whole; restore with Ctrl+Y or `p` in NORMAL mode.
