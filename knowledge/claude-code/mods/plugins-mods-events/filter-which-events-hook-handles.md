---
type: "Feature"
title: "Matchers: filter which events a hook handles"
description: "The second argument to on() is a matcher object that limits a hook by event fields, with wildcards and a plugin field for other mods' UI."
resource: "https://code.claude.com/docs/en/plugins/mods/events"
tags: [mods, matcher, wildcard, hooks]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.323"
surfaces: [cli, desktop, ide]
requires: ""
identifiers:
  - "on('tool.call', { tool: 'Bash' }, hook)"
  - "'classic.*'"
  - "'*'"
  - "{ plugin: 'other-mod' }"
  - "{ plugin: '*' }"
  - "next.event"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-events"
    resource: "https://code.claude.com/docs/en/plugins/mods/events"
    title: "React to events with a mod"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A matcher is an object whose fields are compared with the event's fields; the hook runs only when every field matches. A field can be a value, an array of allowed values, or a regular expression.

# How to use it

- `on('tool.call', { tool: 'Bash' }, hook)` matches one value.
- `{ tool: ['Edit', 'Write'] }` matches any in the array.
- `{ tool: /^mcp__github__/ }` matches by pattern (all tools of one MCP server).
- Wildcard names: `'classic.*'` matches every settings hook event; `'*'` matches every event except telemetry events (those take their own name and a `{ to: 'collector' }` filter).
- Registering the same event twice with no matcher makes the module fail to load with `on("session.start") is registered twice without a matcher`. Register each event once per matcher.

Hooking other mods' drawings and controls: pass `{ plugin: 'other-mod' }` (name without marketplace) or `{ plugin: '*' }` for every mod. Without `plugin`, a hook on `ui.press`, `ui.input`, `ui.select` or `ui.focus` does not run for other mods' controls, and a `ui.render` hook skips their panes and above-prompt rows. A wildcard with no matcher (`on('*', hook)`, `on('ui.*', hook)`) still runs for every mod; a wildcard with a matcher needs `plugin` too.

# Limits and defaults

`{ plugin: '*' }` requires Claude Code v2.1.323 or later. Before that, a hook with no `plugin` ran for every mod and `{ plugin: '*' }` did not run. Cross-version options: `{ plugin: /./ }` on `ui.press`, `ui.input`, `ui.select`; for `ui.focus` and `ui.render` use `on('ui.*', hook)` and check `next.event`.
