---
type: "Feature"
title: "Redrawing a site: invalidate, timer and throttling"
description: "ui.render reruns on prop or width changes; mods call $.ui.invalidate or $.clock.every for data changes, with throttled coalesced redraws."
resource: "https://code.claude.com/docs/en/plugins/mods/interface"
tags: [mods, redraw, invalidate, timer]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop, ide]
requires: ""
identifiers:
  - "$.ui.invalidate"
  - "$.clock.every"
  - "ui.fault"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-interface"
    resource: "https://code.claude.com/docs/en/plugins/mods/interface"
    title: "Draw in the interface with a mod"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A drawing is a snapshot. Claude Code reruns `ui.render` itself when a site's props or the terminal width change, and once more after `ui.fault` hooks return. It never reruns on a timer, and cannot see module variables change.

# How to use it

- After your data changes: `$.ui.invalidate('ui.render')`.
- On a timer: in `session.start`, `$.clock.every(1000, () => $.ui.invalidate('ui.render'))`; the timer stops when the module reloads and the new instance starts its own.
- A value in `$.state` needs no call: writing it redraws sites that read it.

# Limits and defaults

Redraws are throttled per site (see limits table: 10 a second, 30 for the visible terminal pane, expanded band and hint line). Faster calls are coalesced into one redraw that reads the latest data, so an animation cannot run faster than the limit.
