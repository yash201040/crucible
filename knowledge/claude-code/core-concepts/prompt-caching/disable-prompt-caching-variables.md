---
type: "Reference"
title: "Disable prompt caching variables"
description: "Environment variables that turn prompt caching off globally or per model family, with alias-resolution caveats."
resource: "https://code.claude.com/docs/en/prompt-caching"
tags: [prompt-caching, env-vars, disable, haiku, managed-settings]
kind: "env_var"
maturity: "unlabelled"
since: "2.1.283"
surfaces: [cli, headless, sdk]
requires: "Haiku variable covering the main conversation: v2.1.283 or later"
identifiers:
  - "DISABLE_PROMPT_CACHING"
  - "DISABLE_PROMPT_CACHING_HAIKU"
  - "DISABLE_PROMPT_CACHING_SONNET"
  - "DISABLE_PROMPT_CACHING_OPUS"
  - "DISABLE_PROMPT_CACHING_FABLE"
  - "ANTHROPIC_SMALL_FAST_MODEL"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "prompt-caching"
    resource: "https://code.claude.com/docs/en/prompt-caching"
    title: "How Claude Code uses prompt caching"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Disabling caching is occasionally useful for debugging with a specific model or provider. Set the variable to `1`. For normal use, leave caching enabled.

# How to use it

| Variable | Effect |
| - | - |
| `DISABLE_PROMPT_CACHING` | Disable for all models |
| `DISABLE_PROMPT_CACHING_HAIKU` | Disable for the default Haiku model (what the `haiku` alias resolves to), including the main conversation when it is the main model (v2.1.283+) |
| `DISABLE_PROMPT_CACHING_SONNET` | Disable for the model the `sonnet` alias resolves to |
| `DISABLE_PROMPT_CACHING_OPUS` | Disable for the model the `opus` alias resolves to |
| `DISABLE_PROMPT_CACHING_FABLE` | Disable for Fable only |

# Limits and defaults

- The Haiku variable also covers a background model set via the deprecated `ANTHROPIC_SMALL_FAST_MODEL` when it differs from the main model.
- A different Haiku version pinned as main keeps caching; use `DISABLE_PROMPT_CACHING`.
- A Sonnet or Opus model ID set directly keeps caching (example: a session on `claude-sonnet-5` keeps caching while `sonnet` resolves to `claude-sonnet-5-5`); use `DISABLE_PROMPT_CACHING`.
- To set policy organization-wide, put these or the TTL variables in the `env` block of managed settings.
