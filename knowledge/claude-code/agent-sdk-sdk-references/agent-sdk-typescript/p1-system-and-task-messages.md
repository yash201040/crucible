---
type: "Reference"
title: "System, task, progress and status stream messages"
description: "The SDKMessage union members for init, tasks, hooks, tool progress, rate limits, session state, plugin install and conversation reset."
resource: "https://code.claude.com/docs/en/agent-sdk/typescript"
tags: [messages, tasks, init, progress, rate-limit, session-state]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [sdk, headless]
requires: ""
identifiers:
  - "SDKMessage"
  - "SDKAssistantMessage"
  - "SDKSystemMessage"
  - "SDKPartialAssistantMessage"
  - "SDKCompactBoundaryMessage"
  - "SDKInformationalMessage"
  - "SDKWorkerShuttingDownMessage"
  - "SDKPluginInstallMessage"
  - "SDKPermissionDeniedMessage"
  - "SDKPermissionDenial"
  - "SDKContextUsage"
  - "SDKUsageReport"
  - "SDKTaskStartedMessage"
  - "SDKTaskProgressMessage"
  - "SDKTaskUpdatedMessage"
  - "SDKTaskNotificationMessage"
  - "SDKBackgroundTasksChangedMessage"
  - "SDKHookStartedMessage"
  - "SDKHookProgressMessage"
  - "SDKHookResponseMessage"
  - "SDKToolProgressMessage"
  - "SDKThinkingTokensMessage"
  - "SDKSessionStateChangedMessage"
  - "SDKRateLimitEvent"
  - "SDKCommandsChangedMessage"
  - "SDKConversationResetMessage"
  - "SDKControlRequestProgressMessage"
  - "SDKModelRefusalFallbackMessage"
  - "SDKModelRefusalNoFallbackMessage"
  - "SDKStatusMessage"
  - "SDKFilesPersistedEvent"
  - "SDKPromptSuggestionMessage"
  - "SDKToolUseSummaryMessage"
  - "SDKAuthStatusMessage"
  - "CLAUDE_CODE_EMIT_SESSION_STATE_EVENTS"
  - "CLAUDE_CODE_BG_TASKS_REPORT_RUNNING"
  - "CLAUDE_CODE_SYNC_PLUGIN_INSTALL"
  - "agent_id"
  - "parent_tool_use_id"
  - "run_id"
  - "parent_task_id"
  - "spawn_depth"
  - "is_backgrounded"
  - "ambient"
  - "heartbeat"
  - "subagent_retry"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-typescript"
    resource: "https://code.claude.com/docs/en/agent-sdk/typescript"
    title: "Agent SDK reference - TypeScript"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`SDKMessage` is the union a `query()` yields. Besides assistant, user and result messages it includes many `type: "system"` subtypes (distinguish by `subtype`) used to watch agents, tasks, hooks and sessions.

# How to use it

- `SDKSystemMessage` (`subtype: "init"`): `claude_code_version`, `cwd`, `tools` (lists Agent tool as `Task`), `mcp_servers` (`source` v0.3.274+), `model`, `permissionMode`, `slash_commands`, `terminal_slash_commands` (v0.3.229+), `skills`, `plugins`, `plugin_errors` (v0.3.283+), `apiKeySource`, `fast_mode_state`, `effort` (Remote Control init only, v0.3.234+), and `capabilities` (v2.1.205+; open set, feature-detect). Capabilities: `interrupt_receipt_v1`, `interrupt_cancel_queued_v1`, `sdk_mcp_manifests` (v2.1.286+), `sdk_mcp_tools_list_changed` (v2.1.286+).
- `SDKAssistantMessage`: `error` is one of `authentication_failed`, `oauth_org_not_allowed`, `account_on_hold`, `billing_error`, `rate_limit`, `overloaded`, `invalid_request`, `model_not_found`, `server_error`, `max_output_tokens`, `cloud_credential_error` (v0.3.267+), `unknown`; also `aborted` (v0.3.214+), `supersedes`, `agent_id` (v0.3.292+, equals the subagent `task_id`; match subagent messages on `agent_id`, not `parent_tool_use_id`), `context_usage` (`SDKContextUsage`, v0.3.232+, only on `/context` reply), `usage_report` (`SDKUsageReport`, experimental shape, v0.3.273+, needs claude.ai credential with plan type or `user:profile` scope, not usage-based billing).
- Tasks: `task_started` (`task_id`, `run_id` v0.3.292+, `task_type` `local_bash|local_agent|mcp_task|remote_agent`, `is_backgrounded` and `spawn_depth` v0.3.238+, `parent_task_id` v0.3.292+, `ambient` v0.3.247+), `task_progress` (usage totals, `summary` only with `agentProgressSummaries`), `task_updated` (patch with status `pending|running|completed|failed|killed`), `task_notification` (`status` `completed|failed|stopped`, `reason: "worker_restart"` v0.3.273+, `output_file`, `usage`, `resource_links`), `background_tasks_changed` (v2.1.203+; full live set; replace cache each time; snapshot after repeated initialize; no startup emission). Each run of a resumed task has a new `run_id`.
- Hook messages: `hook_started`, `hook_progress`, `hook_response` (`outcome` `success|error|cancelled`). Live delivery restored in v2.1.204 (v2.1.169-203 batched them).
- `tool_progress`: heartbeat every 30 s with `heartbeat: true` for main-conversation tool calls (v0.3.214+; none for calls inside a subagent); `subagent_type` and `subagent_retry` `{ agent_id, attempt, max_retries, retry_delay_ms, error_status, error_category }` (categories `rate_limit`, `overloaded`, `authentication_failed`, `server_error`, `cloud_credential_error`, `unknown`); track indicators by `parent_tool_use_id`; heartbeats whose `tool_use_id` starts with `hook-` come from long-running hooks (v0.3.323+).
- `permission_denied` (`tool_name`, `tool_use_id`, `decision_reason_type`, `decision_reason`, `message`): best-effort; `permission_denials` on the result is authoritative. Not emitted for `PreToolUse` hook denials, nor at all with a `permissionPromptToolName` MCP tool plus default `permissionPrompts`. Before v2.1.223 not emitted in runs without a callback.
- `session_state_changed`: requires `CLAUDE_CODE_EMIT_SESSION_STATE_EVENTS=1`; `state` `running|idle|requires_action`; `idle` and `result` can arrive in either order; `CLAUDE_CODE_BG_TASKS_REPORT_RUNNING` changes whether idle waits for background work.
- `rate_limit_event` (`status` `allowed|allowed_warning|rejected`, `resetsAt`, `utilization`, `errorCode: "credits_required"` v2.1.181+, `overageEnabled` v2.1.295+).
- `plugin_install` (needs `CLAUDE_CODE_SYNC_PLUGIN_INSTALL`), `worker_shutting_down` (`reason` such as `host_exit`; ignore replays), `commands_changed` (MCP prompts v2.1.281+), `conversation_reset` (only `/clear` in `query()`; `trigger` v2.1.281+), `control_request_progress` (v0.3.203+), `model_refusal_fallback` (v0.3.170+), `model_refusal_no_fallback` (v0.3.193+), `compact_boundary`, `status` (`compacting`), `informational` (hook `systemMessage` v2.1.227+), `files_persisted`, `prompt_suggestion`, `tool_use_summary`, `auth_status`, `thinking_tokens` (v2.1.153+).

# Limits and defaults

`SDKLocalCommandOutputMessage` is never emitted; `/context` and `/usage` output arrives as an assistant message. `SDKContextUsage.over_limit.kind` is `hard_limit` or `compaction_window`. `SDKUsageReport.rate_limits.extra_usage` amounts are minor units (cents for USD); `monthly_limit: null` is not unlimited on Team/Enterprise. Task-notification messages sent to the model get a notice that no human input occurred (except scheduled-trigger framing; before v2.1.205 omitted when idle).
