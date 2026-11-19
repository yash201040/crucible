# mcp/mcp

* [Add servers from JSON](add-json-configuration.md) - claude mcp add-json adds a server from a JSON string, piped from stdin from v2.1.327.
* [Add a local stdio server](add-local-stdio-server.md) - Run a local process as an MCP server: the -- separator, --env, CLAUDE_PROJECT_DIR, roots/list and shutdown signals. **[high]**
* [Add a remote HTTP server](add-remote-http-server.md) - HTTP is the recommended transport for remote MCP servers; syntax, headers, the streamable-http alias and rejected entries. **[high]**
* [Convert another client's setup instructions](add-server-from-other-client.md) - How to turn a URL, launch command or mcpServers JSON block written for Claude Desktop or Cursor into a claude mcp command.
* [Add a remote SSE server (deprecated)](add-sse-server.md) - SSE transport is deprecated; HTTP-first fallback to SSE from v2.1.265, or --transport sse directly.
* [Add a remote WebSocket server](add-websocket-server.md) - WebSocket MCP servers keep a persistent connection; configured only via JSON, header-only auth, no OAuth.
* [Automatic backgrounding of long MCP calls](automatic-backgrounding.md) - A main-conversation MCP call running over two minutes moves to a background task; thresholds, switches and exclusions. **[high]**
* [Automatic reconnection and retries](automatic-reconnection.md) - Reconnect behavior for remote and stdio MCP servers in interactive, claude -p and Agent SDK runs, with retry counts and windows. **[high]**
* [Use Claude Code as an MCP server](claude-code-as-mcp-server.md) - claude mcp serve exposes Claude Code's tools over stdio; Claude Desktop config and reading backgroundOutputPath. **[high]**
* [claude.ai connectors in Claude Code](claudeai-connectors.md) - Connectors added at claude.ai load automatically when signed in with a claude.ai subscription; auth conditions and display states.
* [MCP configuration warnings and reserved names](configuration-warnings.md) - Warnings for hidden whitespace, duplicate names across scopes, reserved server names and unset ${VAR} references.
* [How connectors reach sessions and org tool controls](connector-delivery-and-org-controls.md) - Which sessions fetch connectors, what governs each, per-tool ask/blocked org controls, and disableClaudeAiConnectors.
* [Disable a server without removing it](disable-server-without-removing.md) - Per-project toggles in ~/.claude.json: disabledMcpServers opt-out list and enabledMcpServers opt-in list.
* [Dynamic tool updates and list_changed](dynamic-tool-updates.md) - How list_changed notifications refresh tools, prompts and resources, and the v2 notification stream reopen limits.
* [MCP elicitation requests](elicitation-requests.md) - Servers ask for structured input mid-task via form or URL mode dialogs; hook auto-response, cloud cards and declared capabilities.
* [Environment variable expansion in .mcp.json](env-var-expansion-in-mcp-json.md) - ${VAR} and ${VAR:-default} in command, args, env, url and headers, empty-string behavior and credential variables read as empty.
* [headersHelper dynamic headers and gateway sign-in](headers-helper-and-gateway-auth.md) - headersHelper command generates auth headers at connect time; trust, working directory and env rules; OAuth behind header-requiring proxies. **[high]**
* [Import servers from Claude Desktop](import-from-claude-desktop.md) - claude mcp add-from-claude-desktop imports selected servers on macOS and WSL, with name restrictions.
* [MCP installation scopes and precedence](installation-scopes-and-precedence.md) - Local, project and user scopes, where each is stored, approval prompts, and how duplicate servers resolve. **[high]**
* [claude mcp management commands](manage-servers-cli.md) - Commands for listing, inspecting, removing and checking MCP servers from the shell or inside a session.
* [Managed MCP configuration (pointer)](managed-mcp-pointer.md) - Organizations control MCP servers with managed-mcp.json, managedMcpServers, allowedMcpServers and deniedMcpServers; covered on its own page.
* [Push messages with channels](mcp-channels.md) - An MCP server declaring claude/channel can push messages into a session when opted in with --channels.
* [MCP client runtimes v1 and v2](mcp-client-runtimes.md) - Two MCP client runtimes (SDK 1.x vs SDK 2.0 with protocol revision 2026-07-28), how one is chosen and the variables to pick.
* [MCP overview and finding servers](mcp-overview-and-servers.md) - What MCP gives Claude Code, where to find reviewed servers, and how the mcp-server-dev plugin scaffolds one.
* [MCP prompts as slash commands](mcp-prompts-as-commands.md) - Server prompts appear as /servername:promptname (MCP) or /mcp__servername__promptname, with space-separated arguments.
* [Use MCP resources with @ mentions](mcp-resources.md) - Reference MCP resources in prompts as @server:protocol://path; plain text in claude -p; UI resources excluded from listings.
* [MCP tasks for server authors](mcp-tasks-for-authors.md) - Wire format Claude Code expects when a tools/call is answered with a task, tasks/get polling and per-status handling.
* [MCP tasks that run on the server](mcp-tasks-server-side.md) - Public-beta MCP tasks extension: long server-run jobs, footer count, resume behavior, requirements and status messages. **[high]**
* [MCP tool search and deferral](mcp-tool-search.md) - MCP tool definitions are deferred and found on demand; ENABLE_TOOL_SEARCH modes, alwaysLoad, description length limits, gateways. **[high]**
* [Authenticate with remote MCP servers (OAuth)](oauth-authentication-remote.md) - OAuth 2.0 sign-in via /mcp or claude mcp login, when a server is flagged needs-auth, refresh behavior and headless limits. **[high]**
* [OAuth callback port and pre-configured credentials](oauth-callback-port-and-credentials.md) - Fix the OAuth callback port and supply a client ID and secret for servers without dynamic client registration.
* [OAuth metadata override and scope pinning](oauth-metadata-and-scopes.md) - authServerMetadataUrl bypasses OAuth discovery; oauth.scopes pins requested scopes and handles insufficient_scope.
* [MCP output limits and warnings](output-limits-and-warnings.md) - Token and character thresholds for MCP tool output, MAX_MCP_OUTPUT_TOKENS, 16 MiB response cap and image saving. **[high]**
* [Plugin-provided MCP servers](plugin-provided-servers.md) - Plugins bundle MCP servers in .mcp.json or plugin.json; lifecycle, path placeholders and the mcp__plugin_ tool-name form. **[high]**
* [Examples: GitHub and PostgreSQL servers](practical-examples-github-postgres.md) - Worked commands for GitHub's remote MCP server with a PAT header and a DBHub stdio server for PostgreSQL.
* [Tool annotations for server authors](server-author-tool-annotations.md) - _meta and annotations a server sets on a tool: requiresUserInteraction, idempotentHint, readOnlyHint, alwaysLoad. **[high]**
* [Server status, approvals and discovery cache](server-status-and-approvals.md) - Status labels in claude mcp list and /mcp, project-server approval under workspace trust, and the cached status and MCP_DISCOVERY_CACHE. **[high]**
* [Time limits on MCP tool calls](tool-call-time-limits.md) - Per-server timeout, MCP_TOOL_TIMEOUT, MCP_TIMEOUT, the per-request timer and the idle timeout CLAUDE_CODE_MCP_TOOL_IDLE_TIMEOUT. **[high]**
* [Tool input schema rules and exclusions](tool-schema-rules.md) - How Claude Code flattens root-level combinators, excludes invalid schemas and tools with names over 128 characters.
* [Tool availability and servers still connecting](tools-while-server-connecting.md) - How Claude waits for tools of a server still connecting, WaitForMcpServers, the 10-second hold after resume, and cloud tool counts. **[high]**
