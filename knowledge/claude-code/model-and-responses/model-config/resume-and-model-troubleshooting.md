---
type: "Concept"
title: "Resumed-session model and model troubleshooting"
description: "Which model a resumed session uses, why a new session starts on a different model, and the mistyped-model warning."
resource: "https://code.claude.com/docs/en/model-config#which-model-a-resumed-session-uses"
tags: [model, resume, sessions, troubleshooting]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "claude --resume"
  - "--continue"
  - "--model"
  - "ANTHROPIC_MODEL"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "model-config"
    resource: "https://code.claude.com/docs/en/model-config"
    title: "Model configuration"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A session resumed with `claude --resume` or `--continue` keeps the model it was saved on, with exceptions where the normal [priority order](./setting-your-model.md) applies.

# How to use it

Exceptions (priority order applies instead):
- an alias variable such as `ANTHROPIC_DEFAULT_OPUS_MODEL`, or `ANTHROPIC_DEFAULT_MODEL` under its conditions, is set
- the saved model is retired or excluded by `availableModels`
- the provider uses provider-specific deployment IDs (Bedrock, Agent Platform, Foundry)
- `model` setting is `haiku` and the session was saved on a Haiku or Sonnet model (e.g. a session saved on Haiku 4.5 resumes on Haiku 5.5)
- `model` setting is `opusplan` and the session was saved on an Opus or Sonnet model

To resume on a chosen model, pass `--model` or set `ANTHROPIC_MODEL`.

# Notes

New session starts on a different model than you picked, usual causes: you chose it for one session (`s`, `--model`, `/model` in non-interactive mode); something higher priority sets it (project/managed `model`, `ANTHROPIC_MODEL`, an override-on org default); Claude Code could not write `~/.claude/settings.json`; or you resumed a session.

Mistyped name: warnings `Model "<model>" isn't recognized · did you mean "<suggestion>"?` mean the ID nearly matches a known name. Fix the ID, or if deliberate leave it (sent as written) and correct the context window via [custom-ID window settings](./correct-window-for-custom-model-id.md).
