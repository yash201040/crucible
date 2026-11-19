---
type: "Reference"
title: "Alias resolution by provider"
description: "Which model opus, sonnet, haiku and fable resolve to on each provider, plus the Fable gateway caveat."
resource: "https://code.claude.com/docs/en/model-config"
tags: [model, providers, aliases, bedrock, fable]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "ANTHROPIC_DEFAULT_FABLE_MODEL"
  - "ANTHROPIC_DEFAULT_OPUS_MODEL"
  - "ANTHROPIC_DEFAULT_SONNET_MODEL"
  - "claude-fable-5-2"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "model-config"
    resource: "https://code.claude.com/docs/en/model-config"
    title: "Model configuration"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The `opus`, `sonnet` and `haiku` aliases resolve to the newest version on the Anthropic API and to an earlier version on some other providers.

# How to use it

| Provider | `opus` | `sonnet` | `haiku` |
| :- | :- | :- | :- |
| Anthropic API | Opus 5.5 | Sonnet 5.5 | Haiku 5.5 |
| Claude Platform on AWS | Opus 5.5 | Sonnet 4.6 | Haiku 4.5 |
| Claude Models on Google Cloud (Anthropic managed) | Opus 5.5 | Sonnet 5.5 | Haiku 4.5 |
| Amazon Bedrock, Google Cloud's Agent Platform | Opus 5.5 | Sonnet 4.5 | Haiku 4.5 |
| Microsoft Foundry | Opus 4.6 | Sonnet 4.5 | Haiku 4.5 |

Unless `ANTHROPIC_DEFAULT_FABLE_MODEL` is set, `fable` resolves to Fable 5 in Claude apps gateway sessions and to Fable 5.2 everywhere else.

# Limits and defaults

A gateway not configured to serve `claude-fable-5-2` rejects requests for it. To use Fable 5.2 through a gateway that serves it, select it with `/model claude-fable-5-2`.
