---
type: "Reference"
title: "Fast mode requirements and blockers"
description: "Provider, billing, usage-credit, Owner-enablement and organization settings needed for fast mode, with the messages /fast shows."
resource: "https://code.claude.com/docs/en/fast-mode"
tags: [fast-mode, requirements, usage-credits, organization]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, cloud]
requires: "Pro/Max/Ultra/Team/Enterprise with usage credits, or paid Console organization"
identifiers:
  - "CLAUDE_CODE_DISABLE_FAST_MODE"
  - "fastMode"
  - "availableModels"
  - "/usage-credits"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "fast-mode"
    resource: "https://code.claude.com/docs/en/fast-mode"
    title: "Speed up responses with fast mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Everything that must be true for `/fast` to work, plus what blocks it.

# How to use it

- **Provider**: Anthropic Console API, Claude subscription plans using usage credits, and Google Cloud's Agent Platform with conditions. Not Amazon Bedrock, Microsoft Foundry or Claude Platform on AWS (`/fast` says "Fast mode is not available on this provider").
- **Usage credits (subscriptions)**: must be on, else `/fast` reports "Fast mode requires usage credits". Pro/Max/Ultra: Usage credits section of Settings > Usage, or `/usage-credits`. Team/Enterprise: a member with billing access enables them at Organization settings > Usage; others run `/usage-credits` to request. Fast mode draws directly from usage credits even with plan usage left.
- **Paid Console organization**: no usage credits; billed per token. The free Evaluation plan shows "Fast mode unavailable during evaluation. Please purchase credits." Fable 5.2 and Opus 5.5 also depend on the organization's usage tier. Console organizations need provisioned access for Opus 5 or Opus 4.8; without it requests hit the fast mode rate limit and fall back to standard speed.
- **Owner enablement**: disabled by default for Team and Enterprise. Console admins enable in Claude Code preferences at platform.claude.com; Claude AI Owners enable at Organization settings > Claude Code.
- `CLAUDE_CODE_DISABLE_FAST_MODE=1` disables it entirely.

# Limits and defaults

Four organization settings block `/fast`: not enabled for the organization; managed `fastMode: false` (both show "Fast mode has been disabled by your organization."); managed `fastModePerSessionOptIn: true` (refuses `/fast on` outside an interactive terminal session with the same message); `availableModels` excluding the model `/fast` would switch to ("is not in your organization's allowed models"; if already on an allowed model that supports fast mode, `/fast` enables it on that model without switching).
