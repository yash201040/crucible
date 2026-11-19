---
type: "Feature"
title: "Matching MCP tools and Monitor commands"
description: "How to write matchers for MCP server tools (including plugin-scoped names) and how Bash matchers interact with the Monitor tool."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, mcp, monitor, matcher]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.314"
surfaces: [cli]
requires: "Claude Code v2.1.314 or later for Monitor matching"
identifiers:
  - "mcp__<server>__<tool>"
  - "mcp__memory__.*"
  - "mcp__plugin_<plugin-name>_<server-name>__<tool>"
  - "Monitor"
  - "Bash|Monitor"
  - "Monitor(tail *)"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

MCP tools appear as ordinary tools in `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `PermissionRequest` and `PermissionDenied`, named `mcp__<server>__<tool>`. Monitor-tool shell commands are also matched by `Bash` matchers on some events.

# How to use it

MCP:
- Match a whole server by appending `.*`: `mcp__memory__.*`, `mcp__brave-search__.*`. `mcp__memory` alone is an exact string and matches no tool.
- `mcp__.*__write.*` matches tools starting `write` from any server.
- Plugin-bundled MCP servers use `mcp__plugin_<plugin-name>_<server-name>__<tool>`, for example `mcp__plugin_my-plugin_db__query`; a matcher on the bare server key never fires. Use the same scoped name in `if`.

Monitor (requires v2.1.314+):
- A `PreToolUse` or `PermissionRequest` hook with a `Bash` matcher (including `Bash|PowerShell`, `^Bash$`, `Bash.*`) also runs for shell commands started by the Monitor tool, but its `allow` and `updatedInput` have no effect on them. It can deny, or make Claude Code ask.
- A matcher including Monitor (`Bash|Monitor`, `.*`, or none) gets the Monitor call's own input and `allow`/`updatedInput` apply. In `if`, name Monitor, e.g. `Monitor(tail *)`. If `if` names Bash, the hook still gets Monitor input but allow/updatedInput have no effect.
- With a plain `Bash` matcher and `if` naming Monitor, the hook does not run.

# Limits and defaults

A `Bash`-matcher hook does not run for a WebSocket watch, and a `PostToolUse` hook with a Bash matcher does not run for Monitor.
