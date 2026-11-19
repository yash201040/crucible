---
type: "Feature"
title: "Disable a server without removing it"
description: "Per-project toggles in ~/.claude.json: disabledMcpServers opt-out list and enabledMcpServers opt-in list."
resource: "https://code.claude.com/docs/en/mcp"
tags: [mcp, disable, per-project, config]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "disabledMcpServers"
  - "enabledMcpServers"
  - "claude.ai Slack"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "mcp"
    resource: "https://code.claude.com/docs/en/mcp"
    title: "Connect Claude Code to tools via MCP"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Toggling a server off in `/mcp` stops connecting without losing its configuration. The choice is stored per project in `~/.claude.json` in one of two disjoint lists.

# How to use it

| List | Covers |
|---|---|
| `disabledMcpServers` | opt-out list: user-configured servers, plugin servers, managed-settings servers, claude.ai connectors fetched by Claude Code (stored by display name such as `claude.ai Slack`), built-in servers that default to on |
| `enabledMcpServers` | opt-in list for built-in servers default-off, such as `computer-use` |

# Notes

Each server consults exactly one list; a regular server in `enabledMcpServers`, or a default-off built-in in `disabledMcpServers`, is ignored. Both are unrelated to `enabledMcpjsonServers` / `disabledMcpjsonServers`, which approve `.mcp.json` servers.
