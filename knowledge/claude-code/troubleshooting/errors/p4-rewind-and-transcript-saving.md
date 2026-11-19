---
type: "Reference"
title: "Rewind failures and transcript-saving warnings"
description: "/rewind partial and failed restores, and warnings when transcripts are not saved: write failures, CLAUDE_CODE_SKIP_PROMPT_HISTORY, inherited CLAUDE_CODE_CHILD_SESSION."
resource: "https://code.claude.com/docs/en/errors"
tags: [errors, rewind, transcripts, sessions, env-vars]
kind: "env_var"
maturity: "unlabelled"
since: "2.1.217"
surfaces: [cli, headless]
requires: ""
identifiers:
  - "/rewind"
  - "--fork-session"
  - "/branch"
  - "cleanupPeriodDays"
  - "CLAUDE_CODE_SKIP_PROMPT_HISTORY"
  - "CLAUDE_CODE_CHILD_SESSION"
  - "CLAUDE_CODE_FORCE_SESSION_PERSISTENCE"
  - "--resume"
  - "--continue"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "errors"
    resource: "https://code.claude.com/docs/en/errors"
    title: "Error reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Messages about code restore and about sessions that will not be resumable.

# How to use it

| Message | Cause | Fix |
|---|---|---|
| `Restored the code, but skipped N files` | `/rewind` skipped tracked paths that are or became symlinks/hard links/non-regular files, whose directory changed, or whose backup is unreadable; skipped files stay untouched. Before v2.1.216 it wrote through links and gave no partial-restore report | Debug log `~/.claude/debug/<session-id>.txt` names paths (turn on `/debug` first); `find . -type l`, `find . -type f -links +1` |
| `No files were restored: N file failed (backup missing, or the file could not be updated)` | Backup missing or write/delete failed. Backups are removed by the retention sweep, default about 30 days after the session last saved one; forking (`--fork-session`, `/branch`) copies backups and a failed copy (e.g. disk full) leaves them missing. Before v2.1.260 missing-backup files were skipped silently | Ask Claude to undo or use version control; raise `cleanupPeriodDays` for longer backups |
| `Transcript writes are failing (disk full - ENOSPC) ...` | Persistent line under the input box; appears at first failure for non-clearing conditions (full disk, quota, read-only filesystem, path too long, permission error on macOS/Linux) or after repeated failures over at least a minute otherwise (e.g. Windows antivirus). Clears on the next successful write. Before v2.1.217 silent | Fix the named code (ENOSPC, EDQUOT, EACCES, EPERM, EROFS); messages sent meanwhile may be missing on resume |
| `Transcript saving is off - CLAUDE_CODE_SKIP_PROMPT_HISTORY is set` | Variable set: no transcript or prompt history; `--resume`, `--continue` and up-arrow will not find the session | Unset and restart if unintended |
| `Transcript saving is off - inherited CLAUDE_CODE_CHILD_SESSION marker` | Claude Code sets `CLAUDE_CODE_CHILD_SESSION` in subprocesses it spawns and treats an interactive session inheriting it as nested (no transcript). Inside tmux, a marker from the tmux global environment is detected and saving continues | Restart with `CLAUDE_CODE_FORCE_SESSION_PERSISTENCE=1`, or remove the marker from the launcher environment |

# Limits and defaults

- Checkpoint backup retention: about 30 days by default (`cleanupPeriodDays`).

# Notes

Sessions run by an agent that itself launches `claude` inherit `CLAUDE_CODE_CHILD_SESSION`; the docs describe this as intended for sessions Claude itself starts.
