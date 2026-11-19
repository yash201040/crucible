---
type: "Reference"
title: "Advisor requirements and comparison"
description: "Provider, gateway, model and feature-flag requirements for the advisor, and how it compares with opusplan, subagents and /model."
resource: "https://code.claude.com/docs/en/advisor"
tags: [advisor, requirements, opusplan, subagents]
kind: "mixed"
maturity: "experimental"
since: "2.1.300"
surfaces: [cli, headless, sdk]
requires: "Anthropic API or listed cloud providers"
identifiers:
  - "ANTHROPIC_BASE_URL"
  - "DISABLE_TELEMETRY"
  - "opusplan"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "advisor"
    resource: "https://code.claude.com/docs/en/advisor"
    title: "Escalate hard decisions with the advisor tool"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

What an environment needs for the advisor, and the alternatives for combining model strengths.

# How to use it

Requirements:
- **Provider**: Anthropic API, Claude Platform on AWS, or Claude Models on Google Cloud (Anthropic managed); not Bedrock, Google Cloud's Agent Platform or Foundry. The latter two supported ones need v2.1.300+.
- **LLM gateway** (`ANTHROPIC_BASE_URL`): works only if the gateway forwards the request intact to the Anthropic API; otherwise see the LLM gateway protocol page's "Automatic retry and error forwarding".
- **Main model**: Fable, Opus 4.6+, Sonnet 4.6+, Haiku 4.5 or Haiku 5.5.
- **Feature-flag fetching**: unless on the two cloud providers above, the advisor needs a feature flag fetched from Anthropic. A variable that turns fetching off (such as `DISABLE_TELEMETRY`) removes it.

| Approach | When the stronger model runs | How it starts |
| - | - | - |
| Advisor tool | At decision points mid-task | Claude calls it |
| `opusplan` | In plan mode (when allowed by `availableModels`), then Sonnet for execution | You enter plan mode |
| Subagent with `model` set | The whole delegated subtask | Claude delegates or you invoke it |
| `/model` | From the next request onward | You switch |
