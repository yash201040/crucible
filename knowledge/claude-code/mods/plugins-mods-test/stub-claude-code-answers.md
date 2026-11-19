---
type: "Concept"
title: "Stubs: the test's $ and on"
description: "A test function receives $ (acts as Claude Code, fires events) and on (registers stubs that answer mods API calls); mock helpers cover clock, store, env, session."
resource: "https://code.claude.com/docs/en/plugins/mods/test"
tags: [mods, testing, stubs, mocks]
kind: "api"
maturity: "unlabelled"
since: "2.1.293"
surfaces: [cli]
requires: ""
identifiers:
  - "$"
  - "on"
  - "$.tool.call"
  - "$.command.run"
  - "$.prompt.submit"
  - "$.session.start"
  - "$.turn.complete"
  - "$.classic.Stop"
  - "mock.clock(on)"
  - "mock.store(on, { count: 7 })"
  - "mock.env(on, { CI: 'true' })"
  - "mock.session(on)"
  - "appended()"
  - "returned neither { value } nor { deny }"
  - "no implementation for"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-test"
    resource: "https://code.claude.com/docs/en/plugins/mods/test"
    title: "Test a mod"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

No model, store or tool runs in a test, so wherever the mod expects Claude Code to answer, the test supplies a stub. A test function gets two arguments.

# How to use it

| Argument | What it is |
| :- | :- |
| `$` | The test's own object acting as Claude Code (not the mods API a hook receives). Each method fires the event of the same name through the mod's hooks and resolves to the result: `$.tool.call`, `$.command.run`, `$.prompt.submit`, `$.session.start`, `$.turn.complete`. `$.classic.Stop` and other `$.classic` methods fire a settings hook event. A test cannot fire a mods API call such as `ui.close` directly; trigger it through the mod (for example press the closing button). |
| `on` | Registers stubs, hooks that answer in Claude Code's place. Name a stub for a mods API call without the `$.`: a stub `store.get` answers the mod's `$.store.get`. |

A stub for a mods API call returns an object with `value` (what the call resolves to), e.g. `{ value: 7 }`. A stub for a Claude Code event (`turn.step`, `tool.call`) returns that event's own result, e.g. `{ result: 'ok' }`. `$.session.send` and `$.prompt.fill` take their event's result.

Ready-made mocks exported by the kit:

| Mock | What it does |
| :- | :- |
| `mock.clock(on)` | Answers `$.clock`; returns a mock clock the test advances |
| `mock.store(on, { count: 7 })` | Answers `$.store` from a store starting with those entries; returns nothing, so to check what the mod saved write the two `store` stubs yourself |
| `mock.env(on, { CI: 'true' })` | Answers `$.env.get` from those variables |
| `mock.session(on)` | Returns a mock session whose `appended()` lists rows added with `$.session.append`, oldest first. Requires Claude Code v2.1.293 or later |

# Limits and defaults

Errors shown under a block headed `the engine reported:` in a failed test:
- `returned neither { value } nor { deny }`: a mods API stub returned a bare value.
- `no implementation for` plus a name: the mod made a call that no stub answers.

# Notes

See the [stub lookup table](./look-up-stub-returns.md) and [rules](./test-kit-rules.md).
