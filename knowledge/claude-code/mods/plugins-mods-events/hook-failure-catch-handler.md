---
type: "Feature"
title: "Hook failures and the .catch handler"
description: "A failing hook is skipped by default; chain .catch on on() to fail closed, using next.called and next.error."
resource: "https://code.claude.com/docs/en/plugins/mods/events"
tags: [mods, error-handling, fail-closed, catch]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.326"
surfaces: [cli, desktop, ide]
requires: ""
identifiers:
  - "on(...).catch"
  - "next.called"
  - "next.error.kind"
  - "{ refuse: 'the reason' }"
  - "plugin.register"
  - "config.set"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-events"
    resource: "https://code.claude.com/docs/en/plugins/mods/events"
    title: "React to events with a mod"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A hook with no `.catch` that throws, times out or returns the wrong shape does not break the session. If it failed before calling `next`, Claude Code skips it and the next handler runs. If it failed after `next` resolved, that result stands and nothing runs twice. One line names the mod, event and reason, e.g. `my-mod: tool.call hook skipped: threw Error: boom`. A `ui.render` tree that does not validate counts as the wrong shape.

# How to use it

`on('tool.call', { tool: 'Bash' }, guard).catch(async ($, e, next) => { if (next.called) return next(e); return { deny: '...' + next.error.kind } })`. `next.error.kind` is `throw` or `timeout`.

- Before `next`: return the event's refusal: `{ drop }` for `prompt.submit`, `{ deny }` for `config.set`.
- After `next`, refusals returned still hold, so skip the `next.called` test: `tool.check` returns `{ decision: 'deny', reason }`; `plugin.register` returns `{ refuse: 'the reason' }`.
- At `tool.call`, a `deny` after `next` withholds the result from Claude.

# Limits and defaults

- The handler has its own shorter time limit (1 second); if the handler fails the hook is skipped as if it had no handler.
- `plugin.register` `{ refuse }` keeps the other mod's whole plugin out on v2.1.326 or later.
