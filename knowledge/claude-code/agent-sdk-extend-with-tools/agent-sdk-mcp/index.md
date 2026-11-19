# agent-sdk-extend-with-tools/agent-sdk-mcp

* [Add an MCP server to an SDK session](add-mcp-server.md) - Configure MCP servers in the mcpServers option of query() or in a project .mcp.json file. **[high]**
* [MCP tool permissions and naming](allow-mcp-tools-and-naming.md) - MCP tools need explicit permission; names are mcp__server__tool and allowedTools wildcards approve a whole server. **[high]**
* [MCP connection timing and first-turn wait](connection-timing-first-turn.md) - How long the first turn waits for MCP servers to connect, by server type and config source, and how to change it. **[high]**
* [MCP authentication in the SDK](mcp-authentication.md) - Pass credentials through env or headers; the SDK runs no interactive OAuth flow and reports needs-auth or failed instead. **[high]**
* [MCP server status and reconnection](mcp-server-status-and-errors.md) - Init-message status values for MCP servers, how pending differs from failure, and reconnect calls. **[high]**
* [MCP timeouts, output limits and schema warnings](mcp-timeouts-and-output-limits.md) - 30-second connection timeout, MCP_TOOL_TIMEOUT, 25,000-token output cap, and the warning for SDK tools with unconvertible schemas. **[high]**
* [MCP transport types in the SDK](mcp-transport-types.md) - stdio, HTTP, SSE and in-process SDK servers, and which config fields each takes.
