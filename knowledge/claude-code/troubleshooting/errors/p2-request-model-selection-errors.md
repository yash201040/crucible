---
type: "Reference"
title: "Model selection and version errors"
description: "Errors for unknown models, model switching via SDK or Remote Control, plan limits and minimum Claude Code versions per model."
resource: "https://code.claude.com/docs/en/errors"
tags: [errors, models, model-switching, sdk, versions]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk, desktop]
requires: ""
identifiers:
  - "/model"
  - "--model"
  - "ANTHROPIC_MODEL"
  - "setModel()"
  - "set_model()"
  - "supportedModels()"
  - "model_not_found"
  - "claude_code_version_too_old"
  - "claude update"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "errors"
    resource: "https://code.claude.com/docs/en/errors"
    title: "Error reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Errors when the configured or requested model is unknown, unavailable, or needs a newer Claude Code.

# How to use it

| Error | Detail |
|---|---|
| `There's an issue with the selected model (claude-...)` | Unknown or inaccessible model. Interactive: `/model`. `-p`: `--model` or `ANTHROPIC_MODEL` (text shows `Run --model`). SDK: set `model` on Options or `ClaudeAgentOptions(model=...)`; handle structured `model_not_found`. Prefer aliases such as `sonnet` or `opus`. |
| `Model "..." is not a recognized model id` | Local refusal from SDK `setModel()`, Desktop app or Remote Control picks (session keeps its model; v2.1.200+, Remote Control checks v2.1.260+). Through SDK on the Anthropic API only non-IDs (display names, empty strings) fail; on other providers or gateways only an empty string. |
| `Model '<name>' not found` | Verified with a minimal API request. In the TypeScript SDK `supportedModels()` lists switchable models. `opusplan[1m]` was rejected before v2.1.265. |
| `Couldn't confirm model ... with the API` | No answer within 15 seconds; session keeps its model. |
| `API error: 429 ... · model not changed` | Verification request refused (rate limit, server error). |
| `Claude Opus is not available with the Claude Pro plan` | Plan lacks the model; `/logout` and `/login` after upgrading. |
| `Claude Code does not support this model` | 400 with code `claude_code_version_too_old`, per-model minimum or org-policy minimum. Update the binary that made the request: `claude update`, desktop app, VS Code extension, or SDK package (rebuild compiled single-file executables). The stable channel may stay below the minimum. Per-model wording can be bypassed by switching models with `/model`, `setModel()` or `set_model()`. |

# Notes

Before v2.1.206 an unrefreshable expired login failed every model with the selected-model error.
