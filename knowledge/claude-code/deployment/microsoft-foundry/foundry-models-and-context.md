---
type: "Feature"
title: "Foundry model pinning and 1M context"
description: "Pin deployment names as models on Foundry, background-task model default, prompt cache TTL and how 1M context depends on deployment naming."
resource: "https://code.claude.com/docs/en/microsoft-foundry"
tags: [foundry, models, pinning, context-window]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.323"
surfaces: [cli]
requires: "Microsoft Foundry"
identifiers:
  - "ANTHROPIC_DEFAULT_OPUS_MODEL"
  - "ANTHROPIC_DEFAULT_SONNET_MODEL"
  - "ANTHROPIC_DEFAULT_HAIKU_MODEL"
  - "modelOverrides"
  - "CLAUDE_CODE_DISABLE_1M_CONTEXT"
  - "ENABLE_PROMPT_CACHING_1H"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "microsoft-foundry"
    resource: "https://code.claude.com/docs/en/microsoft-foundry"
    title: "Claude Code on Microsoft Foundry"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Model variables hold your Foundry deployment names. Unpinned aliases resolve to built-in defaults that can lag and may not exist in your resource; then Claude Code switches to an older model (message `Switched to <fallback> because <model> is not available`) or the request fails.

# How to use it

- Pin: `ANTHROPIC_DEFAULT_OPUS_MODEL='claude-opus-4-8'`, `ANTHROPIC_DEFAULT_SONNET_MODEL='claude-sonnet-5'`, `ANTHROPIC_DEFAULT_HAIKU_MODEL='claude-haiku-4-5'`. Unpinned `opus` resolves to Opus 4.6.
- Background tasks (small/fast model) default to the primary model, since not every account has Haiku; set `ANTHROPIC_DEFAULT_HAIKU_MODEL` to use Haiku.
- `ENABLE_PROMPT_CACHING_1H=1` requests 1-hour cache TTL (billed higher); caching otherwise automatic.
- 1M window: default for Fable, Sonnet 5 and later, Opus 4.7 and later, provided Claude Code can tell which model a deployment serves. It reads the model from the deployment name, so name deployments with the model ID (e.g. `claude-opus-4-8`) or map with `modelOverrides` (e.g. `{"modelOverrides": {"claude-opus-4-8": "team-opus-prod"}}`). `CLAUDE_CODE_DISABLE_1M_CONTEXT=1` keeps 200K.

# Limits and defaults

- Unrecognized deployment names are assumed to have a 1M window (from v2.1.323; earlier assumed 200K, requiring `[1m]` on the name). Set the real window if the model accepts less.
- Opus 4.6 and Sonnet 4.6 need `[1m]` on the deployment name. Before v2.1.287 Fable and Opus 4.7+ also needed it.
