---
type: "Release Digest"
title: "MCP and tools, 2.1.296 to 2.1.328"
description: "Release-note changes to MCP servers, MCP tasks, tool search, Monitor, Read, Artifact, ExitWorktree and other built-in tools between 2.1.296 and 2.1.328."
resource: "https://code.claude.com/docs/en/changelog"
tags: [mcp, tools, tool-search, monitor, artifact, release-notes]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "claude mcp add-json"
  - "claude mcp add"
  - ".mcp.json"
  - "mcpServers"
  - "managed-mcp.json"
  - "deniedMcpServers"
  - "allowedMcpServers"
  - "CLAUDE_CODE_DISABLE_MCP_TASK_BACKGROUND"
  - "CLAUDE_CODE_DISABLE_MCP_TASKS"
  - "MCP_SDK_GENERATION"
  - "MCP_PROTOCOL_NEGOTIATION"
  - "alwaysLoad"
  - "claude mcp serve"
  - "ToolSearch"
  - "Monitor"
  - "allow_large"
  - "Read"
  - "TaskStop"
  - "Artifact"
  - "CLAUDE_CODE_PROXY_RESOLVES_HOSTS"
  - "/mcp"
  - "/tasks"
  - "/context"
  - "browser_batch"
  - "javascript_tool"
  - "shortcuts_list"
  - "shortcuts_execute"
  - "CLAUDE_CODE_DISABLE_FILE_MENTIONS"
  - "CLAUDE_CODE_DISABLE_CFC_PROMPT"
  - "WebFetch"
  - "WebSearch"
  - "mcp__<server>__*"
  - "CLAUDE_CODE_MAX_CONTEXT_TOKENS"
  - "ExitWorktree"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "changelog"
    resource: "https://code.claude.com/docs/en/changelog"
    title: "Changelog 2.1.296 to 2.1.328"
stale_after: "2027-01-19T00:00:00Z"
---

# What changed

| Version | Date | What changed | Names |
|---|---|---|---|
| 2.1.328 | 2026-11-19 | deniedMcpServers entries of the form claude.ai name now also apply to that connector in cloud and self-hosted runner sessions. | `deniedMcpServers` |
| 2.1.328 | 2026-11-19 | Code Mode: better prompt caching with MCP servers; Claude is told when a server is still connecting or the server list changes. | |
| 2.1.327 | 2026-11-17 | claude mcp add-json takes - to read JSON from stdin so tokens stay off the command line; not available inside a Claude Code session. | `claude mcp add-json` |
| 2.1.327 | 2026-11-17 | claude mcp add --scope project stops instead of overwriting when .mcp.json lists servers at top level without mcpServers. | `claude mcp add`, `.mcp.json`, `mcpServers` |
| 2.1.327 | 2026-11-17 | MCP server logs record the mode, action and field names of elicitation requests and hook answers, not full contents; /mcp pages share one layout. | `/mcp` |
| 2.1.327 | 2026-11-17 | Artifact tool: refuses calls once settings turn Artifacts off, reads uploads by the page's address, ignores prompt, limit and label on calls that do not use them; creation refused at once with nobody to ask where approval is required. | `Artifact` |
| 2.1.326 | 2026-11-16 | Message explains why MCP servers stop loading when an admin adds managed-mcp.json mid-session; it may apply at the next check, restart sessions to apply in full. | `managed-mcp.json` |
| 2.1.326 | 2026-11-16 | claude mcp serve ignores sandbox.excludedCommands. | `claude mcp serve`, `sandbox.excludedCommands` |
| 2.1.326 | 2026-11-16 | MCP tool errors in cloud sessions say the outcome is unknown when a proxied call is cut off after sending; Monitor tells Claude when a watch expired with stderr output and which file holds it. | `Monitor` |
| 2.1.326 | 2026-11-16 | Claude in Chrome browser_batch call has 150 seconds, up from 90. | `browser_batch` |
| 2.1.325 | 2026-11-13 | Esc on a background MCP task's question means answer later: nothing is sent and the question stays in /tasks; Claude is told when a task waits for an answer. | `/tasks` |
| 2.1.325 | 2026-11-13 | Cloud sessions' tool-search MCP descriptions limit raised from 4,096 to 16,384 characters (web fix). | |
| 2.1.325 | 2026-11-13 | CLAUDE_CODE_MAX_CONTEXT_TOKENS also sets the context window of unrecognized claude- model IDs. | `CLAUDE_CODE_MAX_CONTEXT_TOKENS` |
| 2.1.323 | 2026-11-12 | The tool Claude uses to finish an MCP server sign-in asks for confirmation even in bypass and auto modes; use /mcp where nobody can be asked. | `/mcp` |
| 2.1.323 | 2026-11-12 | MCP_SDK_GENERATION=v1 runs the v2 MCP client in a compatibility mode because the v1 client is removed. | `MCP_SDK_GENERATION` |
| 2.1.323 | 2026-11-12 | Project (.mcp.json) MCP server approvals match the server's exact name; /mcp shows how many tools were left out for invalid input schemas. | `.mcp.json`, `/mcp` |
| 2.1.323 | 2026-11-12 | ToolSearch says when a tool searched by short name is already available; Artifact tool accepts .docx uploads; artifact updates ask first when people outside the organization can see the artifact. | `ToolSearch`, `Artifact` |
| 2.1.323 | 2026-11-12 | MCP tool call that times out in a non-interactive session while elicitation is unanswered now tells Claude not to repeat the call (2.1.310). | |
| 2.1.319 | 2026-11-06 | MCP tasks supported in the terminal: a tool call run as a task moves to the background at once and Claude is told the result; CLAUDE_CODE_DISABLE_MCP_TASK_BACKGROUND makes it wait inline. | `CLAUDE_CODE_DISABLE_MCP_TASK_BACKGROUND` |
| 2.1.319 | 2026-11-06 | MCP tasks work without feature-flag fetching; CLAUDE_CODE_DISABLE_MCP_TASKS=1 turns them off. | `CLAUDE_CODE_DISABLE_MCP_TASKS` |
| 2.1.319 | 2026-11-06 | Monitor's WebSocket watch follows rules on every Bash command; CLAUDE_CODE_PROXY_RESOLVES_HOSTS can no longer be set from settings files where the host manages the network. | `Monitor`, `CLAUDE_CODE_PROXY_RESOLVES_HOSTS` |
| 2.1.319 | 2026-11-06 | /context keeps each list to its 10 largest rows; on-demand MCP tools share one row per server until called. | `/context` |
| 2.1.319 | 2026-11-06 | Removed shortcuts_list and shortcuts_execute from the built-in Claude in Chrome tools; javascript_tool results up to 60,000 characters stay in the conversation. | `shortcuts_list`, `shortcuts_execute`, `javascript_tool` |
| 2.1.318 | 2026-11-04 | deniedMcpServers URL entries also block Anthropic-provided servers whose upstream URL matches, and connectors in cloud and runner sessions; deny a connector by name otherwise. | `deniedMcpServers` |
| 2.1.318 | 2026-11-04 | An MCP call made before the tool is loaded returns its input schema. | |
| 2.1.317 | 2026-11-03 | Removed the Read tool's "file unchanged since your last Read" stub; re-reading returns content. | `Read` |
| 2.1.310 | 2026-10-23 | Monitor tool and plugin monitors work on Bedrock, Vertex and Foundry and with telemetry or nonessential traffic disabled; long foreground sleeps are blocked there too. | `Monitor` |
| 2.1.305 | 2026-10-20 | allowedMcpServers no longer filters managed-mcp.json stdio servers that use variables only in env; use deniedMcpServers to keep one off. | `allowedMcpServers`, `managed-mcp.json`, `deniedMcpServers` |
| 2.1.304 | 2026-10-19 | Tool search on by default behind a custom ANTHROPIC_BASE_URL (400 or 422 retried without it); cloud sessions skip waiting for stdio MCP servers from claude.ai plugins unless alwaysLoad is true. | `ToolSearch`, `alwaysLoad`, `ANTHROPIC_BASE_URL` |
| 2.1.299 | 2026-10-14 | MCP allow rules reach only the server they name: mcp__a no longer allows a server named a__b; write mcp__<server>__*. | `mcp__<server>__*` |
| 2.1.299 | 2026-10-14 | CLAUDE_CODE_DISABLE_FILE_MENTIONS gives Claude the paths of @ file mentions, not contents. | `CLAUDE_CODE_DISABLE_FILE_MENTIONS` |
| 2.1.299 | 2026-10-14 | Requests to claude.ai's connector proxy and Anthropic-hosted MCP servers no longer follow redirects; cloud and Remote Control connectors negotiate MCP protocol version 2026-07-28 by default (MCP_PROTOCOL_NEGOTIATION=legacy opts out); first-party MCP descriptions no longer cut at 4,096 characters. | `MCP_PROTOCOL_NEGOTIATION` |
| 2.1.299 | 2026-10-14 | A local session can watch up to 25 published artifacts at once, up from 10. | |
| 2.1.296 | 2026-10-09 | Added allow_large to the Read tool to read a text file past the usual size limits in one call. | `allow_large`, `Read` |
| 2.1.296 | 2026-10-09 | Default limit on MCP tool descriptions sent up front and on server instructions raised from 2,048 to 4,096 characters. | |
| 2.1.321 | 2026-11-09 | Background command notifications and TaskStop results show only the start and end of a command over 1,000 characters. | `TaskStop` |
| 2.1.314 | 2026-10-30 | Hook if conditions match the Monitor tool's commands like Bash. | `Monitor` |
| 2.1.314 | 2026-10-30 | CLAUDE_CODE_DISABLE_CFC_PROMPT also stops the VS Code extension adding Claude in Chrome instructions; browser tools stay available. | `CLAUDE_CODE_DISABLE_CFC_PROMPT` |

# Not found in the documentation pages

- `CLAUDE_CODE_DISABLE_MCP_TASKS`
- `javascript_tool`
- `shortcuts_list`
- `shortcuts_execute`
