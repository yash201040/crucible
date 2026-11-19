---
type: "Reference"
title: "Prompt cache TTL settings"
description: "promptCacheTtl and subagentPromptCacheTtl choose 5m or 1h prompt cache lifetime for the main conversation versus subagents, workflows and helper requests."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [prompt-caching, subagents, cost, ttl]
kind: "setting"
maturity: "unlabelled"
since: "2.1.242"
surfaces: [cli, headless, sdk]
requires: "v2.1.242"
identifiers:
  - "promptCacheTtl"
  - "subagentPromptCacheTtl"
  - "FORCE_PROMPT_CACHING_5M"
  - "CLAUDE_CODE_PROMPT_CACHE_TTL"
  - "CLAUDE_CODE_SUBAGENT_PROMPT_CACHE_TTL"
  - "ENABLE_PROMPT_CACHING_1H"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Two keys, scope `Any file`, type string `"5m"` or `"1h"`, default unset (each request gets its default lifetime). The one-hour lifetime keeps the cache warm across longer breaks but the API bills each cache write at a higher rate than at five minutes.

# How to use it

| Key | Applies to |
| :- | :- |
| `promptCacheTtl` | The main conversation: interactive, `-p` and Agent SDK turns, plus helpers run inline with them |
| `subagentPromptCacheTtl` | Requests outside the main conversation: subagents, workflows, and Claude Code's own background and helper requests such as compaction and session titles |

```json
{ "promptCacheTtl": "1h", "subagentPromptCacheTtl": "5m" }
```

Set both to choose a lifetime for every request.

# Limits and defaults

Precedence (highest first) for `promptCacheTtl`: `FORCE_PROMPT_CACHING_5M`, then `CLAUDE_CODE_PROMPT_CACHE_TTL`, then the key, then `ENABLE_PROMPT_CACHING_1H`. For `subagentPromptCacheTtl`: `FORCE_PROMPT_CACHING_5M`, then `CLAUDE_CODE_SUBAGENT_PROMPT_CACHE_TTL`, then the key, then `ENABLE_PROMPT_CACHING_1H` (asks for one hour on every request). A subagent's own frontmatter value ranks separately (see the prompt-caching page).
