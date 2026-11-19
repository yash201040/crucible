---
type: "Feature"
title: "Agent Platform model pinning and startup checks"
description: "Default models, pinning variables, startup checks, fallbacks, allowlist enforcement and the 1M window on Google Cloud's Agent Platform."
resource: "https://code.claude.com/docs/en/google-vertex-ai"
tags: [vertex-ai, models, pinning, fallback]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.287"
surfaces: [cli]
requires: "Google Cloud Agent Platform"
identifiers:
  - "ANTHROPIC_DEFAULT_OPUS_MODEL"
  - "ANTHROPIC_DEFAULT_SONNET_MODEL"
  - "ANTHROPIC_DEFAULT_HAIKU_MODEL"
  - "ANTHROPIC_DEFAULT_MODEL"
  - "ANTHROPIC_MODEL"
  - "enforceAvailableModels"
  - "availableModels"
  - "modelOverrides"
  - "CLAUDE_CODE_SKIP_MODEL_ACCESS_MEMORY"
  - "CLAUDE_CODE_DISABLE_MODEL_ACCESS_FALLBACK"
  - "CLAUDE_CODE_DISABLE_1M_CONTEXT"
  - "roles/aiplatform.user"
  - "aiplatform.endpoints.predict"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "google-vertex-ai"
    resource: "https://code.claude.com/docs/en/google-vertex-ai"
    title: "Claude Code on Google Cloud's Agent Platform"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Pin versions for multi-user deployments: unpinned aliases resolve to built-in defaults that can lag the newest release and may not be enabled in the project.

# How to use it

- Pin e.g. `ANTHROPIC_DEFAULT_OPUS_MODEL='claude-opus-4-8'`, `ANTHROPIC_DEFAULT_SONNET_MODEL='claude-sonnet-5'`, `ANTHROPIC_DEFAULT_HAIKU_MODEL='claude-haiku-4-5@20251001'`.
- Background tasks use the default Sonnet, not Haiku, unless you pick a primary model (`--model`, `ANTHROPIC_MODEL`, `model` setting, `ANTHROPIC_DEFAULT_MODEL`, or setting `ANTHROPIC_DEFAULT_OPUS_MODEL` without a Sonnet pin) or set `ANTHROPIC_DEFAULT_HAIKU_MODEL`.
- Startup: offers to update an older pin when the project can invoke a newer default (accept writes user settings and restarts; decline remembered). No check or prompt for pins in managed settings `env`; the repeating prompt for managed pins was fixed in v2.1.314.
- Unpinned default unavailable: session-only fallback to earlier versions, or default Sonnet if no Opus. A session started on a specific Sonnet/Opus version acts as a pin for that alias; a bare alias or unrecognized ID does not.
- Refusals remembered up to a day, rechecked after 10 minutes; `CLAUDE_CODE_SKIP_MODEL_ACCESS_MEMORY=1` turns this off.
- `enforceAvailableModels` in managed settings restricts startup checks to `availableModels` (requires v2.1.287+), written in the IDs sent to Agent Platform, e.g. `["claude-opus-4-8", "claude-sonnet-4-5@20250929"]`.
- Mid-session rejection: switches with `Switched to <fallback> because <model> is not available` unless a fallback chain exists; fails on pinned/specific versions or if nothing is available (auto mode switches only to supported models). `CLAUDE_CODE_DISABLE_MODEL_ACCESS_FALLBACK=1` makes requests fail instead.
- IAM: role `roles/aiplatform.user` carries `aiplatform.endpoints.predict` (model invocation and token counting). Dedicated GCP project suggested for cost tracking.

# Limits and defaults

| Item | Default |
|---|---|
| Primary model | `claude-opus-5-5` (before v2.1.280: Opus 5) |
| Small/fast model | `claude-sonnet-4-5@20250929` |
| `sonnet` alias unpinned | Sonnet 4.5 |

Unpinned primary model is billed at the Opus rate. 1M window is default for Fable, Sonnet 5 and later, Opus 4.7 and later (before v2.1.287 needed `[1m]`); Opus 4.6 and Sonnet 4.6 need `[1m]`; `CLAUDE_CODE_DISABLE_1M_CONTEXT=1` keeps 200K.

# Notes

Troubleshooting: "Could not load the default credentials" (run ADC login or set `GOOGLE_APPLICATION_CREDENTIALS`); "model not found" 404 (enable in Model Garden, check location, per-model `VERTEX_REGION_CLAUDE_*` or switch model when `global` unsupported); 429 (check regional support or use `CLOUD_ML_REGION=global`).
