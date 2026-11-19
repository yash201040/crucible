---
type: "Feature"
title: "Auto-compact window"
description: "Control how full context can get before compaction: /autocompact, --autocompact, autoCompactWindow, CLAUDE_CODE_AUTO_COMPACT_WINDOW and defaults."
resource: "https://code.claude.com/docs/en/model-config#set-the-auto-compact-window"
tags: [compaction, context-window, env-var, cost]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.288"
surfaces: [cli, headless, cloud]
requires: "Per-model /autocompact save v2.1.288+; k/M suffix in env var v2.1.304+"
identifiers:
  - "/autocompact"
  - "/autocompact auto"
  - "--autocompact"
  - "autoCompactWindow"
  - "CLAUDE_CODE_AUTO_COMPACT_WINDOW"
  - "modelSettings"
  - "idleCompaction"
  - "used_percentage"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "model-config"
    resource: "https://code.claude.com/docs/en/model-config"
    title: "Model configuration"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The auto-compact window is how full the context window can get before Claude Code compacts the conversation. It is always capped at the model's context window.

# How to use it

| Where | How |
| - | - |
| Current model, now and later | `/autocompact 500k` saves under the model in `modelSettings` in user settings; a higher-priority scope (e.g. managed) keeps its own window and the command says so. `/autocompact auto` returns to the tuned window. Before v2.1.288 it saved one window for all models as top-level `autoCompactWindow` |
| Every model | `autoCompactWindow` in a settings file, e.g. `"autoCompactWindow": 200000`; a per-model `/autocompact` value in the same file wins for that model |
| One launch | `--autocompact <size>`; `claude --autocompact auto` forces the tuned window; not preempted by managed settings |
| Scripts, cloud | `CLAUDE_CODE_AUTO_COMPACT_WINDOW=200000`; beats the command, flag and setting unless ignored; `/autocompact` then reports the override without saving |
| One subagent | see subagent docs (`/docs/en/sub-agents#subagent-auto-compact-window`) |

Command and flag accept 100K tokens or more: plain count (`200000`), `k`/`M` suffix (`500k`, `1M`), or a bare number 100 to 1000 meaning thousands (`200` = 200,000).

# Limits and defaults

Without a setting, compaction happens at the model's context limit, except: cloud sessions compact as the conversation nears the limit; Sonnet 4.6 and Opus 4.6 without extended context compact at 200K; with `CLAUDE_CODE_DISABLE_1M_CONTEXT=1` natively-1M models compact at 200K; native-1M models (Fable, Sonnet 5+, Haiku 5.5, Opus 4.7+) compact at about 967K by default; unrecognized model IDs (e.g. gateway aliases) compact at the window Claude Code assumes. See `idleCompaction` for compaction of idle conversations.

# Notes

The status line's `used_percentage` measures against the full model window, so while the env var is set it does not show when compaction will run. A number without suffix in the env var is tokens: `CLAUDE_CODE_AUTO_COMPACT_WINDOW=200` is 200 tokens, though `/autocompact 200` is 200,000.
