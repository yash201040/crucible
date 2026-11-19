---
type: "Feature"
title: "Change or refuse a settings read (settings.read)"
description: "A settings.read hook can replace or deny the merged settings Claude Code builds or a mod's $.settings.read, with layers by precedence."
resource: "https://code.claude.com/docs/en/plugins/mods/events"
tags: [mods, settings, settings-read, layers]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.304"
surfaces: [cli, desktop, ide]
requires: ""
identifiers:
  - "settings.read"
  - "e.layers"
  - "e.source"
  - "next.origin"
  - "$.settings.read"
  - "settings.read bypassed by cc-plugin-sec-default"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-events"
    resource: "https://code.claude.com/docs/en/plugins/mods/events"
    title: "React to events with a mod"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`settings.read` fires on a mod's `$.settings.read` call and on Claude Code's own merge of the session's settings (first after session mods load, again when settings or loaded plugins change).

| Field | What it holds |
| :- | :- |
| `e.layers` | array of `{ source, settings }`, lowest precedence first: `plugin`, `user`, `project`, `local`, `flag`, `policy`. Empty in `claude plugin test`. |
| `e.source` | the one source a mod asked for (e.g. `$.settings.read({ source: 'policy' })`); absent on Claude Code's own read and merged reads |

`plugin` is a layer name only, not a `source` you can pass. `flag` is `--settings`; `policy` is managed settings.

# How to use it

Tell reads apart with `next.origin`: Claude Code's own read is `{ plugin: 'engine', tier: 'core' }`; a mod's read has the calling mod's name as `plugin`.

Returns: `next(e)` unchanged; `{ value }` (own read: replaces each changed key's whole value if it fits the key's schema; mod read: that call resolves to your `value`); `{ deny: reason }` (own read: settings stay as merged before any hook answered, reason in debug log; mod read: call rejects with `<calling mod>: $.settings.read: <reason>`). `next(e)` resolves to `{ value }` or `{ deny }`. Build `{ value }` from `next(e)`'s value (omitted keys are unset). Keys Claude Code reads from each source separately, such as `env`, are unaffected.

# Limits and defaults

- Claude Code's own read firing and `e.layers` require v2.1.304 or later.
- Where the built-in guard loads, it can skip this hook in a mod you install or load with `--plugin-dir`; search the debug log for `settings.read bypassed by cc-plugin-sec-default`.
- A value outside the key's schema leaves that key at the pre-hook merged value (debug log: `the answer for <key> is no value the key can hold`).
