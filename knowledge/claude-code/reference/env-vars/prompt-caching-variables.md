---
type: "Reference"
title: "Prompt caching and cache TTL variables"
description: "Variables that disable prompt caching globally or per model family and choose the 5-minute or 1-hour cache TTL for main and subagent requests."
resource: "https://code.claude.com/docs/en/env-vars"
tags: [prompt-caching, ttl, cost, subagents]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "DISABLE_PROMPT_CACHING"
  - "DISABLE_PROMPT_CACHING_FABLE"
  - "DISABLE_PROMPT_CACHING_HAIKU"
  - "DISABLE_PROMPT_CACHING_OPUS"
  - "DISABLE_PROMPT_CACHING_SONNET"
  - "ENABLE_PROMPT_CACHING_1H"
  - "ENABLE_PROMPT_CACHING_1H_BEDROCK"
  - "FORCE_PROMPT_CACHING_5M"
  - "CLAUDE_CODE_PROMPT_CACHE_TTL"
  - "CLAUDE_CODE_SUBAGENT_PROMPT_CACHE_TTL"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "env-vars"
    resource: "https://code.claude.com/docs/en/env-vars"
    title: "Environment variables"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Cache on/off and lifetime controls. Cache reads matter for cost and speed of many agents sharing a prefix.

# How to use it

| Variable | What it does |
| :- | :- |
| `DISABLE_PROMPT_CACHING` | `1` disables caching for all models; beats per-model variables. |
| `DISABLE_PROMPT_CACHING_FABLE` | `1` disables caching for Fable models. |
| `DISABLE_PROMPT_CACHING_HAIKU` | `1` disables caching for the default Haiku model, wherever it runs. |
| `DISABLE_PROMPT_CACHING_OPUS` | `1` disables caching for the default Opus model. |
| `DISABLE_PROMPT_CACHING_SONNET` | `1` disables caching for the default Sonnet model. |
| `ENABLE_PROMPT_CACHING_1H` | `1` requests the 1-hour TTL instead of 5 minutes. Meant for API key, Bedrock, Google Cloud's Agent Platform, Foundry and Claude Platform on AWS users. Subscription users within included usage get 1h on the main conversation automatically; those drawing on usage credits can set it. 1-hour writes cost more. |
| `ENABLE_PROMPT_CACHING_1H_BEDROCK` | Deprecated; use `ENABLE_PROMPT_CACHING_1H`. No effect on Claude apps gateway sessions even when routed to Bedrock. |
| `FORCE_PROMPT_CACHING_5M` | `1` forces the 5-minute TTL; overrides `CLAUDE_CODE_PROMPT_CACHE_TTL`, `CLAUDE_CODE_SUBAGENT_PROMPT_CACHE_TTL`, `ENABLE_PROMPT_CACHING_1H`, and the `promptCacheTtl` and `subagentPromptCacheTtl` settings. |
| `CLAUDE_CODE_PROMPT_CACHE_TTL` | `5m` or `1h` only, for the main conversation (interactive, `-p`, SDK turns and inline helpers). Beats `promptCacheTtl` and `ENABLE_PROMPT_CACHING_1H`; `FORCE_PROMPT_CACHING_5M` beats it. Requires v2.1.242+. |
| `CLAUDE_CODE_SUBAGENT_PROMPT_CACHE_TTL` | `5m` or `1h` only, for requests outside the main conversation (subagents, workflows, background work). Beats `subagentPromptCacheTtl` and `ENABLE_PROMPT_CACHING_1H`; `FORCE_PROMPT_CACHING_5M` beats it. Requires v2.1.242+. |
