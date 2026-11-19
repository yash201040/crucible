# agent-sdk-extend-with-tools/agent-sdk-custom-tools

* [Register, call and scope custom tools](call-custom-tool-and-access.md) - Pass the server via mcpServers, pre-approve mcp__server__tool names in allowedTools, and control built-in availability with tools and disallowedTools. **[high]**
* [Define a custom tool](define-custom-tool.md) - Build a tool from name, description, input schema and handler with tool() or @tool, wrapped in an in-process MCP server. **[high]**
* [Handle custom tool errors](handle-tool-errors.md) - A handler error does not stop the agent loop; return isError true to control the message Claude reads.
* [Per-tool permission policy](require-approval-permission-policy.md) - In TypeScript, give an SDK MCP tool permission_policy always_ask or always_deny so allowedTools no longer approves it. **[high]**
* [Tool annotations](tool-annotations-reference.md) - Optional MCP hint fields on a tool (readOnlyHint and others); readOnlyHint lets calls run in parallel, and none are enforced. **[high]**
* [Tool result content blocks](tool-result-content.md) - Content block types a custom tool can return (text, image, audio, resource, resource_link) and structuredContent, with TypeScript and Python differences.
