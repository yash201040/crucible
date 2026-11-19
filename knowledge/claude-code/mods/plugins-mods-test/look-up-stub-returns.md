---
type: "Reference"
title: "What each stub returns"
description: "Table of the stub shape to register for each common mods API call or event, and which calls the kit answers itself."
resource: "https://code.claude.com/docs/en/plugins/mods/test"
tags: [mods, testing, stubs, reference]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "$.command.register"
  - "$.tool.register"
  - "$.ui.toast"
  - "$.ui.log"
  - "$.ui.status"
  - "$.ui.close"
  - "$.store.set"
  - "$.store.get"
  - "$.fs.read"
  - "$.ui.open"
  - "$.ui.ask"
  - "$.model.complete"
  - "$.process.run"
  - "turn.start"
  - "turn.complete"
  - "prompt.submit"
  - "prompt.fill"
  - "$.prompt.read"
  - "$.ui.copy"
  - "$.ui.notify"
  - "$.session.messages"
  - "$.session.id"
  - "$.agent.list"
  - "session.send"
  - "session.receive"
  - "$.ui.invalidate"
  - "$.state"
  - "$.session.append"
  - "$.clock"
  - "{ deny: 'the reason' }"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-test"
    resource: "https://code.claude.com/docs/en/plugins/mods/test"
    title: "Test a mod"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Every mods API call a mod makes in a test needs a stub, except `$.ui.invalidate`, `$.state` and `$.session.append`, which the kit answers itself. For `$.clock` use `mock.clock(on)`, or `$.clock.now()` fails with `no implementation for clock.now`.

# How to use it

Pass the function under the call's name without `$.`, e.g. `on('store.get', ($, e) => ({ value: saved.get(e.key) }))`.

| Your mod calls or passes on | Stub |
| :- | :- |
| `$.command.register`, `$.tool.register`, `$.ui.toast`, `$.ui.log`, `$.ui.status`, `$.ui.close`, `$.store.set` | `() => ({ value: undefined })`; for `ui.toast` and `ui.log` the text is `e.text` |
| `$.store.get` | `($, e) => ({ value: saved.get(e.key) })` |
| `$.fs.read` | `value` string; `e.path` is absolute, compare with `endsWith` |
| `$.ui.open` | `() => ({ value: { isPlaced: true } })` |
| `$.ui.ask` | a `tool.call` stub, since the question arrives as an `AskUserQuestion` tool call: `({ result: { answers: { [e.questions[0].question]: 'Run it' } } })`; check `e.tool` first |
| `$.model.complete` | `() => ({ value: { isAnswered: true, text: '...', usage } })` |
| `$.process.run` | `({ value: { exitCode: 0, stdout: '...', stderr: '' } })`; `e.argv` is the argument list, `e.init` holds `cwd` and `timeoutMs` |
| any call that should fail | `() => ({ deny: 'the reason' })` makes the call reject; a stub that throws is skipped instead |
| `session.start` | `() => ({ cwd: '/work' })` |
| `turn.start` | `($, e) => ({ turnId: e.turnId })` |
| `tool.call` | `() => ({ result: '...' })` |
| `turn.complete` | `() => ({ text: '' })`; fire with `$.turn.complete({ turnId, answer, durationMs, isAborted: false, usage: null })` |
| `prompt.submit` | `($, e) => ({ text: e.text })` |
| `prompt.fill` | `() => ({ isFilled: true })` |
| `$.prompt.read` | `() => ({ value: { text: '...', cursor: 0 } })` |
| `$.ui.copy` | `() => ({ value: { isCopied: true } })` |
| `$.ui.notify` | `() => ({ value: { isSent: true, channel: 'terminal_bell' } })`; text `e.text`, title `e.title` |
| `$.session.messages` | `() => ({ value: [{ role: 'assistant', text: '...', toolUses: [] }] })` |
| `$.session.id`, `$.agent.list` | `() => ({ value: 'abc123' })`, `() => ({ value: [] })` |
| `session.send` | `() => ({ isDelivered: true })`; `e.to` arrives as a string even when the mod passed `{ sessionId }` |
| `session.receive` | `($, e) => ({ text: e.text })`; fire with `$.session.receive({ origin: { kind: 'peer-send-message' }, text })` |
| `ui.render` | `() => ({ type: 'Text', props: {}, children: ['...'] })`; for the band see [kit rules](./test-kit-rules.md) |

# Notes

Mods that spawn or message other agents use `$.agent.list`, `session.send` and `session.receive`; these have stubs too.
