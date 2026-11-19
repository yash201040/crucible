---
type: "Guide"
title: "Maintain the gateway and plan Claude Code upgrades"
description: "Keep a gateway current with new betas, models and credential rotation, and pin Claude Code versions so version-dependent defaults stay constant."
resource: "https://code.claude.com/docs/en/llm-gateway-rollout"
tags: [gateway, upgrades, version-pinning, retries, model-pinning]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.236"
surfaces: [cli]
requires: "ANTHROPIC_DEFAULT_MODEL needs Claude Code v2.1.236 or later"
identifiers:
  - "requiredMaximumVersion"
  - "DISABLE_UPDATES"
  - "ANTHROPIC_DEFAULT_MODEL"
  - "ANTHROPIC_DEFAULT_OPUS_MODEL"
  - "modelOverrides"
  - "ANTHROPIC_MODEL"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "llm-gateway-rollout"
    resource: "https://code.claude.com/docs/en/llm-gateway-rollout"
    title: "Roll out an LLM gateway for your organization"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Three kinds of change reach the gateway after rollout.

# How to use it

| Change | Symptom | Action |
| - | - | - |
| New Claude Code releases add `anthropic-beta` values and body fields | `400` naming a new field after developers update | Forward `anthropic-*` headers and bodies verbatim; test releases before they reach developers |
| New Claude models | `404` on new names; picker lacks them | Add to routing config, rerun the routing check, update `ANTHROPIC_MODEL` or default-model variables if distributed |
| Credential expiry | All requests `401` from upstream | Rotate provider credential separately; developer keys rotate at the gateway; `apiKeyHelper` handles per-developer rotation |

Pin developers to a tested version with `requiredMaximumVersion`, or `DISABLE_UPDATES` if Claude Code is distributed through your own channel; read the changelog and test before raising the pin.

Version-dependent changes without errors:

| Area | Constant via |
| - | - |
| Feature-flag defaults (sessions that do not fetch flags from Anthropic, e.g. cloud provider or telemetry off, use flag defaults built into the installed version) | The version pin |
| Model capability assumptions for unrecognized IDs (adaptive reasoning, effort, context window) | Route Anthropic model IDs at the gateway, or a `modelOverrides` entry mapping the Anthropic ID to your alias |
| Default model and aliases (`opus`, `sonnet` resolution) | `ANTHROPIC_DEFAULT_MODEL` for new sessions (v2.1.236 or later); `ANTHROPIC_DEFAULT_*_MODEL` such as `ANTHROPIC_DEFAULT_OPUS_MODEL` for aliases |

# Limits and defaults

When sizing per-key rate limits, the client retries transient failures including `429` up to 10 times with backoff, honoring `Retry-After`.
