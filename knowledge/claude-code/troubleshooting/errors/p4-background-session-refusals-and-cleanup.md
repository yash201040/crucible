---
type: "Reference"
title: "Background session refusals, attach and delete errors"
description: "Errors for background sessions in agent view: dialog commands refused, no saved transcript, conversation open elsewhere, claude rm unpushed commits."
resource: "https://code.claude.com/docs/en/errors"
tags: [errors, background-sessions, agent-view, worktrees]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.248"
surfaces: [cli]
requires: ""
identifiers:
  - "claude respawn"
  - "claude attach"
  - "claude rm"
  - "claude rm --discard-unpushed"
  - "claude stop"
  - "/background"
  - "/install-github-app"
  - "/mcp enable"
  - "/mcp disable"
  - "/mcp reconnect"
  - "cleanupPeriodDays"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "errors"
    resource: "https://code.claude.com/docs/en/errors"
    title: "Error reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Messages seen in the transcript, attached terminal, or dispatching shell for background sessions (agent view, `claude --bg`, `/background`). Background sessions have no interactive terminal of their own.

# How to use it

| Message | Cause | Fix |
|---|---|---|
| `Can't open MCP settings while no terminal is attached ...` | `/install-github-app`, the `/mcp` settings list and MCP auth actions need a dialog; the session shows **Needs input** in agent view (since v2.1.216). History: before v2.1.208 they opened inside the session; v2.1.208 to v2.1.212 refused even when attached; v2.1.213 to v2.1.215 worked when attached | Attach and run again, or use `/mcp enable`, `/mcp disable`, `/mcp reconnect <server>` without attaching |
| `This session has no saved transcript` | Backgrounded (`←` or `/background`) session stopped before its own first response finished | `claude respawn <id>`, or press Enter twice on the row; on versions before v2.1.214 an unreadable folder in `~/.claude/projects` could cause it |
| `Can't open - this session is running in another terminal` / `already open in another running Claude session` | Stopped session's conversation held by a non-background process (`claude -p`, terminal `--resume`) or by another background session; before v2.1.248 only the second case was refused | Continue in the other process, exit it, or stop the other session |
| `This session's saved conversation is no longer on disk` | Session ended while the background service was off and transcript cleanup (`cleanupPeriodDays`) removed it; before v2.1.248 the original prompt was silently re-run | `claude rm <id>` removes the row; `claude respawn <id>` re-runs the original prompt. `claude attach <id>` prints this text |
| `kept <id> - its worktree is still at ...` with `unpushed commits` | `claude rm` refuses to delete a session worktree holding commits on no remote | Push them (a remote-tracking branch counts) and retry; or discard with `claude rm <id> --discard-unpushed <commit>@<worktree-id>` (also Ctrl+X twice in agent view); pre-v2.1.260 workaround: `git worktree remove --force --force <path>` then `claude rm <id>` |

# Limits and defaults

- Discard route for unpushed commits exists since v2.1.260; before v2.1.268 the summary was on the `kept` line itself.

# Notes

Restart and service-level failures are in [background service and recovery errors](./p4-background-service-and-recovery-errors.md).
