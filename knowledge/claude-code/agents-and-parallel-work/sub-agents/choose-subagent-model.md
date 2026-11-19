---
type: "Feature"
title: "Choosing a subagent's model"
description: "Model order for subagents, nested subagent model, forcing one model for all, alias versions and allowlist substitution."
resource: "https://code.claude.com/docs/en/sub-agents"
tags: [subagents, model, cost, environment-variables]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.257"
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "CLAUDE_CODE_SUBAGENT_MODEL"
  - "CLAUDE_CODE_SUBAGENT_MODEL_FORCE"
  - "ANTHROPIC_DEFAULT_OPUS_MODEL"
  - "availableModels"
  - "inherit"
  - "opusplan"
  - "/tasks"
  - "model"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sub-agents"
    resource: "https://code.claude.com/docs/en/sub-agents"
    title: "Create custom subagents"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

By default a subagent runs on the same model as the conversation that starts it. Values for `model`: alias (`sonnet`, `opus`, `haiku`, `fable`), a full model ID the `--model` flag accepts (such as `claude-opus-5-5`, `claude-sonnet-5`), or `inherit` (main conversation's model, or the spawning subagent's model for a nested one).

# How to use it

Order of precedence, first wins:
1. Per-invocation `model` parameter Claude passes (an alias only, not a full ID or `inherit`).
2. The `model` field in the definition, including `inherit`.
3. `CLAUDE_CODE_SUBAGENT_MODEL` environment variable.
4. The main conversation's model, or spawning subagent's model if nested.

An alias passed per call is kept on resume or follow-up. A mod's `agent.spawn` hook model replaces the per-invocation parameter.

Force one model on every subagent, teammate and workflow agent (v2.1.257 or later):

```json
{"env": {"CLAUDE_CODE_SUBAGENT_MODEL": "haiku", "CLAUDE_CODE_SUBAGENT_MODEL_FORCE": "1"}}
```

While force is on, the definition `model` field is ignored and Claude cannot pass a model. A fork and a skill running in a subagent with `model: inherit` still use the parent's model. With only `_FORCE` set, subagents use the main model (Explore uses its built-in model). `CLAUDE_CODE_SUBAGENT_MODEL` alone does not change Explore and Plan.

# Limits and defaults

- Nested subagents default to the parent subagent's model. Subagents with `model: inherit` or no field, built-in Explore, Plan, general-purpose and forks all run on the spawner's model (e.g. Haiku). In plan mode these run on Opus if the session model is `opusplan`, or Sonnet if it is `haiku`.
- Family alias such as `opus` runs on the parent's model when same family (parent on `claude-opus-4-7` gives that version) or when the family is unknown (such as an unlookup-able Bedrock ARN; only the `opus` alias on non-Anthropic-API providers). Set `ANTHROPIC_DEFAULT_OPUS_MODEL` to choose the version.
- If the `availableModels` allowlist blocks the model: newest permitted version in that family (on supporting providers), then `CLAUDE_CODE_SUBAGENT_MODEL`, then the main/spawner model. A top-level subagent in an interactive session shows a warning.
- Check a subagent's model with `/tasks` (shows model and effort; v2.1.242 or later).
