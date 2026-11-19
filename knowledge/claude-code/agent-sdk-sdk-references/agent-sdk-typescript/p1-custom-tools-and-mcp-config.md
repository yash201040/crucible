---
type: "Feature"
title: "In-process MCP tools, server configs and tool policies"
description: "tool(), createSdkMcpServer(), MCP server config types, per-tool permission_policy, plugin configs, and MCP server provenance."
resource: "https://code.claude.com/docs/en/agent-sdk/typescript"
tags: [mcp, custom-tools, plugins, permissions, in-process]
kind: "api"
maturity: "unlabelled"
since: "0.3.301"
surfaces: [sdk]
requires: "Tool policy list needs SDK v0.3.301+ and Claude Code v2.1.301+; always_deny removal needs Claude Code v2.1.324+"
identifiers:
  - "tool()"
  - "createSdkMcpServer()"
  - "McpStdioServerConfig"
  - "McpSSEServerConfig"
  - "McpHttpServerConfig"
  - "McpSdkServerConfigWithInstance"
  - "McpClaudeAIProxyServerConfig"
  - "McpServerToolPolicy"
  - "permission_policy"
  - "always_allow"
  - "always_ask"
  - "always_deny"
  - "org_max_permission"
  - "ToolAnnotations"
  - "readOnlyHint"
  - "destructiveHint"
  - "idempotentHint"
  - "openWorldHint"
  - "searchHint"
  - "alwaysLoad"
  - "MCP_TOOL_TIMEOUT"
  - "SdkPluginConfig"
  - "skipMcpDiscovery"
  - "McpServerProvenance"
  - "McpServerStatus"
  - "McpSetServersResult"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-typescript"
    resource: "https://code.claude.com/docs/en/agent-sdk/typescript"
    title: "Agent SDK reference - TypeScript"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`tool(name, description, zodShape, handler, extras?)` builds a type-safe MCP tool (Zod 3 or 4). `createSdkMcpServer({ name, version?, instructions?, tools?, alwaysLoad?, timeout? })` hosts tools in your process. `extras` holds `annotations`, `searchHint` (one-line phrase in the deferred-tool list when tool search is active) and `alwaysLoad: true` (keep the full schema in the initial prompt instead of deferring). Server `alwaysLoad` combines with per-tool. Server `timeout` replaces `MCP_TOOL_TIMEOUT` for that server (whole number of at least 1000; v0.3.248+).

# How to use it

- Config types for `mcpServers`: stdio (`command`, `args?`, `env?`), SSE and HTTP (`type`, `url`, `headers?`), in-process `{ type: "sdk", name, timeout?, tools?, instance }`, and `claudeai-proxy` (`url`, `id`).
- `ToolAnnotations` hints (clients should not rely on them for security): `title`, `readOnlyHint` (default false), `destructiveHint` (default true), `idempotentHint`, `openWorldHint` (default true). Set `destructiveHint: true` explicitly on any `always_ask` tool, because Claude Code treats unset as false for `always_ask`, and otherwise the auto-mode classifier can approve instead of `canUseTool`.
- Per-tool policy: spread the `createSdkMcpServer()` result into an object under `mcpServers` and add `tools: [{ name: "delete_record", permission_policy: "always_ask" }]` (bare tool name, no `mcp__server__` prefix). Change at runtime by passing a new `tools` value to `setMcpServers()` (list replaces, empty list clears, no key keeps).
- `always_ask`: each call needs approval even if `allowedTools` covers it; goes to `canUseTool` / `permissionPromptToolName`; in `dontAsk` denied; in `auto`, `plan` and `bypassPermissions` it may be approved earlier (auto classifier; `plan` with `readOnlyHint: true` goes to classifier; with `CLAUDE_CODE_REMOTE=true`, bypass in a cloud session approves without callback). With no callback or `permissionPrompts: 'none'`, it is denied unless a `PermissionRequest` hook allows it.
- `always_deny`: removes the tool from context in every mode incl. `bypassPermissions` (Claude Code v2.1.324+). `always_allow` and `org_max_permission` are ignored on in-process servers; use `allowedTools`. Older Claude Code ignores the list.
- `SdkPluginConfig`: `{ type: "local", path, skipMcpDiscovery? }` (only local plugins supported; `skipMcpDiscovery` skips the plugin's `.mcp.json`/manifest MCP servers).
- `McpServerProvenance` `{ name, source }`: `source` is `sdk`, `plugin`, or a scope (`user`, `project`, `local`, `dynamic`, `managed`, `enterprise`, `claudeai`, `agent`); base trust on `source`, not `name`. v0.3.274+.

# Limits and defaults

`setMcpServers()` outside a cloud session disconnects servers added by earlier calls and in-process servers it does not name (listed in `removed`); servers from `mcpServers`, settings files and plugins keep running; named built-in servers go to `errors`. An `errors` value starting `Blocked by enterprise` means policy (`allowedMcpServers`/`deniedMcpServers` or managed policy) refused it. `McpServerStatus.status` is `connected|failed|needs-auth|pending|disabled`; tool `_meta.ui` is passed only when init `capabilities` lists `mcp_tool_ui_meta_v1`, with `ui` capped at 4,096 characters.
