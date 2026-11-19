---
type: "Feature"
title: "Fallback model chains"
description: "Switch to up to three fallback models when the primary is overloaded or unavailable, via --fallback-model or fallbackModel."
resource: "https://code.claude.com/docs/en/model-config#fallback-model-chains"
tags: [model, fallback, reliability, subagents]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.247"
surfaces: [cli, headless]
requires: "Subagent coverage from v2.1.247"
identifiers:
  - "--fallback-model"
  - "fallbackModel"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "model-config"
    resource: "https://code.claude.com/docs/en/model-config"
    title: "Model configuration"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

When the primary model is overloaded, unavailable or returns another non-retryable server error, Claude Code tries fallback models in order instead of failing. Authentication, billing, rate-limit, request-size and transport errors, and a denial by the organization's policy check, never trigger a switch. It does switch when Bedrock or Agent Platform refuses a model the account cannot invoke. A notice shows on switch; the switch lasts that turn only, so the next message tries the primary again.

# How to use it

- One session: `claude --fallback-model sonnet,haiku` (comma-separated).
- Persistent: `{ "fallbackModel": ["claude-sonnet-5", "claude-haiku-5-5"] }`.
- The flag beats the setting. Entries are a name or alias; `"default"` expands to the default model.

# Limits and defaults

- Chains capped at three models after duplicate removal; extras ignored.
- Not confirmed at startup and not shown in `/status`; the first visible sign is the switch notice.
- An unreachable entry (e.g. retired model) fails over to the next.
- Dropped entries: outside `availableModels`; a model with a smaller context window than the primary during compaction (if all are smaller the original error shows); models unsupported by auto mode (also plan mode while the classifier reviews commands).
- Applies to subagents: a failed subagent request tries the chain and the subagent continues on the accepting model; the session model is unchanged. Before v2.1.247 such a failure ended the subagent.
