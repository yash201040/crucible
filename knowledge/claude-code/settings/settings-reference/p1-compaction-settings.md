---
type: "Reference"
title: "Compaction settings"
description: "autoCompactEnabled, autoCompactWindow and idleCompaction control automatic and idle context compaction, with env and flag overrides."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [compaction, context, settings, cost]
kind: "setting"
maturity: "unlabelled"
since: "2.1.290"
surfaces: [cli, ide, desktop]
requires: "idleCompaction key v2.1.290; /config row v2.1.302"
identifiers:
  - "autoCompactEnabled"
  - "autoCompactWindow"
  - "idleCompaction"
  - "DISABLE_AUTO_COMPACT"
  - "--autocompact"
  - "CLAUDE_CODE_AUTO_COMPACT_WINDOW"
  - "CLAUDE_CODE_IDLE_COMPACT_MIN_TOKENS"
  - "/autocompact"
  - "/compact"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Keys for compacting a conversation when context fills (`autoCompactEnabled`, `autoCompactWindow`) and for compacting a conversation you have stepped away from (`idleCompaction`). All scope `Any file`.

# How to use it

| Key | Type | Default | What it does |
| :- | :- | :- | :- |
| `autoCompactEnabled` | Boolean | `true` | Compact automatically near the limit; `/config` **Auto-compact** writes it to user settings. `DISABLE_AUTO_COMPACT` turns it off for a session and neither can re-enable the other. Manual `/compact` still works; turning it off also turns idle compaction off |
| `autoCompactWindow` | number of tokens, at least `100000` (capped at the model's window) | unset (window tuned for the model) | How full the window gets before compacting. `--autocompact` beats the key; `CLAUDE_CODE_AUTO_COMPACT_WINDOW` beats both unless its value is ignored. `/autocompact` saves per model under `modelSettings`, which wins in the same file |
| `idleCompaction` | Boolean | `true` | Compacts an idle long conversation so the next message sends a summary. `/config` **Idle compaction** row saves to user settings |

```json
{ "idleCompaction": false, "env": { "CLAUDE_CODE_IDLE_COMPACT_MIN_TOKENS": "150000" } }
```

# Limits and defaults

Idle compaction applies only when all hold: interactive terminal session, VS Code chat panel, or desktop Code tab running locally or over SSH; `autoCompactEnabled` on; one-hour prompt cache TTL in use; context reached the threshold (default 200,000 tokens; `CLAUDE_CODE_IDLE_COMPACT_MIN_TOKENS`, positive integer, values below `100000` are raised to `100000`); about an hour since the last request with the computer awake. `DISABLE_AUTO_COMPACT` turns it off too. A notice appears (terminal: `Compacted while idle, before the prompt cache expired`; VS Code/Desktop: `Compacted using a summary written while you were away`). The key needs v2.1.290; earlier versions ignore it, so turn off `autoCompactEnabled`. If `/config` lacks the row on v2.1.302 or later, another source (managed, `--settings`, project or local) sets the key, or on versions before v2.1.314 feature flags could not be fetched from Anthropic so idle compaction does not run.
