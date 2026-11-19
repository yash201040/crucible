---
type: "Reference"
title: "CLAUDE_CODE_AUTO_COMPACT_WINDOW warnings"
description: "Warning texts for an unusable CLAUDE_CODE_AUTO_COMPACT_WINDOW value, the window used and the fix."
resource: "https://code.claude.com/docs/en/model-config#claude_code_auto_compact_window-values"
tags: [compaction, env-var, warnings, troubleshooting]
kind: "env_var"
maturity: "unlabelled"
since: "2.1.304"
surfaces: [cli]
requires: "k/M suffix v2.1.304+"
identifiers:
  - "CLAUDE_CODE_AUTO_COMPACT_WINDOW"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "model-config"
    resource: "https://code.claude.com/docs/en/model-config"
    title: "Model configuration"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A warning quoting your `CLAUDE_CODE_AUTO_COMPACT_WINDOW` value means the session is not using it as set. Set a plain number such as `200000`, or on v2.1.304+ `200k` or `1M`.

# How to use it

| Warning contains | Window used | Fix |
| :- | :- | :- |
| `reads as <N> tokens, so Claude Code treats it as the 100k minimum` | Smaller of 100,000 tokens and the model's window | Set at least `100000`, e.g. `200000`, or `200k` if you meant thousands |
| `is too large, so Claude Code treats it as the 1M maximum` | Smaller of 1,000,000 and the model's window | Already the largest; set `1M` or `1000000` to silence |
| `isn't a usable size, so Claude Code ignores it` | Window from `--autocompact`, `/autocompact` or `autoCompactWindow`, or the default | Set a number or unset the variable |

# Notes

A number with no suffix means that many tokens, so `200` is 200 tokens.
