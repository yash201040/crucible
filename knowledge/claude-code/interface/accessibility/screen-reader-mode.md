---
type: "Feature"
title: "Screen reader mode"
description: "Opt-in mode that replaces the visual terminal UI with labeled linear text for screen readers; how to turn on, off and what it announces."
resource: "https://code.claude.com/docs/en/accessibility"
tags: [accessibility, screen-reader, terminal, voiceover, nvda]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "--ax-screen-reader"
  - "CLAUDE_AX_SCREEN_READER"
  - "axScreenReader"
  - "CLAUDE_AX_STARTUP_QUIET_MS"
  - "CLAUDE_AX_PREPARK_MS"
  - "tui"
  - "/effort"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "accessibility"
    resource: "https://code.claude.com/docs/en/accessibility"
    title: "Use Claude Code with a screen reader"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Screen reader mode prints plain labeled lines instead of boxes, spinners and in-place redraws, so VoiceOver or NVDA can read a full conversation, approvals included. It is opt-in and does not turn on automatically when a screen reader runs. It adapts the terminal UI only; the VS Code extension chat panel needs no setting (v2.1.236+ announces activity there).

# How to use it

Turn on: `claude --ax-screen-reader` (one session); `CLAUDE_AX_SCREEN_READER=1` (shell); `"axScreenReader": true` in the user settings file (all sessions, any terminal). Precedence: flag, then variable, then setting. Over SSH set it on the remote machine. First line confirms: `[Screen Reader Mode: on via flag]`, `on via env` or `on via settings`. Turn off by reversing the method; `CLAUDE_AX_SCREEN_READER=0` keeps it off even when the setting is true.

Behavior: no box drawing or color-only cues; tables read as `Header: value`; diffs as plain `+`/`-` lines; the `tui` setting is ignored (scrolling text, not fullscreen); a 3-second wait after the confirmation line (any key ends it; `CLAUDE_AX_STARTUP_QUIET_MS`, v2.1.217+). `CLAUDE_AX_PREPARK_MS` (v2.1.233+) holds the cursor at line start before writing a changed line. Menus become numbered lists (type number, Enter; Escape cancels); `/effort` slider becomes a numbered list; yes/no prompts take `y`/`n`. Permission-mode changes with `Shift+Tab` are announced (`[plan mode on]`). The terminal bell rings when Claude finishes a reply, a prompt needs an answer, or a tool that ran over 5 seconds finishes. OSC 133 markers allow jump-to-previous-prompt (iTerm2 Cmd+Shift+Up, VS Code terminal Ctrl+Up or Cmd+Up, Windows Terminal via `scrollToMark`; not macOS Terminal or WezTerm).

Transcript labels: `you:`, `claude:`, `thinking:`, `tool:`, `tool error:`, `error:`, `warning:`, `Permission Required:`, `Cost:` (at exit, if the account shows costs).

# Limits and defaults

- Project settings cannot turn it on: `axScreenReader` and `CLAUDE_AX_SCREEN_READER` under `env` in `.claude/settings.json` or `.claude/settings.local.json` are ignored, and startup prints `Screen reader mode is off: project settings can't turn it on`.
- No announcement when the permission mode changes by a command such as `/plan`. Attached background sessions (`claude attach`, agent view) enter the alternate screen with no native scrollback (Left Arrow on empty prompt, or Ctrl+Z if a dialog has focus, to leave).
- Does not change non-interactive mode (`-p`), which already writes plain text.
