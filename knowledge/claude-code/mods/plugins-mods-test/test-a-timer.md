---
type: "Feature"
title: "Test a timer with a mock clock"
description: "mock.clock(on) gives a clock the test controls (advance, set, now, settle, sleep) so timer behavior is checked without waiting."
resource: "https://code.claude.com/docs/en/plugins/mods/test"
tags: [mods, testing, clock, timers]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "mock.clock(on)"
  - "mock.clock(on, { now: 5000 })"
  - "clock.advance"
  - "clock.set"
  - "clock.now()"
  - "clock.settle()"
  - "clock.sleep"
  - "$.clock.every"
  - "$.clock.after"
  - "$.clock.now()"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-test"
    resource: "https://code.claude.com/docs/en/plugins/mods/test"
    title: "Test a mod"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A mod that runs work on a timer needs a clock the test controls. `const clock = mock.clock(on)` returns a mock clock starting at `0` that moves only when the test moves it. Start elsewhere with `mock.clock(on, { now: 5000 })` (milliseconds).

# How to use it

| Method | What it does |
| :- | :- |
| `await clock.advance(1000)` | Moves time forward by that many ms and runs each timer that comes due |
| `await clock.set(5000)` | Moves time forward to that value, as `advance` would |
| `clock.now()` | Returns the time (what the mod's `$.clock.now()` resolves to) |
| `await clock.settle()` | Runs timers already due, such as a chain of zero-delay `$.clock.after` calls, without moving time |
| `await clock.sleep(2000)` | Inside a stub, makes the stub answer only after the test advanced that far, simulating a slow model or process |

Each `advance` resolves after the due timers ran, so the next line sees their effect. The documented example runs `/countdown 3`, advances 2000 then 1000 ms and checks the `Time is up` toast appears once, only at the end.
