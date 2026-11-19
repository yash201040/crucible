---
type: "Feature"
title: "Spell checking in the prompt"
description: "Optional underlining of misspelled words using aspell, hunspell or ispell, configured with the spellcheck setting."
resource: "https://code.claude.com/docs/en/interactive-mode#check-spelling-as-you-type"
tags: [spellcheck, prompt, settings, managed-settings]
kind: "setting"
maturity: "unlabelled"
since: "2.1.235"
surfaces: [cli]
requires: "aspell, hunspell or ispell on PATH"
identifiers:
  - "spellcheck"
  - "spellcheck.enabled"
  - "spellcheck.checker"
  - "spellcheck.language"
  - "spellcheck.color"
  - "--settings"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "interactive-mode"
    resource: "https://code.claude.com/docs/en/interactive-mode"
    title: "Interactive mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Off by default. Checks only prompt-box text (not replies or files) and nothing in shell mode, `Ctrl+R` search, voice dictation or screen reader mode.

# How to use it

```json
{ "spellcheck": { "enabled": true, "checker": "hunspell", "language": "en_GB", "color": "yellow" } }
```

- `checker`: `aspell`, `hunspell` or `ispell`; no fallback from a named checker, other values mean `auto` (first found, in that order).
- `language`: plain dictionary name such as `en_GB`; paths or names with spaces are ignored.
- `color`: color name, `#rrggbb`, `#rgb`, `rgb(r,g,b)`, `ansi256(n)` or `ansi:<name>`; defaults to theme error color.
- Read from user settings, `--settings` file, or managed settings only (project settings ignored). Only one source is used, never merged: managed first, then `--settings`, then user.

# Limits and defaults

Skips commands, `@` mentions, URLs, paths, flags, words with digits, underscores or inner capitals, backticked text, and CJK/Thai/Lao/Khmer/Myanmar text. Checking stops if the checker fails twice in a row, or takes more than 15 seconds three times, until restart. Debug with `claude --debug` and `[spellcheck]` lines in `~/.claude/debug/<session-id>.txt`.
