---
type: "Reference"
title: "How connectors reach sessions and org tool controls"
description: "Which sessions fetch connectors, what governs each, per-tool ask/blocked org controls, and disableClaudeAiConnectors."
resource: "https://code.claude.com/docs/en/mcp"
tags: [mcp, connectors, policy, permissions]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli, ide, sdk, cloud, desktop]
requires: ""
identifiers:
  - "disableClaudeAiConnectors"
  - "ENABLE_CLAUDEAI_MCP_SERVERS"
  - "allowAllClaudeAiMcps"
  - "allowedMcpServers"
  - "deniedMcpServers"
  - "managed-mcp.json"
  - "serverName"
  - "serverUrl"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "mcp"
    resource: "https://code.claude.com/docs/en/mcp"
    title: "Connect Claude Code to tools via MCP"
stale_after: "2027-01-19T00:00:00Z"
---

# How to use it

| Where the session runs | How connectors arrive | What governs them |
|---|---|---|
| Terminal, VS Code, JetBrains, Agent SDK | Claude Code fetches them from claude.ai | settings here and managed MCP configuration |
| Cloud sessions | cloud host passes them in | claude.ai org settings, plus allowlist/denylist settings reaching the session and any `managed-mcp.json` on the host |
| Desktop app local and SSH sessions | desktop app delivers in-process as `type: "sdk"` servers | `blocked` entries in org connector tool controls only |

`disableClaudeAiConnectors`, `ENABLE_CLAUDEAI_MCP_SERVERS` and `allowAllClaudeAiMcps` act only on the first row.

Disable connectors Claude Code fetches: `{"disableClaudeAiConnectors": true}` in any scope (any-source-true: a project `false` cannot re-enable a user or policy `true`; `--mcp-config` servers are unaffected), or `ENABLE_CLAUDEAI_MCP_SERVERS=false claude`. Block single connectors with `deniedMcpServers` by name (`serverName` `"claude.ai Slack"`) or URL pattern, or toggle per project in `/mcp`.

# Limits and defaults

- Cloud: `allowedMcpServers`/`deniedMcpServers` also filter delivered connectors; the session proxy rewrites connector URLs, so a `serverUrl` pattern for the original URL does not match. A `managed-mcp.json` on the host makes Claude Code drop delivered connectors, whether or not `allowAllClaudeAiMcps` is set.
- Org per-tool controls are read at startup and enforced locally (except desktop local/SSH, where blocked tools are withheld before delivery and `ask` falls back to ordinary permission rules):
  - `ask`: prompts on every call with the reason `Your organization requires approval for this tool`, even in `acceptEdits`, `auto`, `bypassPermissions`; choice cannot be saved in the terminal; allow rules do not skip it; in `dontAsk` mode or a `-p` run with nothing to answer, the call is denied.
  - `blocked`: filtered out before Claude sees it; `/mcp` still lists it marked `turned off by your organization`.
- The desktop app skips a connector whose tools are all blocked.
