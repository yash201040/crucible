---
type: "Feature"
title: "Model, effort and fast-mode cache effects"
description: "Switching models, changing effort or toggling fast mode each costs an uncached turn; exceptions for newer models and a PreModelSwitch hook."
resource: "https://code.claude.com/docs/en/prompt-caching"
tags: [prompt-caching, model-switch, effort, fast-mode, opusplan]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.238"
surfaces: [cli]
requires: "Effort changes keep the cache on Fable 5.1 and later, Opus 5.5, Sonnet 5.5 and Haiku 5.5 with an API key or Claude subscription"
identifiers:
  - "/model"
  - "/fast"
  - "PreModelSwitch"
  - "opusplan"
  - "CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "prompt-caching"
    resource: "https://code.claude.com/docs/en/prompt-caching"
    title: "How Claude Code uses prompt caching"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Three settings have their own caches, so changing them recomputes the whole request once.

# How to use it

**Switching models (`/model`).** Next request has no cache hits. At the terminal, Claude Code asks to confirm only while the cache is still warm (within one cache TTL of the last request or response) and the new model is not the one that produced the last response; otherwise it switches without asking. Before v2.1.238 it asked even after expiry. A `PreModelSwitch` hook can require or skip the confirmation. Also model switches: `opusplan` (Opus in plan mode, Sonnet in execution, so each plan toggle switches), automatic model fallback on Fable models, Opus 5.5, Sonnet 5.5 and Opus 5, and a skill or command whose frontmatter `model` differs from the session model (for that turn; a `context: fork` skill sets the forked subagent's model instead).

**Effort level.** On most models a mid-session change reads everything uncached, with a confirmation while warm. With an API key or Claude subscription the cache is kept on Fable 5.1 and later, Opus 5.5, Sonnet 5.5, Haiku 5.5, and the new level applies without asking. It works as on most models on Amazon Bedrock, Google Cloud Agent Platform, a Claude apps gateway, when `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS` is set, or under a HIPAA configuration. Before v2.1.260, effort changes on Fable 5.1 also invalidated the cache.

**Fast mode.** Fast and standard speed keep separate caches. The first time fast mode is turned on in a conversation, the next request reads the whole conversation uncached at fast mode rates; turn it on at session start. Turning it on mid-turn finishes that turn at standard speed. If the model lacks fast mode, `/fast` also switches the model. Each later toggle, including automatic fallback to standard speed after a rate limit and the return, reads uncached what the other speed lacks.
