---
type: "Guide"
title: "Convert another client's setup instructions"
description: "How to turn a URL, launch command or mcpServers JSON block written for Claude Desktop or Cursor into a claude mcp command."
resource: "https://code.claude.com/docs/en/mcp"
tags: [mcp, setup, json, migration]
kind: "cli_flag"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "claude mcp add-json"
  - "--scope project"
  - "--scope user"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "mcp"
    resource: "https://code.claude.com/docs/en/mcp"
    title: "Connect Claude Code to tools via MCP"
stale_after: "2027-01-19T00:00:00Z"
---

# How to use it

| Input found | Meaning | Command shape |
|---|---|---|
| `https://` URL | remote HTTP | `claude mcp add --transport http example https://mcp.example.com/mcp` (add `--header` for a token) |
| `wss://` URL | WebSocket | use [WebSocket](./add-websocket-server.md); `--transport` rejects `ws` |
| `npx`/`uvx`/binary command | local stdio | `claude mcp add example --env API_KEY=your-key -- npx -y @example/mcp-server` (env before `--`) |
| `mcpServers` JSON block | settings for another client | `claude mcp add-json example '{"command":"npx","args":["-y","@example/mcp-server"]}'` (pass the inner object, not the wrapper) |

Two repairs before `add-json`: a `url` with no `type` needs `"type": "http"`, `"sse"` or `"ws"`; server names may use only letters, numbers, hyphens and underscores. Each command writes to local scope unless `--scope project` or `--scope user` is given. `claude mcp get <name>` checks the result.
