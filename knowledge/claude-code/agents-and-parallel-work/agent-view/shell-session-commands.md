---
type: "Reference"
title: "Shell commands for background sessions"
description: "claude agents, attach, logs, stop, respawn, rm and daemon subcommands for scripting background sessions."
resource: "https://code.claude.com/docs/en/agent-view"
tags: [agent-view, cli, daemon, scripting]
kind: "cli_flag"
maturity: "research-preview"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "claude agents"
  - "claude agents --cwd <path>"
  - "claude agents --json"
  - "claude attach <id|name>"
  - "claude logs <id|name>"
  - "claude stop <id>"
  - "claude kill"
  - "claude respawn <id>"
  - "claude respawn --all"
  - "claude rm <id>"
  - "claude daemon status"
  - "claude daemon logs"
  - "claude daemon stop --any"
  - "--keep-workers"
  - "--cwd"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-view"
    resource: "https://code.claude.com/docs/en/agent-view"
    title: "Manage multiple agents with agent view"
stale_after: "2027-01-19T00:00:00Z"
---

# How to use it

Each background session has a short ID (printed by `claude --bg`; its directory name under `~/.claude/jobs/`).

| Command | Purpose |
| :- | :- |
| `claude agents` | Open agent view |
| `claude agents --cwd <path>` | Scope to sessions started under `<path>` (also lists sessions moved into `<path>/.claude/worktrees/`; since v2.1.141) |
| `claude agents --json` | Print sessions as JSON and exit |
| `claude attach <id\|name>` | Attach in this terminal |
| `claude logs <id\|name>` | Print recent output |
| `claude stop <id>` (alias `claude kill`) | Stop a session |
| `claude respawn <id>` | Restart a running or stopped session (e.g. to pick up a new binary); resumes the saved conversation |
| `claude respawn --all` | Restart every running session |
| `claude rm <id>` | Remove from the list, plus a Claude-created worktree when safe |
| `claude daemon status` | Supervisor state, version, socket directory, worker count; warns on version mismatch |
| `claude daemon logs` | Follow `~/.claude/daemon.log` |
| `claude daemon stop --any` | Stop the supervisor and its sessions; `--keep-workers` leaves sessions running for the next supervisor |

# Limits and defaults

`attach` and `logs` accept part of a session name (v2.1.290+); `attach` by name works only while the process runs, so pass the ID to restart a stopped session. `claude respawn <id>` on a session whose conversation was cleaned up runs its original prompt again. See [deleting sessions](./deleting-sessions-and-worktrees.md) for `rm` retry flags.
