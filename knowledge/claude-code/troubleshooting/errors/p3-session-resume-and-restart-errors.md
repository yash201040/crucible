---
type: "Reference"
title: "Session resume, restart and renderer-switch errors"
description: "Errors for claude --resume, /resume, EBADF on Windows, /tui renderer switch refusals and failed self-restart."
resource: "https://code.claude.com/docs/en/errors"
tags: [errors, sessions, resume, tui, restart]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless]
requires: ""
identifiers:
  - "claude --resume"
  - "/resume"
  - "--fork-session"
  - "CLAUDE_CONFIG_DIR"
  - "/tui"
  - "/tui fullscreen"
  - "/tui default"
  - "--system-prompt"
  - "--tools"
  - "--setting-sources"
  - "--permission-prompt-tool"
  - "--allowed-tools"
  - "--disallowed-tools"
  - "tui"
  - "teammateMode"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "errors"
    resource: "https://code.claude.com/docs/en/errors"
    title: "Error reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Errors when loading a saved transcript, finding a session by ID, or when the CLI relaunches itself.

# How to use it

| Message | Cause | Fix |
|---|---|---|
| `Failed to resume the conversation. Run claude --resume <session-id> to retry` | Transcript unreadable from the `claude --resume` picker; exit 1 (before v2.1.216 it hung on the spinner). `/resume` inside a session reports `Failed to resume conversation` and keeps running | Retry; before v2.1.285 run `claude update` (unreadable entries failed the resume); else start new |
| `No conversation found with session ID: <id>` | No transcript matches; exit 1. Lookup covers the current project then every project on the machine (before v2.1.223: only current project and its worktrees). Causes: mistyped ID (for `-p`, use `session_id` from `--output-format json`), transcript deleted after retention (30 days default), different machine, duplicate copies under `~/.claude/projects` | `claude --resume` picker, `Ctrl+A` widens to all projects. `claude -p` and Agent SDK sessions do not appear in the picker |
| `Windows reported an error (EBADF) when Claude Code read this session's transcript file` | Security/encryption tools intercepting reads (since v2.1.282; before no explanation) | Exclude `%USERPROFILE%\.claude\projects` (or `CLAUDE_CONFIG_DIR`) from scanning |
| `Cannot switch renderers while work is running in the background` | `/tui` with a background shell or subagent running | Wait or stop via `/tasks` |
| `Cannot switch renderers in this session` | Session restrictions a restart cannot carry (before v2.1.234 it restarted and dropped them): launch flags `--system-prompt`, `--system-prompt-file`, `--append-system-prompt-file`, `--tools` allowlist, `--setting-sources`, `--permission-prompt-tool`; session-scoped deny/ask rules from a hook or SDK permission update (session-scoped allow rules do not block; a restart drops them); ask rules with no command-line form (only `--allowed-tools`/`--disallowed-tools` are passed back); rules or directories a command line cannot carry intact | Run `/tui fullscreen` or `/tui default` in a session started without them; the `tui` setting is saved |
| `Can't restart while work is running or Remote Control is connected` | Restart declined; session keeps running | Follow the message |
| `Claude Code couldn't restart. Your conversation is saved.` | Relaunch failed, exit status 1 | Run `claude`, then `/resume`; `claude --debug-file claude-debug.log` records a `Failed to relaunch:` line |

# Limits and defaults

- Transcript retention default: 30 days.

# Notes

Rewind and transcript-saving warnings are in [rewind and session saving warnings](./p4-rewind-and-transcript-saving.md).
