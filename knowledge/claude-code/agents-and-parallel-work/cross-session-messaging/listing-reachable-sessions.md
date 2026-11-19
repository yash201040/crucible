---
type: "Feature"
title: "Seeing which sessions Claude can reach"
description: "/list-agents rows, Remote Control detail withholding, session naming and addressing by name or identifier."
resource: "https://code.claude.com/docs/en/cross-session-messaging"
tags: [messaging, listing, naming, remote-control]
kind: "slash_command"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "/list-agents"
  - "/peers"
  - "/rename"
  - "--name"
  - "--verbose"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "cross-session-messaging"
    resource: "https://code.claude.com/docs/en/cross-session-messaging"
    title: "Message your other Claude Code sessions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`/list-agents` prints, first, this session's own name (when present) then rows of reachable sessions: subagents of this session; teammates of its agent team; your other local sessions (including background sessions; a session appears only if it binds an inbox socket); cloud sessions and Remote Control sessions on other machines (shown while this session is connected to Remote Control; Remote Control sessions are labelled `Remote Control`, and `offline` marks a dropped connection).

# How to use it

A session answers to the name set by `/rename` or `--name`, else a Claude Code-chosen name (the same as in listings of running sessions). Local rows show working directories to tell same-named sessions apart. Addressing: one session with the name is addressed by name alone; several sharing a name, or when Claude Code could not check everywhere, get a short identifier per row used in the address.

# Limits and defaults

While connected to Remote Control, the display withholds: each local session's working directory; session names it cannot attribute to a person (row reads `(unnamed session)`); and the first line (this session's name) unless you typed that name at this terminal via `--name` or `/rename` since you launched or last resumed the session. A note says details were withheld. What Claude itself sees is unchanged. In a session started with `--verbose`, arriving messages show full text.
