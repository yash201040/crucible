---
type: "Reference"
title: "Cache TTL controls and precedence"
description: "Settings and environment variables that choose the cache TTL per bucket and the order in which they win."
resource: "https://code.claude.com/docs/en/prompt-caching"
tags: [prompt-caching, ttl, settings, env-vars, subagents]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.242"
surfaces: [cli, headless, sdk]
requires: "Claude Code v2.1.242 or later (cacheTtl frontmatter: v2.1.248 or later)"
identifiers:
  - "promptCacheTtl"
  - "subagentPromptCacheTtl"
  - "CLAUDE_CODE_PROMPT_CACHE_TTL"
  - "CLAUDE_CODE_SUBAGENT_PROMPT_CACHE_TTL"
  - "FORCE_PROMPT_CACHING_5M"
  - "ENABLE_PROMPT_CACHING_1H"
  - "experimental"
  - "cacheTtl"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "prompt-caching"
    resource: "https://code.claude.com/docs/en/prompt-caching"
    title: "How Claude Code uses prompt caching"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

You can set the TTL for either bucket (see [TTL buckets](./cache-lifetime-ttl-buckets.md)). Each control takes `5m` or `1h`; any other value is ignored.

# How to use it

| Name | Kind | Applies to | What it does |
| - | - | - | - |
| `promptCacheTtl` | setting | Main conversation | Sets TTL; set `1h` for an API key or cloud provider to get a one-hour main-conversation cache |
| `CLAUDE_CODE_PROMPT_CACHE_TTL` | env var | Main conversation | Same, via environment |
| `subagentPromptCacheTtl` | setting | Everything else | Sets TTL for subagents, workflows, teammates, forks, compaction, titles |
| `CLAUDE_CODE_SUBAGENT_PROMPT_CACHE_TTL` | env var | Everything else | Same, via environment |
| `cacheTtl` in subagent `experimental` frontmatter | frontmatter | One subagent's requests | Ignores `1h` while the subscription is using usage credits |
| `FORCE_PROMPT_CACHING_5M=1` | env var | Both | Forces five minutes |
| `ENABLE_PROMPT_CACHING_1H=1` | env var | Both | Requests one hour |

Precedence, first match wins: 1) `FORCE_PROMPT_CACHING_5M=1`; 2) the bucket's environment variable; 3) the bucket's setting; 4) for a subagent's requests, `cacheTtl` in its `experimental` frontmatter; 5) `ENABLE_PROMPT_CACHING_1H=1`; 6) the bucket default.

# Notes

Setting only `promptCacheTtl` leaves non-main requests at five minutes until you choose a TTL for that bucket. Use `FORCE_PROMPT_CACHING_5M=1` when debugging, comparing TTLs, or overriding a longer TTL from managed settings.
