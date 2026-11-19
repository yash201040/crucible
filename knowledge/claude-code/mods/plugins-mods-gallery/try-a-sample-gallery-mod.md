---
type: "Guide"
title: "Try an element sample with a gallery mod"
description: "A minimal /gallery mod that opens a pane so any element sample from the gallery can be pasted in and viewed."
resource: "https://code.claude.com/docs/en/plugins/mods/gallery"
tags: [mods, gallery, pane, plugin-dir]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "gallery/.claude-plugin/plugin.json"
  - "gallery/hooks/hooks.json"
  - "gallery/hooks/register.js"
  - "claude --plugin-dir ./gallery"
  - "/gallery"
  - "$.command.register"
  - "$.ui.open"
  - "command.run"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-gallery"
    resource: "https://code.claude.com/docs/en/plugins/mods/gallery"
    title: "Interface gallery for mods"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Samples on the gallery page are snippets, one element each. To see one, create a tiny mod: directory `gallery` with `.claude-plugin/plugin.json` (name, version, description, author) and `hooks/hooks.json` containing `{ "modules": ["./register.js"] }`.

# How to use it

`register.js` exports `register(on)` and registers: a `session.start` hook calling `$.command.register({ name: 'gallery', description: ... })`; a `command.run` hook (matcher `{ command: 'gallery' }`) calling `$.ui.open({ id: 'gallery', focus: true, closeOnEscape: true })` and returning `{}`; a `ui.render` hook (matcher `{ component: 'Pane' }`) that returns early with `next(e)` unless `e.requestId === 'gallery'`, destructures elements from `$.ui.resolve(e)` and returns a sample tree.

Run `claude --plugin-dir ./gallery` from the directory holding `gallery`, then `/gallery`. Paste a sample over the returned `Text(...)`; Claude Code reloads the module on each save, so rerun `/gallery`.

# Notes

A pane is a sidebar beside the transcript in a wide fullscreen terminal, or a framed region above the prompt otherwise. The starter also defines `noop`, a `picked` variable and `cellsOf(rows)` (packs Raster cells; see [Raster and Svg](./draw-pictures-raster-svg.md)).
