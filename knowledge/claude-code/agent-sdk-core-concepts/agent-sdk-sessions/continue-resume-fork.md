---
type: "Concept"
title: "Continue, resume and fork"
description: "Definitions of the three option fields for returning to a session and how fork branches history."
resource: "https://code.claude.com/docs/en/agent-sdk/sessions"
tags: [sessions, fork, resume, continue]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "continue"
  - "resume"
  - "fork_session"
  - "forkSession"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-sessions"
    resource: "https://code.claude.com/docs/en/agent-sdk/sessions"
    title: "Work with sessions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

- Continue: finds the most recent session in the current directory; no tracking; suits one conversation at a time.
- Resume: takes a specific session ID; required for multiple sessions (e.g. one per user) or a session that is not the most recent.
- Fork: creates a new session starting with a copy of the original's history; the original is unchanged and the fork gets its own session ID.

# How to use it

Set `fork_session=True` (Python) / `forkSession: true` (TypeScript) together with `resume`. Example: resume `session_id` with fork and `max_turns=5` to explore OAuth2; then resume the original to continue the JWT thread. In TypeScript the fork's ID is on the init message; in Python read `ResultMessage.session_id`.

# Limits and defaults

Forking branches conversation history, not the filesystem: edits by a forked agent are real and visible to any session in the same directory. Use file checkpointing to revert.
