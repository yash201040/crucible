---
type: "Reference"
title: "Permission mode, auth, MCP, error and survey events"
description: "permission_mode_changed, auth, mcp_server_connection, internal_error and feedback_survey events."
resource: "https://code.claude.com/docs/en/monitoring-usage"
tags: [events, mcp, auth, permission-mode]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "claude_code.permission_mode_changed"
  - "claude_code.auth"
  - "claude_code.mcp_server_connection"
  - "claude_code.internal_error"
  - "claude_code.feedback_survey"
  - "from_mode"
  - "to_mode"
  - "trigger"
  - "auth_method"
  - "error_category"
  - "transport_type"
  - "server_scope"
  - "is_plugin"
  - "plugin_id_hash"
  - "server_name"
  - "error_name"
  - "CLAUDE_CODE_ENABLE_FEEDBACK_SURVEY_FOR_OTEL"
  - "DISABLE_ERROR_REPORTING"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "monitoring-usage"
    resource: "https://code.claude.com/docs/en/monitoring-usage"
    title: "Monitoring"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Smaller events, all with standard attributes plus `event.name`, `event.timestamp`, `event.sequence`.

# How to use it

| Event | Logged when | Attributes |
| - | - | - |
| `claude_code.permission_mode_changed` | Permission mode changes (Shift+Tab, exiting plan mode, auto mode gate check) | `from_mode`, `to_mode`, `trigger` (`shift_tab`, `exit_plan_mode`, `auto_gate_denied`; absent for some changes such as SDK `setPermissionMode()`) |
| `claude_code.auth` | `/login` or `/logout` completes | `action` (`login`/`logout`), `success`, `auth_method` (e.g. `oauth`), `error_category`, `status_code` (string) |
| `claude_code.mcp_server_connection` | MCP server connects, disconnects or fails | `status` (`connected`,`failed`,`disconnected`), `transport_type` (`stdio`,`sse`,`http`), `server_scope` (`user`,`project`,`local`), `duration_ms`, `error_code`, `is_plugin`, `plugin_id_hash`, `plugin.name`; with DETAILS also `server_name`, `error` |
| `claude_code.internal_error` | Claude Code catches an unexpected internal error (class name and errno-style code only, never message or stack) | `error_name`, `error_code`. Not emitted on Amazon Bedrock, Google Cloud's Agent Platform, Microsoft Foundry, or when `DISABLE_ERROR_REPORTING` is set |
| `claude_code.feedback_survey` | A session quality survey is shown or answered | `event_type` (`appeared`,`responded`,`transcript_prompt_appeared`), `appearance_id`, `survey_type` (`session` = "How is Claude doing?"), `response`, `enabled_via_override` (Boolean, true when `CLAUDE_CODE_ENABLE_FEEDBACK_SURVEY_FOR_OTEL` is set) |

# Notes

`plugin.name` on third-party plugins is `third-party` unless `OTEL_LOG_TOOL_DETAILS=1`; `plugin_id_hash` and `plugin.name` go only to your backend.
