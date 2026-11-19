---
type: "Feature"
title: "Add an MCP server to an SDK session"
description: "Configure MCP servers in the mcpServers option of query() or in a project .mcp.json file."
resource: "https://code.claude.com/docs/en/agent-sdk/mcp"
tags: [mcp, mcpservers, config, mcp-json]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "mcpServers"
  - "mcp_servers"
  - ".mcp.json"
  - "settingSources"
  - "allowedTools"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-mcp"
    resource: "https://code.claude.com/docs/en/agent-sdk/mcp"
    title: "Connect to external tools with MCP"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

MCP (Model Context Protocol) servers give the agent external tools without writing custom tool code. They can run as local processes, over HTTP, or in-process within your SDK app.

# How to use it

- In code: `mcpServers: { name: { command, args } }` (stdio) or `{ type: "http", url }`, plus `allowedTools: ["mcp__name__*"]`.
- From a file: a `.mcp.json` at the project root with `{"mcpServers": {...}}`. It is read when the `project` setting source is enabled (the default for `query()`); if you set `settingSources` explicitly, include `"project"`.
- Quickstart server: the Claude Code docs MCP server at `https://code.claude.com/docs/mcp` over `type: "http"`.

# Notes

This page covers SDK configuration; adding servers to the CLI for every project is under MCP installation scopes in the Claude Code MCP docs. See [permissions and naming](./allow-mcp-tools-and-naming.md), [transports](./mcp-transport-types.md).
