---
type: "Reference"
title: "Background tasks, check-in and scheduling variables"
description: "Variables for automatic backgrounding of subagents, worker check-in reminders, background wait ceilings, scheduled tasks and goal check-ins."
resource: "https://code.claude.com/docs/en/env-vars"
tags: [background, subagents, scheduling, headless]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless]
requires: ""
identifiers:
  - "CLAUDE_AUTO_BACKGROUND_TASKS"
  - "CLAUDE_CODE_AUTO_BACKGROUND_WORKER_CHECKIN_SECONDS"
  - "CLAUDE_CODE_WORKER_CHECKIN_SCHEDULE"
  - "CLAUDE_CODE_DISABLE_BACKGROUND_TASKS"
  - "CLAUDE_CODE_BG_TASKS_REPORT_RUNNING"
  - "CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS"
  - "CLAUDE_SUBAGENT_BG_SHELL_MAX_MS"
  - "TASK_MAX_OUTPUT_LENGTH"
  - "CLAUDE_CODE_DISABLE_BG_SHELL_PRESSURE_REAP"
  - "CLAUDE_CODE_DISABLE_CRON"
  - "CLAUDE_CODE_GOAL_CHECKIN_MINUTES"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "env-vars"
    resource: "https://code.claude.com/docs/en/env-vars"
    title: "Environment variables"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

How long-running agent work moves to the background, how Claude is reminded to check on it, and how an unattended `-p` run waits for it.

# How to use it

| Variable | What it does |
| :- | :- |
| `CLAUDE_AUTO_BACKGROUND_TASKS` | `1` force-enables auto-backgrounding: a subagent moves to the background after about two minutes (a queued tool call such as an edit makes it finish in the foreground first). Also auto-backgrounds long MCP tool calls in non-interactive mode on v2.1.212+. |
| `CLAUDE_CODE_WORKER_CHECKIN_SCHEDULE` | With `CLAUDE_AUTO_BACKGROUND_TASKS=1`: comma-separated waits in whole seconds (1 to 86400, such as `600` or `600,1800,3600`) before each reminder to check on running background subagents; last value repeats. Plain digits only; unset means no reminders. Requires v2.1.283+. |
| `CLAUDE_CODE_AUTO_BACKGROUND_WORKER_CHECKIN_SECONDS` | Removed in v2.1.283; use `CLAUDE_CODE_WORKER_CHECKIN_SCHEDULE`. |
| `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS` | `1` removes `run_in_background` from Bash, PowerShell and subagent tools, turns off Ctrl+B and background runs of forked skills, and stops automatic backgrounding of subagents, long MCP calls and timed-out shell commands. MCP tasks and the Monitor tool still background. For background sessions also set `CLAUDE_CODE_DISABLE_AGENT_VIEW`. |
| `CLAUDE_CODE_BG_TASKS_REPORT_RUNNING` | `0` makes a non-interactive session report idle at every turn end even with background work live. Default keeps a running status while a background agent or workflow is live (background shell commands such as a dev server do not hold it). Default and `0` need v2.1.269+; earlier, set `1` to hold running. |
| `CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS` | Ceiling on idle waiting for background subagents or workflows after the final turn of `-p` runs; resets each time Claude handles a background result. Default 600000 (10 min); `0` waits indefinitely; at the ceiling Claude Code stops waiting (a running background command started by the main conversation holds the run open). Requires v2.1.182+. |
| `CLAUDE_SUBAGENT_BG_SHELL_MAX_MS` | Removed in v2.1.260, now a no-op; capped a subagent's background shell command (60-minute default). |
| `TASK_MAX_OUTPUT_LENGTH` | Removed in v2.1.277, now a no-op, with the `TaskOutput` tool; Claude reads background output files with `Read`. |
| `CLAUDE_CODE_DISABLE_BG_SHELL_PRESSURE_REAP` | `1` stops terminating background shells under memory pressure. By default on macOS/Linux they are terminated when the OS reports critical memory pressure and the session has been idle 30 minutes with no turn or subagent running. No effect on Windows. Requires v2.1.193+. |
| `CLAUDE_CODE_DISABLE_CRON` | `1` disables session-scoped scheduled tasks: `/loop` and `CronCreate` become unavailable and scheduled tasks stop firing, including running ones. |
| `CLAUDE_CODE_GOAL_CHECKIN_MINUTES` | Minutes background work may keep an active goal waiting before Claude is asked to check (default 30; `0` off; whole minutes in plain digits, max 10080; other values use the default). Requires v2.1.234+. |
