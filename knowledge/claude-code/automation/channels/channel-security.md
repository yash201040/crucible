---
type: "Concept"
title: "Channel sender allowlists and pairing"
description: "Each approved channel keeps a sender allowlist; Telegram and Discord pair by code, iMessage self-chat bypasses the gate."
resource: "https://code.claude.com/docs/en/channels"
tags: [channels, security, allowlist, permission-relay]
kind: "behavior"
maturity: "research-preview"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "/imessage:access allow"
  - "--channels"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "channels"
    resource: "https://code.claude.com/docs/en/channels"
    title: "Push events into a running session with channels"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Every approved channel plugin maintains a sender allowlist: only added IDs can push messages; everyone else is silently dropped.

# How to use it

Telegram and Discord bootstrap by pairing: message the bot, receive a pairing code, approve it in the Claude Code session, and your sender ID is added. iMessage: texting yourself passes automatically; add others by handle with `/imessage:access allow`.

Further controls: you choose servers per session with `--channels`; the organization controls availability with `channelsEnabled` ([enterprise controls](./channel-enterprise-controls.md)).

# Notes

The allowlist also gates permission relay if the channel declares it. Anyone who can reply through the channel can approve or deny tool use in your session, so allowlist only senders you trust with that authority.
