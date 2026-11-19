---
type: "Feature"
title: "Default model for new sessions"
description: "ANTHROPIC_DEFAULT_MODEL sets the starting model only when no flag, env, setting or org default selects one."
resource: "https://code.claude.com/docs/en/model-config#set-a-default-model-for-new-sessions"
tags: [model, default, env-var, resume]
kind: "env_var"
maturity: "unlabelled"
since: "2.1.236"
surfaces: [cli]
requires: "Claude Code v2.1.236+"
identifiers:
  - "ANTHROPIC_DEFAULT_MODEL"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "model-config"
    resource: "https://code.claude.com/docs/en/model-config"
    title: "Model configuration"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`ANTHROPIC_DEFAULT_MODEL=<alias|name>` chooses the model new sessions start on. It is used only when none of these selects a model: `--model`, `ANTHROPIC_MODEL`, a `model` value in any settings file (including a `/model` save), or an organization default model.

# How to use it

Set the variable before launching. The Default option in `/model` also resolves to it (picker row label "Set by ANTHROPIC_DEFAULT_MODEL") unless an organization default applies. A choice saved with `/model` outranks it on later launches; with `ANTHROPIC_MODEL` set instead, Claude Code returns to that variable's model each launch.

# Limits and defaults

- Ignored (Default resolves as if unset) when set to `default`, `inherit`, `opusplan` or `haiku`; when `enforceAvailableModels` is on; when model restrictions exclude the model; or when the model is not available to the account.
- When a new session would start on the variable's model, sessions resumed with `claude --resume`, `--continue` or `/resume` start on it too, not on the transcript's saved model. Otherwise it is not used on resume.
