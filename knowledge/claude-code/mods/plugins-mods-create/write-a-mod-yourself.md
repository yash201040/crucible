---
type: "Guide"
title: "Write a mod yourself"
description: "Three files (plugin.json, hooks/hooks.json with a modules key, register.js) make a mod; load with --plugin-dir and edits hot-reload."
resource: "https://code.claude.com/docs/en/plugins/mods/create"
tags: [mods, tutorial, hooks-module, hot-reload]
kind: "file"
maturity: "unlabelled"
since: "2.1.287"
surfaces: [cli, headless]
requires: ""
identifiers:
  - "modules"
  - "hooks/hooks.json"
  - "hooks/register.js"
  - "register(on)"
  - "on('session.start')"
  - "on('tool.call')"
  - "on('command.run', { command })"
  - "on('ui.render', { component: 'Spinner' })"
  - "$.command.register"
  - "$.ui.invalidate"
  - "claude --plugin-dir"
  - "claude -p"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-create"
    resource: "https://code.claude.com/docs/en/plugins/mods/create"
    title: "Create a mod"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Tutorial mod `first-mod` counts tool calls, shows the count beside the spinner, and adds `/tally`. Files: `.claude-plugin/plugin.json` (ordinary manifest), `hooks/hooks.json` with `"modules": ["./register.js"]` (one path relative to `hooks.json`; having `modules` is what makes the plugin a mod), and `hooks/register.js` exporting `register(on)`.

# How to use it

`register(on)` is called once on load; each `on(event, [matcher], hook)` registers a hook. The tutorial's four hooks:
- `session.start`: runs before first prompt and on each reload; registers `/tally`; returns `next(e)`.
- `tool.call`: runs before each tool use; increments a counter, calls `$.ui.invalidate('ui.render')`, returns `next(e)`.
- `command.run` with matcher `{ command: 'tally' }`: returns `{ text }`, never calls `next`.
- `ui.render` with `{ component: 'Spinner' }`: returns `next({ ...e, props: { ...e.props, suffix: '...' } })`.

Load with `claude --plugin-dir ./first-mod`. Check non-interactively: `claude -p "/tally" --plugin-dir ./first-mod` prints `first-mod: Claude has made 0 tool calls since this mod loaded`. Claude Code watches a `--plugin-dir` directory and hot-reloads the hooks module on file change; each reload reruns `register`, so module variables reset (see Keep state in the interface docs).

# Notes

Each hook gets three arguments: `$` (the mods API, namespaces such as `$.ui`, `$.command`), `e` (event input as plain data), `next` (passes the event to other mods then Claude Code's own behavior and returns the result). Hooks observe (call `next(e)`), answer (return a result without `next`; a matcher filters events), or rewrite (call `next` with a changed copy of `e`).
