---
type: "Concept"
title: "How a session treats an incoming message"
description: "Messages from other sessions are not user input: they cannot approve, change config or run commands."
resource: "https://code.claude.com/docs/en/cross-session-messaging"
tags: [messaging, security, permissions, trust]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "--verbose"
  - "Waiting to be delivered"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "cross-session-messaging"
    resource: "https://code.claude.com/docs/en/cross-session-messaging"
    title: "Message your other Claude Code sessions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude Code tells the receiving Claude the message came from another session, not you, and limits it: it cannot approve anything (never counts as your consent, cannot answer a pending permission prompt); it cannot change permission settings, `CLAUDE.md` or other configuration; a command in its text such as `/compact` arrives as plain text and is never executed; permission prompts still fire for anything it asks.

# How to use it

Display: a dim one-line preview such as `› Message from @api-worker: Schema migration finished (ctrl+o to expand)` stays in the conversation. Full text via: `Ctrl+O` transcript viewer (messages not yet received are at the end under `Waiting to be delivered`, v2.1.309+); click a truncated preview in fullscreen rendering; or start with `--verbose` to show full text. The preview shortens only the display; Claude reads the full message.

Claude receives the message with the sender's name and a reply address, except a one-way cross-machine message, which has no reply address.
