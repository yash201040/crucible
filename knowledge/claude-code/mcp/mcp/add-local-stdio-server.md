---
type: "Feature"
title: "Add a local stdio server"
description: "Run a local process as an MCP server: the -- separator, --env, CLAUDE_PROJECT_DIR, roots/list and shutdown signals."
resource: "https://code.claude.com/docs/en/mcp"
tags: [mcp, stdio, env, shutdown]
kind: "cli_flag"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "claude mcp add"
  - "--"
  - "--env"
  - "-e"
  - "--transport stdio"
  - "CLAUDE_PROJECT_DIR"
  - "roots/list"
  - "notifications/roots/list_changed"
  - "--add-dir"
  - "/add-dir"
  - "additionalDirectories"
  - "SIGINT"
  - "SIGTERM"
  - "SIGKILL"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "mcp"
    resource: "https://code.claude.com/docs/en/mcp"
    title: "Connect Claude Code to tools via MCP"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Stdio servers run as local processes, for tools needing direct system access or custom scripts.

# How to use it

```
claude mcp add [options] <name> -- <command> [args...]
claude mcp add --env AIRTABLE_API_KEY=YOUR_KEY --transport stdio airtable -- npx -y airtable-mcp-server
```

- `--` separates Claude's own options (`--transport`, `--env`, `--scope`) from the server command; everything after it is passed untouched.
- `--env` takes multiple `KEY=value` pairs. If the server name directly follows `--env`, it is read as another pair and rejected, so put another option (e.g. `--transport stdio`) between them.
- Claude Code sets `CLAUDE_PROJECT_DIR` (project root, same as hooks get) in the server's environment. It does not change when working directories are added mid-session. To reference it with `${VAR}` expansion in `command`/`args` of `.mcp.json` or a local/user entry, use a default: `${CLAUDE_PROJECT_DIR:-.}`. Plugin-provided configs substitute `${CLAUDE_PROJECT_DIR}` directly.
- For allowed-directory logic, implement MCP `roots/list`: Claude Code answers with the launch directory plus every additional working directory (`--add-dir`, `/add-dir`, `additionalDirectories`) and sends `notifications/roots/list_changed` when the set changes.

# Limits and defaults

Shutdown when a stdio server is disconnected (for example at session end):

| Platform | Sequence |
|---|---|
| macOS and Linux | `SIGINT`, then `SIGTERM` after 100 ms if still running, then `SIGKILL` after a further 400 ms |
| Windows | close stdin, then end the process tree if still running after 300 ms |

Before v2.1.296 Windows ended the process tree at once.
