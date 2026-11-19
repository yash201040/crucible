---
type: "Feature"
title: "Test a mod with claude plugin test"
description: "claude plugin test runs tests that fire events at a mod's hooks with no session, sign-in or network."
resource: "https://code.claude.com/docs/en/plugins/mods/create"
tags: [mods, testing, automation]
kind: "cli_flag"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless]
requires: ""
identifiers:
  - "claude plugin test"
  - "claude-code/testing"
  - "tests/first-mod.test.ts"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-create"
    resource: "https://code.claude.com/docs/en/plugins/mods/create"
    title: "Create a mod"
stale_after: "2027-01-19T00:00:00Z"
---

# How to use it

From the mod directory run `claude plugin test`. Tests import `{ expect, test }` from `claude-code/testing`; a test body `async ($, on) => {...}` can stub events (`on('tool.call', () => ({ result: 'ok' }))` answers in Claude Code's place so no tool runs), fire them (`await $.tool.call({ tool: 'Bash', command: 'ls' })`, `await $.command.run({ command: 'tally', args: '' })`) and assert on the result. Example file `first-mod/tests/first-mod.test.ts`. Output lists `(pass)` per test and a summary such as `1 pass 0 fail`.

# Notes

Stubbing a model call or the store, and testing timers and drawings, are covered on the Test a mod page.
