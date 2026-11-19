---
type: "Feature"
title: "Organization default model"
description: "Enterprise admins set a default Claude Code model org-wide or per role; precedence, override option and restriction checks."
resource: "https://code.claude.com/docs/en/model-config#organization-default-model"
tags: [model, enterprise, default, precedence]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.196"
surfaces: [cli]
requires: "Claude Enterprise plan; Claude Code v2.1.196+; Anthropic API sessions"
identifiers:
  - "model"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "model-config"
    resource: "https://code.claude.com/docs/en/model-config"
    title: "Model configuration"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Admins on Claude Enterprise set a default model for members from the claude.ai admin console, for the whole organization or per custom role. The Default option resolves to it, and the `/model` Default row shows its name with the label Org default. A role default beats the org-wide one; with several roles the most capable model applies.

# How to use it

It is a starting point, not a restriction. Taking precedence over it: `--model`, `ANTHROPIC_MODEL`, `model` in managed settings or via `--settings`, and `model` in user, project or local settings (including a `/model` save). Admins can turn on override, which beats user, project and local `model`; a `/model` choice then applies for the session only and `/model` shows `Your organization's default (<model>) applies on restart`. `--model`, `ANTHROPIC_MODEL`, managed settings and `--settings` still win.

# Limits and defaults

- Read once at startup; changes apply on the next launch.
- Without override, the first interactive launch after an admin change clears `model` from user settings once.
- Restriction checks before adoption: with `enforceAvailableModels` an out-of-allowlist default is remapped; an org-restricted model is replaced by the newest allowed in its family or a lower-cost family; `deniedModels` or an `"exact"` list apply; a model unavailable to the account is skipped.
- From v2.1.199 a separate row keeps the account type's usual family in the picker (missing in v2.1.196 to v2.1.198).
- Reaches only Anthropic API sessions; for LLM gateway deployments or elsewhere use `model` in managed settings.
