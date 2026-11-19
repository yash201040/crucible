---
type: "Feature"
title: "Checking cache performance"
description: "Cache token fields, the /usage Prompt cache (main) line with likely-cause text, status line fields and OpenTelemetry."
resource: "https://code.claude.com/docs/en/prompt-caching"
tags: [prompt-caching, usage, statusline, telemetry, metrics]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.251"
surfaces: [cli, headless, sdk]
requires: "/usage and prompt_cache line: v2.1.251 or later; likely-cause text: v2.1.260 or later"
identifiers:
  - "cache_creation_input_tokens"
  - "cache_read_input_tokens"
  - "current_usage"
  - "prompt_cache"
  - "/usage"
  - "Prompt cache (main)"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "prompt-caching"
    resource: "https://code.claude.com/docs/en/prompt-caching"
    title: "How Claude Code uses prompt caching"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The API reports two token counts on every response; a status line script reads them from the `current_usage` object.

# How to use it

| Field | Meaning |
| - | - |
| `cache_creation_input_tokens` | Tokens written to cache this turn, billed at the cache write rate |
| `cache_read_input_tokens` | Tokens served from cache this turn, billed at the cached token rate |

A high read-to-creation ratio means caching works; persistently high creation means the prefix keeps changing. `/usage` adds a `Prompt cache (main)` line to the Session block after the main conversation's first response, showing hit ratio, miss count and whether the cache is warm. It names the likely cause of the last miss when identifiable (e.g. `likely cause: tool definitions changed`). A status line script can read the same data from the `prompt_cache` object.

# Notes

The OpenTelemetry exporter reports cache read and creation tokens per user and session (see the Monitor usage page).
