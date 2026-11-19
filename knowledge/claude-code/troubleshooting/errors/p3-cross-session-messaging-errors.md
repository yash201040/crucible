---
type: "Reference"
title: "Cross-session messaging errors"
description: "Refusals when one session messages another: 1,048,576-character limit, rate limit, dropped messages with reasons, symlink socket checks."
resource: "https://code.claude.com/docs/en/errors"
tags: [errors, cross-session, messaging, limits]
kind: "limit"
maturity: "unlabelled"
since: "2.1.235"
surfaces: [cli]
requires: ""
identifiers:
  - "/status"
  - "Peer address"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "errors"
    resource: "https://code.claude.com/docs/en/errors"
    title: "Error reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Errors when Claude sends a message to another of the user's sessions on the same machine. They appear in the sending session's tool result, not as a terminal banner.

# How to use it

| Message | Cause | Fix |
|---|---|---|
| `Message too large for cross-session delivery` | Serialized message over 1,048,576 characters; recipient got nothing (before v2.1.235 reported as sent and dropped) | Summarize, put bulk content in a file and send the path, or split |
| `Too many messages to this session just now` | Burst reached the recipient inbox rate limit (example: 30 sent recently); before v2.1.236 reported as sent | Batch into one message or wait |
| `Cross-session message was dropped at the recipient session's inbox` | Recipient discarded it; names recipient (e.g. `uds:/tmp/cc-socks/13605.sock`); several drops can be one plural line. Reasons: its queue of undelivered peer messages was full; you sent faster than that session accepts; it repeated your previous message; a relay loop between sessions was cut | Assume not seen; include what matters in one later message; send fewer, larger updates. Loop cuts end when you type the next instruction yourself. Before v2.1.238 the sender got no report |
| `Refusing to send: reply target is a symlink` / `cannot vet reply target` | Socket path is a symlink or could not be inspected; nothing sent | Check what created the link; `/status` shows `Peer address` |

# Limits and defaults

- Message size limit: 1,048,576 characters (serialized).
- Burst example in message: 30 messages.

# Notes

Peer addresses are Unix socket paths (`uds:/tmp/cc-socks/<pid>.sock`); compare with the `Peer address` row of `/status`.
