---
type: "Reference"
title: "Model alias environment variables"
description: "Env vars that map aliases to full model names, set the subagent model, and the deprecated ANTHROPIC_SMALL_FAST_MODEL."
resource: "https://code.claude.com/docs/en/model-config#environment-variables"
tags: [env-var, model, aliases, subagents]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "ANTHROPIC_DEFAULT_FABLE_MODEL"
  - "ANTHROPIC_DEFAULT_OPUS_MODEL"
  - "ANTHROPIC_DEFAULT_SONNET_MODEL"
  - "ANTHROPIC_DEFAULT_HAIKU_MODEL"
  - "CLAUDE_CODE_SUBAGENT_MODEL"
  - "CLAUDE_CODE_SUBAGENT_MODEL_FORCE"
  - "ANTHROPIC_SMALL_FAST_MODEL"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "model-config"
    resource: "https://code.claude.com/docs/en/model-config"
    title: "Model configuration"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Variables controlling which model names the aliases map to. Each value must be a full model name or the provider's equivalent identifier. (`ANTHROPIC_DEFAULT_MODEL` is covered in [default model for new sessions](./default-model-for-new-sessions.md).)

# How to use it

| Variable | Description |
| - | - |
| `ANTHROPIC_DEFAULT_FABLE_MODEL` | Model for `fable`; also the ID Claude Code recognizes as Fable for automatic fallback on third-party providers |
| `ANTHROPIC_DEFAULT_OPUS_MODEL` | Model for `opus`, or for `opusplan` in Plan Mode |
| `ANTHROPIC_DEFAULT_SONNET_MODEL` | Model for `sonnet`, or for `opusplan` outside Plan Mode |
| `ANTHROPIC_DEFAULT_HAIKU_MODEL` | Model for `haiku`, or background functionality |
| `CLAUDE_CODE_SUBAGENT_MODEL` | Default model for subagents, agent team teammates and workflow agents not assigned a model otherwise; alias or full name; a per-invocation model or definition `model` (including `inherit`) takes precedence unless `CLAUDE_CODE_SUBAGENT_MODEL_FORCE` is set |
| `ANTHROPIC_SMALL_FAST_MODEL` | Deprecated in favor of `ANTHROPIC_DEFAULT_HAIKU_MODEL` |

# Notes

On third-party providers see [pinned model display and capabilities](./pinned-model-display-and-capabilities.md).
