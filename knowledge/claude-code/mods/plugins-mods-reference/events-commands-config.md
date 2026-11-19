---
type: "Reference"
title: "Events: commands, configuration and turns"
description: "command.*, config.*, settings.read and the turn.* events with what each hook can return."
resource: "https://code.claude.com/docs/en/plugins/mods/reference"
tags: [mods, events, commands, turns]
kind: "hook"
maturity: "unlabelled"
since: "2.1.304"
surfaces: [cli, desktop, ide]
requires: ""
identifiers:
  - "command.run"
  - "command.describe"
  - "config.set"
  - "config.describe"
  - "settings.read"
  - "turn.start"
  - "turn.step"
  - "turn.complete"
  - "e.layers"
  - "e.source"
  - "next({ ...e, effort })"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-reference"
    resource: "https://code.claude.com/docs/en/plugins/mods/reference"
    title: "Mods reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

| Event | Fires when | A hook can return |
| :- | :- | :- |
| `command.run` | a command is about to run | `{ text }`, `{}`, `next(e)` |
| `command.describe` | once per command, for the command list | `{ description, argumentHint, isHidden }` |
| `config.set` | a `/config` row is about to change | `next({ ...e, value })` or `{ deny: reason }` |
| `config.describe` | once per `/config` row | `{ label, description, isHidden }` |
| `settings.read` | a mod calls `$.settings.read`, or Claude Code builds merged settings; Claude Code's own read and `e.layers` need v2.1.304+ | `next(e)`, `{ value }`, `{ deny: reason }` |
| `turn.start` | a turn begins | `next(e)` |
| `turn.step` | one request is about to go to the model | `yield* next(e)`, `next({ ...e, model })`, `next({ ...e, effort })` |
| `turn.complete` | a turn ended | `next(e)`, or `{ text }` for a line under the answer |

`settings.read` fields: `e.layers` is one `{ source, settings }` per source in use, lowest precedence first; `e.source` is the single source a mod asked for, absent on Claude Code's own read and merged reads.
