---
type: "Feature"
title: "Adaptive reasoning and extended thinking"
description: "Which models always use adaptive reasoning, thinking toggles and env vars, and models where thinking cannot be turned off."
resource: "https://code.claude.com/docs/en/model-config#extended-thinking"
tags: [thinking, adaptive-reasoning, env-var, cost]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING"
  - "MAX_THINKING_TOKENS"
  - "alwaysThinkingEnabled"
  - "showThinkingSummaries"
  - "Option+T"
  - "Alt+T"
  - "Ctrl+O"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "model-config"
    resource: "https://code.claude.com/docs/en/model-config"
    title: "Model configuration"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Adaptive reasoning makes thinking optional per step. Fable models, Sonnet 5 and later, Haiku 5.5, and Opus 4.7 and later always use it; the fixed budget mode and `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING` do not apply to them. On Opus 4.6 and Sonnet 4.6, `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING=1` reverts to the fixed budget controlled by `MAX_THINKING_TOKENS`.

# How to use it

| Control | How |
| :- | :- |
| Toggle for the session | `Option+T` (macOS) or `Alt+T` (Windows/Linux) |
| Global default | `/config` thinking mode; saved as `alwaysThinkingEnabled` in `~/.claude/settings.json` |
| Disable via env | `MAX_THINKING_TOKENS=0` |

Thinking output is collapsed; `Ctrl+O` toggles verbose to show gray italic reasoning. Interactive sessions on the Anthropic API get redacted thinking blocks by default; set `showThinkingSummaries: true` for full summaries on expand. All thinking tokens are charged even when collapsed or redacted.

# Limits and defaults

- Thinking cannot be turned off on Opus 5.5, Sonnet 5.5, Haiku 5.5 or Fable models: the toggle shows `Thinking can't be turned off`, and saved `alwaysThinkingEnabled: false` or `MAX_THINKING_TOKENS=0` have no effect there (they apply again on a model that accepts them). On Anthropic API you can turn it off on e.g. `claude-opus-5`, `claude-sonnet-5`, `claude-haiku-4-5` (by ID, not alias). On Bedrock and Foundry adaptive models may still think; lower effort instead.
- With thinking off on the Anthropic API, Claude Code sends effort `high` instead of a higher level to models known not to accept that combination, such as Opus 5.
