---
type: "Concept"
title: "The order mods run in"
description: "Hooks on one event form one chain ordered by origin: guard and prepend mods, installed mods, appendPlugins, then other built-ins; settings PreToolUse hooks sit at fixed points."
resource: "https://code.claude.com/docs/en/plugins/mods/events"
tags: [mods, ordering, prependplugins, pretooluse]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop, ide]
requires: ""
identifiers:
  - "prependPlugins"
  - "appendPlugins"
  - "sec-default@builtin"
  - "cc-plugin-sec-default"
  - "dependencies"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-events"
    resource: "https://code.claude.com/docs/en/plugins/mods/events"
    title: "React to events with a mod"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The first mod in the chain is outermost: it sees the event first and the result last, and decides whether later mods run. A later mod cannot stop an earlier one seeing an event.

Order:
1. The built-in guard `sec-default@builtin` (listed as `cc-plugin-sec-default`) where it loads, mods in `prependPlugins`, then any other mod counting as the organization's and not in `appendPlugins`
2. Mods you install
3. Mods in `appendPlugins`
4. Other built-in mods

Among installed mods, a mod runs before the mods it lists under `dependencies` in its manifest. Within one module, hooks run in the order `register` called `on`.

# Notes

Settings `PreToolUse` hooks: from managed settings they run before the first mod's `tool.call` hook (a managed block means no mod hook runs). From every other settings file and plugins' `hooks/hooks.json` they run after the last mod calls `next`, as part of Claude Code's behavior; a mod that answers `tool.call` without `next` keeps them from running. `tool.check` fires after `PreToolUse` hooks.
