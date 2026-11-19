---
type: "Feature"
title: "Organization model restrictions"
description: "Enterprise admins disable models in the claude.ai admin console, org-wide or per role; notices and rules per entry point."
resource: "https://code.claude.com/docs/en/model-config#organization-model-restrictions"
tags: [model, enterprise, restrictions, roles]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.187"
surfaces: [cli]
requires: "Claude Enterprise plan; Claude Code v2.1.187+; Anthropic API or LLM gateway"
identifiers: []
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "model-config"
    resource: "https://code.claude.com/docs/en/model-config"
    title: "Model configuration"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Organization admins on Claude Enterprise disable individual models in the claude.ai admin console. The restriction is delivered with the account's entitlements at authentication, separate from `availableModels`, and the server enforces it independently at session creation.

# How to use it

- Applies when a member signs in or uses their own API key. Organization-scoped credentials (for example organization service keys) are not tied to a user, so the restriction does not apply.
- The Claude Console has no restriction control; other organizations use `availableModels` plus `enforceAvailableModels`.
- A restricted model is hidden from `/model`. Via `--model`, `ANTHROPIC_MODEL` or `model`: notice `Model "<name>" is restricted by your organization's settings. Using <model> instead.` and an allowed model is used. `/model <name>` is rejected with `Model '<name>' is restricted by your organization's settings. Run /model to choose a different model.`
- A family alias resolves to its usual model if permitted; otherwise the newest permitted version of the family with a substitution notice. `/model <alias>` is rejected only when every version of the family is restricted; startup aliases are still replaced. Before v2.1.205 substitution used the newest released version only.
- Org-wide or per role: org-level disable removes for everyone; role-level grants differ per custom role and a multi-role member can use any model a role grants. Haiku models are always available.
- Changes take effect on new requests within about a minute; the picker reflects it next session.

# Limits and defaults

A model is selectable only if permitted by `availableModels` and not restricted by the organization. Org restrictions reach only the Anthropic API and LLM gateway deployments; on any other provider use `availableModels`.
