---
type: "Guide"
title: "Add, verify and remove an MCP server"
description: "Quickstart walkthrough: claude mcp add, claude mcp list status table, using a server and removing it."
resource: "https://code.claude.com/docs/en/mcp-quickstart"
tags: [mcp, quickstart, status, cli]
kind: "cli_flag"
maturity: "unlabelled"
since: "2.1.219"
surfaces: [cli]
requires: ""
identifiers:
  - "claude mcp add --transport http claude-code-docs https://code.claude.com/docs/mcp"
  - "claude mcp list"
  - "claude mcp get <name>"
  - "claude mcp remove claude-code-docs"
  - "/mcp"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "mcp-quickstart"
    resource: "https://code.claude.com/docs/en/mcp-quickstart"
    title: "Connect to MCP servers"
stale_after: "2027-01-19T00:00:00Z"
---

# How to use it

1. In a terminal (not inside a `claude` session): `claude mcp add --transport http claude-code-docs https://code.claude.com/docs/mcp`. `--transport http` means a hosted URL; the name is free-form and labels the server's tools. Output: `Added HTTP MCP server claude-code-docs with URL: ... to local config` plus a `File modified:` line.
2. `claude mcp list` shows status:

| Status | Meaning |
|---|---|
| `✔ Connected` | ready |
| `! Connected · tools fetch failed` | connected but could not list tools; see `claude mcp get <name>` |
| `! Needs authentication` | needs browser sign-in or `--header` token |
| `✘ Failed to connect` | server did not respond |
| `✘ Connection error` | the attempt threw an error |
| `⏸ Pending approval (run claude to approve)` | unapproved project-scoped server |
| `⊘ Disabled for this project (re-enable via /mcp)` | in the project's `disabledMcpServers` |
| `✘ Blocked by enterprise managed policy` | org policy blocks it |

Legacy Windows consoles may show `√` and `×` in place of the glyphs.
3. Start `claude` and ask for the server by name; approve the first permission prompt; the tool call is labeled with the server name.
4. Optional: `claude mcp remove claude-code-docs` (prints `Removed MCP server "claude-code-docs" from local config`).

# Notes

Each connected server uses context window space (tool names and server instructions load every session), so remove unused ones. `claude mcp add` works the same in every shell; inside a session use `/mcp`.
