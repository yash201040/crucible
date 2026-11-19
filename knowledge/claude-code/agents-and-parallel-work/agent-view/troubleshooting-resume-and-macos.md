---
type: "Guide"
title: "Troubleshooting restarts, resume and macOS permissions"
description: "Shutdown recovery, conversation already open, missing transcript, dead terminal host, macOS folder and LAN access."
resource: "https://code.claude.com/docs/en/agent-view"
tags: [agent-view, troubleshooting, resume, macos]
kind: "behavior"
maturity: "research-preview"
since: ""
surfaces: [cli]
requires: "macOS items apply to macOS only"
identifiers:
  - "cleanupPeriodDays"
  - "claude respawn <id>"
  - "ended while the background service was off"
  - "This session has no saved transcript"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-view"
    resource: "https://code.claude.com/docs/en/agent-view"
    title: "Manage multiple agents with agent view"
stale_after: "2027-01-19T00:00:00Z"
---

# How to use it

- Shutdown or restart stops running sessions. A session waiting on input stays under `Needs input`. Others: within 48 hours shows failed (attach or reply restarts from the saved conversation; ask it to continue); past 48 hours shows stopped with `ended while the background service was off`; `Enter` then shows `Press enter again to resume this session (it ended while the background service was off), or ctrl+x to remove it.` A reply or `claude attach <id>` resumes without that prompt. Sleep alone does not stop sessions. If transcript cleanup (`cleanupPeriodDays`) removed the saved conversation, opening is refused (nothing to resume): `claude rm <id>` or `claude respawn <id>` (re-runs the original prompt).
- Conversation already open elsewhere: `Can't open — this session is running in another terminal` (e.g. a `claude -p` run or a resumed terminal) or `This conversation is already open in another running Claude session`. A typed reply (not `!`/`/`) is saved and sent on next start.
- No saved transcript (session backgrounded from another conversation, stopped before a turn): `claude attach` prints `This session has no saved transcript`; agent view shows `Press enter again to restart this session fresh`; press `Enter` again or `claude respawn <id>`.
- Terminal host died or session unresponsive: reason shown and restart offered; the conversation is saved. Shell-command rows are never restarted.
- Slow after attach: idle processes (about an hour) restart on attach; a transcript tail shows with `Session is starting` meanwhile. Pin to avoid.
- macOS: the background host asks for protected-folder access separately. For `Operation not permitted` on `~/Desktop`, `~/Documents`, `~/Downloads`, grant Files and Folders or Full Disk Access to the entry named Claude Code or the binary name (may be a version like `2.1.316`; re-check after updates). On macOS 15+, LAN hosts fail with `connect: no route to host` until Local Network permission is granted at first prompt.
- `.claude/worktrees/` filling up: see [deleting sessions](./deleting-sessions-and-worktrees.md).
