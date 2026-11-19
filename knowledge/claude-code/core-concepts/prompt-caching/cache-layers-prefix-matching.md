---
type: "Concept"
title: "How the prompt cache is organized"
description: "Prefix matching, the three request layers (system prompt, project context, conversation), and the model and effort caches."
resource: "https://code.claude.com/docs/en/prompt-caching"
tags: [prompt-caching, prefix, cache, layers]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers: []
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "prompt-caching"
    resource: "https://code.claude.com/docs/en/prompt-caching"
    title: "How Claude Code uses prompt caching"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Every message is a new API request carrying the full context. The API matches the start (prefix) of each request against recently processed content; the match is exact, so a change anywhere in the prefix recomputes everything after it. There is no per-file or per-segment caching. Cached re-reads are billed at the cached token rate.

# How to use it

Claude Code orders requests so rarely changing content comes first:

| Layer | Content | Changes when |
| - | - | - |
| System prompt | Core instructions, tool definitions | The set of loaded tool definitions changes |
| Project context | CLAUDE.md, auto memory, unscoped rules | Session starts, or after `/clear` or `/compact` |
| Conversation | Messages, responses, tool results | Every turn |

A change to the system prompt invalidates everything after it. Plan mode and skill loading append instructions as conversation messages, so the prefix stays intact. Model and effort level sit outside the table: each model has its own cache, and on most models each effort level has its own cache.

# Notes

Pick model and effort at the top of a session and save `/compact` for natural breaks; fewer mid-task changes mean a higher hit rate. Actions are split into [those that invalidate](./models-effort-fast-mode.md) and [those that keep the cache](./actions-that-keep-cache.md).
