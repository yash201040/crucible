---
type: "Release Digest"
title: "MCP and tools, 2.1.261 to 2.1.295"
description: "Release-note entries for MCP servers, MCP protocol negotiation, tool search, built-in tools (Grep, Bash, WebFetch, Monitor, Artifact) from 2.1.261 to 2.1.295."
resource: "https://code.claude.com/docs/en/changelog"
tags: [mcp, tools, tool-search, release-notes, monitor]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "MCP_PROTOCOL_NEGOTIATION"
  - "MCP_SDK_GENERATION"
  - "CLAUDE_CODE_MAX_MCP_DESCRIPTION_LENGTH"
  - "CLAUDE_CODE_MCP_STARTUP_WAIT_MS"
  - "MCP_DISCOVERY_CACHE"
  - "alwaysLoad"
  - "_meta['anthropic/alwaysLoad']"
  - "bareElicitationCapability"
  - "/mcp"
  - "/mcp reconnect all"
  - "claude mcp get"
  - "claude mcp serve"
  - "mcp__server__tool"
  - "resources/list"
  - "widgets"
  - "anthropic-skills"
  - "claude-ai"
  - "managed-mcp.json"
  - "type: sdk"
  - "--mcp-config"
  - "CLAUDE_CODE_DISABLE_WEB_FETCH"
  - "CLAUDE_CODE_WEB_SEARCH_REFILLS_PER_HOUR"
  - "CLAUDE_CODE_ENABLE_TODO_TOOLS"
  - "TaskOutput"
  - "taskOutputMaxChars"
  - "TASK_MAX_OUTPUT_LENGTH"
  - "bashOutputMaxChars"
  - "Grep"
  - "Monitor"
  - "persistent"
  - "Workflow"
  - "Artifact"
  - "WebFetch"
  - "WebSearch"
  - "Skill"
  - "TaskCreate"
  - "TaskGet"
  - "TaskUpdate"
  - "TaskList"
  - "TodoWrite"
  - "browser_batch"
  - "OTEL_LOG_TOOL_CONTENT"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "changelog"
    resource: "https://code.claude.com/docs/en/changelog"
    title: "Changelog 2.1.261 to 2.1.295"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Release-note rows (bug fixes removed) about MCP client behavior, deferred tool loading and built-in tool changes. Newest first.

# How to use it

| Version | Date | What changed | Names |
|---|---|---|---|
| 2.1.295 | 2026-10-08 | MCP tool descriptions loaded through tool search are cut at 16,384 characters (was 2,048). | |
| 2.1.295 | 2026-10-08 | claude.ai connectors negotiate MCP protocol 2026-07-28 by default on installs that fetch no flags; `MCP_PROTOCOL_NEGOTIATION=legacy` opts out. | `MCP_PROTOCOL_NEGOTIATION` |
| 2.1.295 | 2026-10-08 | WebSocket (`ws`) MCP servers: a message over 16 MiB is not parsed and closes the connection. | |
| 2.1.295 | 2026-10-08 | Permission-wait status in Remote Control/claude.ai/desktop names an MCP tool by server and readable name. | `mcp__server__tool` |
| 2.1.295 | 2026-10-08 | Grep runs searches sent with `-l`, `-c` or `-r` instead of failing. | `Grep` |
| 2.1.292 | 2026-10-06 | Local (stdio) MCP servers negotiate 2026-07-28 by default on every install including Bedrock, Vertex, Foundry; stdio servers that ignore the check are remembered 7 days and connected the older way. | `MCP_PROTOCOL_NEGOTIATION` |
| 2.1.292 | 2026-10-06 | Grep accepts `file_path` for `path`; Write, WebFetch, Read ignore a few stray parameters. | `Grep`, `file_path` |
| 2.1.290 | 2026-10-05 | MCP startup behind a proxy: a server blocked with HTTP 403 is not retried three times. | |
| 2.1.288 | 2026-10-02 | Re-authenticate prompt when an MCP server asks for more OAuth scope during a tool call; URL prompts from servers that cannot report completion wait for "I'm done, continue". | |
| 2.1.287 | 2026-10-01 | URL prompts from MCP servers on the 2025-11-25 protocol; if a server stops connecting add `"bareElicitationCapability": true` to its config entry. | `bareElicitationCapability` |
| 2.1.287 | 2026-10-01 | MCP server `alwaysLoad: false` defers all of that server's tools behind tool search. | `alwaysLoad` |
| 2.1.287 | 2026-10-01 | Large MCP tool results use less memory and smaller session files; headless MCP startup retries transient first-connect failures sooner. | |
| 2.1.286 | 2026-09-30 | WebFetch error for a rate-limited domain safety check tells Claude not to retry in a loop. | `WebFetch` |
| 2.1.285 | 2026-09-29 | `CLAUDE_CODE_DISABLE_WEB_FETCH` turns off the WebFetch tool. | `CLAUDE_CODE_DISABLE_WEB_FETCH` |
| 2.1.285 | 2026-09-29 | A tool that sets `_meta['anthropic/alwaysLoad']` to false stays deferred even if its `--mcp-config`, SDK or plugin server sets `alwaysLoad`. | `_meta['anthropic/alwaysLoad']`, `--mcp-config` |
| 2.1.285 | 2026-09-29 | Background Bash/PowerShell commands stop after a time limit (`timeout` with `run_in_background`; default 30 min, max 2 h); Claude is notified. | `run_in_background` |
| 2.1.285 | 2026-09-29 | MCP server name `widgets` is reserved in cloud sessions and self-hosted runners; rename yours. | `widgets` |
| 2.1.285 | 2026-09-29 | `MCP_DISCOVERY_CACHE=1` set in a cloud environment's variables reuses connector tool lists after restart; other MCP servers are not cached. | `MCP_DISCOVERY_CACHE` |
| 2.1.284 | 2026-09-28 | `/mcp reconnect all` retries every failed or unauthenticated MCP server. | `/mcp reconnect all` |
| 2.1.284 | 2026-09-28 | Non-interactive first turn waits up to 2 s for MCP servers named by `--allowedTools` or an `mcp_tool` hook even with `CLAUDE_CODE_MCP_STARTUP_WAIT_MS=0`. | `CLAUDE_CODE_MCP_STARTUP_WAIT_MS` |
| 2.1.283 | 2026-09-25 | MCP tool, WebFetch and WebSearch outputs added to the `tool.output` span event when `OTEL_LOG_TOOL_CONTENT=1`. | `OTEL_LOG_TOOL_CONTENT` |
| 2.1.283 | 2026-09-25 | Images returned by MCP tools are also saved to a file so Bash/Read can open them; `/mcp` marks tools the organization blocked. | |
| 2.1.282 | 2026-09-24 | MCP servers named `anthropic-skills` or `claude-ai` list no skills or prompts (tools still work). | `anthropic-skills`, `claude-ai` |
| 2.1.281 | 2026-09-23 | MCP URL-mode elicitation on 2026-07-28 connections; resource list tool and @-mention suggestions skip MCP Apps UI resources. | |
| 2.1.280 | 2026-09-22 | `CLAUDE_CODE_MAX_MCP_DESCRIPTION_LENGTH` changes the 2,048-character cap on MCP tool descriptions and server instructions. | `CLAUDE_CODE_MAX_MCP_DESCRIPTION_LENGTH` |
| 2.1.277 | 2026-09-18 | TaskOutput tool removed; Claude reads a background task's output file with Read; `taskOutputMaxChars` and `TASK_MAX_OUTPUT_LENGTH` have no effect. | `TaskOutput`, `taskOutputMaxChars`, `TASK_MAX_OUTPUT_LENGTH` |
| 2.1.274 | 2026-09-17 | v2 MCP client and 2026-07-28 negotiation by default on Bedrock, Vertex, Foundry and telemetry-disabled installs (opt out `MCP_SDK_GENERATION=v1` or `MCP_PROTOCOL_NEGOTIATION=legacy`). | `MCP_SDK_GENERATION`, `MCP_PROTOCOL_NEGOTIATION` |
| 2.1.274 | 2026-09-17 | `"type": "sdk"` MCP entries in `.mcp.json`, settings, plugins, agent files are skipped with a warning. | `.mcp.json` |
| 2.1.274 | 2026-09-17 | Monitor script's final output and exit arrive as one notification. | `Monitor` |
| 2.1.273 | 2026-09-15 | Notification when an MCP server disconnects mid-session and reconnection gives up. | `/mcp` |
| 2.1.271 | 2026-09-14 | Monitor watches always have a deadline (max 30 min; 10 in single-prompt `-p`), replacing `persistent`; `claude mcp serve` sends progress every 30 s. | `Monitor`, `persistent`, `claude mcp serve` |
| 2.1.271 | 2026-09-14 | Per-command `allowed_domains` for Bash, PowerShell and Monitor in auto mode with sandboxing. | `allowed_domains` |
| 2.1.268 | 2026-09-10 | Task tools (TaskCreate/Get/Update/List, TodoWrite) offered only on Claude 3.x, Opus 4.0-4.7, Sonnet 4.0-4.6, Haiku 4.5; `CLAUDE_CODE_ENABLE_TODO_TOOLS=1` elsewhere. | `CLAUDE_CODE_ENABLE_TODO_TOOLS` |
| 2.1.268 | 2026-09-10 | Bedrock, Vertex, Foundry keep the tool list byte-stable across a conversation (late tools load deferred). | |
| 2.1.265 | 2026-09-08 | 1 GB cap on tool results saved to disk; preview says when truncated; remote MCP servers needing sign-in get no OAuth client registration until you authenticate. | |
| 2.1.261 | 2026-09-04 | `bashOutputMaxChars` and `taskOutputMaxChars` raise inline output before saving to a file (up to 128K characters). | `bashOutputMaxChars`, `taskOutputMaxChars` |

# Not found in the documentation pages

- `_meta['anthropic/alwaysLoad']`
- `mcp__server__tool`
- `type: sdk`
