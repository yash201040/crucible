---
type: "Feature"
title: "Automatic backgrounding of long MCP calls"
description: "A main-conversation MCP call running over two minutes moves to a background task; thresholds, switches and exclusions."
resource: "https://code.claude.com/docs/en/mcp"
tags: [mcp, background, tasks, headless]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "CLAUDE_CODE_MCP_AUTO_BACKGROUND_MS"
  - "CLAUDE_CODE_DISABLE_BACKGROUND_TASKS"
  - "CLAUDE_AUTO_BACKGROUND_TASKS"
  - "/tasks"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "mcp"
    resource: "https://code.claude.com/docs/en/mcp"
    title: "Connect Claude Code to tools via MCP"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

An MCP tool call in the main conversation still running after two minutes becomes a background task. Claude gets the task ID immediately and the result arrives as a task notification when the call settles. The task shows in `/tasks` (where it can be stopped) with the server's latest progress, and does not survive exiting the session. Stopping cancels the call and tells Claude no result is coming, but the server may still finish the work.

# How to use it

| Name | Effect |
|---|---|
| `CLAUDE_CODE_MCP_AUTO_BACKGROUND_MS` | threshold in ms; `0` turns backgrounding off (and Claude then also waits for MCP tasks in interactive sessions) |
| `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1` | turns off automatic backgrounding and background commands |
| `CLAUDE_AUTO_BACKGROUND_TASKS=1` | enables backgrounding in non-interactive mode |

# Limits and defaults

- Per-call wall-clock (`timeout`/`MCP_TOOL_TIMEOUT`) and idle limits still apply while backgrounded.
- Never backgrounded: calls from subagents (only main-conversation calls move), calls to IDE servers, calls in non-interactive mode unless `CLAUDE_AUTO_BACKGROUND_TASKS=1`, and a call waiting on an open elicitation dialog (deferred until it closes).
