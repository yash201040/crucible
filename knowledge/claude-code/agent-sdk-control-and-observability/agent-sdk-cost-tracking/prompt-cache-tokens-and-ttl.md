---
type: "Feature"
title: "Cache tokens and 1-hour prompt cache TTL"
description: "Cache creation and read token fields, and the env vars and settings that choose a 5-minute or 1-hour cache TTL."
resource: "https://code.claude.com/docs/en/agent-sdk/cost-tracking"
tags: [prompt-caching, ttl, cost, environment]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: "API key, Bedrock, Google Cloud's Agent Platform, Microsoft Foundry or Claude Platform on AWS for the 5-minute default"
identifiers:
  - "cache_creation_input_tokens"
  - "cache_read_input_tokens"
  - "ENABLE_PROMPT_CACHING_1H"
  - "CLAUDE_CODE_PROMPT_CACHE_TTL"
  - "promptCacheTtl"
  - "CLAUDE_CODE_SUBAGENT_PROMPT_CACHE_TTL"
  - "subagentPromptCacheTtl"
  - "CLAUDE_CODE_USE_BEDROCK"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-cost-tracking"
    resource: "https://code.claude.com/docs/en/agent-sdk/cost-tracking"
    title: "Track cost and usage"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The SDK uses prompt caching automatically. Usage carries `cache_creation_input_tokens` (new cache entries, higher rate) and `cache_read_input_tokens` (reads, reduced rate); track them separately from `input_tokens`. In Python they are keys of `ResultMessage.usage`.

# How to use it

Cache entries for your own turns default to a 5-minute TTL with an API key or on Bedrock, Google Cloud's Agent Platform, Microsoft Foundry or Claude Platform on AWS. To get a 1-hour TTL on cache writes set `ENABLE_PROMPT_CACHING_1H` (shell, container, or `options.env`), e.g. `env={"CLAUDE_CODE_USE_BEDROCK": "1", "ENABLE_PROMPT_CACHING_1H": "1"}` (needs working AWS credentials).

| Control | Bucket | Value |
| - | - | - |
| `ENABLE_PROMPT_CACHING_1H` | both buckets | 1-hour TTL on every request |
| `CLAUDE_CODE_PROMPT_CACHE_TTL` or `promptCacheTtl` | main conversation (your turns plus inline helpers) | `5m` or `1h` |
| `CLAUDE_CODE_SUBAGENT_PROMPT_CACHE_TTL` or `subagentPromptCacheTtl` | everything else, such as subagents | `5m` or `1h` |

The per-bucket controls take precedence over `ENABLE_PROMPT_CACHING_1H`.

# Limits and defaults

1-hour writes cost more than 5-minute writes. On a Claude subscription within included usage you get the 1-hour TTL on your own turns without setting anything, and Claude Code drops to 5 minutes once you draw on usage credits; `promptCacheTtl` set to `1h` keeps 1 hour while on credits.
