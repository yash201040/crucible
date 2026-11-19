---
type: "Concept"
title: "Non-interactive sessions and the inbox socket"
description: "claude -p workers can receive messages; the per-session socket, token env vars, auth line and sandbox settings."
resource: "https://code.claude.com/docs/en/cross-session-messaging"
tags: [messaging, headless, socket, hooks]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless]
requires: ""
identifiers:
  - "CLAUDE_CODE_MESSAGING_SOCKET"
  - "CLAUDE_CODE_MESSAGING_TOKEN"
  - "dialogExpiry"
  - "crossSessionInbound"
  - "sandbox.network.allowAllUnixSockets"
  - "sandbox.network.allowUnixSockets"
  - "/tmp/cc-socks-<uid>"
  - "claude -p"
  - "--settings"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "cross-session-messaging"
    resource: "https://code.claude.com/docs/en/cross-session-messaging"
    title: "Message your other Claude Code sessions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude Code binds an inbox socket for each session with messaging enabled: a Unix domain socket on macOS and Linux (including WSL 2), a named pipe on native Windows. `claude -p` sessions bind one like interactive sessions, so a long-running `-p` worker can receive messages and appears in the listing. Sessions started in bare mode do not bind it, so they cannot receive messages and are not listed.

# How to use it

- `-p` sessions cannot show the approval dialog. A default-held message is kept until the `dialogExpiry` deadline (five minutes by default): delivered if a mode or settings change allows it, otherwise dropped and reported expired to a reachable sender. Set `dialogExpiry` to `"never"` to keep default-held messages until the session ends. A message held by an explicit `hold` does not expire.
- To let a `-p` worker take messages unattended, start it with `crossSessionInbound` set to `accept` in its `--settings` value (an `accept` in user settings also works but applies to every session).
- Socket path: `Peer address` row in `/status` (prefix `uds:`), and the environment variable `CLAUDE_CODE_MESSAGING_SOCKET` exported to hooks and Bash commands (before any hook, including `SessionStart`).
- Scripts can post to their own session's socket. A per-session token is exported as `CLAUDE_CODE_MESSAGING_TOKEN`; the first line may be `{"type":"auth","token":"<token>"}` (optional on macOS/Linux, required on native Windows, where other first lines close the connection). Open the connection only when the message is ready: a connection without a complete line within 30 seconds is closed.

# Limits and defaults

- Socket is restricted to your OS user (native Windows: key authentication). Claude Code refuses an unacceptable directory (e.g. owned by another user) and uses `/tmp/cc-socks-<uid>`; with none acceptable the session runs without an inbox (`/status` shows `unavailable` and reason; `--debug` logs it).
- Own-child messages: with no `crossSessionInbound` value, a message verified as from the session's own child process (hook or Bash command) is delivered. Verification: Linux by process evidence even after exit; macOS only while the posting process runs, else by token; containers with Claude Code as PID 1 and native Windows have no process evidence (token only on Windows). If unverifiable it is treated as asserting no permission class, so a bypassing session holds it.
- Sandboxed sessions: reaching the socket from a Bash command is controlled by `sandbox.network.allowAllUnixSockets` and `sandbox.network.allowUnixSockets`.
