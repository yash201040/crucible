---
type: "Feature"
title: "Place a row in the transcript ($.ui.place)"
description: "$.ui.place adds a mod-drawn row at the end of the transcript, drawn at the Placed render site, that Claude does not see."
resource: "https://code.claude.com/docs/en/plugins/mods/interface"
tags: [mods, transcript, ui-place, placed]
kind: "api"
maturity: "unlabelled"
since: "2.1.314"
surfaces: [cli]
requires: ""
identifiers:
  - "$.ui.place"
  - "Placed"
  - "isPlaced"
  - "requestId"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-interface"
    resource: "https://code.claude.com/docs/en/plugins/mods/interface"
    title: "Draw in the interface with a mod"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A row is a line a mod adds to the terminal transcript after the latest message; it stays at that spot and Claude does not see it. Call `$.ui.place({ id })` (id 1 to 64 letters, digits, `_`, `-`, unique per row) and draw at `{ component: 'Placed' }`, checking `e.props.plugin === $.plugin.name` and `e.props.id`.

# How to use it

Result: `{ isPlaced: true, requestId }` when drawn; otherwise `isPlaced: false` and `reason` (e.g. `no attached surface draws placed rows yet`, or the row limit). A second call with the same `id` while the row exists adds no row and returns that `requestId`; redraw to change content. A command can fall back: `placed.isPlaced ? {} : { text: '...' }`.

# Limits and defaults

- Requires v2.1.314 or later.
- The row goes away when the conversation ends, when the user rewinds past it, or (outside fullscreen rendering) on compaction. `--resume` does not bring it back.
- 500 placed rows per mod per conversation.
