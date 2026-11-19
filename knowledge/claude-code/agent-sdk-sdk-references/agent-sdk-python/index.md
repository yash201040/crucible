# agent-sdk-sdk-references/agent-sdk-python

* [AgentDefinition and Agent tool](agent-definition-and-agent-tool.md) - Programmatic subagents via AgentDefinition, the Agent tool's input and output shapes, and background task messages. **[high]**
* [Timeout, retry and stall variables](api-timeouts-and-stalls.md) - Environment variables the CLI subprocess reads for API timeouts, retries and stall watchdogs, passed via ClaudeAgentOptions.env. **[high]**
* [Built-in tool input and output schemas](builtin-tool-schemas.md) - Input and output dict shapes for Claude Code built-in tools as seen in Python tool_use_result, with version gates and limits.
* [ClaudeAgentOptions fields](claude-agent-options.md) - Every field of the Python ClaudeAgentOptions dataclass: tools, permissions, budgets, sessions, models, hooks, sandbox, session store and more. **[high]**
* [Custom tools and MCP server types](custom-tools-and-mcp.md) - The @tool decorator, in-process SDK MCP servers, ToolAnnotations and the MCP config and status types. **[high]**
* [Messages, ResultMessage cost fields and errors](messages-results-and-errors.md) - Python message types, ResultMessage fields and subtypes, usage and model_usage accounting, rate-limit events and exception classes. **[high]**
* [Permission modes, can_use_tool and hooks](permissions-and-callbacks.md) - Python types for permission modes, the can_use_tool callback and results, permission updates, and the hook system with its input and output types. **[high]**
* [Python query() and ClaudeSDKClient](query-and-client.md) - The two Python entry points: one-shot query() and the session-keeping ClaudeSDKClient with interrupt, model and MCP controls. **[high]**
* [Python SandboxSettings](sandbox-settings.md) - Programmatic sandbox configuration for Bash commands: enable flags, network rules, unsandboxed fallback and platform notes. **[high]**
* [Python session management functions](session-functions.md) - Synchronous helpers to list, read, rename, tag and fork stored sessions, plus the SDKSessionInfo shape. **[high]**
