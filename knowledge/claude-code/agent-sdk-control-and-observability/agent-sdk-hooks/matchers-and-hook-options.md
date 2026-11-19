---
type: "Reference"
title: "HookMatcher fields and matcher rules"
description: "The matcher, hooks, timeout and onFailure fields of a hook registration, and how patterns match tool names."
resource: "https://code.claude.com/docs/en/agent-sdk/hooks"
tags: [hooks, matcher, timeout, regex]
kind: "api"
maturity: "unlabelled"
since: "2.1.314"
surfaces: [sdk]
requires: ""
identifiers:
  - "matcher"
  - "hooks"
  - "timeout"
  - "onFailure"
  - "on_failure"
  - "^mcp__"
  - "Write|Edit|NotebookEdit"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-hooks"
    resource: "https://code.claude.com/docs/en/agent-sdk/hooks"
    title: "Intercept and control agent behavior with hooks"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The `matcher` field matches a different value per event type: tool-based hooks match the tool name, `Notification` matches the notification type. SDK matchers follow the same rules as settings-file matchers (exact-string and regex paths; see the hooks reference, matcher patterns).

# How to use it

| Option | Type | Default | Description |
| - | - | - | - |
| `matcher` | string | undefined | pattern vs the event's filter field; for tools, the tool name (`Bash`, `Read`, `Write`, `Edit`, `Glob`, `Grep`, `WebFetch`, `Agent`, ...). MCP tools: `mcp__<server>__<action>` |
| `hooks` | `HookCallback[]` | required | callbacks to run on a match |
| `timeout` | number | undefined | seconds; omitted means the event default; SDK callbacks follow `command` hook defaults |
| `onFailure` | `"continue"` or `"block"` | undefined | what a failed callback does; Python `on_failure` |

Examples: `Write|Edit|NotebookEdit` (pipe-separated exact list), `^mcp__` (regex, all MCP tools), no matcher (every event). Matchers only match tool names, not file paths or arguments; check `tool_input.file_path` inside the hook. With a `Bash` matcher, callbacks run for Bash commands and, on Claude Code v2.1.314 or later, also on `PreToolUse` and `PermissionRequest` for Monitor commands, which they can deny but not approve. `Stop` ignores matchers entirely; non-tool hooks like `Notification` and `SubagentStop` match different fields.
