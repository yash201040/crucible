---
type: "Reference"
title: "claude remote-control server mode and flags"
description: "Ways to start Remote Control (server mode, interactive flag, slash command) and the flags accepted by claude remote-control."
resource: "https://code.claude.com/docs/en/remote-control"
tags: [remote-control, server-mode, cli-flags, spawn, worktree]
kind: "cli_flag"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop, ide]
requires: "Remote Control eligibility"
identifiers:
  - "claude remote-control"
  - "claude rc"
  - "--name"
  - "--remote-control-session-name-prefix"
  - "CLAUDE_REMOTE_CONTROL_SESSION_NAME_PREFIX"
  - "-c"
  - "--continue"
  - "--session-id"
  - "--spawn"
  - "same-dir"
  - "worktree"
  - "session"
  - "--capacity"
  - "--create-session-in-dir"
  - "--no-create-session-in-dir"
  - "--permission-mode"
  - "--settings"
  - "--chrome"
  - "--no-chrome"
  - "-d"
  - "--debug"
  - "--debug-file"
  - "--verbose"
  - "--sandbox"
  - "--no-sandbox"
  - "claude --remote-control"
  - "--rc"
  - "/remote-control"
  - "/rc"
  - "/mobile"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "remote-control"
    resource: "https://code.claude.com/docs/en/remote-control"
    title: "Continue local sessions from any device with Remote Control"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Three CLI invocation modes plus slash command in Desktop and VS Code. Server mode (`claude remote-control`, alias `claude rc`) stays running in the terminal, shows a URL (spacebar toggles a QR code) and serves many concurrent sessions from one process. `claude --remote-control ["name"]` (or `--rc`) starts a normal interactive session also reachable remotely. `/remote-control` (`/rc`) inside a session carries over the current history; VS Code's version takes no name argument and shows no QR code; `--verbose` is not available with it. A one-time confirmation (`Enable Remote Control? (y/n)`) is shown first.

# How to use it

Flags after `remote-control`:

| Flag | Default | What it does |
|---|---|---|
| `--name "My Project"` | | Session title in claude.ai/code list |
| `--remote-control-session-name-prefix <prefix>` | machine hostname | Prefix for auto names such as `myhost-graceful-unicorn`; env `CLAUDE_REMOTE_CONTROL_SESSION_NAME_PREFIX` does the same |
| `-c`, `--continue` | | Resume the session the last server in this directory started (v2.1.200+); not combinable with `--session-id`, `--spawn`, `--capacity`, `--create-session-in-dir` |
| `--session-id <id>` | | Resume one session by ID (v2.1.200+); same exclusions |
| `--spawn <mode>` | `same-dir` when no mode saved | `same-dir` shares cwd; `worktree` gives each on-demand session its own git worktree (needs git repo or `WorktreeCreate` hook); `session` serves exactly one session (startup only). Press `w` at runtime to toggle same-dir/worktree; the choice is saved as project default |
| `--capacity <N>` | 32 | Max concurrent sessions; not with `--spawn=session` |
| `--[no-]create-session-in-dir` | on | Pre-create a session in cwd. With `--no-create-session-in-dir`, stopping the server archives its sessions (nothing to resume) |
| `--permission-mode <mode>` | | Starting permission mode for the server's sessions; `manual` aliases `default`; invalid mode stops startup |
| `--settings <file>` | | JSON settings file path (not a string) applied to sessions (v2.1.321+) |
| `--chrome` / `--no-chrome` | Chrome off in pre-created and self-started sessions | Chrome integration in created sessions (v2.1.273+) |
| `-d`, `--debug[=<filter>]` | | Debug logging, `=` form only (v2.1.282+) |
| `--debug-file <path>` | | Debug log file |
| `--verbose` | | Detailed connection/session logs |
| `--sandbox`, `--no-sandbox` | | Removed in v2.1.300; passing either exits with an error. Turn on sandboxing in a settings file instead |

# Limits and defaults

- Global `claude` flags placed before `remote-control` are not carried to created sessions; some (`--verbose`, `--model`) still start the server, others stop it. Put `--settings` after `remote-control`.
- Resume after Ctrl+C within about four hours: plain `claude remote-control` brings back all sessions; `--continue` only the starting session (falls back to newest from other worktrees of the repo); `--session-id` one by ID (ID is the part of the claude.ai/code URL between `/code/` and `?`). Archived sessions are unarchived by `--continue`/`--session-id` on v2.1.228+.
- A server on `--spawn session` cannot run a fork.
- Resuming with `claude --continue` / `--resume` in a second terminal prints `Remote Control not started here` and leaves it off there.
- Mobile: `/mobile` shows a QR code for the app.
