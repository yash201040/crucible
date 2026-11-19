---
type: "Concept"
title: "Gate inbound messages by sender"
description: "An ungated channel is a prompt-injection vector; gate on sender identity, not room, before emitting a notification."
resource: "https://code.claude.com/docs/en/channels-reference"
tags: [channels, security, prompt-injection, allowlist]
kind: "behavior"
maturity: "research-preview"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "message.from.id"
  - "access.json"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "channels-reference"
    resource: "https://code.claude.com/docs/en/channels-reference"
    title: "Channels reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Anyone who can reach a channel endpoint can put text in front of Claude, so a channel listening to a chat platform or public endpoint needs a real sender check before it emits anything.

# How to use it

Check the sender against an allowlist before `mcp.notification()` and drop silently otherwise. Gate on the sender's identity (`message.from.id`), not the chat or room identity (`message.chat.id`): in group chats they differ and gating on the room lets anyone in an allowlisted group inject messages.

# Notes

The Telegram and Discord channels gate on a sender allowlist bootstrapped by pairing. The iMessage channel detects the user's own addresses from the Messages database at startup and lets them through automatically, adding other senders by handle.
