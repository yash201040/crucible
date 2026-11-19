---
type: "Feature"
title: "Custom tools and MCP server types"
description: "The @tool decorator, in-process SDK MCP servers, ToolAnnotations and the MCP config and status types."
resource: "https://code.claude.com/docs/en/agent-sdk/python"
tags: [mcp, custom-tools, tool-decorator, annotations, python]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "tool()"
  - "create_sdk_mcp_server()"
  - "SdkMcpTool"
  - "ToolAnnotations"
  - "readOnlyHint"
  - "destructiveHint"
  - "idempotentHint"
  - "openWorldHint"
  - "maxResultSizeChars"
  - "anthropic/maxResultSizeChars"
  - "McpSdkServerConfig"
  - "McpServerConfig"
  - "McpStdioServerConfig"
  - "McpSSEServerConfig"
  - "McpHttpServerConfig"
  - "McpServerStatus"
  - "McpStatusResponse"
  - "McpServerStatusConfig"
  - "claudeai-proxy"
  - "ContextUsageResponse"
  - "SdkPluginConfig"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-python"
    resource: "https://code.claude.com/docs/en/agent-sdk/python"
    title: "Agent SDK reference - Python"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Define in-process tools with the `@tool(name, description, input_schema, annotations=None)` decorator, bundle them with `create_sdk_mcp_server(name, version="1.0.0", tools=[...])`, and pass the result in `ClaudeAgentOptions.mcp_servers`. Tool functions are async, take `args` and return `{"content": [{"type": "text", "text": ...}]}`. Allow them as `mcp__<server>__<tool>`, for example `mcp__calc__add`.

# How to use it

Input schema forms: a simple type mapping (`{"text": str, "count": int}`, recommended), a JSON Schema dict, or a `TypedDict` class (`NotRequired` keys are left out of `required`; on Python 3.10 import `NotRequired` from `typing_extensions`, which the SDK installs). Wrap a type in `Annotated[type, "description"]` to describe a field.

`ToolAnnotations` (all optional, hints only, not for security decisions; camelCase or snake_case accepted, snake_case needs Python Agent SDK 0.2.140+):

| Field | Default | Meaning |
| :- | :- | :- |
| `title` | `None` | human-readable title |
| `readOnlyHint` | `False` | tool does not modify its environment |
| `destructiveHint` | `True` | may do destructive updates (only if not read-only) |
| `idempotentHint` | `False` | repeat calls have no extra effect |
| `openWorldHint` | `True` | talks to external entities |
| `maxResultSizeChars` | `None` | chars of text result kept inline instead of saved to a file, up to 500,000; images unaffected; sent in `_meta` as `anthropic/maxResultSizeChars`; SDKs 0.1.55 to 0.2.139 can pass it as a keyword |

MCP configs: `McpStdioServerConfig` (`command`, `args`, `env`), `McpSSEServerConfig` and `McpHttpServerConfig` (`url`, `headers`), `McpSdkServerConfig` (`type: "sdk"`, `name`, `instance`). `get_mcp_status()` returns `McpStatusResponse` with `mcpServers` list; each `McpServerStatus` has `name`, `status` (`connected`, `failed`, `needs-auth`, `pending`, `disabled`), `serverInfo`, `error`, `config` (adds output-only `claudeai-proxy` variant with `url`, `id`), `scope`, `tools`.

`get_context_usage()` returns `ContextUsageResponse`: `categories`, `totalTokens`, `maxTokens` (model window or lower auto-compaction window), `rawMaxTokens`, `percentage`, `model`, `isAutoCompactEnabled`, `memoryFiles`, `mcpTools`, `agents`, `gridRows`, optional `autoCompactThreshold`, `slashCommands`, `skills`, `messageBreakdown`, `apiUsage` (latest response only). `deferredBuiltinTools`, `systemTools`, `systemPromptSections` are declared but not populated.

# Limits and defaults

Plugins: `SdkPluginConfig` is `{"type":"local","path":...}`; only local plugins are supported.

In-process `tool()` results have `resource_link` blocks flattened to text. TypedDict types (for example MCP configs, `ThinkingConfig`) are plain dicts at runtime; dataclasses (for example `ResultMessage`, `AgentDefinition`) support attribute access.
