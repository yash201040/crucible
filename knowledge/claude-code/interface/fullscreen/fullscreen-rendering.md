---
type: "Feature"
title: "Fullscreen rendering"
description: "Alternate-screen renderer for the CLI that removes flicker, keeps memory flat and adds mouse support; how to switch and which renderer you start in."
resource: "https://code.claude.com/docs/en/fullscreen"
tags: [fullscreen, rendering, tui, terminal, research-preview]
kind: "mixed"
maturity: "research-preview"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "/tui fullscreen"
  - "/tui default"
  - "/tui"
  - "tui"
  - "CLAUDE_CODE_NO_FLICKER"
  - "CLAUDE_CODE_DISABLE_ALTERNATE_SCREEN"
  - "CLAUDE_CODE_ALT_SCREEN_FULL_REPAINT"
  - "/feedback"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "fullscreen"
    resource: "https://code.claude.com/docs/en/fullscreen"
    title: "Fullscreen rendering"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A research-preview renderer that draws on the terminal's alternate screen (like `vim`) and renders only visible messages, so memory stays constant and the input box stays fixed. It has nothing to do with window size.

# How to use it

`/tui fullscreen` saves the `tui` setting and relaunches; `/tui default` switches back; `/tui` alone prints the active renderer. Env: `CLAUDE_CODE_NO_FLICKER=1 claude`. The relaunch carries the on-screen conversation (honoring a prior `/rewind`), permission mode, effort, `/model` choice, `--allowed-tools`/`--disallowed-tools`, `--agent`, `--agents`, `--append-system-prompt`, `--system-prompt-snapshot`, and `--chrome`/`--no-chrome`. It declines (error `Cannot switch renderers in this session`) if the session has restrictions it cannot pass on: `--system-prompt` replacement, `--tools` allowlist, `--setting-sources`, or deny/ask rules added by a hook or SDK permission update. `/tui` clears `CLAUDE_CODE_NO_FLICKER` in the relaunched process.

Which renderer at startup (first matching row): `CLAUDE_CODE_DISABLE_ALTERNATE_SCREEN=1` or `CLAUDE_CODE_NO_FLICKER=0` gives classic; `CLAUDE_CODE_NO_FLICKER=1` fullscreen; a past failed fullscreen start gives classic; iTerm2 `tmux -CC` or SSH to Claude Code on Windows gives classic; a saved `tui` setting wins; sessions without feature-flag fetching (Bedrock, Agent Platform, Microsoft Foundry, telemetry off) get fullscreen if the machine's first launch ran v2.1.239+ (classic if the startup dialog was retired); sessions with feature flags get fullscreen if first used on or after May 6, 2026; otherwise classic. A startup dialog may offer the switch, at most three launches; "Not now" stops it.

# Limits and defaults

- Screen reader mode always uses the classic renderer, except attached background sessions (agent view, `claude attach`), which always render fullscreen and ignore `tui` and `CLAUDE_CODE_DISABLE_ALTERNATE_SCREEN`.
- Failed starts: after one crash before a successful start (first frame drawn, then 10 s up or `/exit`, Ctrl+C or Ctrl+D) the next session starts classic with `Claude Code's fullscreen renderer didn't finish starting last time on this machine`; after two, classic stays until update or `/tui fullscreen`. `CLAUDE_CODE_NO_FLICKER=1` overrides and is not counted. Before v2.1.236 it kept starting fullscreen.
- Stale text on Windows Terminal/ConPTY: `CLAUDE_CODE_ALT_SCREEN_FULL_REPAINT=1` (auto-enabled on Windows for background sessions and agent view).
- tmux: set `set -g mouse on` for wheel scrolling; incompatible with iTerm2 `tmux -CC`; tmux up to 3.6 lacks synchronized output so more flicker.
- The conversation is in the alternate buffer, so `Cmd+f` and tmux search do not see it; use `Ctrl+o` transcript mode then `/` search, `[` to write the full conversation to native scrollback, or `v` to open it in `$VISUAL`/`$EDITOR`. `/focus` shows only last prompt, tool-call summaries and final response. `/diff` opens a panel beside the conversation. `/clear` starts a new conversation; `Ctrl+L` redraws (`Cmd+K` too where it reaches Claude Code); before v2.1.238 `Ctrl+L` twice ran `/clear`.
