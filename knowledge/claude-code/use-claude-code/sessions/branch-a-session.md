---
type: "Feature"
title: "Branching a session"
description: "Copy a conversation into a new session with /branch or --fork-session, and what state the branch inherits."
resource: "https://code.claude.com/docs/en/sessions"
tags: [sessions, branch, fork, parallel]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "/branch"
  - "--fork-session"
  - "claude --continue --fork-session"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sessions"
    resource: "https://code.claude.com/docs/en/sessions"
    title: "Manage sessions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Branching copies the conversation so far and switches you into the copy; the original stays intact on disk and in the picker.

# How to use it

- Inside: `/branch [name]` (e.g. `/branch try-streaming-approach`). Without a name the branch is named after the first prompt. The confirmation prints the new and original session IDs; return with `/resume <original-name>` or its ID.
- Command line: `claude --continue --fork-session` (or `--resume ... --fork-session`).

| State | After `/branch` |
| :- | :- |
| Conversation history | Copied up to the point of `/branch` |
| "Allow for this session" grants | Carried over (same process); a separate process from `--fork-session` starts without them |
| In-flight background subagents and background Bash | Keep running; output appears in the new branch |
| Remote Control connection | Stays connected and follows into the branch |

# Limits and defaults

Resuming the same session in two terminals or two `claude -p` runs at once makes both write to one transcript, and messages from one can be missing later. Add `--fork-session` to each command to keep both. For rewind inside one session see Checkpointing.
