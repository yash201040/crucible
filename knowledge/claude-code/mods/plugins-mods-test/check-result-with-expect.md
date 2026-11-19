---
type: "Concept"
title: "Check results with expect"
description: "The kit's expect has its own matcher set; .not, .resolves and .rejects work; a failing expect inside a plain stub makes the test fail."
resource: "https://code.claude.com/docs/en/plugins/mods/test"
tags: [mods, testing, assertions]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "expect"
  - "toEqual"
  - "toHaveLength"
  - ".not"
  - ".resolves"
  - ".rejects"
  - "claude-code/index.d.ts"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-test"
    resource: "https://code.claude.com/docs/en/plugins/mods/test"
    title: "Test a mod"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`expect` has its own assertions such as `toEqual` and `toHaveLength`, placed after the value, as in `expect(answer.text).toBe('ok')`.

# How to use it

- For the full list, search `claude-code/index.d.ts` in the types for your build for `type Matchers`.
- Put `.not` before the assertion to invert it.
- Put `.resolves` or `.rejects` right after `expect(...)` and `await` the line: `await expect(promise).rejects.toThrow()`.

# Limits and defaults

When an `expect` fails inside a stub or hook passed to `on` as a plain function (not an async generator), the test fails, the engine skips that hook, and the output names it, e.g. `in the test's store.set hook`.
