---
type: "Guide"
title: "Other surfaces and connection troubleshooting"
description: "Where MCP servers are added on other surfaces, and fixes for missing servers, failed connections, timeouts and duplicates."
resource: "https://code.claude.com/docs/en/mcp-quickstart"
tags: [mcp, troubleshooting, timeout, surfaces]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.219"
surfaces: [cli, desktop, ide, web, cloud]
requires: ""
identifiers:
  - "MCP_TIMEOUT"
  - "claude mcp add-from-claude-desktop"
  - "claude mcp reset-project-choices"
  - "--env"
  - "disabledMcpServers"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "mcp-quickstart"
    resource: "https://code.claude.com/docs/en/mcp-quickstart"
    title: "Connect to MCP servers"
stale_after: "2027-01-19T00:00:00Z"
---

# How to use it

Other surfaces: desktop app via the Connectors UI; Claude Desktop chat app servers copied with `claude mcp add-from-claude-desktop` (macOS or WSL); VS Code; cloud sessions load a committed `.mcp.json` when a session has one repository (threads in a project use claude.ai connectors); connectors added at claude.ai/customize/connectors load in the CLI when signed in with that account.

Troubleshooting:
- `/mcp` shows No MCP servers: local-scoped servers are tied to the project where added (repo root, or exact directory when not a git repo), so re-add there or use `--scope user`; wrong file path; or a malformed `.mcp.json` entry, which is skipped while others load (see the parse warning in `claude mcp list`).
- `Failed to connect` / `Connection error`: also appears for HTTP servers rejecting a `headers.Authorization` token. Detail on `Failed to connect` shown from v2.1.219 (before, bare status); `Connection error` never carries detail. A 404 shows `MCP endpoint not found at <origin>. Check the URL in your MCP config.` (path omitted from v2.1.219; before v2.1.191 a generic `Error POSTing to endpoint`). Check reachability with `curl -I <url>` (PowerShell `curl.exe`): `404`/`405` means up, `401`/`403` means authenticate, no response means URL or network. For stdio, run the command in a terminal; if it works but `claude mcp get <name>` shows a different command you likely omitted `--`. Before v2.1.285 `claude mcp get` printed no `Command` line for a stdio entry without `type`; use `claude mcp list`.
- Startup timeout: default 30 seconds; raise with `MCP_TIMEOUT=60000 claude` (PowerShell `$env:MCP_TIMEOUT = "60000"; claude`). Before v2.1.299 some connections to up HTTP servers timed out regardless of `MCP_TIMEOUT`.
- Server already exists: remove it or rename; `exists in multiple scopes` needs `--scope`.
- No tools appear: usually a missing env var; pass `--env KEY=value` or the `env` field. Before v2.1.302 `/mcp` showed `tools fetch failed` for a protocol revision 2026-07-28 server that omitted `resultType`, `ttlMs` or `cacheScope`.
- `.mcp.json` changes need a session restart; reset rejected approvals with `claude mcp reset-project-choices`.
- OAuth sign-in fails: re-run Authenticate in `/mcp` or open the printed URL manually.
