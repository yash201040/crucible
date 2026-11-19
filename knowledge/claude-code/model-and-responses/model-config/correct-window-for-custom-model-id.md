---
type: "Feature"
title: "Correct the window for a gateway or custom model ID"
description: "Fix the context window Claude Code assumes for unrecognized model IDs using modelOverrides, [1m], CLAUDE_CODE_MAX_CONTEXT_TOKENS and related variables."
resource: "https://code.claude.com/docs/en/model-config#correct-the-window-for-a-gateway-or-custom-model-id"
tags: [context-window, gateway, custom-model, env-var]
kind: "env_var"
maturity: "unlabelled"
since: "2.1.324"
surfaces: [cli]
requires: "Unrecognized ID like claude-sonnet-latest needs v2.1.324+"
identifiers:
  - "CLAUDE_CODE_MAX_CONTEXT_TOKENS"
  - "CLAUDE_CODE_DISABLE_1M_CONTEXT"
  - "DISABLE_COMPACT"
  - "CLAUDE_CODE_DISABLE_UNKNOWN_MODEL_WINDOW_ENFORCEMENT"
  - "modelOverrides"
  - "modelPicker"
  - "behavesAs"
  - "[claude-code:unrecognized_model]"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "model-config"
    resource: "https://code.claude.com/docs/en/model-config"
    title: "Model configuration"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

When Claude Code does not recognize a session's model ID it warns (`Model "my-gateway-opus" isn't recognized · context assumed to be 1m tokens · ...`) and assumes a context window, auto-compacting to fit. If the assumed window is the real one, nothing to fix.

# How to use it

- Newer model than your version: `claude update`.
- Gateway/provider name for a known model: add a `modelOverrides` entry mapping the Anthropic ID to yours (e.g. `"claude-opus-4-8": "my-gateway-opus"`), or list the ID in a `modelPicker` row with `behavesAs` set to that model.
- 1M model: append `[1m]` where you set the model, e.g. `claude --model 'my-gateway-opus[1m]'`.
- Any other window: set `CLAUDE_CODE_MAX_CONTEXT_TOKENS` (e.g. `400000`) in the environment that starts Claude Code.

# Limits and defaults

How `CLAUDE_CODE_MAX_CONTEXT_TOKENS` applies:
- Unrecognized ID without `[1m]`: applies on its own; proactive compaction continues at the declared window (for IDs like `claude-sonnet-latest` needs v2.1.324+).
- Unrecognized ID with `[1m]` (any casing): Claude Code assumes 1M; a smaller value does not apply alone. Also set `CLAUDE_CODE_DISABLE_1M_CONTEXT=1` so it sizes like the ID without `[1m]`. A declared window above 200K makes the "200K limit isn't enforced" warning expected.
- ID resolving to a recognized model (contains a known Claude name, e.g. `anthropic/claude-opus-4-8`, `us.anthropic.claude-…-v1:0`, `claude-sonnet-4-5@20250929`, also with `[1m]`, which resolves to Opus 4.8 even with `CLAUDE_CODE_DISABLE_1M_CONTEXT` set): takes effect only with `DISABLE_COMPACT` (disables all compaction).
- For an unrecognized ID, `CLAUDE_CODE_DISABLE_UNKNOWN_MODEL_WINDOW_ENFORCEMENT=1` compacts only after the API rejects with a recognized too-long error; this recovery does not run if a gateway rewrites the error.
- A `[claude-code:unrecognized_model]` diagnostic line stops when a `modelOverrides` entry has that ID as its value.
