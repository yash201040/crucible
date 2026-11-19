---
type: "Feature"
title: "Background Bash commands"
description: "Run shell commands asynchronously with task IDs, output files, cleanup rules and memory-pressure stops."
resource: "https://code.claude.com/docs/en/interactive-mode#background-bash-commands"
tags: [background, bash, tasks, cleanup, limits]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, cloud]
requires: ""
identifiers:
  - "Ctrl+B"
  - "/tasks"
  - "CLAUDE_CODE_DISABLE_BACKGROUND_TASKS"
  - "CLAUDE_CODE_DISABLE_BG_SHELL_PRESSURE_REAP"
  - "BASH_DEFAULT_TIMEOUT_MS"
  - "BASH_MAX_TIMEOUT_MS"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "interactive-mode"
    resource: "https://code.claude.com/docs/en/interactive-mode"
    title: "Interactive mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A background command returns a task ID immediately while Claude Code keeps responding to prompts. Output goes to a file that Claude reads with the Read tool.

# How to use it

- Ask Claude to background a command, or press `Ctrl+B` on a running Bash call (tmux: twice).
- A command that reaches its timeout is moved to the background instead of stopped, unless it starts with `sleep`.
- `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1` turns background commands off, also removing `Ctrl+B` and other background features such as running skills in the background. Bare mode (`--bare`) has the same effect, and a command then stops at its timeout.
- `CLAUDE_CODE_DISABLE_BG_SHELL_PRESSURE_REAP=1` turns off memory-pressure stops.

# Limits and defaults

- Tasks are terminated automatically if output exceeds 5GB.
- Background tasks are cleaned up when Claude Code exits; on macOS and Linux, detached processes (e.g. under `setsid` or `timeout`) stop too when stopped from `/tasks` or at exit. If the session is backgrounded rather than exited, tasks keep running.
- On macOS and Linux, tasks are stopped under critical OS memory pressure if the session has been idle at least 30 minutes with no turn or subagent running; the debug log says why.
- Local interactive sessions (terminal, desktop app, VS Code) have no time limit on background commands; unattended sessions (`-p`, cloud) stop them at a [time limit](../tools-reference/background-command-time-limits.md).
- A background command started by a foreground subagent ends when that subagent's run ends.
