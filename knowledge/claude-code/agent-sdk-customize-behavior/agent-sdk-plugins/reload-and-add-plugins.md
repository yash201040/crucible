---
type: "Feature"
title: "Reload and add plugins in a running session"
description: "Apply plugin changes or add plugin folders to a live SDK session with reloadPlugins() (TypeScript) or /reload-plugins (Python)."
resource: "https://code.claude.com/docs/en/agent-sdk/plugins"
tags: [plugins, reload, running-session, typescript]
kind: "api"
maturity: "unlabelled"
since: "0.3.301"
surfaces: [sdk]
requires: "TypeScript Agent SDK v0.3.301 or later for addPlugins"
identifiers:
  - "reloadPlugins()"
  - "addPlugins"
  - "/reload-plugins"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-plugins"
    resource: "https://code.claude.com/docs/en/agent-sdk/plugins"
    title: "Plugins in the SDK"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Ways to change which plugins (and their skills, commands, agents, hooks) are active without starting a new session.

# How to use it

| Need | TypeScript | Python |
| --- | --- | --- |
| Pick up edits to a plugin's skills, commands, agents or hooks | `reloadPlugins()` on the `Query` object that `query()` returned | No method; send `/reload-plugins` as a prompt in the session |
| Add plugin folders to a running session | `q.reloadPlugins({ addPlugins: [{ type: "local", path: "/abs/path" }] })` | Not described |

- Each `addPlugins` entry is a `{ type: "local", path }` object with an absolute `path`.
- The result has a `plugins` array; `result.plugins.map((p) => p.path)` lists every plugin in the session. If the added path is missing, or the call rejects, the TypeScript reference page has a troubleshooting section for it.

# Limits and defaults

`addPlugins` requires TypeScript Agent SDK v0.3.301 or later. The Python SDK has no equivalent method.
