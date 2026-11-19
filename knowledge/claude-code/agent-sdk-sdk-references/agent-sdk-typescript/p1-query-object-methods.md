---
type: "Reference"
title: "Query object methods and runtime control"
description: "Methods on the object query() returns: interrupt, mid-session setters, reload, MCP control, background tasks, readFile, and applyFlagSettings rules."
resource: "https://code.claude.com/docs/en/agent-sdk/typescript"
tags: [query-object, runtime-control, streaming-input, mcp, settings]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: "Setters (setModel, setPermissionMode, applyFlagSettings, interrupt) only in streaming input mode"
identifiers:
  - "interrupt()"
  - "rewindFiles()"
  - "setPermissionMode()"
  - "setModel()"
  - "setMaxThinkingTokens()"
  - "applyFlagSettings()"
  - "updateSettings()"
  - "initializationResult()"
  - "reinitialize()"
  - "supportedCommands()"
  - "supportedModels()"
  - "supportedAgents()"
  - "mcpServerStatus()"
  - "getContextUsage()"
  - "readFile()"
  - "reloadPlugins()"
  - "reloadSkills()"
  - "reloadOutputStyles()"
  - "seedReadState()"
  - "accountInfo()"
  - "reconnectMcpServer()"
  - "toggleMcpServer()"
  - "setMcpServers()"
  - "setMcpPermissionModeOverride()"
  - "readMcpResource()"
  - "streamInput()"
  - "stopTask()"
  - "backgroundTasks()"
  - "close()"
  - "holdOnCacheImpact"
  - "addPlugins"
  - "interrupt_receipt_v1"
  - "interrupt_cancel_queued_v1"
  - "ultracode"
  - "effortLevel"
  - "CLAUDE_CODE_DISABLE_BACKGROUND_TASKS"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-typescript"
    resource: "https://code.claude.com/docs/en/agent-sdk/typescript"
    title: "Agent SDK reference - TypeScript"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The `Query` interface extends `AsyncGenerator<SDKMessage, void>` and adds control methods for a running session. This is how a host steers, inspects and tears down an agent without restarting it.

# How to use it

| Method | Notes |
| :- | :- |
| `interrupt()` | Streaming input only. On CLIs advertising `interrupt_receipt_v1` (v2.1.205+) resolves with `{ still_queued: string[]; cancelled?: string[] }`; `undefined` on older CLIs. Receipt lists pending user-message UUIDs (only those with a UUID, main thread only; may include UUIDs you never sent, e.g. scheduled-task triggers). Unlisted-cancelled messages still enter the conversation, so resending delivers twice. Raw control request can set `cancel_queued: true` (capability `interrupt_cancel_queued_v1`, v2.1.219+); `interrupt()` never sends it |
| `rewindFiles(userMessageId, { dryRun? })` | Needs `enableFileCheckpointing: true`; result has `canRewind`, `filesChanged`, `insertions`, `deletions`, `skippedLinks` (v2.1.216+) |
| `setPermissionMode(mode)` / `setModel(model?)` / `setMaxThinkingTokens(n|null)` | Streaming only; `setModel(undefined|"default")` resets; an `auto` session drops to `default` if new model lacks auto mode; `setMaxThinkingTokens` deprecated |
| `applyFlagSettings(settings)` | Streaming only; TypeScript-only (no Python equivalent). Merges into flag-settings layer. Applied next turn: `ultracode`, `permissions`, `hooks`, `skillOverrides`, `fastMode`, `agent`. Current turn: `model` (subagents keep their own; before v2.1.212 waited for next turn). Next call/turn: `effortLevel`. No effect mid-session: system prompt options. Successive calls shallow-merge top-level keys (a new `permissions` replaces the old whole). `null` clears a key; `effortLevel: null`, `agent: null`, `ultracode: null` reset session state. `{ ultracode: true, effortLevel: "xhigh" }` ; `ultracode` needs v2.1.203+ (before v2.1.284 it also set `xhigh`) |
| `updateSettings(source, settings)` | `localSettings` accepts `outputStyle` (writes `.claude/settings.local.json`); `userSettings` accepts `effortLevel` (under `modelSettings`; `max` writes nothing; needs SDK v0.3.277+). Needs SDK v0.3.257+. Rejects other keys, remote transport, or excluded `settingSources` |
| `initializationResult()` / `reinitialize()` | Cached vs fresh init; `reinitialize()` (v2.1.195+) re-delivers pending permission requests to `canUseTool` after a transport gap; make callback idempotent per request ID |
| `supportedCommands()` `supportedModels()` `supportedAgents()` `mcpServerStatus()` `accountInfo()` | Listings; `supportedCommands()` tracks mid-session changes from v0.3.216; `supportedAgents()` keeps init-time list |
| `getContextUsage({ detail })` | `'full'` (default, token-counting API requests not in the stream; unbilled on Anthropic API) or `'summary'` (local estimates); `detail` needs v0.3.257+ |
| `readFile(path, { maxBytes, encoding })` | Default cap 1 MB, ceiling 10 MB; `'utf-8'` or `'base64'`; null on denial/missing; serves files in working dirs and some Claude Code files; Read deny/ask rules still apply; v0.2.121+ |
| `reloadPlugins({ holdOnCacheImpact, addPlugins })` | v0.2.85+; `holdOnCacheImpact` v0.3.268+ returns `held: true` with `cache_impact` instead of applying; `addPlugins` (absolute paths) v0.3.301+ and Claude Code v2.1.301+ |
| `reloadSkills()` / `reloadOutputStyles()` | v0.3.163+ / v0.3.261+ |
| `seedReadState(path, mtime)` | Avoid `File has not been read yet`; whole-ms mtime; skipped if file changed; v0.2.83+ |
| `reconnectMcpServer(name)` / `toggleMcpServer(name, enabled)` / `setMcpServers(servers)` | Name resolution prefers `mcpServers`/`setMcpServers` over settings-file entries (v2.1.257+). Disabling removes tools; mid-session added servers need v2.1.285+, in-process servers v2.1.286+ |
| `setMcpPermissionModeOverride(server, 'default'|'auto'|null)` | Stricter mode for one server; effective only while session is in `bypassPermissions` or `auto`; v0.3.187+; resolves `{ warning }` for unknown server |
| `readMcpResource(server, uri)` | Alpha; `ui://` only; v0.3.280+; capability `mcp_read_resource_v1` |
| `streamInput(stream)` | Multi-turn input |
| `stopTask(taskId)` | Stop background task |
| `backgroundTasks(toolUseId?)` | Same as Ctrl+B; resolves boolean; rejects if background tasks disabled (`CLAUDE_CODE_DISABLE_BACKGROUND_TASKS`); v0.2.139+; emits `task_notification` on finish |
| `close()` | Forcefully ends query and process |

# Limits and defaults

`SDKControlInitializeResponse` fields: `commands`, `agents`, `output_style`, `available_output_styles`, `models`, `account`, `fast_mode_state`, `fast_mode_disabled_reason`, `hooks_applied` (v0.3.238+; false on repeated initialize to a remote session), `claude_code_version` (v0.3.296+), plus a `pending_permission_requests` array on the control-response wrapper (always present, v2.1.268+). `SDKControlGetContextUsageResponse` carries `categories` (`id` values `system_prompt`, `system_tools`, `mcp_tools`, `mcp_instructions`, `mcp_tools_deferred`, `system_tools_deferred`, `custom_agents`, `memory_files`, `skills`, `messages`, `autocompact_buffer`, `compact_buffer`, `free_space`; `kind` `used|free|buffer|deferred`), `totalTokens`, `maxTokens`, `percentage`, `mcpTools`, `memoryFiles`, `agents`, `skills`, `messageBreakdown`, `apiUsage`, `autoCompactThreshold`, `isAutoCompactEnabled`.
