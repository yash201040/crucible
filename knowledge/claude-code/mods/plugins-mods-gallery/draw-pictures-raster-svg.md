---
type: "Reference"
title: "Gallery: Raster and Svg"
description: "Raster draws a packed grid of colored cells in the terminal; Svg draws an SVG document in the Desktop app and VS Code only."
resource: "https://code.claude.com/docs/en/plugins/mods/gallery"
tags: [mods, raster, svg, drawing]
kind: "ui"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop, ide]
requires: ""
identifiers:
  - "Raster"
  - "Svg"
  - "e.surface"
  - "cellsOf"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-gallery"
    resource: "https://code.claude.com/docs/en/plugins/mods/gallery"
    title: "Interface gallery for mods"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`Raster({ key, columns, rows, cells })` is a grid of colored character cells (heat map, sparkline, game board), drawn by the terminal. `cells` is a base64 string produced by packing, for each cell, the code point, color and background (the starter's `cellsOf` does this with `Uint32Array` then `toBase64()`). A default color is `0x01000000`.

`Svg({ alt, width, height, source })` draws an SVG document in the Desktop app and the VS Code extension.

# Limits and defaults

- A `Raster` rounds each color to a smaller palette (`0x2e7d32` draws as `#337733`).
- In the terminal, a pane that returns only an `Svg` opens empty; check `e.surface` and return a different tree there.
