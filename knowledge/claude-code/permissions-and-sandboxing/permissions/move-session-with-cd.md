---
type: "Feature"
title: "Move the session with /cd"
description: "/cd changes the primary working directory, keeps the conversation and applies the new directory's project configuration at once."
resource: "https://code.claude.com/docs/en/permissions"
tags: [permissions, cd, working-directories, sessions]
kind: "slash_command"
maturity: "unlabelled"
since: "2.1.246"
surfaces: [cli]
requires: ""
identifiers:
  - "/cd"
  - "--resume"
  - "${CLAUDE_PROJECT_DIR}"
  - ".mcp.json"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permissions"
    resource: "https://code.claude.com/docs/en/permissions"
    title: "Configure permissions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`/cd <path>` moves the primary working directory (instead of adding one alongside). Claude Code keeps the conversation, loads the new directory's `CLAUDE.md`, and prompts to trust the workspace if new. `--resume` from the new directory finds the moved session. Restrict targets with `Cd` rules (see [Agent and Cd rules](./agent-and-cd-rules.md)).

# How to use it

On moving, Claude Code applies immediately:
- the new directory's project settings, including permission rules and hooks;
- its `.mcp.json` servers (same approval as at startup) and local-scope MCP servers registered there;
- plugins its settings enable, its skills and subagents;
- its `env` values, layered on top of the previous directory's (which stay).

It disconnects the previous directory's project and local-scope MCP servers and servers of plugins no longer enabled. Additional directories come from the new directory's settings, keeping those added with `--add-dir` or `/add-dir`. Hooks activated by the move still get `${CLAUDE_PROJECT_DIR}` set to the project root where the session started.

# Notes

For an untrusted directory the trust prompt lists the allow rules, additional directories, hooks and helper commands the settings would activate; declining leaves the session where it was. Before v2.1.246 `/cd` did not apply the new directory's settings, hooks, MCP servers or skills until resume, and the prompt did not list them.
