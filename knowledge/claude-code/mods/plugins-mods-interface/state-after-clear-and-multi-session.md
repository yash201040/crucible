---
type: "Concept"
title: "Reload saved state after /clear and share the store across sessions"
description: "$.state resets on /clear, /resume and /branch, so reload from $.store via classic.SessionStart; sessions share one non-atomic $.store."
resource: "https://code.claude.com/docs/en/plugins/mods/interface"
tags: [mods, state, clear, race-condition]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "classic.SessionStart"
  - "e.source"
  - "session.start"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-interface"
    resource: "https://code.claude.com/docs/en/plugins/mods/interface"
    title: "Draw in the interface with a mod"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`/clear`, `/resume` and `/branch` reset every `$.state` value to its default, and `session.start` does not fire again. `classic.SessionStart` does fire after each, with `e.source` of `clear`, `resume` or `fork` (also at startup and after compaction, which does not reset `$.state`). Use `on('classic.SessionStart', { source: ['clear', 'resume', 'fork'] }, ...)` to copy the saved value from `$.store` into `$.state` again; otherwise drawing shows the default and a save callback overwrites the stored value with the default. `session.start` also fires on every module reload, so save on every change.

# Notes

Every session on the machine running the mod shares one `$.store`; get-then-set is not atomic, so concurrent sessions race and the second write wins. Mitigate: one key per item; re-`get` right before writing, building the new value from that read. A write between your `get` and `set` is still lost.
