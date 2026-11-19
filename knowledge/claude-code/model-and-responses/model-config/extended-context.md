---
type: "Feature"
title: "Extended context (1M window)"
description: "Which models have the 1M window natively or via [1m], plan requirements, gateway behavior, disabling 1M, and Haiku 5.5 pricing."
resource: "https://code.claude.com/docs/en/model-config#extended-context"
tags: [context-window, 1m, plans, gateway, cost]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.323"
surfaces: [cli]
requires: "Opus 4.6 and Sonnet 4.6 need [1m] variants and plan access"
identifiers:
  - "[1m]"
  - "CLAUDE_CODE_DISABLE_1M_CONTEXT"
  - "CLAUDE_CODE_AUTO_COMPACT_WINDOW"
  - "ANTHROPIC_BASE_URL"
  - "claude-haiku-5-5"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "model-config"
    resource: "https://code.claude.com/docs/en/model-config"
    title: "Model configuration"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A 1M token context window is supported by Fable models, Sonnet 5 and later, Haiku 5.5, Opus 4.6 and later, and Sonnet 4.6. Fable models, Sonnet 5 and later, Haiku 5.5 and Opus 4.7 and later run with it by default, no `[1m]` needed, including on Bedrock, Agent Platform, Foundry and Claude apps gateway. Opus 4.6 and Sonnet 4.6 reach 1M only via `[1m]`.

# How to use it

`/model claude-opus-4-6[1m]`, `/model claude-sonnet-4-6[1m]`, or `/model opus[1m]` (suffix applies to the alias's resolved model).

| Plan | Opus 4.6 1M | Sonnet 4.6 1M |
| - | - | - |
| Max, Ultra, Team, Enterprise | Included with subscription | Requires usage credits |
| Pro | Requires usage credits | Requires usage credits |
| API and pay-as-you-go | Full access | Full access |

Turn off: `CLAUDE_CODE_DISABLE_1M_CONTEXT=1` (shell or settings file) removes `[1m]` variants from the picker and treats natively-1M models as 200K. With auto-compaction on, sessions compact at 200K (an auto-compact window above 200K does not lift it; it is capped at the model's window); with auto-compaction off they stop at 200K with the context-limit error.

# Limits and defaults

- On the Anthropic API, 1M uses standard pricing with no premium beyond 200K, except Haiku 5.5, which costs more on prompts over 100K tokens. Haiku 5.5 (`claude-haiku-5-5`) has 1M on every plan, no suffix; `/model claude-haiku-5-5` or `claude --model claude-haiku-5-5`; auto-compacts at about 967K by default.
- Plan requirements are checked only on a direct Anthropic API connection. With `ANTHROPIC_BASE_URL` at an LLM gateway and the saved claude.ai login active, the plan's usage credits are not checked and `[1m]` options stay available (before v2.1.229 `/model sonnet[1m]` was rejected there).
- Behind a gateway, each recognized model gets its Anthropic API window; Claude Code cannot detect a lower limit the gateway enforces. If the gateway rejects requests above 200K set `CLAUDE_CODE_AUTO_COMPACT_WINDOW=200000` so all models compact there.
