---
type: "Feature"
title: "opusplan model setting"
description: "Hybrid alias that plans with Opus and executes with Sonnet, with 1M variant and allowlist substitution rules."
resource: "https://code.claude.com/docs/en/model-config#opusplan-model-setting"
tags: [model, plan-mode, opus, sonnet]
kind: "setting"
maturity: "unlabelled"
since: "2.1.265"
surfaces: [cli]
requires: "/model opusplan[1m] needs v2.1.265+"
identifiers:
  - "opusplan"
  - "opusplan[1m]"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "model-config"
    resource: "https://code.claude.com/docs/en/model-config"
    title: "Model configuration"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`opusplan` uses `opus` in plan mode and automatically `sonnet` in execution mode (env vars: `ANTHROPIC_DEFAULT_OPUS_MODEL` for plan mode, `ANTHROPIC_DEFAULT_SONNET_MODEL` otherwise).

# How to use it

Set `opusplan`. To request the 1M window where `opus` and `sonnet` lack it by default, use `opusplan[1m]`, e.g. `/model opusplan[1m]` (on versions before v2.1.265 use the `--model` flag or the `model` setting).

# Limits and defaults

- If `availableModels` excludes the newest Opus but permits an older one, planning uses the newest permitted Opus and stays on Sonnet only when every Opus is excluded. A Haiku session that would upgrade to Sonnet in plan mode likewise uses the newest permitted Sonnet. Before v2.1.205, plan mode stayed on the session model.
- That substitution applies on the Anthropic API and Claude Platform on AWS. On Bedrock, Agent Platform, Foundry and Mantle, plan mode stays on the session's model whenever the upgrade model is excluded.
- For a mid-task second-model consult instead, see the advisor tool (`/docs/en/advisor`).
