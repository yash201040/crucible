---
type: "Reference"
title: "SDKResultMessage, SDKUserMessage and message origin"
description: "Result fields (cost, usage, terminal_reason, startup failures), user message controls (priority, shouldQuery), UUID echoing and origin kinds."
resource: "https://code.claude.com/docs/en/agent-sdk/typescript"
tags: [result, cost, usage, origin, user-message, startup-failure]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [sdk, headless]
requires: ""
identifiers:
  - "SDKResultMessage"
  - "SDKUserMessage"
  - "SDKUserMessageReplay"
  - "SDKMessageOrigin"
  - "total_cost_usd"
  - "modelUsage"
  - "usage"
  - "num_turns"
  - "permission_denials"
  - "terminal_reason"
  - "result_index"
  - "queued_turn_count"
  - "deferred_tool_use"
  - "structured_output"
  - "startup_failure_reason"
  - "SDKStartupFailureReason"
  - "CLAUDE_CODE_STARTUP_FAILURE_RESULTS"
  - "error_max_turns"
  - "error_during_execution"
  - "error_max_budget_usd"
  - "error_max_structured_output_retries"
  - "user_message_uuid"
  - "user_message_uuids"
  - "resume_reason"
  - "CLAUDE_CODE_RESUME_INTERRUPTED_TURN"
  - "shouldQuery"
  - "client_composed"
  - "priority"
  - "isSynthetic"
  - "pasted_content"
  - "inline_pastes"
  - "origin"
  - "CLAUDE_CODE_HOST_SCHEDULED_RUN"
  - "fast_mode_disabled_reason"
  - "tool_use_result"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-typescript"
    resource: "https://code.claude.com/docs/en/agent-sdk/typescript"
    title: "Agent SDK reference - TypeScript"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`SDKResultMessage` is the final message of a turn. Success arm: `subtype: "success"` with `result`, `structured_output`, `stop_reason`, timings. Error arm: `subtype` `error_max_turns`, `error_during_execution`, `error_max_budget_usd` or `error_max_structured_output_retries`, with an `errors: string[]`. Both carry `duration_ms`, `duration_api_ms`, `is_error`, `num_turns`, `total_cost_usd`, `usage`, `modelUsage`, `permission_denials`.

# How to use it

- Cost and tokens: use `modelUsage` (per-model totals for every call in the query pipeline: main loop, subagents, compaction, Workflow agents; excludes permission classifier and token-count calls; cumulative across turns in streaming input, so read the latest result). `usage` is the main loop only, per-turn in streaming input. `total_cost_usd` is a client-side estimate, not a billing statement.
- `terminal_reason`: `completed`, `max_turns`, `tool_deferred`, `aborted_streaming`, `aborted_tools`, `hook_stopped`, `stop_hook_prevented`, `background_requested`, `blocking_limit`, `rapid_refill_breaker`, `prompt_too_long`, `image_error`, `model_error`, `api_error`, `malformed_tool_use_exhausted`, `budget_exhausted`, `structured_output_retry_exhausted`, `tool_deferred_unavailable`, `turn_setup_failed`.
- A `PreToolUse` hook returning `permissionDecision: "defer"` yields `stop_reason: "tool_deferred"` and `deferred_tool_use { id, name, input }`; resume with the same `session_id`.
- Other result fields: `api_error_status`, `ttft_ms`, `ttft_stream_ms`, `time_to_request_ms` (v2.1.162+), `local_command` (v0.3.268+), `result_index` (v0.3.268+; gap = lost result), `queued_turn_count` (v0.3.242+; counts only `origin: {kind:"human"}` messages), `fast_mode_state` (`on|off|cooldown`) and `fast_mode_disabled_reason` (codes `free`, `preference`, `extra_usage_disabled`, `network_error`, `unknown`, `not_first_party`, `disabled_by_env`, `model_not_allowed`, `sdk_opt_in_required`, `pending`; v2.1.219+).
- `startup_failure_reason` (v0.3.274+) on an `error_during_execution` result with zeroed totals. Set `CLAUDE_CODE_STARTUP_FAILURE_RESULTS=1` in `env` to get it for every value; otherwise only for worktree resume failures (`worktree_unverified`, `worktree_resume_refused`), `session_held_by_background`, `sandbox_required_unavailable` and `config_file_invalid`. Values: `org_pin_api_key_conflict`, `provider_not_allowed`, `org_verify_failed`, `org_pin_mismatch`, `managed_settings_invalid`, `remote_settings_required_unavailable`, `gateway_signin_required`, `gateway_access_denied`, `proxy_invalid`, `temp_dir_unusable`, `cwd_unavailable`, `shell_tool_missing`, `session_held_by_background`, `worktree_resume_refused`, `worktree_unverified`, `cli_version_too_old`, `bypass_root`, `org_config_required_unavailable`, `org_config_refused`, `sandbox_required_unavailable`, `config_file_invalid`.
- Message UUID echo: set a `uuid` on a streamed `SDKUserMessage`; the result, first reply frame (assistant message or first non-ping stream event) and `thinking_tokens` frames echo `user_message_uuid` (and `user_message_uuids`, up to 64, v0.3.259+). Merged messages echo only the last UUID in `user_message_uuid`. A `UserPromptSubmit` hook that blocks a message picked up mid-turn drops it with no result; set a wait timeout. With `continue: false` it is stopped, not dropped. `resume_reason` (e.g. `interrupted_turn`, v0.3.268+) marks a turn continued under `CLAUDE_CODE_RESUME_INTERRUPTED_TURN`.
- `SDKUserMessage` controls: `shouldQuery: false` appends to the transcript without a model call; `client_composed: true` (v0.3.280+, Claude Code v2.1.248+) disables `@path` expansion and `/` command execution; `priority` `'next'` (default), `'later'` (hold until turn ends), `'now'` (interrupts; with `origin: {kind:"human"}` on v2.1.286+ moves shell, subagents, MCP calls to background, v2.1.287+ also WebFetch/WebSearch, leaving `tool_use_result: { detachedToolCall: true }`); `pasted_content` (v0.3.277+, ignored if over 1,000 entries) and `inline_pastes` (v0.3.280+, first 100 non-blank). `tool_use_result` shapes: Agent -> `AgentOutput`; MCP `resourceLinks` (max 50 links, 64 KiB; v0.3.257+); `structuredContent` (omitted past 1,048,576 characters with `structuredContentOmitted: true`, v2.1.287+; `ui://` tools 8,388,608 from v2.1.295; in-process SDK servers exempt).
- `SDKMessageOrigin.kind`: `human`, `channel` (`server`), `peer`, `task-notification` (`subkind` `scheduled-trigger` | `peer-send-message`, `fireReason`, `runId`), `coordinator`, `auto-continuation`, `unclassified` (v2.1.223+). Apps may set only `human` and the scheduled-trigger form. Text the user did not write should be sent with `isSynthetic: true`, `origin` unset and `client_composed: true`.
- Declare a scheduled run: start with `CLAUDE_CODE_HOST_SCHEDULED_RUN=1` in `env`, then send `origin: { kind: "task-notification", subkind: "scheduled-trigger", fireReason: "scheduled" }` without `isSynthetic` (v0.3.280+). Ignored if the process has `CLAUDECODE` or `CLAUDE_CODE_CHILD_SESSION` set. `fireReason` is 1 to 32 lowercase letters or underscores.
- Peer origin fields: `from`, `fromMode` (`bypass|prompting`), `senderTaskId`, `name`, `body`, `fromSession`, `verifiedPeerPid` (use this, not `from`, to identify sender).

# Limits and defaults

Background-task completions queued together can be answered in one turn: all but the last produce empty results with `num_turns: 0`. Check `origin.kind` before suppressing injected follow-up results; a declared scheduled run also carries `task-notification`.
