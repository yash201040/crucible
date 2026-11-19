---
type: "Reference"
title: "claude agents --json and reading state from scripts"
description: "JSON fields and state values for polling background sessions from a script or supervising session."
resource: "https://code.claude.com/docs/en/agent-view"
tags: [agent-view, json, polling, state]
kind: "api"
maturity: "research-preview"
since: ""
surfaces: [cli, headless]
requires: ""
identifiers:
  - "claude agents --json"
  - "--all"
  - "state"
  - "status"
  - "waitingFor"
  - "sessionId"
  - "CLAUDE_JOB_DIR"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-view"
    resource: "https://code.claude.com/docs/en/agent-view"
    title: "Manage multiple agents with agent view"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`claude agents --json` prints active sessions as a JSON array and exits: every live session plus background sessions still working or blocked even if the process exited. `--all` adds completed background sessions; `--cwd <path>` limits to a directory. It is the supported way to read state from a status bar, scheduler or a supervising Claude session; poll `claude agents --json --all`.

# How to use it

| Field | Present | Description |
| :- | :- | :- |
| `cwd`, `kind`, `startedAt` | Always | Working directory, `interactive` or `background`, start time in Unix ms |
| `id` | Background | Short ID for `attach`, `logs`, `stop` |
| `state` | Background | `working`, `blocked`, `done`, `failed`, `stopped` |
| `pid`, `status` | Process alive | PID and `busy`, `waiting` or `idle` |
| `waitingFor` | `status` is `waiting` | `permission prompt`, `input needed`, `sandbox request`, `worker request`, or `dialog open` |
| `sessionId`, `name` | When set | Full UUID for `claude --resume`; interactive `name` is the default display name until named or a plan is accepted |

| `state` | Meaning |
| :- | :- |
| `working` | Turn running, or between steps it drives itself (a `/loop` iteration, waiting on CI) |
| `blocked` | Needs something from you: a question, permission/sandbox decision, an error only you can clear such as an expired login, or its first prompt if started without one |
| `done` | Last turn finished; ready for next prompt (even if the process is gone) |
| `failed`, `stopped` | Ended with an error / was stopped |

A session waiting for your next instruction is `done`, not `blocked`.

# Limits and defaults

Files under `~/.claude/jobs/<id>/` are not a stable interface; values written to `state`, `detail`, `tempo` or `needs` are overwritten. For progress in a session's own words have it write its own file, e.g. under `$CLAUDE_JOB_DIR/tmp`.
