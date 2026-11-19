---
type: "Feature"
title: "Register, call and scope custom tools"
description: "Pass the server via mcpServers, pre-approve mcp__server__tool names in allowedTools, and control built-in availability with tools and disallowedTools."
resource: "https://code.claude.com/docs/en/agent-sdk/custom-tools"
tags: [custom-tools, allowedtools, permissions, tool-names]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "mcpServers"
  - "mcp_servers"
  - "allowedTools"
  - "allowed_tools"
  - "disallowedTools"
  - "disallowed_tools"
  - "tools"
  - "mcp__{server_name}__{tool_name}"
  - "mcp__weather__*"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-custom-tools"
    resource: "https://code.claude.com/docs/en/agent-sdk/custom-tools"
    title: "Give Claude custom tools"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Two steps make a custom tool callable: pass the MCP server to `query` in `mcpServers`, then list the tool's fully qualified name in `allowedTools` to pre-approve it.

# How to use it

- Name convention `mcp__{server_name}__{tool_name}`, where `{server_name}` is the key in `mcpServers`; characters like `.` or spaces become `_`. A wildcard `mcp__weather__*` covers every tool on a server.
- Two layers are controlled with `tools`, `allowedTools`, `disallowedTools`:

| Option | Layer | Effect |
| --- | --- | --- |
| `tools: ["Read", "Grep"]` | Availability | Only listed built-ins in context; unlisted built-ins removed; MCP tools unaffected |
| `tools: []` | Availability | All built-ins removed; only your MCP tools |
| allowed tools | Permission | Listed tools pre-approved (except calls no allow rule approves); others go through the permission flow |
| disallowed tools | Both | Bare name such as `"Bash"` removes the tool from context; scoped rule such as `"Bash(rm *)"` keeps it but denies matching calls |

# Notes

Tool search is on by default and defers SDK MCP tools; see [tool search](../agent-sdk-tool-search/how-tool-search-works.md). In TypeScript, `alwaysLoad: true` in the `extras` argument of `tool()` or the options of `createSdkMcpServer()` keeps a tool's full schema in the initial prompt. With tool search off every tool in the array uses context on every turn.
