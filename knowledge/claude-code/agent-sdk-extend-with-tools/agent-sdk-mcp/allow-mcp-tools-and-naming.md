---
type: "Feature"
title: "MCP tool permissions and naming"
description: "MCP tools need explicit permission; names are mcp__server__tool and allowedTools wildcards approve a whole server."
resource: "https://code.claude.com/docs/en/agent-sdk/mcp"
tags: [mcp, permissions, allowedtools, tool-names]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "mcp__<server-name>__<tool-name>"
  - "mcp__github__*"
  - "allowedTools"
  - "allowed_tools"
  - "permissionMode"
  - "acceptEdits"
  - "bypassPermissions"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-mcp"
    resource: "https://code.claude.com/docs/en/agent-sdk/mcp"
    title: "Connect to external tools with MCP"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Without permission Claude sees MCP tools but cannot call them. Tools are named `mcp__<server-name>__<tool-name>`; characters such as `.` and spaces in the server name become `_` (key `my.server` gives `mcp__my_server__list_issues`). For a plugin-provided server the server name takes the plugin-scoped form and starts with `plugin_`.

# How to use it

Auto-approve with `allowedTools`: `"mcp__github__*"` (whole server), `"mcp__db__query"` (one tool), `"mcp__slack__send_message"`. Use the same full names in MCP permission rules.

Prefer `allowedTools` over permission modes for MCP access: `permissionMode: "acceptEdits"` does not auto-approve MCP tools (only file edits and filesystem Bash commands); `"bypassPermissions"` does, but disables most other safety prompts.

# Notes

Discover tools by inspecting the `tools` array of the `system` init message (names start with `mcp__`). It lists tools of servers connected by the first-turn wait plus servers with a cached tool list; other unconnected servers' tools are absent. You can also ask Claude to list a server's tools.
