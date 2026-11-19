---
type: "Reference"
title: "Hook handler types and common fields"
description: "The five handler types and fields shared by all of them: type, if, timeout, statusMessage, once, with timeout defaults and parallelism."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, handlers, timeout, if-filter]
kind: "frontmatter"
maturity: "unlabelled"
since: ""
surfaces: [cli, ide, desktop, cloud]
requires: ""
identifiers:
  - "type"
  - "if"
  - "timeout"
  - "statusMessage"
  - "once"
  - "command"
  - "http"
  - "mcp_tool"
  - "prompt"
  - "agent"
  - "CLAUDE_CODE_REMOTE"
  - "CLAUDE_CODE_BRIDGE_SESSION_ID"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Each object in a matcher group's `hooks` array is a handler. Five types: `command` (shell command, JSON on stdin, results via exit code and stdout), `http` (POST of the JSON, same output format via response body), `mcp_tool` (calls a tool on a configured MCP server; text output treated like stdout), `prompt` (single-turn Claude evaluation returning JSON), `agent` (spawns a subagent with tools like Read, Grep, Glob to verify conditions; agent hooks are experimental and may change).

# How to use it

| Field | Required | Description |
| :- | :- | :- |
| `type` | yes | `"command"`, `"http"`, `"mcp_tool"`, `"prompt"` or `"agent"` |
| `if` | no | One permission-rule-syntax filter, e.g. `"Bash(git *)"`, `"Edit(*.ts)"`. Only evaluated on `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, `PermissionRequest`, `PermissionDenied`; on any other event a hook with `if` never runs |
| `timeout` | no | Seconds before cancel (see defaults) |
| `statusMessage` | no | Custom spinner message while the hook runs |
| `once` | no | If `true`, hook is removed after its first successful run. Only honored in skill frontmatter; ignored in settings files and agent frontmatter. A failed, exit-2 or timed-out run stays in place |

`if` holds exactly one rule: no `&&`, `||` or lists; use separate handlers. For file tools `"Edit(src/**)"` matches only `src` in the working directory; use `"Edit(**/src/**)"` for any depth. Bash `if` patterns: leading `VAR=value` is stripped; each subcommand is checked; commands inside `$()` and backticks are checked; patterns specifying more than the command name (e.g. `Bash(git push *)`) run the hook anyway when `$()`, backticks or `$VAR` appear. If Claude Code cannot split the Bash input, the hook runs regardless. `if` is best effort, so use the permission system for hard allow/deny.

# Limits and defaults

- `timeout` defaults: 600 for `command`, `http`, `mcp_tool`; 30 for `prompt`; 60 for `agent`. For `command`/`http`/`mcp_tool` the default drops to 30 on `UserPromptSubmit`, `PreModelSwitch`, `PostModelSwitch` and to 10 on `MessageDisplay`. `SessionEnd` hooks share a 1.5-second budget, raised to match a longer per-hook `timeout` up to 60 seconds. Not enforced on a command hook with `async: true`.
- Matching hooks run in parallel. If more than 12 are prompt or agent hooks, 12 run at once and the rest start as others finish; each `timeout` starts when that hook starts.
- Handlers run in the current directory; if it no longer exists, command hooks fall back to the session start directory, project root, home, then system temp, and log a warning in the debug log.

# Notes

`$CLAUDE_CODE_REMOTE` is `"true"` in remote web environments and unset in the local CLI. v2.1.199+ sets `$CLAUDE_CODE_BRIDGE_SESSION_ID` to the Remote Control session ID while a connection is active.
