---
type: "Guide"
title: "Change the Desktop app colors with a mod"
description: "Ask Claude or write a colors mod using makeColors and $.theme.set to recolor the Desktop Code tab; fix and remove steps."
resource: "https://code.claude.com/docs/en/plugins/mods/interface"
tags: [mods, desktop, colors, makecolors]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.324"
surfaces: [desktop]
requires: "Claude Code v2.1.324 or later in the Code tab; Claude Desktop with a Claude account (not third-party provider on Desktop v5.11492.5 or earlier)"
identifiers:
  - "makeColors"
  - "make-colors.js"
  - "make-colors.d.ts"
  - "~/.claude/skills/paper/hooks/"
  - "$.theme.set"
  - "surface-0"
  - "text-primary"
  - "text-muted"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-interface"
    resource: "https://code.claude.com/docs/en/plugins/mods/interface"
    title: "Draw in the interface with a mod"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude Code in the terminal keeps its own colors; the Desktop Code tab can be recolored by a mod.

# How to use it

- Ask Claude in a local Code-tab session (e.g. "make a mod that makes the app cream in light mode and dark brown in dark mode") and approve its questions about files and hot reloading.
- Write it: have Claude copy `make-colors.js` and `make-colors.d.ts` from its `plugin-authoring` skill into `~/.claude/skills/paper/hooks/`; add `.claude-plugin/plugin.json` and `hooks/hooks.json` under `~/.claude/skills/paper/` (a mod under `~/.claude/skills/` loads at session start); in `register.js` call `makeColors({ label, light: { gray: { anchors: { 'surface-0', 'text-primary', 'text-muted' } } }, dark: {...} })` and `await $.theme.set({ colors: theme })` in `session.start`. Start a new local session to see it.

# Notes

Fixing missing colors: update Desktop and start a new session; confirm the mod loaded; a refused theme throws or lists a `problems` entry starting `Desktop won't paint this theme`; any other `$.theme.set` or `$.theme.clear()` in the session drops earlier colors and backdrop (pass `colors` and `backdrop` in one call; use one theme-setting mod). Remove: turn off the mod first (move the directory out of the mods folder or `~/.claude/skills/`, or disable it in **Manage plugins**), start a new session, then Settings, search `code appearance`, **Remove colors**.
