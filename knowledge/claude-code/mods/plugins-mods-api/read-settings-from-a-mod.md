---
type: "Feature"
title: "Read settings from a mod"
description: "$.settings.read returns merged settings, one source, or one top-level key; the key option needs v2.1.304."
resource: "https://code.claude.com/docs/en/plugins/mods/api"
tags: [mods, settings, precedence]
kind: "api"
maturity: "unlabelled"
since: "2.1.304"
surfaces: [cli]
requires: "Claude Code v2.1.304 or later for the key argument"
identifiers:
  - "$.settings.read"
  - "source"
  - "key"
  - "user"
  - "project"
  - "local"
  - "flag"
  - "policy"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-api"
    resource: "https://code.claude.com/docs/en/plugins/mods/api"
    title: "Use the mods API"
stale_after: "2027-01-19T00:00:00Z"
---

# How to use it

| Call | Resolves to |
| :- | :- |
| `$.settings.read()` | All sources merged by precedence, as one object with settings.json top-level keys |
| `$.settings.read({ source: 'policy' })` | That source's settings, or `{}` |
| `$.settings.read({ key: 'spinnerTipsEnabled' })` | That key's merged value, or `undefined` |
| `$.settings.read({ key: 'spinnerTipsEnabled', source: 'user' })` | That key in that source, or `undefined` |

`source` values: `user` (`~/.claude/settings.json`), `project` (`.claude/settings.json`), `local` (`.claude/settings.local.json`), `flag` (what `--settings` passes, and the SDK's inline settings), `policy` (managed settings).

# Limits and defaults

`key` is the exact name of one top-level key, not a dotted path into a nested object.
