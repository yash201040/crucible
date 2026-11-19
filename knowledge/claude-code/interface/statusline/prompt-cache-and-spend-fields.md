---
type: "Reference"
title: "Prompt cache and spend limit fields"
description: "The prompt_cache and rate_limits.spend_limit objects in status line input: cache hit ratio, misses, miss causes, and gateway spend."
resource: "https://code.claude.com/docs/en/statusline"
tags: [prompt-cache, spend-limit, cost, statusline]
kind: "api"
maturity: "unlabelled"
since: "2.1.251"
surfaces: [cli]
requires: "Claude Code v2.1.251 or later; spend_limit needs a Claude apps gateway with spend limits"
identifiers:
  - "prompt_cache"
  - "prompt_cache.warm"
  - "prompt_cache.caching_observed"
  - "prompt_cache.ttl"
  - "prompt_cache.expires_at"
  - "prompt_cache.requests"
  - "prompt_cache.misses"
  - "prompt_cache.expected_rebuilds"
  - "prompt_cache.hit_ratio"
  - "prompt_cache.cache_write_tokens"
  - "prompt_cache.miss_recache_tokens"
  - "prompt_cache.last_miss_at"
  - "prompt_cache.last_miss_cause"
  - "prompt_cache.miss_causes"
  - "prompt_cache.recache_tokens_if_cold"
  - "rate_limits.spend_limit.used_percentage"
  - "rate_limits.spend_limit.resets_at"
  - "rate_limits.spend_limit.used_usd"
  - "rate_limits.spend_limit.limit_usd"
  - "rate_limits.spend_limit.period"
  - "tools_changed"
  - "system_prompt_changed"
  - "ttl_expired_5m"
  - "likely_server_side"
  - "tools_added"
  - "tools_removed"
  - "system_char_delta"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "statusline"
    resource: "https://code.claude.com/docs/en/statusline"
    title: "Customize your status line"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Two optional objects in the status line JSON. `prompt_cache` summarizes cache use for the main conversation (subagent requests are not counted), computed from cache token counts in API responses so it works on every provider. It appears after the first main-conversation API response and needs v2.1.251+. The same stats show on the `/usage` command's `Prompt cache (main)` line. `rate_limits.spend_limit` shows spend against a Claude apps gateway spend limit.

# How to use it

| Field | Meaning |
| - | - |
| `warm` | Cached prefix still within TTL; false when last response reported no cache tokens |
| `caching_observed` | Any response reported cache tokens; false means caching off or provider does not report it |
| `ttl` | `"5m"` or `"1h"` |
| `expires_at` | Epoch seconds when it goes cold; null if no cache tokens last response |
| `requests`, `misses` | Requests recorded; misses = re-processed content the cache held (over 5% and at least 2,000 tokens, with no compaction or tool-result clearing to explain it) |
| `expected_rebuilds` | Rebuilds after compaction or clearing old tool results |
| `hit_ratio` | Cache read tokens over all input tokens, 0 to 1; null while counts are zero |
| `cache_write_tokens`, `miss_recache_tokens` | All tokens written to cache; tokens written by miss requests |
| `last_miss_at` | Epoch seconds, null with no misses |
| `last_miss_cause`, `miss_causes` | Likely cause(s) of last miss and counts per cause (v2.1.260+). Causes include `tools_changed`, `system_prompt_changed`, `ttl_expired_5m`, `likely_server_side`; extra counts `tools_added`, `tools_removed`, `system_char_delta` |
| `recache_tokens_if_cold` | Tokens the next request re-caches if cold; null right after compaction/clearing |

Spend limit (behind a Claude apps gateway with spend limits, v2.1.251+):

| Field | Meaning |
| - | - |
| `used_percentage`, `resets_at` | Arrive with every response; percentage can exceed 100 |
| `used_usd`, `limit_usd`, `period` | Estimate in USD and the period (`daily`, `weekly`, `monthly`); fetched about every five minutes; requires v2.1.284+ on both Claude Code and gateway; may be absent |

# Notes

- Before v2.1.295, `used_usd`, `limit_usd`, `period` stayed absent if `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` was set.
- `used_usd` is computed from token counts by the gateway, an estimate not a billed amount.
