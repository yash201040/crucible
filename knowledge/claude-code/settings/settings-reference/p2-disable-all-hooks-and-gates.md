---
type: "Feature"
title: "disableAllHooks and status-line gates"
description: "Turns off hooks, custom status line and file suggestion; reach depends on which file carries the key."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [settings, hooks, managed, sdk]
kind: "setting"
maturity: "unlabelled"
since: "2.1.242"
surfaces: [cli, sdk]
requires: ""
identifiers:
  - "disableAllHooks"
  - "--safe-mode"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`disableAllHooks` (any file, Boolean, default unset) turns off hooks, any custom status line and any custom file suggestion command without deleting them. Only managed settings can disable managed hooks.

# How to use it

`{ "disableAllHooks": true }`. Reach by carrier:

| Where set | What stops | What keeps running |
| :- | :- | :- |
| Managed settings | every configured hook including managed; mods in every installed plugin | Agent SDK in-process hooks (keeping them needs v2.1.242+); built-in mods |
| Agent SDK `managedSettings` option | user, project, local, plugin hooks and SDK `settings` hooks. Ignored on a machine with admin-deployed managed settings unless the admin lets an embedding host add policy. Needs v2.1.309+ | admin managed hooks, force-enabled plugin hooks, SDK hook callbacks |
| Any other file | user, project, local, plugin hooks; user-installed mods | managed hooks, SDK hooks, force-enabled plugin hooks, the organization's mods, built-in mods |

# Limits and defaults

Status line and file suggestion decisions, in order:
1. Off entirely when managed settings set `disableAllHooks`, or the folder is untrusted (same workspace-trust rule as hooks).
2. Narrowed to managed settings when `allowManagedHooksOnly` is set, when `disableAllHooks` is `true` outside managed settings after precedence, or when started with `--safe-mode`. A managed value runs if deployed; otherwise yours is skipped without warning (status line disabled, `@` autocomplete uses the built-in).

`/goal` cannot run while hooks are disabled, and `/hooks` shows a notice instead of your hooks. Related: [allowManagedHooksOnly](./p2-allow-managed-hooks-only.md).
