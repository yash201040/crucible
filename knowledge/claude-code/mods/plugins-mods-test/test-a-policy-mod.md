---
type: "Guide"
title: "Test a policy mod"
description: "tier() sets the load tier of the mod under test and test options plugins adds inline mods, to check a prependPlugins policy admits or refuses another mod."
resource: "https://code.claude.com/docs/en/plugins/mods/test"
tags: [mods, testing, policy, admin]
kind: "api"
maturity: "unlabelled"
since: "2.1.326"
surfaces: [cli]
requires: ""
identifiers:
  - "tier('prepend')"
  - "tier"
  - "plugins"
  - "prependPlugins"
  - "hooks module left out"
  - "refused"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-test"
    resource: "https://code.claude.com/docs/en/plugins/mods/test"
    title: "Test a mod"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A mod an organization lists in `prependPlugins` can refuse another mod before it loads. The kit lets a test set the mod's tier and supply a second mod.

# How to use it

- **`tier`**: call once at the top of the test file, `tier('prepend')`, to load the mod under test as `prepend`, `append` or `builtin` (its place in the order mods run). Without it the mod loads as `user`.
- **`plugins`**: pass `test` an options object before the body, `test('name', { plugins: [runner] }, async ($, on) => {...})`. Each inline mod has `name` and `register`; add `tier` to load it somewhere other than `user`.

The kit loads every mod at the test's first call on `$`. When the mod under test stops one, that call throws and the message names both mods. Match with `/^runner: (hooks module left out|refused) by acme-guard/`: the wording is "hooks module left out" on v2.1.326 or later and "refused" on earlier versions. A mod that is admitted answers the tool call before the stub.
