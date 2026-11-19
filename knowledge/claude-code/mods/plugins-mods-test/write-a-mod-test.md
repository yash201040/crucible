---
type: "Guide"
title: "Write and run a mod test"
description: "claude plugin test runs *.test.ts files that fire events through a mod's hooks with no session, sign-in or network."
resource: "https://code.claude.com/docs/en/plugins/mods/test"
tags: [mods, testing, ci, plugin-test]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "claude plugin test"
  - "claude-code/testing"
  - "*.test.ts"
  - "test()"
  - "declares no test(): nothing ran"
  - "claude plugin test: hooks modules are turned off"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-test"
    resource: "https://code.claude.com/docs/en/plugins/mods/test"
    title: "Test a mod"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A mod is a plugin whose code registers event handlers (hooks). `claude plugin test` loads the mod, sends events through its hooks the way Claude Code would, and checks what the hooks did. No session, sign-in or network is needed. Each test file imports the test kit from the `claude-code/testing` module.

# How to use it

- Name test files `*.test.ts` (for example `first-mod.test.ts`) and save them anywhere in the plugin directory.
- Every file needs at least one `test()`, otherwise the run fails with `declares no test(): nothing ran`.
- Test files can import the mod's own files and sibling `.ts` helpers, so plain functions can be unit tested without the kit.
- Run `claude plugin test` from the mod's directory. Output lists each test as pass or fail with timings and a count line.

```typescript
import { expect, test } from 'claude-code/testing'
test('name', async ($, on) => {
  on('tool.call', () => ({ result: 'ok' }))
  await $.tool.call({ tool: 'Bash', command: 'ls' })
  const answer = await $.command.run({ command: 'tally', args: '' })
  expect(answer.text).toBe('...')
})
```

# Limits and defaults

- Exit status is 1 when a test fails, so it works in CI.
- If the mods cannot load in the shell running it, it prints a line starting `claude plugin test: hooks modules are turned off` with the reason and exits 1.
- Stubbed tool calls mean no real tool runs (no `ls` executes, no file is read).

# Notes

See [stubs](./stub-claude-code-answers.md) and [kit rules](./test-kit-rules.md). The CLI form is also listed in the [plugin commands reference](../../plugins-reference/plugins-cli-reference/plugin-test.md).
