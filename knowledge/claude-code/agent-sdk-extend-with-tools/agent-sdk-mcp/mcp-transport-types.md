---
type: "Reference"
title: "MCP transport types in the SDK"
description: "stdio, HTTP, SSE and in-process SDK servers, and which config fields each takes."
resource: "https://code.claude.com/docs/en/agent-sdk/mcp"
tags: [mcp, transports, stdio, http, sse]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "command"
  - "args"
  - "env"
  - "type: \"http\""
  - "type: \"sse\""
  - "streamable-http"
  - "url"
  - "headers"
  - "McpHttpServerConfig"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-mcp"
    resource: "https://code.claude.com/docs/en/agent-sdk/mcp"
    title: "Connect to external tools with MCP"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

How to pick a transport: docs give a command to run, use stdio; docs give a URL, use HTTP or SSE; building your own tools in code, use an SDK MCP server.

# How to use it

| Transport | Config | Use |
| --- | --- | --- |
| stdio | `command`, `args`, optional `env` | Local processes over stdin/stdout |
| SSE | `type: "sse"`, `url`, optional `headers` | Cloud-hosted servers |
| HTTP (streamable) | `type: "http"`, `url`, optional `headers` | Cloud-hosted servers and remote APIs |
| SDK server | `createSdkMcpServer` | In-process; see the custom tools guide |

# Notes

In `.mcp.json` and other JSON config files `"streamable-http"` is accepted as an alias for `"http"`; the SDKs' `McpHttpServerConfig` type declares only `"http"`, so use `"http"` for servers passed in code.
