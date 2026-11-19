---
type: "Concept"
title: "Tool availability and servers still connecting"
description: "How Claude waits for tools of a server still connecting, WaitForMcpServers, the 10-second hold after resume, and cloud tool counts."
resource: "https://code.claude.com/docs/en/mcp"
tags: [mcp, tools, startup, resume]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, cloud]
requires: ""
identifiers:
  - "WaitForMcpServers"
  - "ToolSearch"
  - "ENABLE_TOOL_SEARCH=false"
  - "No such tool available"
  - "_meta.ui.visibility"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "mcp"
    resource: "https://code.claude.com/docs/en/mcp"
    title: "Connect Claude Code to tools via MCP"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The `/mcp` panel shows a tool count per connected server and flags servers that advertise the tools capability but expose none.

# How to use it

If a request needs tools from a server still connecting in the background, Claude waits:
- With [tool search](./mcp-tool-search.md) (default): the wait happens inside the `ToolSearch` call.
- Without tool search (`ENABLE_TOOL_SEARCH=false`, or a model earlier than Opus 4.5, Sonnet 4.5, Haiku 4.5 on Google Cloud's Agent Platform): Claude uses the `WaitForMcpServers` tool.
- Microsoft Foundry deployments hosted on Azure start on the tool-search path; after the switch to upfront loading, tools from a server that finishes connecting become available on Claude's next request.

With tool search, a server that finishes connecting mid-turn has its tool names listed to Claude on the next request in the same turn.

# Limits and defaults

- After resuming a session, a call to a saved-conversation tool whose server is on its first connection attempt is held up to 10 seconds. If it is not connected in time, or is already retrying, the call fails with `No such tool available`.
- Cloud session `3 of 13 tools available` means a repo `.claude/settings.json` deny rule, a full tool name over 128 characters, or a server that lists the tool for its own UI only. Server authors give Claude the tool by adding `model` to `_meta.ui.visibility`.
