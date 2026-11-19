---
type: "Feature"
title: "Resuming a running background session"
description: "How --resume and /resume behave when the target is a background session that is still running, and when Claude Code refuses to attach."
resource: "https://code.claude.com/docs/en/sessions"
tags: [sessions, background, resume, attach]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.285"
surfaces: [cli]
requires: "Claude Code v2.1.285 or later"
identifiers:
  - "claude attach <id>"
  - "claude stop <id>"
  - "claude agents"
  - "--bg"
  - "--fork-session"
  - "--output-format"
  - "--json-schema"
  - "--max-turns"
  - "--max-budget-usd"
  - "--permission-mode"
  - "--model"
  - "--settings"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sessions"
    resource: "https://code.claude.com/docs/en/sessions"
    title: "Manage sessions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

When the conversation you resume belongs to a [background session](https://code.claude.com/docs/en/agent-view) that is still running, Claude Code opens the running session itself. With `--bg` on the command line, the resume is a background dispatch instead. Before v2.1.285 it refused and told you to `claude attach <id>` or `claude stop <id>` first.

# How to use it

- From the shell: `claude --resume <session>` runs `claude attach` on that session in the same terminal. A prompt on the command line (`claude --resume <session> "check the tests too"`) is sent as the session's next turn first, printing `Sent your prompt to the background session (<id>); opening it…`. `claude -p --resume <session> "prompt"` typed at a terminal does the same, so `-p` does not keep it non-interactive.
- It does not open the session when the command line has: piped or redirected input/output; session-configuring flags such as `--permission-mode`, `--model`, `--settings`; output-reading flags such as `--output-format json` or `--json-schema`; limiting or rewinding flags such as `--max-turns` or `--max-budget-usd`. It then sends nothing and exits with status 1, printing that the session runs in the background plus the `claude attach <id>` command (or telling you to look in `claude agents` if the ID is unknown). Also true when agent view is turned off.
- Add `--fork-session` to resume a copy instead. To continue the conversation itself with your flags, run `claude stop <id>` then repeat.
- A prompt starting with `/` or `!` is not sent, nor is any prompt while the session waits on your answer to a question; the message includes `Your prompt was not sent to it` with the reason.
- From inside a session: `/resume` moves the current conversation to the background and attaches to the running one, printing `Opening "<title>", running in the background (<id>)`. Press `←` on an empty prompt to return to agent view. If the conversation cannot move to the background (already attached to a background session, or session persistence is off), `/resume` prints the `claude attach` command instead.

# Notes

Do not repeat launch flags when reopening a background session while it runs, or when resuming it by full session ID with `--bg` after it stops: it keeps its flags.
