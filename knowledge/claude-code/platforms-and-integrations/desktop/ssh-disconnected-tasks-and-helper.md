---
type: "Limit"
title: "SSH tasks while Desktop is disconnected"
description: "How SSH tasks keep running when Desktop sleeps or quits, the limits that end them, and what the remote helper installs."
resource: "https://code.claude.com/docs/en/desktop"
tags: [desktop, ssh, unattended, reconnect, limits]
kind: "limit"
maturity: "unlabelled"
since: "v2.31226.0"
surfaces: [desktop]
requires: "Claude Desktop v2.31226.0 or later"
identifiers:
  - "KillUserProcesses"
  - "KillExcludeUsers"
  - "StopIdleSessionSec"
  - "PermissionRequest"
  - "Notification"
  - "Stop"
  - "StopFailure"
  - "~/.claude/remote/srv/"
  - "~/.claude/remote/ccd-cli/"
  - "~/.claude/remote/run/"
  - "remote-server.log"
  - "claude --resume"
  - "--fork-session"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "desktop"
    resource: "https://code.claude.com/docs/en/desktop"
    title: "Desktop application"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude Code runs as a process under a background helper Desktop installs on the remote, so a task continues if your computer sleeps, loses network or Desktop quits, until it finishes, needs you, or hits a limit.

# How to use it

Before a long task: update Desktop (an update restart waits while Claude works; by default proceeds after 72 hours if Desktop can rejoin), use prompt-free SSH login, pick a permission mode/rules/hooks that reduce waits, test by quitting during a short task. Hooks that help unattended: `PermissionRequest` (answers), `Notification` with `permission_prompt` matcher (alerts), `Stop` (done; not on API error), `StopFailure`. Place in remote `~/.claude/settings.json` (or managed settings if managed-hooks-only).

# Limits and defaults

- With a Claude account the task's sign-in is renewed only while Desktop runs, connected and signed in; it can expire after a few minutes. Do not count on overnight runs; use a cloud session for asleep/off machines.
- Ended by: remote restart; `KillUserProcesses=yes` in systemd-logind (exempt with `KillExcludeUsers`); idle-terminal logout (`StopIdleSessionSec`) when terminal and `!` commands share Desktop's connection; helper replacement on update; helper stops and ends Claude processes after 30 days without a Desktop connection (Linux/macOS).
- Disconnected failures: worktree file edits wait about 30 s then fail (can keep working on Linux/macOS remotes with OpenSSH client); folder-restriction checks wait up to 10 minutes; connectors fail after about 30 s; new workflows wait up to 10 minutes; MCP servers started by Claude Code on the remote keep working.
- Waiting approvals have no time limit while the process lives; lost if Desktop starts a new process. Buffer: helper keeps 16 MiB of recent output per session.
- Windows Desktop before v3.1623.0, and third-party providers on macOS/Linux before v2.42304.0, cannot rejoin a task after quit.
- Reconnect backoff: about one attempt every five minutes on long outages; macOS/Linux stop after three unanswered jump-host pushes.
- Do not run `claude --resume` on the remote for a conversation whose process still runs; use `--fork-session` to copy (both still edit the same files).
- Helper files: `~/.claude/remote/srv/`, `ccd-cli/`, `run/` (socket `rpc.sock`, mode 600), `plugins/`, and `~/.claude/uploads/`. Runs as the connecting user, no sudo, no network port. Archive a session in Desktop to end its process. Remove by quitting Desktop, killing Claude Code processes before `server` processes, deleting `~/.claude/remote/`.
