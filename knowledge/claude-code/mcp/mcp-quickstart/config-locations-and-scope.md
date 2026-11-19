---
type: "Reference"
title: "Where MCP config lives and changing scope"
description: "File locations for local, project and user scope, CLAUDE_CONFIG_DIR effect, and how to re-add a server at another scope."
resource: "https://code.claude.com/docs/en/mcp-quickstart"
tags: [mcp, scopes, config-files, quickstart]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "~/.claude.json"
  - ".mcp.json"
  - "--scope local"
  - "--scope user"
  - "--scope project"
  - "CLAUDE_CONFIG_DIR"
  - "claude mcp get claude-code-docs"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "mcp-quickstart"
    resource: "https://code.claude.com/docs/en/mcp-quickstart"
    title: "Connect to MCP servers"
stale_after: "2027-01-19T00:00:00Z"
---

# How to use it

| Scope | File | Available to |
|---|---|---|
| `local` | `~/.claude.json`, under this project's entry | only you, only this project (default) |
| `project` | `.mcp.json` in the project root | everyone who clones the project |
| `user` | `~/.claude.json`, top-level `mcpServers` key | only you, all projects |

On Windows `~/.claude.json` is `%USERPROFILE%\.claude.json`. If `CLAUDE_CONFIG_DIR` is set, `.claude.json` is read from inside that directory. `claude mcp get <name>` shows which scope holds a definition.

A server's scope is fixed at add time, so change it by removing and re-adding: `claude mcp remove claude-code-docs --scope local`, then `claude mcp add --scope user --transport http ...` (all projects) or `--scope project` (writes `.mcp.json`; commit it, and teammates get an approval prompt).

# Notes

Claude Code reads only `~/.claude.json` and `<project>/.mcp.json`; it does not read `~/.claude/.mcp.json`, `~/.claude/config/mcp.json`, `~/.claude/mcp.json` or `%APPDATA%\Claude\mcp.json`.
