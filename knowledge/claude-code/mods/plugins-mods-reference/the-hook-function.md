---
type: "Reference"
title: "The hook function: $, e, next and their fields"
description: "Arguments passed to every mod hook, including next.signal, origin, budget, to, error and called, and the on() registration."
resource: "https://code.claude.com/docs/en/plugins/mods/reference"
tags: [mods, hooks, next, api]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop, ide]
requires: ""
identifiers:
  - "on"
  - "$"
  - "e"
  - "next"
  - "next.signal"
  - "next.origin"
  - "next.budget"
  - "next.budget.ms"
  - "next.budget.remainingMs"
  - "next.to(e, tier)"
  - "next.error"
  - "next.called"
  - ".catch(handler)"
  - "prepend"
  - "user"
  - "append"
  - "builtin"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-reference"
    resource: "https://code.claude.com/docs/en/plugins/mods/reference"
    title: "Mods reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`on(eventName, matcher?, hook)` is called inside `register`, e.g. `on('tool.call', { tool: 'Bash' }, async ($, e, next) => next(e))`. It returns a registration with one method, `.catch(handler)`, the hook's error handler.

| Argument | What it is |
| :- | :- |
| `$` | the mods API; write each call in full (`$.fs.read('notes.md')`) |
| `e` | event input, deeply frozen plain data; pass a copy to `next` to change it |
| `next(e)` | next handler, middleware style; resolves to the event's result |
| `next.signal` | `AbortSignal` that aborts when the event is abandoned |
| `next.origin` | `{ plugin, tier }` of whoever fired the event; Claude Code is `{ plugin: 'engine', tier: 'core' }`; `tier` is `prepend`, `user`, `append` or `builtin` |
| `next.budget` | time limit: `.ms` whole, `.remainingMs` left |
| `next.to(e, tier)` | skip to a later tier (`append`, `builtin`, `core`); only mods in `prependPlugins` or `appendPlugins` can call it |
| `next.error` | `.catch` only: `kind` is `throw` or `timeout`, `message` the text |
| `next.called` | `.catch` only: `true` if the hook had called `next` |

# Notes

See [how a hook handles an event](../plugins-mods-events/how-a-hook-handles-event.md) and [failures](../plugins-mods-events/hook-failure-catch-handler.md).
