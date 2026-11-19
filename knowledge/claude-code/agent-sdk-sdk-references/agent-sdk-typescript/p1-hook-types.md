---
type: "Reference"
title: "Hook events, inputs and JSON output types"
description: "HookEvent names, HookCallback and HookCallbackMatcher, per-event input fields, and the SyncHookJSONOutput hookSpecificOutput shapes."
resource: "https://code.claude.com/docs/en/agent-sdk/typescript"
tags: [hooks, callbacks, hook-input, hook-output, events]
kind: "hook"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "PreToolUse"
  - "PostToolUse"
  - "PostToolUseFailure"
  - "PostToolBatch"
  - "Notification"
  - "UserPromptSubmit"
  - "UserPromptExpansion"
  - "SessionStart"
  - "SessionEnd"
  - "Stop"
  - "StopFailure"
  - "SubagentStart"
  - "SubagentStop"
  - "PreCompact"
  - "PostCompact"
  - "PreModelSwitch"
  - "PostModelSwitch"
  - "PermissionRequest"
  - "PermissionDenied"
  - "Setup"
  - "TeammateIdle"
  - "TaskCreated"
  - "TaskCompleted"
  - "Elicitation"
  - "ElicitationResult"
  - "ConfigChange"
  - "DirectoryAdded"
  - "WorktreeCreate"
  - "WorktreeRemove"
  - "InstructionsLoaded"
  - "CwdChanged"
  - "FileChanged"
  - "MessageDisplay"
  - "HookEvent"
  - "HookCallback"
  - "HookCallbackMatcher"
  - "onFailure"
  - "BaseHookInput"
  - "HookJSONOutput"
  - "AsyncHookJSONOutput"
  - "SyncHookJSONOutput"
  - "hookSpecificOutput"
  - "permissionDecision"
  - "updatedInput"
  - "additionalContext"
  - "updatedToolOutput"
  - "classifierContext"
  - "sessionTitle"
  - "initialUserMessage"
  - "watchPaths"
  - "reloadSkills"
  - "displayContent"
  - "terminalSequence"
  - "prompt_id"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-typescript"
    resource: "https://code.claude.com/docs/en/agent-sdk/typescript"
    title: "Agent SDK reference - TypeScript"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

TypeScript types for SDK hook callbacks registered through the `hooks` option: `Partial<Record<HookEvent, HookCallbackMatcher[]>>`. A callback is `(input: HookInput, toolUseID: string | undefined, { signal }) => Promise<HookJSONOutput>`.

# How to use it

- `HookCallbackMatcher`: `{ matcher?: string; hooks: HookCallback[]; timeout?: number (seconds, for all hooks in the matcher); onFailure?: "continue" | "block" }`. `"block"` blocks the action when a callback fails.
- Events (33): `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `PostToolBatch`, `Notification`, `UserPromptSubmit`, `UserPromptExpansion`, `SessionStart`, `SessionEnd`, `Stop`, `StopFailure`, `SubagentStart`, `SubagentStop`, `PreCompact`, `PostCompact`, `PreModelSwitch`, `PostModelSwitch`, `PermissionRequest`, `PermissionDenied`, `Setup`, `TeammateIdle`, `TaskCreated`, `TaskCompleted`, `Elicitation`, `ElicitationResult`, `ConfigChange`, `DirectoryAdded`, `WorktreeCreate`, `WorktreeRemove`, `InstructionsLoaded`, `CwdChanged`, `FileChanged`, `MessageDisplay`.
- All inputs extend `BaseHookInput`: `session_id`, `transcript_path`, `cwd`, `prompt_id` (v2.1.196+, matches OpenTelemetry `prompt.id`), `permission_mode`, `effort { level }`, `agent_id`, `agent_type`.
- Tool events carry `tool_name`, `tool_input`, `tool_use_id`, and `mcp_server` (v0.3.274+). `PostToolUse` adds `tool_response`, `duration_ms`; `PostToolUseFailure` adds `error`, `is_interrupt`; `PostToolBatch` fires once after all calls in a batch resolve and carries `tool_calls`; `PermissionDenied` adds `reason`.
- `Stop` / `SubagentStop`: `stop_hook_active`, `last_assistant_message`, `background_tasks` (`BackgroundTaskSummary`), `session_crons` (`SessionCronSummary`); `SubagentStop` adds `agent_id`, `agent_transcript_path`, `agent_type`. `StopFailure`: `error`, `error_details`.
- `PreModelSwitch` / `PostModelSwitch`: `from_model`, `to_model`, `requested_model`, `source` (`command|picker|sdk`, post adds `auto|resume`), `context_tokens`, `prompt_cache_warm`, `cache_ttl` (`5m|1h`), `estimated_cache_write_usd`, `pricing` (`configured|catalog|default`).
- Others: `SessionStart` (`source` `startup|resume|clear|compact|fork`), `SessionEnd` (`reason`), `PreCompact`/`PostCompact` (`trigger` `manual|auto`), `Setup` (`trigger` `init|maintenance`), `TeammateIdle` (`teammate_name`; `team_name` deprecated since v2.1.178), `TaskCreated`/`TaskCompleted` (`task_id`, `task_subject`), `Elicitation`/`ElicitationResult`, `ConfigChange` (`source`), `InstructionsLoaded` (`memory_type`, `load_reason`), `DirectoryAdded` (`source` `slash_command|register_repo_root`), `WorktreeCreate` (`name`), `WorktreeRemove` (`worktree_path`), `CwdChanged`, `FileChanged` (`event` `change|add|unlink`), `MessageDisplay` (`turn_id`, `message_id`, `index`, `final`, `delta`).
- Output: `AsyncHookJSONOutput` `{ async: true; asyncTimeout? }`. `SyncHookJSONOutput`: `continue`, `suppressOutput`, `stopReason`, `decision` (`approve|block`), `systemMessage`, `reason`, `terminalSequence` (interactive CLI only; SDK ignores it), and `hookSpecificOutput` by event: `PreToolUse` (`permissionDecision` `allow|deny|ask|defer`, `permissionDecisionReason`, `updatedInput`, `additionalContext`), `UserPromptSubmit` (`additionalContext`, `sessionTitle`, `suppressOriginalPrompt`), `SessionStart` (`additionalContext`, `initialUserMessage`, `sessionTitle`, `watchPaths`, `reloadSkills`), `PreModelSwitch` (`permissionDecision` `allow|deny|ask`; only interactive `/model` shows `ask`, others treat it as refusal), `PostToolUse` (`additionalContext`, `classifierContext` capped at 2000 chars, `updatedToolOutput`; `updatedMCPToolOutput` deprecated), `PermissionDenied` (`retry`), `PermissionRequest` (`decision` allow/deny with `updatedInput`, `updatedPermissions`, `message`, `interrupt`), `Elicitation`/`ElicitationResult` (`action`, `content`), `CwdChanged`/`FileChanged` (`watchPaths`), `WorktreeCreate` (`worktreePath`), `MessageDisplay` (`displayContent`), and `additionalContext` for `UserPromptExpansion`, `Setup`, `PostModelSwitch`, `SubagentStart`, `PostToolUseFailure`, `PostToolBatch`, `Stop`, `SubagentStop`, `Notification`.

# Limits and defaults

Hook lifecycle messages in the stream need `includeHookEvents` (except SessionStart and Setup). `Notification`, `SessionEnd`, `PreCompact`, `PostCompact` never produce `hook_started`. Hooks guide: https://code.claude.com/docs/en/agent-sdk/hooks.
