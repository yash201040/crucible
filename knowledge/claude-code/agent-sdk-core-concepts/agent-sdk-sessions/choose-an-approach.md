---
type: "Guide"
title: "Choosing a session approach"
description: "Which session mechanism fits one-shot, multi-turn, restart, specific-session, fork and stateless use cases."
resource: "https://code.claude.com/docs/en/agent-sdk/sessions"
tags: [sessions, resume, persistence, stateless]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "ClaudeSDKClient"
  - "continue"
  - "continue_conversation"
  - "resume"
  - "persistSession"
  - "CLAUDE_CODE_SKIP_PROMPT_HISTORY"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-sessions"
    resource: "https://code.claude.com/docs/en/agent-sdk/sessions"
    title: "Work with sessions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A session is the accumulated conversation: prompt, tool calls, results, responses, written to disk automatically. Sessions persist the conversation, not the filesystem; use file checkpointing to revert file changes.

# How to use it

| Building | Use |
| :- | :- |
| One-shot task | One `query()` call |
| Multi-turn chat in one process | `ClaudeSDKClient` (Python) or `continue: true` (TypeScript) |
| Pick up after a process restart | `continue_conversation=True` / `continue: true` (most recent session in the directory) |
| A specific past session | Capture the ID, pass to `resume` |
| Alternative approach, keep original | Fork |
| Stateless, nothing on disk | `persistSession: false` (TypeScript only); in Python set `CLAUDE_CODE_SKIP_PROMPT_HISTORY` in `env` to suppress transcript writes |

# Notes

Within a single `query()` the agent already takes as many turns as needed; permission prompts and `AskUserQuestion` are handled in-loop and do not end the call.
