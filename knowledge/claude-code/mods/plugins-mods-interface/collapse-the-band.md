---
type: "Feature"
title: "User collapse of the band above the prompt"
description: "The user can collapse the band to one dim row; the mod cannot expand it and nothing in it can be pressed while collapsed."
resource: "https://code.claude.com/docs/en/plugins/mods/interface"
tags: [mods, band, collapse, keybindings]
kind: "ui"
maturity: "unlabelled"
since: "2.1.321"
surfaces: [cli]
requires: ""
identifiers:
  - "[-]"
  - "abovePrompt:toggle"
  - "e.props.isCollapsed"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-interface"
    resource: "https://code.claude.com/docs/en/plugins/mods/interface"
    title: "Draw in the interface with a mod"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

While a mod draws in the band, the user can collapse it: click `[-]` at the right end of its first row (fullscreen rendering) or press Ctrl+X then Ctrl+A (rebindable through the `abovePrompt:toggle` action). The collapsed band hides all mod drawings and shows one dim row: `▸ plugin panel hidden · ctrl+x ctrl+a or click to show`.

# Limits and defaults

- While collapsed nothing in the band can be pressed: no hotkey, no typed digit, no `action` keybinding. Focus returns to the prompt on collapse; Ctrl+X then Tab skips the band.
- It stays collapsed until the user expands it, even after `/clear`, and is expanded on the next start. A mod cannot expand it, so do not make the band the only place for something the user must answer.
- `e.props.isCollapsed` in a `ui.render` hook (which keeps running) tells the mod; requires v2.1.321 or later.
