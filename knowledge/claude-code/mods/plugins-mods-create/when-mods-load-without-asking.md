---
type: "Limit"
title: "When Claude-written mods load or cannot load"
description: "auto and bypassPermissions load mods without asking; dontAsk, untrusted workspaces, --safe-mode, --bare and disableAllHooks prevent loading."
resource: "https://code.claude.com/docs/en/plugins/mods/create"
tags: [mods, permissions, headless, safe-mode]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless]
requires: ""
identifiers:
  - "auto"
  - "bypassPermissions"
  - "default"
  - "acceptEdits"
  - "dontAsk"
  - "--safe-mode"
  - "--bare"
  - "disableAllHooks"
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

Rules for whether a mod that Claude writes in a session loads.

# Limits and defaults

- Loads without asking: `auto` and `bypassPermissions` modes enable hot reloading without a question and load at end of turn. Resuming a session (interactive or `claude -p`) can load mods already in its mods folder without asking; delete a mod's directory to prevent it.
- To be asked first: start a new session in `default` or `acceptEdits`, or switch to either before the session's first mod.
- Does not load, and Claude Code does not ask: `dontAsk` mode; a `claude -p` run in `default` or `acceptEdits` that writes the mod (cannot show the question); an interactive session in an untrusted workspace (trust prompt not accepted); mods disabled by `--safe-mode`, `--bare`, the `disableAllHooks` setting, or managed settings.
