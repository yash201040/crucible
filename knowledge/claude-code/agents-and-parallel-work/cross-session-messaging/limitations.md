---
type: "Limit"
title: "Cross-session messaging limits"
description: "Plain text only, size cap about a million characters, burst and loop throttling, 50 queued, and exchange pauses."
resource: "https://code.claude.com/docs/en/cross-session-messaging"
tags: [messaging, limits, throttling, loops]
kind: "limit"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "Not sent"
  - "Not delivered: this session keeps answering other sessions"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "cross-session-messaging"
    resource: "https://code.claude.com/docs/en/cross-session-messaging"
    title: "Message your other Claude Code sessions"
stale_after: "2027-01-19T00:00:00Z"
---

# Limits and defaults

- Plain text only; structured agent-team protocol messages stay within a team.
- Same-machine size cap: refused once the serialized message passes about a million characters; nothing reaches the receiver; the error names exact sizes.
- Rapid bursts to one local session are refused at the sender once the session's inbox limit is reached; the refusal tells Claude to batch the rest or wait.
- Loops are throttled in the receiver: repeated messages rate-limited per sender, identical repeats in a short window dropped, at most 50 accepted messages queued for Claude to read.
- Slower loops continue: two sessions answering each other slowly can exchange thousands of messages without a prompt from you, each counting toward usage. Stop by ending one session or stopping receipt; end a background session by attaching and running `/stop`.
- After a long exchange, a `SendMessage` result starting `Not delivered: this session keeps answering other sessions` means sending paused; type a prompt in that session to resume.
- Long reply chains (for example including a session beyond this machine) can be cut off; type a prompt in one session of the chain to continue.
- A refused-or-unsent cross-machine message result begins `Not sent`.
