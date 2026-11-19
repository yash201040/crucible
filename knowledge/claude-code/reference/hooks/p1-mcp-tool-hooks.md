---
type: "Feature"
title: "MCP tool hooks"
description: "Hook handler type mcp_tool that calls a tool on a configured MCP server, with timing and availability limits."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, mcp, handler, limits]
kind: "frontmatter"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: "A configured MCP server"
identifiers:
  - "mcp_tool"
  - "server"
  - "tool"
  - "input"
  - "MCP_TIMEOUT"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`type: "mcp_tool"` calls a tool on a configured MCP server. Its text content is read like command-hook stdout (the exit-code-0 parsing rule).

# How to use it

| Field | Required | Description |
| :- | :- | :- |
| `server` | yes | Configured server name; for a plugin-bundled server use `plugin:<plugin-name>:<server-name>`, e.g. `plugin:my-plugin:db` |
| `tool` | yes | Tool name on that server |
| `input` | no | Arguments; string values support `${path}` substitution from the hook's JSON input, e.g. `"${tool_input.file_path}"` |

Example: `PostToolUse`, matcher `Write|Edit`, `{"type":"mcp_tool","server":"my_server","tool":"security_scan","input":{"file_path":"${tool_input.file_path}"}}`.

# Limits and defaults

- If the tool returns `isError: true`, the hook produces a non-blocking error.
- If the tool's answer is too large (message too large, or result without text), the hook gives no verdict: on `PreToolUse` Claude Code refuses the tool call; on other events (`UserPromptSubmit`, `PostToolUse`, `Stop`) the error is non-blocking. Return less data.
- On events that can block or change results (`PreToolUse`, `Stop`), Claude Code waits for a connecting server, at most `MCP_TIMEOUT` and within the hook `timeout`. On observational events (`Notification`, `SessionEnd`) it does not wait.
- A server in `cached` status connects when the hook calls it; if still not connected, a non-blocking error. The hook never starts OAuth; authenticate from `/mcp` first.
- `SessionStart` at launch (including `--continue`/`--resume`) and every `Setup` event fire before MCP servers are available: their `mcp_tool` hooks are skipped (debug log: `mcp_tool hooks are not available for the 'SessionStart' hook event (no MCP client context)`). `SessionStart` after `/clear` or compaction does run them. Use a `command` hook for launch-time needs.
