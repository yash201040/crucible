---
type: "Guide"
title: "Working effectively: steer, delegate, get help"
description: "Interrupting with Esc, queueing messages, delegating with context, and the /init and /doctor helper commands."
resource: "https://code.claude.com/docs/en/how-claude-code-works"
tags: [interrupt, steering, init, doctor, queue]
kind: "slash_command"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "/init"
  - "/doctor"
  - "Esc"
  - "Enter"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "how-claude-code-works"
    resource: "https://code.claude.com/docs/en/how-claude-code-works"
    title: "How Claude Code works"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude Code is conversational: refine rather than restart.

# How to use it

- `Esc` stops Claude immediately; the running tool call is cancelled. Queued messages are then sent next.
- Typing a correction and pressing `Enter` while Claude works queues the message; if tool calls are running Claude reads it when they finish, within the same turn, and adjusts before its next step.
- `/init` generates a starter CLAUDE.md. `/doctor` runs a setup checkup that diagnoses installation and configuration issues and can fix them.
- Delegate with context and direction (what is broken, where the code is) rather than listing files and commands.
- Claude can answer questions about how to use Claude Code itself.
