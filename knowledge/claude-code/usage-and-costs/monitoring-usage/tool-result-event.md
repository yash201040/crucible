---
type: "Reference"
title: "Tool result event"
description: "claude_code.tool_result: emitted when a tool completes, with success, timing, decision source and git commit identity."
resource: "https://code.claude.com/docs/en/monitoring-usage"
tags: [events, tools, audit, git]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "claude_code.tool_result"
  - "tool_name"
  - "tool_use_id"
  - "success"
  - "duration_ms"
  - "error_type"
  - "decision_type"
  - "decision_source"
  - "tool_input_size_bytes"
  - "tool_result_size_bytes"
  - "mcp_server_scope"
  - "vcs.ref.head.revision"
  - "vcs.ref.head.name"
  - "vcs.ref.head.type"
  - "tool_parameters"
  - "tool_input"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "monitoring-usage"
    resource: "https://code.claude.com/docs/en/monitoring-usage"
    title: "Monitoring"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Logged when a tool completes execution. Not emitted for rejected calls (see the [tool decision event](./tool-decision-event.md)).

# How to use it

| Attribute | Meaning |
| - | - |
| `tool_name` | Tool name |
| `tool_use_id` | Same as the ID passed to hooks, so OTel events can be joined to hook-captured data |
| `request_id` | ID of the API response that contained the call (v2.1.310+) |
| `success` | `"true"`/`"false"` |
| `duration_ms` | Execution time |
| `error_type` | e.g. `Error:ENOENT`, `ShellError` |
| `error` | Full message, with `OTEL_LOG_TOOL_DETAILS=1` |
| `decision_type` | Always `accept` |
| `decision_source` | `config`, `hook`, `user_permanent`, `user_temporary` (`user_abort`/`user_reject` never appear) |
| `tool_input_size_bytes`, `tool_result_size_bytes` | Sizes in bytes |
| `mcp_server_scope` | For MCP tools |
| `vcs.ref.head.revision`, `.name`, `.type` | With DETAILS: commit SHA, branch, `branch` of a successful `git commit` by Bash/PowerShell; name and type omitted on detached HEAD; v2.1.269+ |
| `tool_parameters` | With DETAILS, JSON string. Bash: `bash_command`, `full_command`, `timeout`, `description`, `dangerouslyDisableSandbox`, plus `git_commit_id` and `git_branch` after a successful commit. Desktop workspace Bash: only `bash_command`, `full_command`, `timeout`. MCP: `mcp_server_name`, `mcp_tool_name`. Skill: `skill_name`. Agent/Task: `subagent_type` |
| `tool_input` | With DETAILS, JSON arguments; values over 512 chars truncated, total bounded to about 4K chars; all tools incl. MCP |
