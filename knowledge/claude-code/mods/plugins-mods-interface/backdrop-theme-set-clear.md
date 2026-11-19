---
type: "Feature"
title: "Backdrop and theme ($.theme.set, $.theme.clear)"
description: "$.theme.set sets a backdrop and colors for the Desktop or mobile app; $.theme.clear removes them; replaces the removed $.ui.backdrop."
resource: "https://code.claude.com/docs/en/plugins/mods/interface"
tags: [mods, theme, backdrop, desktop]
kind: "api"
maturity: "unlabelled"
since: "2.1.319"
surfaces: [desktop, mobile]
requires: "Claude Code v2.1.319 or later (example needs v2.1.323)"
identifiers:
  - "$.theme.set"
  - "$.theme.clear"
  - "$.ui.backdrop"
  - "Backdrop"
  - "backdrop.scene"
  - "overrideColorScheme"
  - "isDrawn"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-interface"
    resource: "https://code.claude.com/docs/en/plugins/mods/interface"
    title: "Draw in the interface with a mod"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`$.theme.set({ backdrop: { scene: 'night-sky' }, overrideColorScheme: 'dark' })` sets a backdrop drawn at the `Backdrop` render site (hook checks `e.props.plugin` and `e.props.scene`). `$.theme.clear()` removes any mod's backdrop. The terminal draws no backdrop. `$.ui.backdrop` was removed in v2.1.319.

# Limits and defaults

- Neither a module reload nor `--resume` keeps the backdrop; set it in `session.start`.
- `$.theme.set` resolves `isDrawn: true` when a connected Desktop or mobile app says it draws backdrops; otherwise `isDrawn: false` with a `reason`.
- One theme per session: any `$.theme.set` replaces the session's backdrop and colors, and `$.theme.clear()` removes them, whichever mod set them. Call clear only when the user asks.
- Before v2.1.323: use `id` instead of `scene` (also in `e.props`), and `colorScheme` inside `backdrop` instead of `overrideColorScheme`.
- `scene` is a name of letters, digits, `_`, `-`, up to 64 characters.
