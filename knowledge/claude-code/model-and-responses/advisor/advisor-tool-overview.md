---
type: "Feature"
title: "Advisor tool overview"
description: "Claude consults a second, stronger server-side model at key moments; experimental and limited to some providers."
resource: "https://code.claude.com/docs/en/advisor"
tags: [advisor, models, experimental, server-tool]
kind: "tool"
maturity: "experimental"
since: ""
surfaces: [cli, headless, sdk, desktop]
requires: "Anthropic API, Claude Platform on AWS, or Claude Models on Google Cloud (Anthropic managed); v2.1.300+ on the latter two"
identifiers: []
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "advisor"
    resource: "https://code.claude.com/docs/en/advisor"
    title: "Escalate hard decisions with the advisor tool"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The advisor lets the main model consult a second, typically stronger model before committing to an approach, when stuck on a recurring error, or before declaring a task complete. The advisor receives the full conversation (every tool call and result) and returns guidance Claude applies. It runs server-side on Anthropic infrastructure as a server tool, for subscription and API-billed accounts. You choose the advisor model; Claude decides when to call it. Docs label it experimental: behavior, pricing and availability may change. Not available on Amazon Bedrock, Google Cloud's Agent Platform or Microsoft Foundry.

# How to use it

Best for long multi-step tasks where plan quality decides the outcome (large refactors, recurring errors, independent completion checks). Less useful for short tasks or work needing the strongest model every turn; switch the main model instead.

Claude's timing is model-driven, not rule-based. You can ask in a prompt (for example `consult the advisor before you continue`). There is no setting to cap or force advisor calls.

# Notes

Subagents inherit the configured advisor and apply the same pairing check against their own model. See [enabling](./enable-the-advisor.md), [model pairings](./advisor-model-pairings.md), [cost and caching](./advisor-cost-and-caching.md).
