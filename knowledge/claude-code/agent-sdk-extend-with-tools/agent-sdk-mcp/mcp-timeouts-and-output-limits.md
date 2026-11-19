---
type: "Limit"
title: "MCP timeouts, output limits and schema warnings"
description: "30-second connection timeout, MCP_TOOL_TIMEOUT, 25,000-token output cap, and the warning for SDK tools with unconvertible schemas."
resource: "https://code.claude.com/docs/en/agent-sdk/mcp"
tags: [mcp, timeouts, output-limits, tokens]
kind: "env_var"
maturity: "unlabelled"
since: "0.3.286"
surfaces: [sdk]
requires: ""
identifiers:
  - "MCP_TIMEOUT"
  - "MCP_TOOL_TIMEOUT"
  - "MAX_MCP_OUTPUT_TOKENS"
  - "anthropic/maxResultSizeChars"
  - "CLAUDE_SDK_MCP_TOOL_SCHEMA_UNCONVERTIBLE"
  - "timeout"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-mcp"
    resource: "https://code.claude.com/docs/en/agent-sdk/mcp"
    title: "Connect to external tools with MCP"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Time and size limits on MCP use in SDK sessions, the same as in Claude Code.

# How to use it

| Name | Default | Effect |
| --- | --- | --- |
| `MCP_TIMEOUT` | 30 seconds (value in ms) | Connection limit; a slower server fails to connect |
| `MCP_TOOL_TIMEOUT` | not stated | How long a running tool call may take |
| `timeout` in `createSdkMcpServer()` | not stated | TypeScript only: tool-call limit for a single SDK MCP server |
| `MAX_MCP_OUTPUT_TOKENS` | 25,000 tokens limit | A successful result with no image content over the limit is saved to a file, and the tool result becomes an error naming the path so the agent can read it in portions |
| `anthropic/maxResultSizeChars` | n/a | Annotation a tool declares; without it, a successful text result over 50,000 characters is saved to a file regardless of the token limit |

# Notes

TypeScript: when an input schema cannot be converted to JSON Schema, `createSdkMcpServer()` leaves that tool out and emits a warning (Node.js process warning code `CLAUDE_SDK_MCP_TOOL_SCHEMA_UNCONVERTIBLE`). Before TypeScript Agent SDK v0.3.286, one unconvertible schema made the whole listing fail silently, so none of that server's tools reached Claude.
