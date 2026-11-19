---
type: "Concept"
title: "How a hook resolves"
description: "Event, matcher, optional if filter and handler fit together; worked PreToolUse example that blocks rm -rf."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, matcher, pretooluse, example]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: "jq for the bash example scripts"
identifiers:
  - "matcher"
  - "if"
  - "permissionDecision"
  - "permissionDecisionReason"
  - "hookSpecificOutput"
  - "${CLAUDE_PROJECT_DIR}"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Configuration has three nesting levels: a hook event, a matcher group that filters when it fires, and one or more hook handlers that run when matched. Terms: hook event = lifecycle point, matcher group = filter, hook handler = the command, HTTP endpoint, MCP tool, prompt or agent.

# How to use it

Example: a `PreToolUse` group with `"matcher": "Bash"` and a handler `{"type":"command","if":"Bash(rm *)","command":"${CLAUDE_PROJECT_DIR}/.claude/hooks/block-rm.sh","args":[]}`. Steps for `Bash "rm -rf /tmp/build"`:
1. Event fires; the hook gets JSON such as `{ "tool_name": "Bash", "tool_input": { "command": ... } }` on stdin.
2. The matcher `Bash` matches the tool name. Omitted matcher or `"*"` matches every occurrence.
3. The `if` condition `Bash(rm *)` matches a subcommand, so the handler spawns. For `npm test` it would never spawn (saves process spawn cost). `if` is optional; without it every handler in the group runs.
4. The script prints `hookSpecificOutput` with `hookEventName: "PreToolUse"`, `permissionDecision: "deny"`, `permissionDecisionReason`.
5. Claude Code blocks the call and shows Claude the reason.

Exit 0 with no output means no decision: the normal permission flow continues. A hook can deny, but staying silent does not approve. The Windows variant uses matcher `Bash|PowerShell` with two handlers (`Bash(rm *)` and `PowerShell(Remove-Item *)`) running `powershell.exe` with `-NoProfile -ExecutionPolicy Bypass -File`.

# Notes

A single `if` rule names one tool, so each tool needs its own handler. Bash example scripts need `jq` on `PATH`.
