---
type: "Limit"
title: "MCP tool schema and name limits"
description: "Invalid tool input schemas and MCP tool names over 128 characters, and how Claude Code excludes or retries them."
resource: "https://code.claude.com/docs/en/errors"
tags: [errors, mcp, tools, limits, schema]
kind: "limit"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "input_schema"
  - "mcp__<server>__<tool>"
  - "claude --debug"
  - "claude update"
  - "~/.claude/debug/<session-id>.txt"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "errors"
    resource: "https://code.claude.com/docs/en/errors"
    title: "Error reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Limits the API enforces on tool definitions, which affect any MCP-heavy agent.

# How to use it

- **Tool input schema is invalid:** `API Error: 400 ... tools.N.custom.input_schema: JSON schema is invalid` (not valid JSON Schema draft 2020-12) or a property key not matching `^[a-zA-Z0-9_.-]{1,64}$`. `N` is the tool's position, not a name. Claude Code excludes invalid MCP tools when loading, but it can still happen when feature flags have not arrived (before v2.1.328 also with fetching off) or the schema declares another `$schema` dialect. Before v2.1.300 the request was not retried without the rejected tool's parameters; update with `claude update`. Server logs name the offending tool on v2.1.216+; otherwise disable servers one at a time.
- **MCP tool name over 128 characters:** the full name `mcp__<server>__<tool>` must be at most 128 characters; longer tools are left out of the request, other tools keep working. With `claude --debug` the debug log `~/.claude/debug/<session-id>.txt` records `Tool "..." is not sent to Claude: its name has <N> characters and the API accepts at most 128`. Shorten the server alias (renaming also requires updating permission rules and hook matchers). A plugin-bundled server's name includes the plugin name. Before v2.1.292 it was sent anyway and every request failed with 400.

# Notes

Related: [tool_use.name over 200 characters](./p2-request-gateway-history-errors.md).
