---
type: "Feature"
title: "Pin a managed machine to one gateway with allowedProviders"
description: "Set allowedProviders to [customEndpoint] plus a pinned ANTHROPIC_BASE_URL in managed settings so Claude Code refuses any other destination."
resource: "https://code.claude.com/docs/en/llm-gateway"
tags: [gateway, managed-settings, allowed-providers, enforcement]
kind: "setting"
maturity: "unlabelled"
since: "2.1.285"
surfaces: [cli, desktop]
requires: "Claude Code v2.1.285 or later"
identifiers:
  - "allowedProviders"
  - "customEndpoint"
  - "anthropic"
  - "ANTHROPIC_BASE_URL"
  - "ANTHROPIC_BEDROCK_BASE_URL"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "llm-gateway"
    resource: "https://code.claude.com/docs/en/llm-gateway"
    title: "Other LLM gateways"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

In the same managed settings file, set `allowedProviders` to `["customEndpoint"]` and put the gateway's `ANTHROPIC_BASE_URL` in the file's `env` block. Claude Code then refuses a session pointed anywhere else (Anthropic directly, a developer's own proxy) and accepts `ANTHROPIC_BASE_URL` only with the managed value.

# How to use it

- For a gateway reached through a provider-specific variable such as `ANTHROPIC_BEDROCK_BASE_URL`, the `allowedProviders` entry says which variable to pin.
- Requires Claude Code v2.1.285 or later.

# Notes

With Desktop signed in to claude.ai, a Cowork session on the user's machine counts as `"anthropic"`. Leave it out of the list in an MDM or managed settings policy and that session is refused; with it in, sessions sent directly to Anthropic also pass.
