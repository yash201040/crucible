---
type: "Reference"
title: "Model aliases"
description: "Aliases accepted by the model setting (default, best, fable, sonnet, opus, haiku, [1m] variants, opusplan) and what each selects."
resource: "https://code.claude.com/docs/en/model-config"
tags: [model, aliases, fable, opus, sonnet]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "default"
  - "best"
  - "fable"
  - "sonnet"
  - "opus"
  - "haiku"
  - "sonnet[1m]"
  - "opus[1m]"
  - "opusplan"
  - "model"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "model-config"
    resource: "https://code.claude.com/docs/en/model-config"
    title: "Model configuration"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The `model` setting accepts a model alias or a model name. A name is a full Anthropic API model name, a Bedrock inference profile ARN, a Microsoft Foundry deployment name, or a Google Cloud Agent Platform version name. Aliases track the recommended version for the provider and change over time. To pin, use a full name such as `claude-opus-5-5` or set `ANTHROPIC_DEFAULT_OPUS_MODEL`.

# How to use it

| Alias | Behavior |
| - | - |
| `default` | Not a real alias: clears any override and returns to the runtime default for the account |
| `best` | Same model as `opus` |
| `fable` | The Fable model for the provider, for the hardest and longest tasks |
| `sonnet` | Latest Sonnet, for daily coding |
| `opus` | Latest Opus, for complex reasoning |
| `haiku` | Fast Haiku, for simple tasks |
| `sonnet[1m]` | Sonnet with 1M context; no effect when `sonnet` already resolves to Sonnet 5.5 or Sonnet 5 (native 1M) |
| `opus[1m]` | Opus with 1M context; no effect when `opus` resolves to Opus 4.7 or later (native 1M) |
| `opusplan` | Opus in plan mode, then Sonnet for execution |

Use: `claude --model opus`, then `/model sonnet` in the session.

# Limits and defaults

- Sonnet 5.5 needs Claude Code v2.1.284+, Opus 5.5 needs v2.1.280+, Haiku 5.5 needs v2.1.293+ (run `claude update`).
- Where `opus` or `sonnet` resolves to an older model, pick the newer one by full name or by `ANTHROPIC_DEFAULT_OPUS_MODEL` / `ANTHROPIC_DEFAULT_SONNET_MODEL`.
- `ANTHROPIC_BASE_URL` changes where requests go, not which model answers.
- See [alias resolution by provider](./alias-resolution-by-provider.md) and [version history](./alias-version-history.md).
