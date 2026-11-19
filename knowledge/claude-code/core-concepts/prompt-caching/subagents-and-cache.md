---
type: "Feature"
title: "Subagents, forks and cache sharing"
description: "Subagents warm their own cache; forks, session copies, resumed subagents and workflow fan-outs can read an earlier prefix."
resource: "https://code.claude.com/docs/en/prompt-caching"
tags: [prompt-caching, subagents, fork, workflows, fan-out]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, sdk]
requires: ""
identifiers:
  - "/fork"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "prompt-caching"
    resource: "https://code.claude.com/docs/en/prompt-caching"
    title: "How Claude Code uses prompt caching"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A subagent has its own system prompt and tool set, so its first request does not read the parent's cache; it warms a cache of its own. The parent's cache is unaffected: the subagent's call and result just append. Subagents fall outside the main-conversation TTL bucket, so they get five minutes even on a subscription unless you choose a longer TTL (see [TTL controls](./cache-ttl-controls-reference.md)).

# How to use it

Requests that can read an earlier prefix:

| Case | Behavior |
| - | - |
| Fork | Inherits parent's system prompt, tools and history exactly; first request reads the parent's cache |
| Session copy via `/fork` | Isolation instruction is added as a message at the end of the copied conversation, so the original cache stays intact |
| Compaction | Summarization call uses the same prefix-sharing approach |
| Resumed subagent | First request can read the cache the original run warmed |
| Workflow fan-out of same-prefix agents | Claude Code holds all but the first for up to 5 seconds by default so their first requests can read the first agent's cached prefix |
