---
type: "Feature"
title: "Inbound controls: crossSessionInbound"
description: "accept, hold or refuse arriving messages, the default permission-mode rule, the approval dialog and held-message limits."
resource: "https://code.claude.com/docs/en/cross-session-messaging"
tags: [messaging, crosssessioninbound, hold, approval]
kind: "setting"
maturity: "unlabelled"
since: "2.1.232"
surfaces: [cli, ide, desktop]
requires: ""
identifiers:
  - "crossSessionInbound"
  - "dialogExpiry"
  - "/config"
  - "Messages from your other sessions"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "cross-session-messaging"
    resource: "https://code.claude.com/docs/en/cross-session-messaging"
    title: "Message your other Claude Code sessions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`crossSessionInbound` sets what a session does with messages from your other sessions. Precedence rules live in the settings reference.

# How to use it

| Value | Behavior |
| :- | :- |
| `accept` | Deliver each message to Claude |
| `hold` | Show a notice per message, do not deliver; released if an `accept` later applies |
| `refuse` | Drop each message |

The `/config` row "Messages from your other sessions" (v2.1.232+) writes the value to user settings; it is hidden when managed settings or `--settings` set the key. `/config crossSessionInbound=value` shorthand is rejected for this key.

When no value applies, the decision uses permission modes. Sessions that bypass permission prompts are one class (plan mode counts as bypassing in interactive terminal sessions with bypass available); all others, including auto, `acceptEdits`, `dontAsk`, are the other class.
- Receiver prompts for permissions: delivers, but holds only if the sender identifies as bypassing.
- Receiver bypasses prompts: holds each message for approval, delivering only if the sender also bypasses.

# Limits and defaults

A default hold in an interactive terminal session opens an approval dialog: Approve delivers one message; Deny or dismiss drops it; unanswered past `dialogExpiry` (default five minutes) it closes and drops the message. A background session with no terminal attached keeps the dialog open past the deadline; after attach, a full unanswered deadline drops it. If the permission-mode class changes while held, rules are re-applied and a notice shown. VS Code extension and Desktop app cannot show the dialog and keep the message until the deadline. At most 100 messages are held; the oldest are dropped beyond that.
