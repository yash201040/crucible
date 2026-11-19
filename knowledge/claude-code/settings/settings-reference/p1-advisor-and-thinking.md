---
type: "Reference"
title: "Advisor model and thinking settings"
description: "advisorModel, alwaysThinkingEnabled, showThinkingSummaries: choose the advisor model and control extended thinking and its display."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [advisor, thinking, model, settings]
kind: "setting"
maturity: "unlabelled"
since: "2.1.300"
surfaces: []
requires: "advisorModel \"fable\" needs Fable access; advisor not available on Amazon Bedrock"
identifiers:
  - "advisorModel"
  - "alwaysThinkingEnabled"
  - "showThinkingSummaries"
  - "--advisor"
  - "CLAUDE_CODE_DISABLE_ADVISOR_TOOL"
  - "MAX_THINKING_TOKENS"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Three model-behavior keys, all scope `Any file`.

# How to use it

| Key | Type | Default | What it does |
| :- | :- | :- | :- |
| `advisorModel` | string: alias `"fable"`, `"opus"`, `"sonnet"` or a full model ID such as `"claude-opus-5-5"` | unset = advisor off | Model that answers when Claude calls the server-side advisor tool. Must be at least as capable as the main model. `/advisor` opens a picker and saves here |
| `alwaysThinkingEnabled` | Boolean | unset (thinking on) | `false` turns extended thinking off for every session; `true` changes nothing |
| `showThinkingSummaries` | Boolean | `false` | `true` shows full thinking summaries when expanded with `Ctrl+O`; otherwise a collapsed stub (the API redacts thinking) |

```json
{ "advisorModel": "opus", "alwaysThinkingEnabled": false, "showThinkingSummaries": true }
```

# Limits and defaults

- `--advisor` overrides `advisorModel` for one session. `CLAUDE_CODE_DISABLE_ADVISOR_TOOL` turns the advisor off and the key cannot turn it back on.
- A pick made from a Remote Control client or in a session attached to a remote worker applies to that session only.
- Picking Fable in `/advisor` saves nothing until the usage-credits consent is accepted with `/model fable`.
- `advisorModel` has no effect on providers without the advisor (such as Amazon Bedrock); on Claude Platform on AWS or Claude Models on Google Cloud (Anthropic managed) it needs v2.1.300 or later.
- `alwaysThinkingEnabled: false` has no effect on always-thinking models (Opus 5.5, Sonnet 5.5, Haiku 5.5, the Fable models). On third-party providers Claude Code omits the `thinking` parameter instead, so adaptive models may still think. With thinking off on the Anthropic API, models that reject the combination (such as Opus 5) get effort `high` instead of a higher level.
- `MAX_THINKING_TOKENS` overrides for one session: `0` turns thinking off (same limits), a positive value turns it on even if the key is `false`; on adaptive-reasoning models the number is ignored.
- Redaction in `showThinkingSummaries` changes only what you see, not what the model generates.
