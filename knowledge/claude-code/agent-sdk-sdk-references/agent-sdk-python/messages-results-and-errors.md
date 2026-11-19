---
type: "Reference"
title: "Messages, ResultMessage cost fields and errors"
description: "Python message types, ResultMessage fields and subtypes, usage and model_usage accounting, rate-limit events and exception classes."
resource: "https://code.claude.com/docs/en/agent-sdk/python"
tags: [messages, cost, usage, errors, rate-limits]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "Message"
  - "UserMessage"
  - "AssistantMessage"
  - "SystemMessage"
  - "ResultMessage"
  - "StreamEvent"
  - "RateLimitEvent"
  - "RateLimitInfo"
  - "ConversationResetMessage"
  - "total_cost_usd"
  - "model_usage"
  - "ModelUsage"
  - "terminal_reason"
  - "stop_reason"
  - "api_error_status"
  - "permission_denials"
  - "deferred_tool_use"
  - "structured_output"
  - "error_during_execution"
  - "error_max_turns"
  - "error_max_budget_usd"
  - "error_max_structured_output_retries"
  - "ClaudeSDKError"
  - "CLINotFoundError"
  - "CLIConnectionError"
  - "ProcessError"
  - "ResultError"
  - "CLIJSONDecodeError"
  - "AssistantMessageError"
  - "TextBlock"
  - "ThinkingBlock"
  - "ToolUseBlock"
  - "ToolResultBlock"
  - "resourceLinks"
  - "resource_links"
  - "origin"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-python"
    resource: "https://code.claude.com/docs/en/agent-sdk/python"
    title: "Agent SDK reference - Python"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The stream from `query()` or `receive_messages()` yields a `Message` union: `UserMessage`, `AssistantMessage`, `SystemMessage`, `ResultMessage`, `StreamEvent`, `RateLimitEvent`, `ConversationResetMessage`. Content blocks: `TextBlock`, `ThinkingBlock`, `ToolUseBlock`, `ToolResultBlock`, `ServerToolUseBlock`, `ServerToolResultBlock`.

# How to use it

`ResultMessage` (final message): `subtype` (`"success"`, `"error_during_execution"`, `"error_max_turns"`, `"error_max_budget_usd"`, `"error_max_structured_output_retries"`), `duration_ms`, `duration_api_ms`, `is_error`, `num_turns`, `session_id`, `stop_reason`, `total_cost_usd`, `usage`, `result`, `structured_output`, `model_usage`, `permission_denials`, `deferred_tool_use`, `errors`, `api_error_status`, `uuid`, `terminal_reason`, `origin`.
- `is_error` on `"success"` can be True: check `stop_reason` for `"refusal"` or `"tool_deferred_unavailable"` (a deferred tool was unavailable on resume; the call stays pending unless dropped), otherwise read `terminal_reason`, `result`, `api_error_status`.
- `terminal_reason` examples: `"completed"`, `"max_turns"`, `"api_error"`, `"aborted_streaming"`, `"aborted_tools"`; `None` on old CLIs, local commands such as `/voice` or `/usage`, or synthesized fatal-error results.
- `origin` (SDK 0.2.137+): `None` or `{"kind":"human"}` for your own prompt, `"task-notification"` for a background-task turn. When several background tasks finish together, you get one `ResultMessage` per notification; all but the last have `num_turns` 0 and empty `result`.

`usage` covers the main loop only (keys `input_tokens`, `output_tokens`, `cache_creation_input_tokens`, `cache_read_input_tokens`); in streaming input mode it is per turn. `model_usage` (prefer it for accounting) maps model name to `ModelUsage` and covers main loop, subagents and internal calls such as compaction and Workflow agents; it excludes the permission classifier and token-counting calls. In streaming input mode `model_usage` and `total_cost_usd` are cumulative: read the latest, do not sum. Treat as an estimate, not billing.

| `ModelUsage` key | Notes |
| :- | :- |
| `inputTokens`, `outputTokens`, `cacheReadInputTokens`, `cacheCreationInputTokens`, `webSearchRequests` | counts |
| `thinkingTokens` | included in `outputTokens`; read with `.get()`; SDK 0.2.150+ |
| `costUSD` | client-side estimate |
| `contextWindow`, `maxOutputTokens` | model limits |
| `canonicalModel`, `provider` | pricing id; provider such as `firstParty`, `bedrock`, `vertex`, `foundry`, `anthropicAws`, `mantle`, `gateway` |
| `costBasis` | `list`, `managed` (a `modelPricing` table) or `unknown`; Claude Code 2.1.246+; read with `.get()` |

Other messages: `StreamEvent` (only with `include_partial_messages=True`; `parent_tool_use_id` always `None`, main session only). `RateLimitEvent` carries `RateLimitInfo`: `status` (`allowed`, `allowed_warning`, `rejected`), `resets_at`, `rate_limit_type` (`five_hour`, `seven_day`, `seven_day_opus`, `seven_day_sonnet`, `overage`), `utilization` (0.0 to 1.0), `overage_status`, `overage_resets_at`, `overage_disabled_reason`, `raw`. `ConversationResetMessage` (SDK 0.2.137+) is emitted after something like `/clear`; later messages carry a new `session_id`. `AssistantMessage` has `usage`, `message_id`, `stop_reason`, `error`; `AssistantMessageError` literals `authentication_failed`, `billing_error`, `rate_limit`, `invalid_request`, `server_error`, `unknown` (the CLI may emit others such as `max_output_tokens`; treat as `unknown`).

`UserMessage.tool_use_result` for external MCP tools with `resource_link` blocks holds `resourceLinks` (max 50 links, list capped at 64 KiB of JSON; omitted for subagent results and in-process `tool()` tools); needs SDK 0.2.150+ and Claude Code 2.1.257+. The same links arrive as `resource_links` in `message.data` of a `"completed"` `TaskNotificationMessage` for a backgrounded MCP call.

# Limits and defaults

Exceptions: `ClaudeSDKError` (base), `CLIConnectionError`, `CLINotFoundError` (CLI missing), `ProcessError` (`exit_code`, `stderr`), `ResultError` (subclass of `ProcessError`, SDK 0.2.140+; raised when a single-shot `query()` ends in an error result; attributes `subtype`, `errors`, `result`, `api_error_status`, `terminal_reason`, `session_id`, `data`), `CLIJSONDecodeError` (bad JSON or a message above `max_buffer_size`). Classify a failure by `data["stop_reason"]` first, then `terminal_reason`, then `subtype`. Catch `ResultError` before `ProcessError`.
