---
type: "Reference"
title: "Bedrock prefixes, IAM, 1M context, tiers, guardrails"
description: "Cross-region inference profile prefixes, required IAM actions, 1M context behavior, service tiers and Guardrails headers on Bedrock."
resource: "https://code.claude.com/docs/en/amazon-bedrock"
tags: [bedrock, iam, context-window, service-tier]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.287"
surfaces: [cli]
requires: "Amazon Bedrock"
identifiers:
  - "ANTHROPIC_BEDROCK_REGION_PREFIX"
  - "ANTHROPIC_BEDROCK_SERVICE_TIER"
  - "X-Amzn-Bedrock-Service-Tier"
  - "CLAUDE_CODE_DISABLE_1M_CONTEXT"
  - "ANTHROPIC_CUSTOM_HEADERS"
  - "X-Amzn-Bedrock-GuardrailIdentifier"
  - "X-Amzn-Bedrock-GuardrailVersion"
  - "bedrock:InvokeModel"
  - "bedrock:InvokeModelWithResponseStream"
  - "bedrock:ListInferenceProfiles"
  - "bedrock:GetInferenceProfile"
  - "aws-marketplace:ViewSubscriptions"
  - "aws-marketplace:Subscribe"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "amazon-bedrock"
    resource: "https://code.claude.com/docs/en/amazon-bedrock"
    title: "Claude Code on Amazon Bedrock"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Reference for routing, permissions and per-request options on the Bedrock Invoke API.

# How to use it

| AWS region | Preferred prefix |
|---|---|
| `us-gov-*` | `us-gov.` (always, variable ignored) |
| `us-*` | `us.` |
| `eu-*` | `eu.` |
| `ap-*` | `apac.` |
| other | `global.` |

- `ANTHROPIC_BEDROCK_REGION_PREFIX` valid values: `us`, `eu`, `apac`, `jp`, `au`, `global`; invalid falls back to region-derived. With profile listing available it picks the preferred-prefix profile, else any matching profile, else the built-in ID with that prefix; without discovery it applies the prefix blindly (400 if not enabled). User-configured IDs/ARNs and `modelOverrides` values are not rewritten.
- IAM policy actions: `bedrock:InvokeModel`, `bedrock:InvokeModelWithResponseStream`, `bedrock:ListInferenceProfiles`, `bedrock:GetInferenceProfile` on inference-profile, application-inference-profile and foundation-model ARNs; plus `aws-marketplace:ViewSubscriptions` and `aws-marketplace:Subscribe` conditioned on `aws:CalledViaLast` = `bedrock.amazonaws.com`. Without `GetInferenceProfile` Claude Code retries once with the alternate request shape (extra round trip per model, common with bearer tokens). Docs suggest a dedicated AWS account for cost tracking.
- 1M context: Fable models, Sonnet 5 and later, Opus 4.7 and later get 1M by default on Invoke and Mantle (no `[1m]`); before v2.1.287 Invoke defaulted to 200K for those. Opus 4.6 and Sonnet 4.6 need `[1m]` on the model ID. `CLAUDE_CODE_DISABLE_1M_CONTEXT=1` keeps 200K. ARNs get 1M when a `modelOverrides` entry maps the model.
- Service tiers: `ANTHROPIC_BEDROCK_SERVICE_TIER` = `default`, `flex` or `priority`, sent as `X-Amzn-Bedrock-Service-Tier` on every Invoke request except model access checks. No effect on Mantle or through a Claude apps gateway. For background sessions, set it in the settings `env` block (a shell export reaches them only if the shell that started the supervisor exported it).
- Guardrails: create and publish a Guardrail (enable cross-region inference if using such profiles), then set `ANTHROPIC_CUSTOM_HEADERS` to `X-Amzn-Bedrock-GuardrailIdentifier: <id>\nX-Amzn-Bedrock-GuardrailVersion: 1` in settings `env`. A mid-stream block keeps streamed text and ends with the guardrail's blocked message.
