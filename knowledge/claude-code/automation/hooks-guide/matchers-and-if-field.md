---
type: "Reference"
title: "Hook matchers and the if field"
description: "What each event's matcher filters, example values, and permission-rule-syntax if filtering for tool events."
resource: "https://code.claude.com/docs/en/hooks-guide"
tags: [hooks, matchers, if-field, filtering]
kind: "hook"
maturity: "unlabelled"
since: ""
surfaces: [cli, sdk]
requires: ""
identifiers:
  - "matcher"
  - "if"
  - "Bash(git *)"
  - "Edit(*.ts)"
  - "mcp__<server>__<tool>"
  - "mcp__.*"
  - "mcp__plugin_my-plugin_db__query"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks-guide"
    resource: "https://code.claude.com/docs/en/hooks-guide"
    title: "Automate actions with hooks"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Without a matcher a hook fires on every occurrence of its event. `"Edit|Write"` or `"Edit, Write"` (comma) fires only for those tools. Matchers are case-sensitive. Hooks that must see every file change should add a `Stop` hook scanning the working tree, or also match `Bash|PowerShell` and list files with `git status --porcelain`; `FileChanged` runs when a specific file changes whatever wrote it.

# How to use it

| Event | Matcher filters | Examples |
| --- | --- | --- |
| `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `PermissionRequest`, `PermissionDenied` | tool name | `Bash`, `Edit\|Write`, `mcp__.*` |
| `SessionStart` | how it started | `startup`, `resume`, `clear`, `compact`, `fork` |
| `Setup` | CLI flag | `init`, `maintenance` |
| `SessionEnd` | why it ended | `clear`, `resume`, `logout`, `prompt_input_exit`, `other` |
| `Notification` | notification type | see notification matchers |
| `SubagentStart`, `SubagentStop` | agent type | `general-purpose`, `Explore`, `Plan`, custom names |
| `PreCompact`, `PostCompact` | trigger | `manual`, `auto` |
| `PreModelSwitch`, `PostModelSwitch` | canonical model name switched to | `claude-opus-5`, `.*opus.*` |
| `ConfigChange` | config source | `user_settings`, `project_settings`, `local_settings`, `policy_settings`, `skills` |
| `DirectoryAdded` | how added | `slash_command`, `register_repo_root` |
| `StopFailure` | error type | `rate_limit`, `authentication_failed`, `oauth_org_not_allowed`, `account_on_hold`, `billing_error`, `invalid_request`, `model_not_found`, `server_error`, `max_output_tokens`, `cloud_credential_error`, `unknown` |
| `InstructionsLoaded` | load reason | `session_start`, `nested_traversal`, `path_glob_match`, `include`, `compact` |
| `Elicitation`, `ElicitationResult` | MCP server name | configured names |
| `FileChanged` | literal filenames | `.envrc\|.env` |
| `UserPromptExpansion` | command name | skill or command names |
| `UserPromptSubmit`, `PostToolBatch`, `Stop`, `TeammateIdle`, `TaskCreated`, `TaskCompleted`, `WorktreeCreate`, `WorktreeRemove`, `CwdChanged`, `MessageDisplay` | no matcher support | always fires |

MCP tools are named `mcp__<server>__<tool>` (plugin-bundled servers use a scoped segment like `mcp__plugin_my-plugin_db__query`); use regex such as `mcp__github__.*` or `mcp__.*__write.*`.

`if` field: permission rule syntax on a handler (`"if": "Bash(git *)"`, `"Edit(*.ts)"`) so the process spawns only on matching calls. For Bash each subcommand is checked, including inside `$()` and backticks; patterns specifying more than the command name run anyway on `$()`, backticks or `$VAR`; if the input cannot be split, the hook runs regardless. Best-effort: use permissions for hard enforcement.

# Limits and defaults

`if` works only on `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `PermissionRequest`, `PermissionDenied`; on any other event it prevents the hook from running. For several tool names use separate handlers or the `matcher` pipe.
