---
type: "Feature"
title: "Prompt caching in mod model calls"
description: "Pass prompt or system as an array of { text } blocks and mark the static prefix with cache: true; breakpoints, TTL and where to put them."
resource: "https://code.claude.com/docs/en/plugins/mods/api"
tags: [mods, prompt-caching, cost, model]
kind: "api"
maturity: "unlabelled"
since: "2.1.292"
surfaces: [cli]
requires: "Claude Code v2.1.292 or later for block arrays"
identifiers:
  - "cache: true"
  - "usage.cache_creation_input_tokens"
  - "usage.cache_read_input_tokens"
  - "subagentPromptCacheTtl"
  - "DISABLE_PROMPT_CACHING"
  - "model.complete"
  - "e.prompt"
  - "e.system"
  - "e.promptBlocks"
  - "e.systemBlocks"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-api"
    resource: "https://code.claude.com/docs/en/plugins/mods/api"
    title: "Use the mods API"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`$.model.complete` supports Claude API prompt caching. When every call starts with the same long static content, set a cache breakpoint at the end of it so later calls read it from the cache. Pass `prompt` (or `system`) as an array of `{ text }` blocks and add `cache: true` to the last static block; Claude Code sends it with the API's `cache_control`.

# How to use it

Example: `prompt: [{ text: RULES, cache: true }, { text: e.args }]`.

Where to put static content: put it at the start of `prompt` unless requests go directly to the Claude API. Directly to the API (API key or subscription): either field works. Through Amazon Bedrock, Claude Platform on AWS, Google Cloud's Agent Platform, Microsoft Foundry or an LLM gateway: use `prompt`, because the system prompt starts with an attribution block whose fingerprint derives from the start of the user message (api.anthropic.com strips it before caching; other endpoints do not). In a mod others run, use `prompt`. `system` precedes `prompt` in the prefix, so a `prompt` breakpoint covers `system`, and a different `system` misses the cache.

Check hits in the result's `usage.cache_creation_input_tokens` (written) and `usage.cache_read_input_tokens` (read): expect a write first, reads later within the TTL.

# Limits and defaults

- TTL: five minutes after last use; comes from the user's Claude Code settings, not the call. For one hour set `subagentPromptCacheTtl` to `1h`.
- Up to four breakpoints per request; one more returns an `api-error` in `r.reason`.
- Versions before v2.1.292 reject an array in `prompt` (error ending `takes { model, prompt } (host check)`) and leave an array in `system` out.
- Zero in both fields on answered calls: prefix below model minimum length (no error), a `DISABLE_PROMPT_CACHING` variable applies, a gateway strips `cache_control`, or another mod rewrote the start of the text (then sent without breakpoints).

# Notes

A hook on the `model.complete` event reads `e.prompt` (always a string), `e.system` (string or absent), and `e.promptBlocks`/`e.systemBlocks` (the caller's arrays). Claude Code keeps leading blocks that still match the start of the string you pass to `next`, with their breakpoints, and sends the rest without one: `next({ ...e, prompt: e.prompt + NOTE })` keeps breakpoints; changing the start removes them.
