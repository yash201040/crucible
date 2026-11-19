---
type: "Reference"
title: "What each event's matcher filters"
description: "Per-event table of the field a matcher is tested against and its allowed values."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, matcher, events, reference]
kind: "hook"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "startup"
  - "resume"
  - "clear"
  - "compact"
  - "fork"
  - "init"
  - "maintenance"
  - "logout"
  - "prompt_input_exit"
  - "other"
  - "permission_prompt"
  - "idle_prompt"
  - "auth_success"
  - "auth_storage_failure"
  - "elicitation_dialog"
  - "elicitation_url_dialog"
  - "elicitation_complete"
  - "elicitation_response"
  - "agent_needs_input"
  - "agent_completed"
  - "quota_auto_resume_fired"
  - "quota_auto_resume_stale"
  - "quota_auto_resume_disabled"
  - "plugin_notification"
  - "manual"
  - "auto"
  - "user_settings"
  - "project_settings"
  - "local_settings"
  - "policy_settings"
  - "skills"
  - "slash_command"
  - "register_repo_root"
  - "rate_limit"
  - "authentication_failed"
  - "oauth_org_not_allowed"
  - "account_on_hold"
  - "billing_error"
  - "invalid_request"
  - "model_not_found"
  - "server_error"
  - "max_output_tokens"
  - "cloud_credential_error"
  - "unknown"
  - "session_start"
  - "nested_traversal"
  - "path_glob_match"
  - "include"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Each event matches on a different field of its input. Tool events match `tool_name`; `PreModelSwitch`/`PostModelSwitch` match the canonical name derived from `to_model`.

# How to use it

| Event | Matcher filters | Values |
| :- | :- | :- |
| `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `PermissionRequest`, `PermissionDenied` | tool name | `Bash`, `Edit\|Write`, `mcp__.*` |
| `SessionStart` | how session started | `startup`, `resume`, `clear`, `compact`, `fork` |
| `Setup` | which CLI flag | `init`, `maintenance` |
| `SessionEnd` | why it ended | `clear`, `resume`, `logout`, `prompt_input_exit`, `other` |
| `Notification` | notification type | `permission_prompt`, `idle_prompt`, `auth_success`, `auth_storage_failure`, `elicitation_dialog`, `elicitation_url_dialog`, `elicitation_complete`, `elicitation_response`, `agent_needs_input`, `agent_completed`, `quota_auto_resume_fired`, `quota_auto_resume_stale`, `quota_auto_resume_disabled`, `plugin_notification` |
| `SubagentStart`, `SubagentStop` | agent type | `general-purpose`, `Explore`, `Plan`, custom names, plugin-scoped like `^my-plugin:reviewer$` |
| `PreCompact`, `PostCompact` | trigger | `manual`, `auto` |
| `PreModelSwitch`, `PostModelSwitch` | canonical target model name | `claude-opus-5`, `claude-opus-4-6\|claude-opus-5`, `.*opus.*` |
| `ConfigChange` | config source | `user_settings`, `project_settings`, `local_settings`, `policy_settings`, `skills` |
| `DirectoryAdded` | how added | `slash_command`, `register_repo_root` |
| `FileChanged` | literal filenames to watch | `.envrc\|.env` |
| `StopFailure` | error type | `rate_limit`, `authentication_failed`, `oauth_org_not_allowed`, `account_on_hold`, `billing_error`, `invalid_request`, `model_not_found`, `server_error`, `max_output_tokens`, `cloud_credential_error`, `unknown` |
| `InstructionsLoaded` | load reason | `session_start`, `nested_traversal`, `path_glob_match`, `include`, `compact` |
| `UserPromptExpansion` | command name | your skill or command names |
| `Elicitation`, `ElicitationResult` | MCP server name | configured server names |
| `CwdChanged` | no matcher support | always fires |
| `UserPromptSubmit`, `PostToolBatch`, `Stop`, `TeammateIdle`, `TaskCreated`, `TaskCompleted`, `WorktreeCreate`, `WorktreeRemove`, `MessageDisplay` | no matcher support | always fires |

# Notes

Rules for how the matcher string is parsed are in [matcher evaluation rules](./p1-matcher-patterns.md). `cloud_credential_error` needs v2.1.267+.
