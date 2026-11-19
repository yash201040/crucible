---
type: "Guide"
title: "Test a drawing after /clear"
description: "Each test starts with $.state at defaults as /clear leaves them; fire classic.SessionStart with source clear to test reload of saved values."
resource: "https://code.claude.com/docs/en/plugins/mods/test"
tags: [mods, testing, clear, state]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "classic.SessionStart"
  - "$.classic.SessionStart({ source: 'clear' })"
  - "$.state"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-test"
    resource: "https://code.claude.com/docs/en/plugins/mods/test"
    title: "Test a mod"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Every test begins with each `$.state` value at its default, which is how `/clear` leaves them. To test what the mod does next, skip `session.start` and fire `classic.SessionStart` with `source: 'clear'`, then check what it draws.

# How to use it

Stub the store and the event, fire it, then mount:
`on('store.get', () => ({ value: 7 }))`, `on('classic.SessionStart', () => ({}))`, `await $.classic.SessionStart({ source: 'clear' })`, then `$.ui.mount(...)`, press the tab and `find` the text. The test passes when the mod's `classic.SessionStart` hook copied the stored value into `$.state` before drawing; without that hook the pane shows the default and `find` returns `undefined`.
