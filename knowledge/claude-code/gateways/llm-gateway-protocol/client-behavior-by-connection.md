---
type: "Reference"
title: "Client behavior by connection method"
description: "How model IDs, anthropic-beta values, request fields, cache TTL and background-task model differ across Bedrock/Agent Platform, Anthropic Messages and Claude apps gateway."
resource: "https://code.claude.com/docs/en/llm-gateway-protocol"
tags: [gateway, model-ids, betas, prompt-caching, defaults]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.323"
surfaces: [cli]
requires: ""
identifiers:
  - "CLAUDE_CODE_USE_BEDROCK"
  - "CLAUDE_CODE_USE_VERTEX"
  - "CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS"
  - "extended-cache-ttl"
  - "cache_control"
  - "modelOverrides"
  - "ANTHROPIC_DEFAULT_HAIKU_MODEL"
  - "ANTHROPIC_DEFAULT_OPUS_MODEL_SUPPORTED_CAPABILITIES"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "llm-gateway-protocol"
    resource: "https://code.claude.com/docs/en/llm-gateway-protocol"
    title: "Claude Code gateway compatibility guide"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A gateway sees one of three client behaviors, depending on how the developer connects. Microsoft Foundry and Claude Platform on AWS also use the Anthropic Messages format via their own variables and are left out of the comparison.

# How to use it

| Behavior | Bedrock or Agent Platform format | Anthropic Messages format | Claude apps gateway sign-in |
| - | - | - | - |
| Model IDs | Provider form, for example `us.anthropic.claude-opus-4-8` | Anthropic IDs, for example `claude-opus-4-8` | Anthropic IDs |
| `anthropic-beta` values | Subset Bedrock and Agent Platform accept | Full set, unless `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS` | Subset Bedrock and Agent Platform accept |
| Unrecognized model ID (alias) request fields | Fixed-budget thinking, no effort or context management; still sends mid-conversation system messages | Everything current models accept (adaptive reasoning, effort, context management), which a Bedrock or Agent Platform upstream can reject | Same as Bedrock or Agent Platform |
| One-hour prompt cache TTL (developer opt-in) | `ttl` in `cache_control`, no beta | `ttl` plus `extended-cache-ttl` in `anthropic-beta` (must be forwarded) | `ttl`, no beta |
| Background tasks model unless `ANTHROPIC_DEFAULT_HAIKU_MODEL` pins one | Default Sonnet, or main model once selected | Main model, or default Haiku when `ANTHROPIC_API_KEY` or `apiKeyHelper` supplies an Anthropic Console key and `ANTHROPIC_AUTH_TOKEN` is unset | Main model |

# Limits and defaults

For unrecognized model IDs: Claude Code assumes a 1M token context window by default since v2.1.323. A gateway alias can take the capabilities of the model behind it via a `modelOverrides` entry in distributed settings. The `ANTHROPIC_DEFAULT_*_MODEL_SUPPORTED_CAPABILITIES` variables apply only in provider configurations.
