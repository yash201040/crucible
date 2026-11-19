---
type: "Concept"
title: "The supervisor process"
description: "The background service that hosts sessions: lifecycle rules, idle shutdown, restarts and keeping sessions alive."
resource: "https://code.claude.com/docs/en/agent-view"
tags: [agent-view, supervisor, daemon, lifecycle]
kind: "behavior"
maturity: "research-preview"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "CLAUDE_CODE_DISABLE_BG_EXIT_HANDOFF"
  - "CLAUDE_CONFIG_DIR"
  - "/status"
  - "~/.claude/daemon.log"
  - "~/.claude/daemon/roster.json"
  - "~/.claude/jobs/<id>/state.json"
  - "~/.claude/jobs/<id>/tmp/"
  - "~/.claude/daemon.lock"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-view"
    resource: "https://code.claude.com/docs/en/agent-view"
    title: "Manage multiple agents with agent view"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Every session listed in agent view is a background session, attached or not; a plain `claude` is tied to its terminal. The supervisor is a background service that starts the first time you background a session or open agent view. Each session is its own process under it. `/status` shows `Session kind`: `background job · attached`, `background job · unattended`, or `interactive`.

# How to use it

Process rules by state:
- Working, paused on a permission prompt/dialog, or attached: kept running. Running subagents, workflows, monitors and pending session-scoped scheduled tasks (such as a `/loop` wakeup) count as working.
- Finished or waiting for next message and unattached about an hour: process stopped to free resources; resumes on attach or reply. Pin with `Ctrl+T` to keep it. With low memory it also stops idle sessions, and idle pinned ones if that freed nothing.
- Exited unexpectedly: restarted. A `←`/`/background` session you kill is marked stopped instead.
- After an auto-update: supervisor restarts onto the new version and moves idle sessions over; working, waiting or attached sessions are not interrupted.
- Supervisor itself stops (macOS/Linux): sessions stop unless a new supervisor connects within about a minute; run `claude agents`. Agent view exit prints `Background sessions still running will stop in about a minute. Run 'claude agents' to keep them.` (since v2.1.295 exiting `claude agents` no longer starts a new supervisor itself).

Background shell commands and background subagents carry to the next process; running monitors and subagent-started shell commands stop; deleting the session stops everything. Set `CLAUDE_CODE_DISABLE_BG_EXIT_HANDOFF` to `1` to stop all with the process.

# Limits and defaults

Supervisor and sessions use the same stored credentials as interactive sessions. State lives under `~/.claude` (or `CLAUDE_CONFIG_DIR`, which runs a separate supervisor instance with its own sessions).

| Path | Contents |
| :- | :- |
| `~/.claude/daemon.log` | Supervisor log |
| `~/.claude/daemon/roster.json` | Running sessions, for reconnect |
| `~/.claude/jobs/<id>/state.json` | Per-session state (read via `--json`) |
| `~/.claude/jobs/<id>/tmp/` | Scratch dir; `Write`/`Edit` there need no permission prompt; removed on delete |

Each background session has `CLAUDE_JOB_DIR` set to its job dir so shell commands can use `$CLAUDE_JOB_DIR/tmp` without colliding with parallel sessions.
