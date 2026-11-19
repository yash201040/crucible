---
type: "Reference"
title: "Keep state: variable, $.state and $.store"
description: "Three places a mod keeps values with different lifetimes, and the atom/read/update helpers with their validation rules."
resource: "https://code.claude.com/docs/en/plugins/mods/interface"
tags: [mods, state, store, persistence]
kind: "api"
maturity: "unlabelled"
since: "2.1.299"
surfaces: [cli, desktop, ide]
requires: ""
identifiers:
  - "$.state"
  - "$.store"
  - "$.store.get"
  - "$.store.set"
  - "atom"
  - "read"
  - "update"
  - "types/index.d.ts"
  - "PluginState"
  - "types"
  - "cleanupPeriodDays"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-interface"
    resource: "https://code.claude.com/docs/en/plugins/mods/interface"
    title: "Draw in the interface with a mod"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

| Keep it in | Lasts until | Use for |
| :- | :- | :- |
| Module variable | module reloads (every file save in development) | losable values |
| `$.state` | session ends, or `/clear`, `/resume`, `/branch` | drawing values that should survive a reload |
| `$.store` | mod deletes it, or no session reads/writes the store for `cleanupPeriodDays`; key-value, JSON file under `~/.claude/plugins/store/` | settings, history, anything expected next time |

`$.store.get(key)` resolves the value or `undefined`; `$.store.set(key, value)` takes any JSON value.

# How to use it

`$.state` is reactive: a `ui.render` hook that reads a value is redrawn on each write. Set up: declare values in `types/index.d.ts` (`declare module 'claude-code' { interface PluginState { 'hello-tabs': { tab: 'one'|'two'; count: number } } }`); add `"types": "./types/index.d.ts"` to the manifest so `claude plugin validate` checks it (leaving `types` out needs v2.1.299+); in code `import { atom, read, update } from 'claude-code'`, `const count = atom({ plugin: 'hello-tabs', key: 'count' }, 0)`, `await read($, count)`, `update($, count, (v) => v + 1)`.

# Limits and defaults

- Write `plugin` and `key` as string literals; hold each `atom` in a `const` (a `let` fails with `takes a source the scan can read`); declare every value (else `hello-tabs.count is not declared`).
- A `ui.render` hook can read state but not write it; write from `onPress`, `onSubmit` or another event's hook.
