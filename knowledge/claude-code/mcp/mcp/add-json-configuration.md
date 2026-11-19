---
type: "Feature"
title: "Add servers from JSON"
description: "claude mcp add-json adds a server from a JSON string, piped from stdin from v2.1.327."
resource: "https://code.claude.com/docs/en/mcp"
tags: [mcp, json, cli, scripting]
kind: "cli_flag"
maturity: "unlabelled"
since: "2.1.327"
surfaces: [cli]
requires: ""
identifiers:
  - "claude mcp add-json"
  - "-"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "mcp"
    resource: "https://code.claude.com/docs/en/mcp"
    title: "Connect Claude Code to tools via MCP"
stale_after: "2027-01-19T00:00:00Z"
---

# How to use it

```
claude mcp add-json <name> '<json>'
claude mcp add-json weather-api '{"type":"http","url":"https://api.weather.com/mcp","headers":{"Authorization":"Bearer token"}}'
claude mcp add-json local-weather '{"type":"stdio","command":"/path/to/weather-cli","args":["--api-key","abc123"],"env":{"CACHE_DIR":"/tmp"}}'
cat server.json | claude mcp add-json <name> -
```

Verify with `claude mcp get <name>`. Escape the JSON for your shell. Piping with `-` runs outside a Claude Code session and needs v2.1.327 or later. `--scope user` stores it in user config instead of the project. The JSON must match the MCP server configuration schema.
