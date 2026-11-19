---
type: "Reference"
title: "Image and Client elements, terminal image support"
description: "Which terminals draw Image, when alt text shows instead, the CLAUDE_CODE_FORCE_TERMINAL_IMAGES override and tmux requirements."
resource: "https://code.claude.com/docs/en/plugins/mods/gallery"
tags: [mods, image, tmux, terminal]
kind: "ui"
maturity: "unlabelled"
since: "2.1.310"
surfaces: [cli]
requires: "kitty 0.28+, Ghostty, or iTerm2 3.5+ (iTerm2 needs Claude Code v2.1.305+)"
identifiers:
  - "Image"
  - "Client"
  - "CLAUDE_CODE_FORCE_TERMINAL_IMAGES"
  - "CLAUDE_CODE_ALT_SCREEN_FULL_REPAINT"
  - "/tui fullscreen"
  - "source.png"
  - "source.rgba"
  - "source.file"
  - "allow-passthrough"
  - "focus-events"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-gallery"
    resource: "https://code.claude.com/docs/en/plugins/mods/gallery"
    title: "Interface gallery for mods"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`Image` draws a PNG or raw pixels in the terminal; `Client` is a region a second file of yours draws, for animation and pointer input. No samples; props are in the reference.

`Image` draws as a picture in kitty 0.28 or later, Ghostty, and iTerm2 3.5 or later (iTerm2 drawing requires Claude Code v2.1.305 or later). Elsewhere the user sees the `alt` text, dimmed. `alt` also shows in: GNU screen; tmux without its requirements; every background session (see agent view); iTerm2 outside fullscreen rendering or with `CLAUDE_CODE_ALT_SCREEN_FULL_REPAINT=1` (run `/tui fullscreen` and leave it unset); a file-path source in iTerm2 or tmux (use base64 `source.png` or `source.rgba` instead of `source.file`).

# How to use it

If a kitty-graphics terminal with Unicode placeholders shows dim text, set `CLAUDE_CODE_FORCE_TERMINAL_IMAGES=1`. Do not set it inside GNU screen, tmux older than 3.3, a tmux popup, or with `allow-passthrough` off (user sees a box instead of alt text and no picture).

Inside tmux require: Claude Code v2.1.310+; tmux 3.3+; a tmux pane (not popup); tmux inside kitty 0.28+/Ghostty/iTerm2 3.5+; `focus-events` and `allow-passthrough` `on` (kitty/Ghostty may use `all`); in iTerm2, no `-CC`, fullscreen rendering on, `CLAUDE_CODE_ALT_SCREEN_FULL_REPAINT` unset, tmux window not bigger than the iTerm2 window (`tmux display-message -p '#{window_bigger}'` must not print `1`); picture passed as `png` or `rgba` bytes. Fix with `tmux set -g allow-passthrough on` and `tmux set -g focus-events on`, detach, reattach, restart Claude Code (again whenever tmux is attached from a different terminal); persist in `~/.tmux.conf`.
