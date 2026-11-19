---
type: "Reference"
title: "What the default option resolves to"
description: "The account-type default model per plan and provider, history of earlier defaults, and how org default and enforcement change it."
resource: "https://code.claude.com/docs/en/model-config#default-model-setting"
tags: [model, default, plans, providers]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.280"
surfaces: [cli]
requires: ""
identifiers:
  - "default"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "model-config"
    resource: "https://code.claude.com/docs/en/model-config"
    title: "Model configuration"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The `default` setting resolves by account type.

# How to use it

| Account | Default |
| :- | :- |
| Pro, Max, Ultra, Team, Enterprise, Anthropic API | Opus 5.5 |
| Claude Platform on AWS, Claude Models on Google Cloud (Anthropic managed), Amazon Bedrock, Google Cloud's Agent Platform | Opus 5.5 |
| Microsoft Foundry | Sonnet 4.5 |

History: before v2.1.280, `default` was Sonnet 5 on Pro and Team Standard, and Opus 5 on Max, Ultra, Team Premium, Enterprise, Anthropic API, Claude Platform on AWS, Bedrock and Agent Platform from v2.1.219. Before v2.1.219 it was Opus 4.8 on Anthropic API, Max, Ultra, Team Premium and Enterprise pay-as-you-go from v2.1.154, and on Claude Platform on AWS, Bedrock and Agent Platform from v2.1.207. Before v2.1.207: Opus 4.7 on Claude Platform on AWS, Sonnet 4.5 on Bedrock and Agent Platform.

# Limits and defaults

- An organization default model (v2.1.196+), `ANTHROPIC_DEFAULT_MODEL`, or the model recorded on the account replaces the account-type default.
- With nothing recorded, `enforceAvailableModels` on, and the account-type default outside `availableModels`, Default resolves to the enforced Default. When an org default and enforcement both apply, the org default replaces first, then enforcement applies to it.
- Fable models are never the account-type default; choosing one with `/model` saves it as the selected model.
