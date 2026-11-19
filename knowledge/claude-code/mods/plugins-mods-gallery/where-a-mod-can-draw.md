---
type: "Concept"
title: "Where a mod can draw (pointers)"
description: "Index of the places a mod can show output: pane, band, Claude Code's own rows, toast, status line, log line and question dialog."
resource: "https://code.claude.com/docs/en/plugins/mods/gallery"
tags: [mods, render-sites, toast, dialog]
kind: "ui"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop, ide]
requires: ""
identifiers: []
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-gallery"
    resource: "https://code.claude.com/docs/en/plugins/mods/gallery"
    title: "Interface gallery for mods"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Beyond the pane used in the samples, a mod can draw in: the pane and the band above the prompt; Claude Code's own rows such as the spinner; toast, status line and log line (via the mods API `$.ui` calls); and the question dialog (via `$.ui.ask`). See [pick where to draw](../plugins-mods-interface/pick-where-to-draw-pane-band.md).
