---
type: "Feature"
title: "Cache lifetime and TTL buckets"
description: "Five-minute versus one-hour TTL, which request bucket gets which by default, and how to verify the TTL used."
resource: "https://code.claude.com/docs/en/prompt-caching"
tags: [prompt-caching, ttl, subagents, subscription, usage-credits]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: "One-hour default needs a Claude subscription within plan usage"
identifiers:
  - "ephemeral_1h_input_tokens"
  - "ephemeral_5m_input_tokens"
  - "usage.cache_creation"
  - "anthropic-beta"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "prompt-caching"
    resource: "https://code.claude.com/docs/en/prompt-caching"
    title: "How Claude Code uses prompt caching"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Cached prefixes expire after inactivity; each cache hit resets the timer. The API offers a five-minute TTL and a one-hour TTL that costs a higher rate for cache writes. The longer TTL helps with idle-then-return sessions and costs more on short bursts that never idle past five minutes.

# How to use it

Claude Code picks a TTL per request, in one of two buckets:

- Main conversation: interactive turns, non-interactive `-p` runs, Agent SDK turns, plus helpers run inline.
- Everything else: subagents, workflows, in-process teammates, forks, compaction, session titles.

| Request bucket | Claude subscription, within plan usage | Usage credits, API key, or cloud provider |
| - | - | - |
| Main conversation | One hour | Five minutes |
| Everything else | Five minutes (server-controlled helper requests get one hour) | Five minutes |

Once over plan usage and drawing on usage credits, the main conversation drops to five minutes. To confirm which TTL writes used, run `claude -p "hello" --output-format json` and read `usage.cache_creation`.

Getting one hour elsewhere: through an LLM gateway the `anthropic-beta` header must be forwarded unchanged; with a Claude apps gateway ask the admin for the one-hour setting in a gateway policy; on Amazon Bedrock support, minimum prefix length and one-hour TTL availability vary by model (zero cache tokens means check supported models and regions).
