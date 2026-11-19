---
type: "Reference"
title: "Variables Claude Code sets for subprocesses"
description: "Read-only variables Claude Code exports to Bash, hooks and MCP subprocesses: session IDs, parent PID, effort, job dir, messaging socket and cloud markers."
resource: "https://code.claude.com/docs/en/env-vars"
tags: [subprocess, session-id, hooks, detection]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, cloud]
requires: ""
identifiers:
  - "CLAUDECODE"
  - "CLAUDE_CODE_CHILD_SESSION"
  - "CLAUDE_CODE_SESSION_ID"
  - "CLAUDE_PID"
  - "CLAUDE_EFFORT"
  - "CLAUDE_JOB_DIR"
  - "CLAUDE_CODE_BRIDGE_SESSION_ID"
  - "CLAUDE_CODE_REMOTE"
  - "CLAUDE_CODE_REMOTE_SESSION_ID"
  - "CLAUDE_CODE_MESSAGING_SOCKET"
  - "CLAUDE_CODE_MESSAGING_TOKEN"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "env-vars"
    resource: "https://code.claude.com/docs/en/env-vars"
    title: "Environment variables"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Variables Claude Code sets itself so scripts and tools can detect and correlate with the session that launched them.

# How to use it

| Variable | Set where / meaning |
| :- | :- |
| `CLAUDECODE` | `1` in subprocesses Claude Code spawns (Bash, PowerShell, tmux sessions, hook, status line and stdio MCP server subprocesses); IDE extensions also set it in integrated terminals. Use `CLAUDE_CODE_CHILD_SESSION` to tell a direct spawn from a stdio MCP server. |
| `CLAUDE_CODE_CHILD_SESSION` | `1` in subprocesses from Bash, PowerShell, Monitor, hook and status line commands; not set for stdio MCP servers; not set by IDE extensions, so it reliably identifies a nested session. A nested interactive `claude` TUI is excluded from `--resume`, `--continue`, up-arrow history and the `claude agents` list; non-interactive `claude -p` sessions still persist. Override with `CLAUDE_CODE_FORCE_SESSION_PERSISTENCE=1`. Requires v2.1.172+. |
| `CLAUDE_CODE_SESSION_ID` | Current session ID in Bash, PowerShell, hook and stdio MCP subprocesses. Matches the hook JSON `session_id` and updates on `/clear`. An MCP subprocess keeps its spawn-time ID; on `--resume <id>` it gets the resumed ID; on `--continue` or `--resume` without an ID it may get the initial startup ID. |
| `CLAUDE_PID` | Claude Code's own process ID in Bash, PowerShell and hook subprocesses; on Linux the Bash tool uses it to refuse a `pkill` pattern matching Claude Code. Requires v2.1.214+. |
| `CLAUDE_EFFORT` | Effort level (`low`, `medium`, `high`, `xhigh`, `max`) in Bash and hook subprocesses; matches the hook `effort.level` field; set only when the model supports effort. |
| `CLAUDE_JOB_DIR` | In each background session: its `~/.claude/jobs/<id>` directory; write scratch files to `$CLAUDE_JOB_DIR/tmp` (no permission prompt for Write/Edit there); removed with the session. |
| `CLAUDE_CODE_BRIDGE_SESSION_ID` | In Bash and hook subprocesses while a Remote Control connection is active (removed when it ends): the session ID in `session_` form, as in the `claude.ai/code` URL. Requires v2.1.199+. In cloud sessions read `CLAUDE_CODE_REMOTE_SESSION_ID`. |
| `CLAUDE_CODE_REMOTE` | Set to `true` automatically in cloud sessions; use in hooks or setup scripts to detect them. |
| `CLAUDE_CODE_REMOTE_SESSION_ID` | Set in cloud sessions to the session ID, for links back to the transcript. |
| `CLAUDE_CODE_MESSAGING_SOCKET` | Path of the session's inbox socket, exported to hooks and Bash commands when the socket binds (before any hook in a session that starts with messaging on). Each session exports its own; settings `env` cannot set it. Requires v2.1.224+. |
| `CLAUDE_CODE_MESSAGING_TOKEN` | Per-session token exported alongside the socket; a script may send `{"type":"auth","token":"<token>"}` as the first line. Native Windows requires it and closes connections that lack it. Never inherited from a parent. Requires v2.1.228+. |
