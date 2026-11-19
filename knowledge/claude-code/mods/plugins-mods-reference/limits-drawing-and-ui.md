---
type: "Limit"
title: "Limits: drawing, redraw, toast, panes and placed rows"
description: "Tree size and nesting limits, redraw throttling, toast timing, pane placement widths and the placed-row cap."
resource: "https://code.claude.com/docs/en/plugins/mods/reference"
tags: [mods, limits, ui, throttling]
kind: "limit"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop, ide]
requires: ""
identifiers:
  - "$.ui.toast"
  - "{ timeoutMs }"
  - "$.ui.invalidate('ui.render')"
  - "$.ui.place"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-reference"
    resource: "https://code.claude.com/docs/en/plugins/mods/reference"
    title: "Mods reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A tree over the nesting, element, `Raster` cell or `Image` byte limit is not drawn.

| Limit | Value |
| :- | :- |
| Text in one tree | first 100,000 characters drawn |
| A `Code`'s `language` or `path`, a `Select` option's `value`, a `Client`'s `module` | 10,000 characters; longer makes the returning `ui.render` hook fail |
| A `Link`'s `href` | 2,048 characters; longer makes the hook fail |
| Nesting depth of one tree | 32 levels below the root |
| Elements and text children in one tree | 20,000 |
| `Raster` cells in one tree (`columns` x `rows`) | 262,144 |
| Rows above the prompt, stacked | elements, Raster cells and Image bytes add up across rows against the one-tree limits |
| PNG or RGBA bytes of all `Image`s in one tree | 2 MiB |
| `$.ui.invalidate('ui.render')` redraws | throttled to 10 a second, or 30 in the terminal for the visible pane, expanded band and hint line; sooner calls are coalesced |
| `$.ui.toast` | shown 4 seconds unless `{ timeoutMs }`; in the classic renderer a mod's newer toast can replace its older one |
| A pane opened without the user asking | placed from 144 terminal columns, 110 after the user has opened it once |
| Rows from `$.ui.place` one mod has in a conversation | 500; at the limit a new `id` resolves to `{ isPlaced: false, reason: 'a plugin holds at most 500 placed rows' }` |
