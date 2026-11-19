---
type: "Reference"
title: "Files of a mod"
description: "Required and optional files in a mod plugin directory, and the register(on, options) entry point."
resource: "https://code.claude.com/docs/en/plugins/mods/reference"
tags: [mods, files, manifest, hooks-module]
kind: "file"
maturity: "unlabelled"
since: "2.1.299"
surfaces: [cli, desktop, ide]
requires: ""
identifiers:
  - ".claude-plugin/plugin.json"
  - "hooks/hooks.json"
  - "modules"
  - "hooks/register.js"
  - "register(on, options)"
  - "types/index.d.ts"
  - "userConfig"
  - ".test.ts"
  - ".test.tsx"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-reference"
    resource: "https://code.claude.com/docs/en/plugins/mods/reference"
    title: "Mods reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Reference entries cover the CLI and Desktop as of v2.1.290 and the VS Code extension as of v2.1.299. The complete reference is Claude Code's TypeScript declarations for mods (`mods/types/claude-code.d.ts` in the Claude Code repository); the copy Claude Code writes for your version wins over GitHub's when they differ.

| File | Required | Contents |
| :- | :- | :- |
| `.claude-plugin/plugin.json` | Yes | plugin manifest; mods add no required fields |
| `hooks/hooks.json` | Yes | `modules`: array of one path relative to this file, e.g. `"modules": ["./register.js"]`; may also hold settings hooks under `hooks` |
| hooks module, e.g. `hooks/register.js` | Yes | entry point exporting `register(on, options)`; extensions `.js .mjs .cjs .jsx .ts .mts .cts .tsx`; an ES module |
| `types/index.d.ts` (or the path in manifest `types`) | when the mod uses `$.state` or adds a mods API namespace | declares `PluginState` values and namespaces; omitting `types` from the manifest needs v2.1.299+ |
| `*.test.ts`, `*.test.tsx` | No | tests run by `claude plugin test` |

`options` holds the manifest's `userConfig` values with defaults filled in.
