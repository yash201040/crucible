---
type: "Feature"
title: "Prompt cache statistics line"
description: "A Prompt cache (main) line in the /usage Session block reporting cache hit share, misses, expected rebuilds and warm/cold state."
resource: "https://code.claude.com/docs/en/costs"
tags: [prompt-cache, usage, statusline, cache-miss, metrics]
kind: "ui"
maturity: "unlabelled"
since: "2.1.251"
surfaces: [cli]
requires: "Claude Code v2.1.251 or later (likely-cause text v2.1.260 or later)"
identifiers:
  - "Prompt cache (main)"
  - "prompt_cache"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "costs"
    resource: "https://code.claude.com/docs/en/costs"
    title: "Manage costs effectively"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

After the main conversation's first API response, `/usage` adds a `Prompt cache (main)` line: request count, share of input tokens served from cache, misses, and whether the cache is warm.

# How to use it

Example: `14 requests · 91% of input tokens from cache · 2 misses (last 6m 10s ago, 310.2k tokens re-cached) · 1 expected rebuild (compaction or tool-result clearing) · warm (1h TTL, last activity 40s ago)`.

| Part | Meaning |
| - | - |
| Misses | Requests that re-processed content the cache already held, with last-miss time and tokens re-cached; may name a likely cause such as `likely cause: tool definitions changed` (v2.1.260+) |
| Expected rebuilds | Misses after Claude Code itself rewrote the conversation (compaction or clearing old tool results); appears only after at least one |
| Warm or cold | Whether the cached prefix is within its cache lifetime, with TTL; when cold shows idle time; if the API reported no cache tokens, ends with `no prompt caching reported by the API` |

Status line scripts can read the same numbers from the `prompt_cache` object.

# Limits and defaults

- Counts come from cache token fields in API responses, so it works on every provider and gateway.
- Covers the main conversation only, not subagents. `/clear` resets it.
