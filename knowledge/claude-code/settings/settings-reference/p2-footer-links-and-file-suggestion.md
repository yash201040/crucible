---
type: "Feature"
title: "Footer badges and custom file suggestion"
description: "footerLinksRegexes turns IDs in output into footer link badges; fileSuggestion replaces the @ autocomplete with your own command."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [settings, footer, autocomplete, regex]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "footerLinksRegexes"
  - "fileSuggestion"
  - "CLAUDE_PROJECT_DIR"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`footerLinksRegexes` (user or managed scope) renders clickable footer badges when a regex matches turn output (tool results and Claude's replies). `fileSuggestion` (any file) runs your command to supply `@` path autocomplete.

# How to use it

`footerLinksRegexes`: array of `{ "type": "regex", "pattern", "url", "label"? }`; `{name}` placeholders in `url` and `label` come from named capture groups, for example `\\b(?<key>PROJ-\\d+)\\b` with `https://issues.example.com/browse/{key}`.

`fileSuggestion`: `{ "type": "command", "command": "~/.claude/file-suggestion.sh" }`. The command gets the same environment as hooks (including `CLAUDE_PROJECT_DIR`), JSON on stdin `{"query": "src/comp"}`, and prints newline-separated paths.

# Limits and defaults

| Constraint | Value |
| :- | :- |
| Badge URL origin | must match the template's literal origin; captures are URL-encoded |
| URL length | over 2048 characters dropped |
| URL scheme | `https`, `http`, or `vscode`, `vscode-insiders`, `cursor`, `windsurf`, `zed`, `jetbrains`, `idea`, `slack`, `linear`, `notion`, `figma` |
| Label | defaults to matched text, truncated to 28 display columns |
| Badge count | max 5; oldest displaced; `/clear` removes them |
| `fileSuggestion` wait | 5 seconds; at most 15 paths shown |

# Notes

Regexes run on the main thread after each turn: nested quantifiers such as `(a+)+$` can freeze the session. Badges render alongside a custom status line. `fileSuggestion` is skipped without warning (built-in used) under managed-only narrowing; see [hook and status-line gates](./p2-disable-all-hooks-and-gates.md).
