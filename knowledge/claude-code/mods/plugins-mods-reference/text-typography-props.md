---
type: "Reference"
title: "Text typography props and bold deprecation"
description: "size, weight, mono and tabular on Text, how terminal and VS Code treat them, and bold deprecated in favor of weight."
resource: "https://code.claude.com/docs/en/plugins/mods/reference"
tags: [mods, text, typography, deprecated]
kind: "ui"
maturity: "deprecated"
since: "2.1.299"
surfaces: [cli, ide]
requires: ""
identifiers:
  - "size"
  - "weight"
  - "mono"
  - "tabular"
  - "bold"
  - "weight: 'semibold'"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-reference"
    resource: "https://code.claude.com/docs/en/plugins/mods/reference"
    title: "Mods reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

| Prop | Values | Terminal | VS Code |
| :- | :- | :- | :- |
| `size` | `'caption'`, `'footnote'`, `'body'`, `'heading'`, `'title'` | ignored (one size) | ignored |
| `weight` | `'regular'`, `'medium'`, `'semibold'`, `'bold'` | `semibold` and `bold` draw bold | same |
| `mono` | `true` | ignored (always monospaced) | ignored |
| `tabular` | `true` | ignored | ignored |

An ignored prop leaves the text drawn as if omitted.

# Limits and defaults

- These four props need v2.1.299+; on earlier releases a tree that sets one does not draw.
- `bold` on `Text` is deprecated in favor of `weight` and still works. Replace `bold: true` with `weight: 'semibold'` (v2.1.299+). If both are set, `bold` has no effect. A tree setting `weight` does not draw before v2.1.299.
