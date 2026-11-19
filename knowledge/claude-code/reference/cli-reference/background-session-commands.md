---
type: "Reference"
title: "Background session and supervisor commands"
description: "claude agents, attach, logs, respawn, stop, rm and the daemon subcommands for managing background sessions from the shell."
resource: "https://code.claude.com/docs/en/cli-reference"
tags: [background-sessions, agent-view, daemon, supervisor]
kind: "cli_flag"
maturity: "unlabelled"
since: "2.1.290"
surfaces: [cli]
requires: ""
identifiers:
  - "claude agents"
  - "claude agents --json"
  - "claude agents --json --all"
  - "--cwd"
  - "claude attach <id|name>"
  - "claude logs <id|name>"
  - "claude respawn <id>"
  - "claude respawn --all"
  - "claude stop <id>"
  - "claude kill"
  - "claude rm <id>"
  - "claude daemon logs"
  - "claude daemon run"
  - "claude daemon status"
  - "claude daemon stop --any"
  - "--keep-workers"
  - "~/.claude/daemon.log"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "cli-reference"
    resource: "https://code.claude.com/docs/en/cli-reference"
    title: "CLI reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Shell commands to monitor, attach to, restart and stop background sessions, and to inspect the supervisor process that hosts them.

# How to use it

| Command | What it does |
| :- | :- |
| `claude agents` | Open agent view to monitor and dispatch parallel background sessions; needs an interactive terminal. `--cwd <path>` limits to sessions started under that directory; `--json` prints active sessions as a JSON array for scripting (`--json --all` adds completed ones). `--permission-mode`, `--model`, `--effort`, `--agent` set defaults for dispatched sessions. Accepts `--settings`, `--add-dir`, `--plugin-dir`, `--mcp-config` |
| `claude attach <id\|name>` | Attach to a background session in this terminal. A partial name in place of the ID needs v2.1.290+ |
| `claude logs <id\|name>` | Print recent output of a background session. Partial name needs v2.1.290+ |
| `claude respawn <id>` | Restart a running or stopped background session with its conversation intact. `--all` restarts every running session, for example to pick up a new binary |
| `claude stop <id>` | Stop a background session. Also `claude kill` |
| `claude rm <id>` | Remove a session from the list; the transcript stays available through `claude --resume`. A worktree can make Claude Code refuse the delete |
| `claude daemon logs` | Follow the supervisor log `~/.claude/daemon.log` until Ctrl+C |
| `claude daemon run` | Run the supervisor in the foreground, printing its log |
| `claude daemon status` | Print supervisor state, version, socket directory and worker count; exits 1 if it is not running |
| `claude daemon stop --any` | Stop the supervisor and its sessions. `--keep-workers` leaves sessions running for the next supervisor to reconnect to. `--any` confirms stopping an on-demand supervisor (the default) |

# Notes

`claude --dangerously-skip-permissions daemon <subcommand>` works when `claude` is aliased with the flag, but only a leading `--dangerously-skip-permissions` or `--allow-dangerously-skip-permissions` routes to `daemon`; any other flag ahead of `daemon` stops the subcommand from running.
