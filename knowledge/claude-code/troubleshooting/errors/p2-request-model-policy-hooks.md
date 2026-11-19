---
type: "Reference"
title: "Model policy, PreModelSwitch hook and advisor errors"
description: "Org-restricted models, blocked default model, PreModelSwitch hook denials, default-save failures and advisor ranking notes."
resource: "https://code.claude.com/docs/en/errors"
tags: [errors, models, managed-settings, hooks, advisor]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "availableModels"
  - "availableModelsMatch"
  - "deniedModels"
  - "PreModelSwitch"
  - "--advisor"
  - "/advisor"
  - "~/.claude/settings.json"
  - "--safe-mode"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "errors"
    resource: "https://code.claude.com/docs/en/errors"
    title: "Error reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Errors where policy, hooks or settings stop a model choice.

# How to use it

- **Model is restricted by your organization's settings:** an admin disabled it in the claude.ai console or managed settings exclude it through `availableModels` or `deniedModels`. At startup (`--model`, `ANTHROPIC_MODEL`, `model` setting) Claude Code substitutes a permitted model and says so. A notice prefixed with an agent, skill or command name applies to that subagent's requested model only (any launch since v2.1.223). Family aliases `opus`, `sonnet`, `haiku`, `fable` resolve to the newest permitted version (since v2.1.205); rejected only when every version is restricted. `/model <name>` for a restricted model is rejected.
- **Can't switch to the default model:** managed settings block it via `deniedModels`, or `availableModels` with `availableModelsMatch` set to `"exact"` omits it, or managed settings could not be read.
- **Model switch was blocked by a PreModelSwitch hook:** reasons include a hook-written deny reason; `did not respond before its timeout` (raise the hook `timeout`); `confirmation required, and this session cannot ask` (a hook returned `ask` with no reason; `-p` `/model` adds `(run /model interactively to confirm)`); `organization-managed PreModelSwitch hooks could not be checked` (before v2.1.323, managed plugin hook load failure); hook failed or cancelled before answering. Cancelled or failed runs are never treated as approval. SDK host or Remote Control switches omit the target model name. Debug with `claude --debug`.
- **Couldn't save it as your default:** write to `~/.claude/settings.json` failed (`can't be written (<code>)` such as `EROFS`, or `isn't valid JSON`); the switch applied for the session only. A notice `couldn't confirm it was saved` means the write exceeded three seconds. Before v2.1.265 the notice claimed it was saved.
- **Advisor is less capable than the current main model:** the advisor must rank at least as high as the main model or it will not activate on the main model (subagents may still use it). `--advisor` in non-interactive mode warns on stderr (not in background sessions) and runs anyway. Ranking changed in v2.1.287.

# Notes

See [Model selection errors](./p2-request-model-selection-errors.md).
