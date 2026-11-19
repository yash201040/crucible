---
type: "Reference"
title: "Effort, thinking and output token variables"
description: "Variables that set the effort level, thinking budget, adaptive reasoning, output token cap and the advisor and ultrathink features."
resource: "https://code.claude.com/docs/en/env-vars"
tags: [effort, thinking, output-tokens, models]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "CLAUDE_CODE_EFFORT_LEVEL"
  - "CLAUDE_CODE_ALWAYS_ENABLE_EFFORT"
  - "CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING"
  - "CLAUDE_CODE_DISABLE_THINKING"
  - "MAX_THINKING_TOKENS"
  - "CLAUDE_CODE_MAX_OUTPUT_TOKENS"
  - "CLAUDE_CODE_DISABLE_ULTRATHINK"
  - "CLAUDE_CODE_DISABLE_ADVISOR_TOOL"
  - "DISABLE_INTERLEAVED_THINKING"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "env-vars"
    resource: "https://code.claude.com/docs/en/env-vars"
    title: "Environment variables"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Reasoning depth and response size controls, relevant for tuning cost and quality of unattended agents.

# How to use it

| Variable | What it does |
| :- | :- |
| `CLAUDE_CODE_EFFORT_LEVEL` | `low`, `medium`, `high`, `xhigh`, `max` (available levels depend on model). Beats `--effort`, `/effort`, and the `modelSettings` and `effortLevel` settings; a `maxEffortLevel` cap still applies. `auto` or `unset` sends no effort level so the API applies its model default. |
| `CLAUDE_CODE_ALWAYS_ENABLE_EFFORT` | `1` sends the effort parameter on every request even for unrecognized model IDs (gateways, custom IDs). Models that reject it (Opus 4.1, Sonnet 4.5, Haiku 4.5 and earlier) stay excluded. |
| `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING` | `1` disables adaptive reasoning on Opus 4.6 and Sonnet 4.6 and falls back to the fixed `MAX_THINKING_TOKENS` budget. No effect on Fable models, Sonnet 5 and later, Haiku 5.5, Opus 4.7 and later (always adaptive). |
| `CLAUDE_CODE_DISABLE_THINKING` | `1` omits the `thinking` parameter entirely (proxy compatibility). Models that think by default may still think. To disable thinking on the Anthropic API use `MAX_THINKING_TOKENS=0`. Neither turns thinking off on Opus 5.5, Sonnet 5.5, Haiku 5.5 or Fable models. On third-party providers `MAX_THINKING_TOKENS=0` also just omits the parameter. |
| `MAX_THINKING_TOKENS` | Fixed extended-thinking budget; capped at one below max output tokens and never below 1,024. Unset: adaptive models choose depth, others use the cap. `0` disables thinking on the Anthropic API (not on the models listed above). With thinking off, effort `high` is sent instead of higher levels to models that reject that combination (such as Opus 5). A positive value's number is ignored on adaptive models unless adaptive reasoning is disabled. |
| `CLAUDE_CODE_MAX_OUTPUT_TOKENS` | Max output tokens for most requests; defaults and caps vary by model; values above a model's cap are lowered to it. For an ID Claude Code cannot resolve, default 32000 and cap 128000. |
| `CLAUDE_CODE_DISABLE_ULTRATHINK` | `1` turns the `ultrathink` keyword off. Requires v2.1.316+. |
| `CLAUDE_CODE_DISABLE_ADVISOR_TOOL` | `1` disables the advisor tool: `/advisor` unavailable, `advisorModel` ignored, `--advisor` accepted but no effect (scripts keep working). |
| `DISABLE_INTERLEAVED_THINKING` | `1` stops sending the interleaved-thinking beta header, for gateways or providers that do not support it. |
