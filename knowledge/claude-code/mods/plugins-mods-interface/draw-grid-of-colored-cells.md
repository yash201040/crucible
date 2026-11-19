---
type: "Feature"
title: "Draw a grid of colored cells (Raster and $.ui.blit)"
description: "Raster packs cells as base64 (code point, color, background) for terminal heat maps; $.ui.blit repaints one Raster without re-rendering."
resource: "https://code.claude.com/docs/en/plugins/mods/interface"
tags: [mods, raster, blit, animation]
kind: "ui"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "Raster"
  - "cells"
  - "columns"
  - "rows"
  - "$.ui.blit"
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

For a terminal heat map, sparkline or game board, draw one `Raster` rather than a `Box` per cell. Props: `key`, `columns`, `rows`, `cells`. Each cell is three numbers: character code point, color, background color. A color is 24-bit RGB (`0xc62828`); `0x01000000` means the terminal default.

# How to use it

Other apps have no `Raster`, so check `e.surface` and draw text. Each character must be one cell wide. To animate a drawn `Raster`: `$.ui.blit({ requestId: 'heat', key: 'grid', columns: 3, rows: 2, cells })` with the pane's `id` as `requestId`; it repaints that element without rerunning `ui.render`.
