---
type: "Reference"
title: "MCP tool timeouts, backgrounding, output and tool search variables"
description: "Variables for MCP tool call timeouts, automatic backgrounding, output and description size limits, tool search, claude.ai connectors and OAuth."
resource: "https://code.claude.com/docs/en/env-vars"
tags: [mcp, timeouts, tool-search, output-limits]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "MCP_TOOL_TIMEOUT"
  - "CLAUDE_CODE_MCP_TOOL_IDLE_TIMEOUT"
  - "CLAUDE_CODE_MCP_AUTO_BACKGROUND_MS"
  - "CLAUDE_CODE_DISABLE_MCP_TASK_BACKGROUND"
  - "MAX_MCP_OUTPUT_TOKENS"
  - "CLAUDE_CODE_MAX_MCP_DESCRIPTION_LENGTH"
  - "ENABLE_TOOL_SEARCH"
  - "ENABLE_CLAUDEAI_MCP_SERVERS"
  - "MCP_CLIENT_SECRET"
  - "MCP_OAUTH_CALLBACK_PORT"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "env-vars"
    resource: "https://code.claude.com/docs/en/env-vars"
    title: "Environment variables"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Execution-time limits for MCP tool calls, size caps that protect context, and tool loading behavior.

# How to use it

| Variable | What it does |
| :- | :- |
| `MCP_TOOL_TIMEOUT` | Timeout for MCP tool execution (default 100000000 ms, about 28 hours). HTTP, SSE and claude.ai connector servers also time out each request after 60 s by default; set this or the per-server `timeout` above 60000 to raise that (a lower value shortens the overall timeout but leaves the per-request limit). Stdio and WebSocket servers have no per-request timer. Per-server `timeout` in `.mcp.json` overrides it; a per-server `timeout` of at least 1000 also sets the minimum idle window (v2.1.203+). For the variable values below 1000 floor to one second; for the per-server field values below 1000 are ignored. |
| `CLAUDE_CODE_MCP_TOOL_IDLE_TIMEOUT` | Idle timeout for MCP tool calls (stdio, HTTP, SSE, WebSocket, claude.ai connector): aborts with an error when no response or progress notification arrives for this long. Overrides per-transport defaults of 300000 (network) and 1800000 (stdio). `0` disables; values under 1000 raised to one second; capped at the effective `MCP_TOOL_TIMEOUT`. Not for IDE or SDK in-process servers. Requires v2.1.187+; before v2.1.203 stdio servers were exempt. |
| `CLAUDE_CODE_MCP_AUTO_BACKGROUND_MS` | Elapsed ms before a running MCP tool call moves to a background task (default 120000). `0` turns auto-backgrounding off and, interactively, makes Claude wait for MCP tasks. Requires v2.1.212+. |
| `CLAUDE_CODE_DISABLE_MCP_TASK_BACKGROUND` | `1` makes Claude wait for an MCP task result in an interactive session (with auto-backgrounding on, a call still backgrounds after two minutes by default). Requires v2.1.304+. |
| `MAX_MCP_OUTPUT_TOKENS` | Max tokens in MCP tool responses (default 25000); warning above 10,000. Tools declaring `anthropic/maxResultSizeChars` use that character limit for text (images still use this variable). A successful text result over 50,000 characters from a tool without that annotation is saved to a file regardless. |
| `CLAUDE_CODE_MAX_MCP_DESCRIPTION_LENGTH` | Max characters of MCP tool descriptions and server instructions sent to the model; replaces both defaults (4096, and 16384 for a tool description loaded through tool search). Positive whole number, plain digits. Requires v2.1.280+. |
| `ENABLE_TOOL_SEARCH` | Controls MCP tool search. Unset or `true` defers MCP tools (except in cases that keep it off); `auto` defers once definitions reach 10% of the context window; `auto:N` sets another threshold (`auto:5` = 5%); `false` loads all tools upfront. |
| `ENABLE_CLAUDEAI_MCP_SERVERS` | `false` stops fetching claude.ai MCP servers (enabled by default for logged-in users). Per project or org, use the `disableClaudeAiConnectors` setting. |
| `MCP_CLIENT_SECRET` | OAuth client secret for MCP servers needing pre-configured credentials; avoids the prompt when adding a server with `--client-secret`. |
| `MCP_OAUTH_CALLBACK_PORT` | Fixed OAuth redirect callback port, alternative to `--callback-port` when adding an MCP server with pre-configured credentials. |
