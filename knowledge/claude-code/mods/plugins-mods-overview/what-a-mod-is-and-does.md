---
type: "Concept"
title: "What a mod is and what it can do"
description: "A mod is a plugin of JavaScript/TypeScript event handlers that run inside Claude Code and can draw UI, rewrite events and add commands."
resource: "https://code.claude.com/docs/en/plugins/mods/overview"
tags: [mods, plugins, hooks, extensibility]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.287"
surfaces: [cli, desktop, ide]
requires: "Claude Code v2.1.287 or later in the terminal; Desktop v2.1.286"
identifiers:
  - "plugin.json"
  - "hooks/hooks.json"
  - "hooks/register.js"
  - "register"
  - "tool.call"
  - "ui.render"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-overview"
    resource: "https://code.claude.com/docs/en/plugins/mods/overview"
    title: "Mods overview"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A mod is a plugin whose JavaScript or TypeScript code registers event handlers ("hooks"). Claude Code runs a handler on an event (tool call, submitted prompt, interface part being drawn) and the handler can observe, rewrite or answer it. In these docs "hook" means a mod's handler; the settings-file kind (shell command, HTTP request, prompt) is a "settings hook".

A mod runs inside Claude Code, so it can: draw interfaces (pane beside the transcript, band above the prompt, tabs, buttons, fields); redraw Claude Code's own interface (tool rows, spinner, question dialog); step into a tool call or request (hold it to ask the user, answer without running the tool, send a request to a different model); run code on a `/command` immediately, with no Claude turn, even while Claude works; and share data between its hooks through shared file variables.

# How to use it

Smallest mod: `first-mod/.claude-plugin/plugin.json`, `first-mod/hooks/hooks.json` (points to the code file), `first-mod/hooks/register.js` (exports `register(on)`). Example: a `tool.call` hook increments `calls` and calls `$.ui.invalidate('ui.render')`; a `ui.render` hook with `{ component: 'Spinner' }` adds `' · tool calls: N…'` via `next({ ...e, props: { ...e.props, suffix } })`.

A hook can observe, rewrite or answer. To do anything outside its own code (draw, add a command, call a model, read a file, start a process, network) it must call the mods API; that is why Claude Code can list what a mod does before install.

# Notes

Mods work in the CLI, the Desktop Code tab and the VS Code extension. See [where mods run](./where-mods-run.md) for `claude -p`, SDK and cloud.
