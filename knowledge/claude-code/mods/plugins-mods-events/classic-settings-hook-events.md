---
type: "Feature"
title: "Settings hook events as classic.<Event>"
description: "Each settings hook event is also a mod event named classic.<Event>, receiving the same JSON a settings hook gets on stdin."
resource: "https://code.claude.com/docs/en/plugins/mods/events"
tags: [mods, hooks, classic, settings-hooks]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop, ide]
requires: ""
identifiers:
  - "classic.Stop"
  - "classic.SessionEnd"
  - "classic.PostToolUse"
  - "classic.SessionStart"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-events"
    resource: "https://code.claude.com/docs/en/plugins/mods/events"
    title: "React to events with a mod"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Settings hooks are the command, HTTP, prompt and agent hooks configured in settings files. Each settings hook event (`Stop`, `SessionEnd`, `PostToolUse`, ...) is also a mod event named `classic.` plus the event name. `e` is the JSON a settings hook receives on stdin, including `transcript_path`.

# How to use it

`on('classic.Stop', async ($, e, next) => { $.ui.log('Transcript saved at ' + e.transcript_path); return next(e) })`. Return `next(e)` so settings-file Stop hooks still run.

# Limits and defaults

Where the built-in guard loads, a hook on these events in a mod you install does not run (see the admin page, "hooks the guard passes over"). `'classic.*'` matches all of them.
