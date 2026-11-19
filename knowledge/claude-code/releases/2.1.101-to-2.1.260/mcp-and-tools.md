---
type: "Release Digest"
title: "MCP servers and tools (2.1.101 to 2.1.260)"
description: "Release notes 2.1.101 to 2.1.260 on MCP configuration, tool availability, tool search and built-in tool behavior."
resource: "https://code.claude.com/docs/en/changelog"
tags: [mcp, tools, release-notes]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "managedMcpServers"
  - "allowedMcpServers"
  - "deniedMcpServers"
  - "managed-mcp.json"
  - "SendFeedback"
  - "feedbackDrafts"
  - "/mcp"
  - "claude mcp list"
  - "claude mcp get"
  - "headersHelper"
  - "TaskCreate"
  - "TaskGet"
  - "TaskUpdate"
  - "TaskList"
  - "TodoWrite"
  - "CLAUDE_CODE_ENABLE_TODO_TOOLS"
  - "CLAUDE_CODE_WEBFETCH_CACHE_TTL_MS"
  - "Write"
  - "Edit"
  - "Monitor"
  - "mcp_server_errors"
  - "EndConversation"
  - "CLAUDE_CODE_MCP_AUTO_BACKGROUND_MS"
  - "CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION"
  - "WebSearch"
  - "roots/list"
  - "notifications/roots/list_changed"
  - "claude mcp login"
  - "claude mcp logout"
  - "--no-browser"
  - "CLAUDE_CODE_SESSION_ID"
  - "--tools"
  - "Grep"
  - "Glob"
  - "Bash"
  - "CLAUDECODE"
  - "allowAllClaudeAiMcps"
  - "Read"
  - "CLAUDE_PROJECT_DIR"
  - "workspace"
  - "alwaysLoad"
  - "ENABLE_TOOL_SEARCH"
  - "EnterWorktree"
  - "WebFetch"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "changelog"
    resource: "https://code.claude.com/docs/en/changelog"
    title: "Changelog 2.1.101 to 2.1.260"
stale_after: "2027-01-19T00:00:00Z"
---

# Changes by version

| Version | Date | What changed | Names |
|---|---|---|---|
| 2.1.259 | 2026-09-02 | managedMcpServers managed setting provides HTTP/SSE MCP servers to every user (entries naming a command are skipped); allowedMcpServers now governs only user-added servers, use deniedMcpServers to keep a managed-mcp.json server off | `managedMcpServers`, `allowedMcpServers`, `deniedMcpServers`, `managed-mcp.json` |
| 2.1.257 | 2026-09-01 | MCP connection and OAuth logs redact credentials in server URLs and headers |  |
| 2.1.251 | 2026-08-28 | MCP server names are sanitized in errors, menus and command results |  |
| 2.1.247 | 2026-08-26 | On Bedrock, Vertex, Foundry or telemetry-off sessions Claude is told when a configured MCP server failed to connect; SendFeedback tool drafts feedback reports, feedbackDrafts turns it off | `SendFeedback`, `feedbackDrafts` |
| 2.1.243 | 2026-08-25 | managed marker in /mcp and /plugins on claude.ai connectors whose auth is managed by the organization | `/mcp` |
| 2.1.238 | 2026-08-20 | claude mcp list and get show disabled servers as Disabled without connecting; MCP headersHelper in project .mcp.json and inline agent-file servers require accepted folder trust; helpers from project, plugin or agent files run without inherited credential env vars | `claude mcp list`, `claude mcp get`, `headersHelper` |
| 2.1.233 | 2026-08-14 | Todo/task tools (TaskCreate, TaskGet, TaskUpdate, TaskList, TodoWrite) are unavailable on Opus 4.8, Sonnet 5, Fable 5, Mythos 5 and newer; CLAUDE_CODE_ENABLE_TODO_TOOLS=1 restores them; CLAUDE_CODE_WEBFETCH_CACHE_TTL_MS sets the WebFetch URL cache TTL (default 15 minutes) | `TaskCreate`, `TaskGet`, `TaskUpdate`, `TaskList`, `TodoWrite`, `CLAUDE_CODE_ENABLE_TODO_TOOLS`, `CLAUDE_CODE_WEBFETCH_CACHE_TTL_MS` |
| 2.1.228 | 2026-08-11 | Write tool lets newer models overwrite an existing unread file, like Edit | `Write`, `Edit` |
| 2.1.221 | 2026-08-04 | Monitor reports when a watch exits without output; tool search re-enabled on Vertex AI for Claude 4.5-generation and newer | `Monitor` |
| 2.1.219 | 2026-07-24 | mcp_server_errors in stream-json init; claude mcp list and /mcp show HTTP status and error text on failed connect; managed MCP allow/deny list ${VAR} entries resolve from startup environment | `mcp_server_errors`, `/mcp` |
| 2.1.214 | 2026-07-18 | EndConversation tool lets Claude end sessions with highly abusive users or jailbreak attempts; periodic progress heartbeat for long tool calls | `EndConversation` |
| 2.1.212 | 2026-07-17 | MCP tool calls longer than 2 minutes move to the background automatically (CLAUDE_CODE_MCP_AUTO_BACKGROUND_MS configures or disables); WebSearch cap of 200 per session via CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION; web search/fetch retry 529 and rate limits | `CLAUDE_CODE_MCP_AUTO_BACKGROUND_MS`, `CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION`, `WebSearch` |
| 2.1.208 | 2026-07-14 | MCP server with empty URL shows not configured in /mcp |  |
| 2.1.205 | 2026-07-08 | Claude Browser reserved as MCP server name alongside Claude Preview |  |
| 2.1.203 | 2026-07-07 | Session additional working directories are sent in MCP roots/list with notifications/roots/list_changed | `roots/list`, `notifications/roots/list_changed` |
| 2.1.202 | 2026-07-06 | Clearer MCP error when a server config has url but no type (use type http) |  |
| 2.1.193 | 2026-06-25 | Startup notice when MCP servers need auth; MCP headersHelper reruns and reconnects on 401/403 tool results | `headersHelper` |
| 2.1.191 | 2026-06-24 | MCP capability discovery retries transient network errors; MCP OAuth retries once; headless OAuth skips the browser and prompts for the pasted URL |  |
| 2.1.186 | 2026-06-22 | claude mcp login <name> and logout <name> with --no-browser stdin completion for SSH | `claude mcp login`, `claude mcp logout`, `--no-browser` |
| 2.1.169 | 2026-06-08 | TaskCreate repairs malformed inputs automatically | `TaskCreate` |
| 2.1.163 | 2026-06-04 | stdio MCP servers receive the same CLAUDE_CODE_SESSION_ID on --resume | `CLAUDE_CODE_SESSION_ID` |
| 2.1.162 | 2026-06-03 | --tools lists Grep and Glob to provide the dedicated search tools on native builds | `--tools`, `Grep`, `Glob` |
| 2.1.161 | 2026-06-02 | Parallel tool calls: a failed Bash command no longer cancels the other calls in the batch | `Bash` |
| 2.1.154 | 2026-05-28 | stdio MCP subprocesses receive CLAUDE_CODE_SESSION_ID and CLAUDECODE=1; claude mcp list/get show unapproved .mcp.json servers as Pending approval; streaming tool execution always on | `CLAUDE_CODE_SESSION_ID`, `CLAUDECODE` |
| 2.1.149 | 2026-05-22 | allowAllClaudeAiMcps managed setting loads claude.ai connectors alongside managed-mcp.json | `allowAllClaudeAiMcps` |
| 2.1.145 | 2026-05-19 | Read tool returns a truncated first page with a PARTIAL view notice instead of an error for oversized whole-file reads | `Read` |
| 2.1.139 | 2026-05-11 | MCP stdio servers receive CLAUDE_PROJECT_DIR; /mcp Reconnect picks up .mcp.json edits | `CLAUDE_PROJECT_DIR` |
| 2.1.128 | 2026-05-04 | workspace is a reserved MCP server name; /mcp shows tool counts; reconnects summarize re-announced tools by server prefix | `workspace` |
| 2.1.121 | 2026-04-28 | MCP server alwaysLoad option skips tool-search deferral; MCP servers retry transient startup errors up to 3 times; claude.ai connectors with same upstream URL deduplicated | `alwaysLoad` |
| 2.1.119 | 2026-04-23 | Tool search disabled by default on Vertex AI (opt in with ENABLE_TOOL_SEARCH); subagent and SDK MCP reconfiguration connects servers in parallel | `ENABLE_TOOL_SEARCH` |
| 2.1.117 | 2026-04-22 | Native macOS/Linux builds replace Glob and Grep tools with embedded bfs and ugrep via Bash; local and claude.ai MCP servers connect concurrently | `Glob`, `Grep` |
| 2.1.116 | 2026-04-20 | Bash tool hints when gh hits GitHub API rate limit; faster stdio MCP startup, resources/templates/list deferred |  |
| 2.1.110 | 2026-04-15 | Bash tool enforces the documented maximum timeout; push notification tool for mobile when Remote Control and Push when Claude decides are on |  |
| 2.1.105 | 2026-04-13 | EnterWorktree path parameter; WebFetch strips style and script contents; MCP large-output prompt gives format-specific recipes | `EnterWorktree`, `WebFetch` |
