---
type: "Concept"
title: "Where the cache lives and gateways"
description: "Cache location by provider, and how LLM gateways or custom base URLs that handle cache_control markers change what stays cached."
resource: "https://code.claude.com/docs/en/prompt-caching"
tags: [prompt-caching, gateway, bedrock, cache-control, providers]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "ANTHROPIC_BASE_URL"
  - "ANTHROPIC_BEDROCK_BASE_URL"
  - "CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS"
  - "cache_control"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "prompt-caching"
    resource: "https://code.claude.com/docs/en/prompt-caching"
    title: "How Claude Code uses prompt caching"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Caching is server-side, in the infrastructure serving your model. Entries expire after inactivity.

# How to use it

| Authentication | Cache location |
| - | - |
| API key, Claude subscription, Claude Platform on AWS | Anthropic infrastructure via the Claude API |
| Amazon Bedrock, Google Cloud Agent Platform | Your cloud provider's serving infrastructure |
| Microsoft Foundry | Azure for "Hosted on Azure" deployments; Anthropic for "Hosted on Anthropic" |
| Custom `ANTHROPIC_BASE_URL` or LLM gateway | Wherever requests are forwarded; depends on the gateway |

Claude Code appends mid-conversation system context (such as file-change notices) and marks that block for caching on every provider, unless `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS` is set, in which case it is sent uncached.

Gateway or base-URL override (including `ANTHROPIC_BEDROCK_BASE_URL`) behavior with `cache_control` markers:

- Forwards unchanged: same caching as the provider's endpoint.
- Rejects with a `400` naming `cache_control`: Claude Code re-sends with the marker moved to the last conversation message and keeps it there until exit; the block bills uncached, the conversation stays cached.
- Removes markers while returning success: the whole conversation bills as uncached input every turn. A gateway converting block-form system content to a plain string drops the marker the same way.
