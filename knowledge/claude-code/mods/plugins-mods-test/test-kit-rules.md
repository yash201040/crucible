---
type: "Reference"
title: "Test kit rules"
description: "Rules for stubs and events in the mod test kit: register before first $ call, session.start does not run itself, ui.render and turn.step stubs."
resource: "https://code.claude.com/docs/en/plugins/mods/test"
tags: [mods, testing, rules, stubs]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.321"
surfaces: [cli]
requires: ""
identifiers:
  - "on(\"ui.render\") after the test first called $"
  - "session.start"
  - "ui.render"
  - "next(e)"
  - "ui.find"
  - "keepsBeneath()"
  - "{ plugin: 'my-mod' }"
  - "turn.step"
  - "$.turn.step"
  - "tool.call"
  - "command.register"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-test"
    resource: "https://code.claude.com/docs/en/plugins/mods/test"
    title: "Test a mod"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Five rules govern how tests, stubs and events behave in the kit.

# How to use it

1. **Register every stub before the test's first call on `$`.** Calling `on` later throws, e.g. `on("ui.render") after the test first called $`.
2. **`session.start` does not run by itself.** Each test starts with the module freshly loaded and no hooks called, so module variables hold initial values. Fire it yourself: `on('session.start', () => ({ cwd: '/work' }))`, `on('command.register', () => ({ value: undefined }))`, then `await $.session.start({ surface: 'terminal', isInteractive: true, cwd: '/work' })`. Without the `command.register` stub the call rejects with `no implementation for command.register`, the kit skips the hook, and the skip is listed under `the engine reported:` only if a later check fails.
3. **`ui.render` stub chooses what `next(e)` returns.** With no stub, a mount succeeds when the hook returns `next(e)`. To return an element you pick, register e.g. `on('ui.render', () => ({ type: 'Text', props: {}, children: ['drawn by Claude Code'] }))`; `ui.find({ type: 'Text' })` then returns it where the site can draw it. On v2.1.323 or later, for the band, pass the mod name as second argument to `on`: `{ plugin: 'my-mod' }`, or the stub does not answer `next(e)`. Before v2.1.321 the mount fails with `no implementation for ui.render` without the stub.
4. **A `turn.step` stub is an async generator**: each `yield { kind: 'text', index: 0, text: 'ok' }` is a streamed piece; the `return` value (`turnId`, `index`, `answer`, `toolUses`, `stopReason`, `usage`) is the request result. The test reads the stream with `$.turn.step({ turnId, index, model, messageCount })` and `stream.next()` until `done`; the final value is the result after the mod's `turn.step` hook may have changed it.
5. **Fire a tool call with the tool name and arguments as fields**, e.g. `$.tool.call({ tool: 'Bash', command: 'ls' })`, and register a `tool.call` stub returning `{ result }`.

# Notes

Related: [stub return table](./look-up-stub-returns.md), [drawing tests](./test-a-drawing.md).
