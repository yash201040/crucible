---
type: "Feature"
title: "Stop hook event and background task data"
description: "Runs when the main agent finishes; can block stopping, with an 8-continuation cap and background_tasks/session_crons input."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, stop, loops, background-tasks]
kind: "hook"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "Stop"
  - "stop_hook_active"
  - "last_assistant_message"
  - "background_tasks"
  - "session_crons"
  - "CLAUDE_CODE_STOP_HOOK_BLOCK_CAP"
  - "decision"
  - "reason"
  - "hookSpecificOutput.additionalContext"
  - "/goal"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Runs when the main Claude Code agent has finished responding. Does not run if the stoppage was a user interrupt; API errors fire [StopFailure](./p2-stopfailure-event.md) instead. The `/goal` command is a built-in shortcut for a session-scoped prompt-based Stop hook.

# How to use it

Input adds `stop_hook_active` (true when already continuing because of a stop hook; check it to avoid blocking on a condition that never resolves), `last_assistant_message` (Claude's final text; prefer it over reading `transcript_path`, which may lack the final message at Stop time on some versions), `background_tasks`, `session_crons`. Both arrays are present when the task registry is reachable and empty when nothing is in flight; they let a hook tell "session done" from "paused waiting for background work".

`background_tasks` entry fields: `id`; `type` (`shell`, `subagent`, `monitor`, `workflow`, `teammate`, `cloud session`, `MCP task`, or the raw discriminant for unrecognized types); `status`; `description` (max 1000 chars, with `… [+N chars]` marker); `command` (shell only, max 1000); `agent_type` (subagent only); `server` and `tool` (`monitor` and `MCP task` only); `name` (workflow only).

`session_crons` entry fields (from `CronCreate`, `ScheduleWakeup`, `/loop`): `id`, `schedule` (cron expression), `recurring` (false for one-shot), `prompt` (max 1000 chars, same marker).

Decision (shared with SubagentStop): `decision: "block"` prevents stopping, requires `reason` (Claude's next instruction); exit 2 routes stderr the same way. `hookSpecificOutput.additionalContext` gives non-error feedback: the conversation continues, shown as `Stop hook feedback` with no hook error notification, under the same loop protections.

# Limits and defaults

- 8-consecutive-continuation cap: after stop hooks continue the turn eight times in a row, Claude Code overrides the next block and ends the turn. The count resets each time Claude calls a tool. Raise with `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP`.
