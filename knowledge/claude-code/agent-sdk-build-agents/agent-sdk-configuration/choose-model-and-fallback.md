---
type: "Feature"
title: "Choose a model and fallback chain"
description: "model pins a model or alias; fallbackModel switches to backups when the primary is overloaded and retries the primary each user turn."
resource: "https://code.claude.com/docs/en/agent-sdk/configuration"
tags: [model, fallback, aliases, cost]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "model"
  - "fallbackModel"
  - "fallback_model"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-configuration"
    resource: "https://code.claude.com/docs/en/agent-sdk/configuration"
    title: "Configure your agent"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Unless `model`, settings or environment select one, a new session uses Claude Code's default model. `model` takes an alias or full model name; pick a smaller model for faster, cheaper agents.

# How to use it

`fallbackModel` (TypeScript) / `fallback_model` (Python) names a backup. When the primary is overloaded or unavailable the session switches; the primary is retried at the start of each user turn. Both languages accept one model or a comma-separated list. Examples: `model: "claude-fable-5", fallbackModel: "claude-opus-5,claude-sonnet-5"`; Python `fallback_model="claude-opus-5"`.

# Limits and defaults

- In TypeScript a fallback equal to `model` throws at startup.
- Order and the chain cap are on the model-config page (Fallback model chains).
- The Messages API parameters `temperature`, `top_p` and `max_tokens` have no option fields in either language; use the effort level or a spend cap, or call the Messages API directly.
