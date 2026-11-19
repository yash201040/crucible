---
type: "Feature"
title: "Automatic session management"
description: "Python ClaudeSDKClient and TypeScript continue:true track sessions without handling IDs; V2 session API removed."
resource: "https://code.claude.com/docs/en/agent-sdk/sessions"
tags: [sessions, claudesdkclient, continue, multi-turn]
kind: "api"
maturity: "unlabelled"
since: "0.3.142"
surfaces: [sdk]
requires: ""
identifiers:
  - "ClaudeSDKClient"
  - "client.query()"
  - "client.receive_response()"
  - "connect()"
  - "disconnect()"
  - "continue: true"
  - "createSession()"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-sessions"
    resource: "https://code.claude.com/docs/en/agent-sdk/sessions"
    title: "Work with sessions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

- Python `ClaudeSDKClient`: each `client.query()` continues the same session automatically; iterate with `client.receive_response()`. Use as an async context manager or call `connect()`/`disconnect()`.
- TypeScript: no session-holding client. Pass `continue: true` on each subsequent `query()` to pick up the most recent session in the current directory.

# Limits and defaults

The experimental V2 session API (`createSession()` with `send`/`stream`) was removed in TypeScript Agent SDK 0.3.142; use `query()` and the session options.
