---
type: "Reference"
title: "Context window and compaction variables"
description: "Variables that adjust assumed context size, 1M context, auto-compaction thresholds, idle compaction and the file read token limit."
resource: "https://code.claude.com/docs/en/env-vars"
tags: [context, compaction, tokens, limits]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "CLAUDE_CODE_DISABLE_1M_CONTEXT"
  - "CLAUDE_CODE_MAX_CONTEXT_TOKENS"
  - "CLAUDE_CODE_DISABLE_UNKNOWN_MODEL_WINDOW_ENFORCEMENT"
  - "CLAUDE_AUTOCOMPACT_PCT_OVERRIDE"
  - "CLAUDE_CODE_AUTO_COMPACT_WINDOW"
  - "CLAUDE_CODE_IDLE_COMPACT_MIN_TOKENS"
  - "DISABLE_AUTO_COMPACT"
  - "DISABLE_COMPACT"
  - "CLAUDE_CODE_FILE_READ_MAX_OUTPUT_TOKENS"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "env-vars"
    resource: "https://code.claude.com/docs/en/env-vars"
    title: "Environment variables"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Controls for how much context a session assumes and when it compacts.

# How to use it

| Variable | What it does |
| :- | :- |
| `CLAUDE_CODE_DISABLE_1M_CONTEXT` | `1` removes `[1m]` model variants from the picker and holds models that default to 1M to 200K. For enterprise compliance. |
| `CLAUDE_CODE_MAX_CONTEXT_TOKENS` | Override the context window assumed for the active model (for a gateway model whose window differs). As of v2.1.193 how it applies depends on how the model ID resolves. |
| `CLAUDE_CODE_DISABLE_UNKNOWN_MODEL_WINDOW_ENFORCEMENT` | `1` skips proactive auto-compaction when the model ID is unrecognized (gateway alias). Requires v2.1.223+. |
| `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` | Percentage 1-100 of the auto-compact window at which auto-compaction triggers; can only lower the threshold (values above the default are ignored). Only in sessions that compact before the model limit; applies to main conversation and subagents. |
| `CLAUDE_CODE_AUTO_COMPACT_WINDOW` | Auto-compact window as a token count of `100000` or more; suffixed values like `200k` need v2.1.304+. |
| `CLAUDE_CODE_IDLE_COMPACT_MIN_TOKENS` | Context size at which idle compaction applies (default `200000`); positive whole number, values below `100000` raised to `100000`. Idle compaction is on by default when conditions are met; turn off with `idleCompaction: false`. Requires v2.1.290+. |
| `DISABLE_AUTO_COMPACT` | `1` disables automatic compaction and idle compaction; manual `/compact` stays. Overrides `autoCompactEnabled`. |
| `DISABLE_COMPACT` | `1` disables all compaction, automatic and manual `/compact`. |
| `CLAUDE_CODE_FILE_READ_MAX_OUTPUT_TOKENS` | Token limit for file reads (default 25,000). A read with `allow_large` can exceed it when the window has room. |
