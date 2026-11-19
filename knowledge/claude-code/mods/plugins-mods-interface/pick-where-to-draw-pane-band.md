---
type: "Feature"
title: "Pick where to draw: pane and band above the prompt"
description: "A ui.render hook picks a render site by component matcher; Pane and AbovePrompt are empty until a mod fills them."
resource: "https://code.claude.com/docs/en/plugins/mods/interface"
tags: [mods, pane, band, render-site]
kind: "ui"
maturity: "unlabelled"
since: "2.1.323"
surfaces: [cli, desktop, ide]
requires: ""
identifiers:
  - "ui.render"
  - "{ component: 'Pane' }"
  - "{ component: 'AbovePrompt' }"
  - "e.component"
  - "e.surface"
  - "e.props"
  - "e.requestId"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-interface"
    resource: "https://code.claude.com/docs/en/plugins/mods/interface"
    title: "Draw in the interface with a mod"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Each place a mod can draw is a render site. Claude Code fires `ui.render` before drawing one; the hook returns what to draw. Filter with `{ component: 'Pane' }`. In the hook: `e.component` names the site, `e.surface` the app, `e.props` the site's data, and for a pane `e.requestId` is the `id` it was opened with.

- **Pane**: sidebar beside the transcript in a wide fullscreen terminal, otherwise a framed region above the prompt; each open pane gets a titled tab. Appears when the mod calls `$.ui.open` with a chosen `id`.
- **Band** (`AbovePrompt`): a strip directly above the prompt input; each mod gets its own row, stacked in the mod run order. Return a tree to draw, `next(e)` to draw nothing.

# Limits and defaults

Before v2.1.323 all mods shared one band drawing and your tree replaced what later mods drew; to support those releases put `await next(e)` among the children of a valid `Box`. A mod can also place a transcript row (see [place a row](./place-a-row-in-transcript.md)).
