---
type: "Feature"
title: "Append to preset and cross-user prompt caching"
description: "Add instructions after the claude_code preset and use excludeDynamicSections so identical configs share a cache entry."
resource: "https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts"
tags: [append, prompt-caching, exclude-dynamic-sections, fleet]
kind: "setting"
maturity: "unlabelled"
since: "0.2.98"
surfaces: [sdk, cli]
requires: "@anthropic-ai/claude-agent-sdk v0.2.98 or later, or claude-agent-sdk v0.1.58 or later for Python"
identifiers:
  - "append"
  - "excludeDynamicSections"
  - "exclude_dynamic_sections"
  - "--exclude-dynamic-system-prompt-sections"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-modifying-system-prompts"
    resource: "https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts"
    title: "Modifying system prompts"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`append` on the preset object adds your instructions while keeping built-in behavior. By default two sessions with the same preset and `append` still cannot share a cache entry if their auto memory locations differ: the preset embeds that location (an absolute path under `~/.claude/projects/` named for the repository path) ahead of `append`. CLAUDE.md and environment details (working directory, platform, shell, OS version) do not affect the cache because they are delivered in the conversation.

# How to use it

Set `excludeDynamicSections: true` (TypeScript) or `"exclude_dynamic_sections": True` (Python) on the preset object. Per-user context moves into the first user message, so identical configurations share a cache entry across users and machines. CLI equivalent: `--exclude-dynamic-system-prompt-sections`.

# Limits and defaults

The option is ignored when you pass a custom prompt instead of the preset. Tradeoff: the moved text (at least the auto memory directory location, often the whole section) reaches Claude in a user message, which carries marginally less weight, so auto memory guidance may be followed less consistently.
