---
type: "Reference"
title: "Events: interface, other mods, telemetry, settings hooks and API calls"
description: "ui.* events, plugin.register and engine.create, telemetry events, classic.<Event>, and every mods API method as an event."
resource: "https://code.claude.com/docs/en/plugins/mods/reference"
tags: [mods, events, ui, telemetry]
kind: "hook"
maturity: "unlabelled"
since: "2.1.321"
surfaces: [cli, desktop, ide]
requires: ""
identifiers:
  - "ui.render"
  - "ui.resolve"
  - "ui.press"
  - "ui.input"
  - "ui.select"
  - "ui.focus"
  - "ui.scroll"
  - "ui.close"
  - "ui.message"
  - "ui.fault"
  - "plugin.register"
  - "engine.create"
  - "telemetry.log"
  - "telemetry.mark"
  - "{ to: 'collector' }"
  - "classic.<Event>"
  - "http.fetch"
  - "e.uses"
  - "e.init.compress"
  - "value.isStreaming"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-reference"
    resource: "https://code.claude.com/docs/en/plugins/mods/reference"
    title: "Mods reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

| Event | Fires when | Return |
| :- | :- | :- |
| `ui.render` | a render site is about to be drawn | element tree, or `next` |
| `ui.resolve` | mods load, once per app, render site and mod; result is the element table `$.ui.resolve(e)` reads | |
| `ui.press`, `ui.input`, `ui.select` | a mod-drawn Button, Input or Select is used | |
| `ui.focus`, `ui.scroll` | focused control or pane/band scroll position is about to change | |
| `ui.close` | a pane is about to close; `e.id` is the pane, `e.origin.kind` is `plugin`, `person` or `unload` | |
| `ui.message` | a `Client` posts data to its mod | |
| `ui.fault` | a `Client` failed; `e.phase` is `load`, `render` or `run`, `e.reason` the message; v2.1.289+ | |
| `plugin.register` | a hooks module is about to load; `e.uses` lists its events, API calls (no `$.` prefix, e.g. `fs.read`), env vars and state as `claude plugin validate` prints them | `{ refuse: reason }` |
| `engine.create` | the mods API is built for a mod | a changed mods API to add a namespace; a mod outside the `user` tier can also withhold one |
| `telemetry.log`, `telemetry.mark` | a telemetry record is about to be logged, or a feature use marked | `next(e)` or `{ deny: reason }` |
| `classic.<Event>` | each settings hook event, e.g. `classic.Stop`; `e` is its stdin JSON | |

Telemetry hooks in an installed mod need the filter `{ to: 'collector' }` (`on('telemetry.log', { to: 'collector' }, hook)`) or the mod fails `claude plugin validate`; `*` does not match them.

# How to use it

Every mods API method is also an event named by namespace and method (`fs.read`, `model.complete`, `ui.open`); a hook on one can return `next(e)`, `{ deny: reason }`, or `{ value }`. Some also fire for Claude Code's own actions: check `next.origin.plugin` is `engine` before refusing. When another mod calls a method on a namespace you added in `engine.create`, your method's `$` calls run in that hook's context until all hooks on the event return (relative paths resolve against its working directory; `$.prompt.submit` rejects while the turn waits on it).

# Limits and defaults

`http.fetch` events with `next.origin` `{ plugin: 'engine', tier: 'core' }` are Claude Code's own requests (such as model requests); with the built-in guard loaded, a mod gets them only if it counts as the organization's. Fields: `e.init.compress` (set when Claude Code compresses the body after your hook; `e.init.body` is uncompressed; send uncompressed via `next({ ...e, init: { ...e.init, compress: undefined } })`); `value.isStreaming` (true when Claude Code reads the body itself so `value.text` is empty; read `value.status`/`value.headers`; to answer with your own `text`, return a `value` without `isStreaming`). These need v2.1.321+.
