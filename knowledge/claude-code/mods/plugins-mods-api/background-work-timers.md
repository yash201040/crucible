---
type: "Feature"
title: "Background work and timers in mods"
description: "$.clock.every and $.clock.after replace setInterval and setTimeout; timer callbacks run outside any event."
resource: "https://code.claude.com/docs/en/plugins/mods/api"
tags: [mods, timers, background, abort]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "$.clock.every"
  - "$.clock.after"
  - "$.clock.now"
  - "$.clock.sleep"
  - "cancel()"
  - "next.signal"
  - "$.process.run"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-api"
    resource: "https://code.claude.com/docs/en/plugins/mods/api"
    title: "Use the mods API"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A hook runs for one event and has a time limit on its own execution; time waiting on `next` or a mods API call does not count (except `$.clock.sleep`). Work that outlives an event runs on a timer started from `session.start`.

# How to use it

`$.clock.every(ms, fn)` and `$.clock.after(ms, fn)` (delay first, milliseconds) replace `setInterval`/`setTimeout`; each returns a timer with `cancel()`; `await $.clock.now()` gives milliseconds. Example: every `60_000` ms run `$.process.run(['gh','pr','checks','--json','state'])` and show with `$.ui.status`. Return `next(e)` without waiting for the timer so the session starts at once.

# Limits and defaults

- The callback runs outside any event, keeps running between turns, and does not start a turn. If it throws, the error goes to the debug log and the timer runs again next interval.
- Timers stop after the module reloads.
- `next.signal` is an `AbortSignal` that aborts when the event being handled is abandoned (for example the user interrupts); pass it to long-running work.
