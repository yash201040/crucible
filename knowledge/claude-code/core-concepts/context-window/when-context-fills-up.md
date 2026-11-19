---
type: "Guide"
title: "Managing a filling context window"
description: "Automatic compaction, manual /compact focus, /rewind summarize, /autocompact, /clear, delegating to subagents and 1M-token window support."
resource: "https://code.claude.com/docs/en/context-window"
tags: [compaction, context, autocompact, rewind]
kind: "slash_command"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: "1M window: Fable models, Sonnet 5 and later, Haiku 5.5, Opus 4.6 and later, Sonnet 4.6"
identifiers:
  - "/compact"
  - "/rewind"
  - "/autocompact"
  - "/clear"
  - "[1m]"
  - "idleCompaction"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "context-window"
    resource: "https://code.claude.com/docs/en/context-window"
    title: "Explore the context window"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude Code compacts automatically as the limit approaches, so a full window does not end the session. The automatic pass works like `/compact`. Idle conversations can also be compacted (see the `idleCompaction` setting).

# How to use it

| Action | Command |
| - | - |
| Compact with a focus | `/compact focus on the auth bug fix` |
| Compact part of the conversation | `/rewind`, select a message, choose **Summarize from here** or **Summarize up to here** |
| Compact earlier | `/autocompact 500k` (sets how full the window gets before the automatic pass) |
| Clear between tasks | `/clear` (old conversation crowds out files and costs tokens on every message) |
| Delegate large reads | Send research to a subagent so contents stay in its window |

# Limits and defaults

- Fable models, Sonnet 5 and later, Haiku 5.5, Opus 4.6 and later, and Sonnet 4.6 support a 1 million token context window via a `[1m]` model variant; compaction works the same at the larger limit.
- Auto-compact thresholds depend on model and configuration; the model-config page lists defaults per model and how to correct the window for a gateway or custom model ID (e.g. an LLM gateway alias).

# Notes

Related pages named: prompt caching (which actions invalidate the cached prefix), costs (reduce token usage), best practices (keep cost and context down).
