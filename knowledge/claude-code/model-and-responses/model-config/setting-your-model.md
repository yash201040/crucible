---
type: "Feature"
title: "Setting your model"
description: "Priority order for choosing a model (/model, --model, env, settings), picker keys, subagent inheritance, validation and non-interactive behavior."
resource: "https://code.claude.com/docs/en/model-config#setting-your-model"
tags: [model, priority, picker, headless, subagents]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk, desktop]
requires: "/model in -p mode needs v2.1.205+; SDK/app switch confirmation needs v2.1.268+"
identifiers:
  - "/model"
  - "--model"
  - "ANTHROPIC_MODEL"
  - "ANTHROPIC_DEFAULT_MODEL"
  - "model"
  - "modelPicker:thisSessionOnly"
  - "PreModelSwitch"
  - "setModel()"
  - "modelUsage"
  - "claude --debug"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "model-config"
    resource: "https://code.claude.com/docs/en/model-config"
    title: "Model configuration"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The ways to choose the model, listed in priority order, and how each behaves across sessions, subagents, headless runs and the SDK.

# How to use it

1. During session: `/model <alias|name>` (or `/model` for the picker).
2. At startup: `claude --model <alias|name>`.
3. Environment: `ANTHROPIC_MODEL=<alias|name>`.
4. Settings file `model` field.
5. Default for new sessions: `ANTHROPIC_DEFAULT_MODEL` (see [default model for new sessions](./default-model-for-new-sessions.md)).

Picker keys: `Enter` switches and saves as default (writes `model` in user settings); `s` switches for this session only (rebind with `modelPicker:thisSessionOnly`). `/model <name>` behaves like `Enter`. `--model` and `ANTHROPIC_MODEL` apply only to the session launched with them, so run different models in different terminals via separate `--model` flags.

Example settings: `{ "permissions": {"allow": ["Bash(npm run lint)"]}, "model": "opus" }`.

# Limits and defaults

- Subagent inheritance: a `/model` switch reaches subagents that inherit the main model (resolved when started). To keep a custom subagent on a smaller model set `model` in its definition.
- `-p` mode: `/model` applies to the current session only, not saved as default.
- Enterprise plan logged in with claude.ai: saving a default with `/model` also records it on the account (v2.1.280+); the Default option can resolve to it when no organization default exists. Choosing Default or `opusplan` does not change the recorded choice.
- PreModelSwitch hooks run before a switch and can block it or ask to confirm. If a managed plugin's hooks fail to load, switching still works; before v2.1.323 it refuses with `so organization-managed PreModelSwitch hooks could not be checked`. Use `/plugin` Errors tab, `claude --debug`, `/reload-plugins`.
- Agent SDK `setModel()`, apps or Remote Control: with v2.1.268+, an ID not accepted locally is confirmed with the provider the first time (on every provider); invalid IDs are refused at the switch. Remote Control on the Anthropic API checks locally with no request.
- `--model`, `ANTHROPIC_MODEL` and `model` setting are not validated up front; the first request errors, and on the Anthropic API a near-miss name that doesn't start with `claude-` gives a closest-name warning.
- Retiring or remapped models show a warning naming the requested model: startup notice interactively; from v2.1.182 on stderr in non-interactive default text output (suppressed for `--output-format json` and `stream-json`; read the actual model from the `modelUsage` field of the result message). Also covers `model` in subagent frontmatter.
- By default a session started on the Anthropic API with a Claude Opus 4 or Opus 4.1 ID (such as `claude-opus-4-1`) runs on the model `opus` resolves to.
- When project or managed settings set the startup model, the header names the file.
- With `CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST`, host model configuration beats managed model settings; a managed `availableModels` allowlist stays unless the host supplies its own.
- Picker prices show only when talking to the Anthropic API (directly or via an LLM gateway); not on third-party providers or Claude apps gateway. In v2.1.144 through v2.1.152, `/model` applied to the current session only and `d` saved a default.
