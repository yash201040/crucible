---
type: "Reference"
title: "claude mcp management commands"
description: "Commands for listing, inspecting, removing and checking MCP servers from the shell or inside a session."
resource: "https://code.claude.com/docs/en/mcp"
tags: [mcp, cli, commands, oauth]
kind: "slash_command"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "claude mcp list"
  - "claude mcp get"
  - "claude mcp remove"
  - "claude mcp reset-project-choices"
  - "claude mcp login"
  - "claude mcp logout"
  - "claude mcp serve"
  - "claude mcp add-from-claude-desktop"
  - "/mcp"
  - "/mcp reconnect all"
  - "--scope"
  - "-s"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "mcp"
    resource: "https://code.claude.com/docs/en/mcp"
    title: "Connect Claude Code to tools via MCP"
stale_after: "2027-01-19T00:00:00Z"
---

# How to use it

| Command | What it does |
|---|---|
| `claude mcp list` | list servers with health status |
| `claude mcp get <name>` | details for one server |
| `claude mcp remove <name> [--scope <scope>]` | remove; also deletes stored OAuth tokens and client registration (not revoked at the auth server) |
| `claude mcp logout <name>` | clear stored credentials; run before `remove` to revoke where the auth server supports it |
| `claude mcp login <name>` | run OAuth from the shell |
| `claude mcp reset-project-choices` | reset approval choices for `.mcp.json` servers |
| `claude mcp serve` | run Claude Code as a stdio MCP server |
| `claude mcp add-from-claude-desktop` | import from Claude Desktop |
| `/mcp` (in session) | panel: status, tools, authenticate, reconnect, disable |
| `/mcp reconnect all` | retry every failed or needs-auth server; interactive only, needs v2.1.284 or later (earlier prints `MCP server "all" not found`) |

`-s`/`--scope` chooses where config is stored: `local` (default), `project`, `user`. A server's scope is fixed when added, so changing scope means removing and re-adding.

# Notes

`claude mcp add` that prints `was not saved` or `may not have been saved` points to the errors page. Adding does not validate credentials.
