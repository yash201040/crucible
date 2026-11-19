---
type: "Reference"
title: "Prompt caching environment variables"
description: "DISABLE_PROMPT_CACHING variables to turn prompt caching off globally or per model tier."
resource: "https://code.claude.com/docs/en/model-config#prompt-caching-configuration"
tags: [prompt-caching, env-var, cost, models]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "DISABLE_PROMPT_CACHING"
  - "DISABLE_PROMPT_CACHING_HAIKU"
  - "DISABLE_PROMPT_CACHING_SONNET"
  - "DISABLE_PROMPT_CACHING_OPUS"
  - "DISABLE_PROMPT_CACHING_FABLE"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "model-config"
    resource: "https://code.claude.com/docs/en/model-config"
    title: "Model configuration"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude Code uses prompt caching automatically to improve performance and reduce cost. You can disable it globally or per model tier.

# How to use it

| Variable | Description |
| - | - |
| `DISABLE_PROMPT_CACHING` | `1` disables caching for all models; takes precedence over per-model settings |
| `DISABLE_PROMPT_CACHING_HAIKU` | `1` disables for the default Haiku model |
| `DISABLE_PROMPT_CACHING_SONNET` | `1` disables for the default Sonnet model |
| `DISABLE_PROMPT_CACHING_OPUS` | `1` disables for the default Opus model |
| `DISABLE_PROMPT_CACHING_FABLE` | `1` disables for Fable models only |

# Notes

To pick the cache TTL for the main conversation and subagents separately, see the prompt-caching page's "choose the TTL yourself" section; for what triggers a cache miss see `/docs/en/prompt-caching`.
