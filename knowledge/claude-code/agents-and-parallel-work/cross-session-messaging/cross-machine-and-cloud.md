---
type: "Concept"
title: "Messaging sessions on other machines and in the cloud"
description: "Transport per location, offline and cannot-receive conditions, container limits and reply rules for cloud sessions."
resource: "https://code.claude.com/docs/en/cross-session-messaging"
tags: [messaging, remote-control, cloud, transport]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.225"
surfaces: [cli, cloud]
requires: "Remote Control; claude.ai sign-in as active authentication"
identifiers:
  - "crossSessionInbound"
  - "isolatePeerMachines"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "cross-session-messaging"
    resource: "https://code.claude.com/docs/en/cross-session-messaging"
    title: "Message your other Claude Code sessions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

| Target runs | Transport |
| :- | :- |
| On this machine | Per-session socket (macOS/Linux) or named pipe (native Windows); never via Anthropic servers |
| On another of your machines | Through Anthropic servers, over that machine's Remote Control connection |
| In the cloud | Through Anthropic servers, straight to the cloud session |

Starting a conversation with a session on another machine needs v2.1.225+.

# How to use it

Listing conditions: `offline` means the message goes through and arrives after that machine reconnects. `can't receive cross-session messages (off in that session)` means messaging is unavailable there or its `crossSessionInbound` is `refuse`; Claude Code refuses before the message leaves, and the `SendMessage` result begins `Not sent` with the reason. Later listings drop the condition once fixed.

# Limits and defaults

- A container session and a host session cannot reach each other; two sessions inside the same container can, including on a self-hosted runner. WSL 2 and native Windows sessions on one computer cannot reach each other.
- A cloud session (including on a self-hosted runner) cannot answer a cross-machine message with `SendMessage`, even with a reply address; read its response in its transcript at claude.ai/code.
- To receive a reply from another of your machines, connect your session to Remote Control before sending; otherwise the message carries no reply address (a one-way message).
- `isolatePeerMachines` can require your approval for messages beyond this machine; see [restricting messaging](./restrict-and-turn-off.md).
