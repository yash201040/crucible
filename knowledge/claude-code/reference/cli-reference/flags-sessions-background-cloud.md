---
type: "Reference"
title: "Session, background, cloud and worktree flags"
description: "Flags for continuing, resuming and forking sessions, background agents, cloud and Remote Control sessions, worktrees and team display."
resource: "https://code.claude.com/docs/en/cli-reference"
tags: [sessions, resume, background, cloud, worktree]
kind: "cli_flag"
maturity: "unlabelled"
since: "2.1.285"
surfaces: [cli, cloud, desktop]
requires: ""
identifiers:
  - "--continue"
  - "-c"
  - "--resume"
  - "-r"
  - "--fork-session"
  - "--session-id"
  - "--name"
  - "-n"
  - "--from-pr"
  - "--bg"
  - "--background"
  - "--exec"
  - "--cloud"
  - "--remote"
  - "--teleport"
  - "--environment"
  - "--ref"
  - "--desktop"
  - "--remote-control"
  - "--rc"
  - "--remote-control-session-name-prefix"
  - "CLAUDE_REMOTE_CONTROL_SESSION_NAME_PREFIX"
  - "--worktree"
  - "-w"
  - "--tmux"
  - "--teammate-mode"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "cli-reference"
    resource: "https://code.claude.com/docs/en/cli-reference"
    title: "CLI reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Flags that pick, create, fork or detach sessions and isolate them in worktrees or remote environments.

# How to use it

| Flag | Version | What it does |
| :- | :- | :- |
| `--continue`, `-c` | finished background sessions v2.1.257+ | Load the most recent conversation in the directory (including finished background sessions and sessions that added the directory with `/add-dir`). Skips `claude -p`/SDK sessions and sessions whose first prompt was `/loop`; `claude -p --continue` includes them |
| `--resume`, `-r` | ID search across projects v2.1.223+; attach to running v2.1.285+ | Resume by ID or name, absolute path to a `.jsonl` transcript, or open a picker. ID search covers the current project and its git worktrees, then all projects. Resuming a running background session opens it via `claude attach`; a command-line prompt goes to it as its next turn |
| `--fork-session` | | With `--resume`/`--continue`, create a new session ID instead of reusing it |
| `--session-id` | | Use a specific session ID (valid UUID) |
| `--name`, `-n` | | Display name for `/resume` and the terminal title; resume with `claude --resume <name>` |
| `--from-pr` | | Session picker filtered to a PR: number, GitHub or GitHub Enterprise URL, GitLab merge request URL or Bitbucket PR URL |
| `--bg`, `--background` | | Start a background agent and return immediately with the session ID. Combine with `--exec` for a shell job or `--agent` for a subagent. Checks workspace trust first. Cannot combine with `-p` |
| `--exec` | | Run a shell command as a PTY-backed background job, with `--bg` |
| `--cloud` | | With a task: new cloud session. With a session ID (`session_...` or `cse_...`) or claude.ai/code URL: queue a message into it with `-p` |
| `--remote` | deprecated | Deprecated alias of `--cloud` |
| `--teleport` | | Resume a cloud session in the local terminal |
| `--environment <environment-id>` | v2.1.224+ | New cloud session on a self-hosted environment (IDs start with `ccpool_`) |
| `--ref <branch>` | v2.1.224+ | With `--environment`, base the checkout on a named ref |
| `--desktop` | v2.1.285+ | Open the Claude Desktop app on the current directory and exit; accepts only `--continue`, `--resume <id>`, `--verbose`, `--debug`. macOS and x64 Windows with a Claude subscription |
| `--remote-control`, `--rc` | | Interactive session with Remote Control; optional name |
| `--remote-control-session-name-prefix <prefix>` | | Prefix for auto-generated Remote Control names (default: machine hostname); env `CLAUDE_REMOTE_CONTROL_SESSION_NAME_PREFIX` |
| `--worktree`, `-w` | GitLab MR v2.1.233+ | Isolated git worktree at `<repo>/.claude/worktrees/<name>`; name generated if omitted; `#<number>`, GitHub PR URL or GitLab MR URL branches the worktree from that PR or MR fetched from `origin` |
| `--tmux` | | tmux session for the worktree; requires `--worktree`; iTerm2 native panes when available, `--tmux=classic` for tmux |
| `--teammate-mode` | | Agent team display: `in-process` (default), `auto`, `tmux`, `iterm2`; overrides `teammateMode` |
