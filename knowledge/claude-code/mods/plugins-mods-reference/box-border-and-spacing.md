---
type: "Reference"
title: "Box borderStyle names and spacing steps"
description: "Valid borderStyle values and what each draws, and the xs to xl spacing steps in cells for terminal and VS Code."
resource: "https://code.claude.com/docs/en/plugins/mods/reference"
tags: [mods, box, border, spacing]
kind: "ui"
maturity: "unlabelled"
since: "2.1.299"
surfaces: [cli, ide]
requires: ""
identifiers:
  - "borderStyle"
  - "'single'"
  - "'double'"
  - "'round'"
  - "'bold'"
  - "'singleDouble'"
  - "'doubleSingle'"
  - "'classic'"
  - "'arrow'"
  - "'dashed'"
  - "'quote'"
  - "gap"
  - "columnGap"
  - "rowGap"
  - "padding"
  - "margin"
  - "paddingX"
  - "marginTop"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-reference"
    resource: "https://code.claude.com/docs/en/plugins/mods/reference"
    title: "Mods reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

| `borderStyle` | Terminal draws | Top edge |
| :- | :- | :- |
| `'single'` | thin square corners | `┌──┐` |
| `'double'` | double lines | `╔══╗` |
| `'round'` | thin rounded corners | `╭──╮` |
| `'bold'` | thick lines | `┏━━┓` |
| `'singleDouble'` | thin top/bottom, double sides | `╓──╖` |
| `'doubleSingle'` | double top/bottom, thin sides | `╒══╕` |
| `'classic'` | ASCII `+`, `-`, `\|` | `+--+` |
| `'arrow'` | arrows pointing into the Box | `↘↓↓↙` |
| `'dashed'` | dashed, blank corners | `╌╌` |
| `'quote'` | bar `▎` down the left, blank elsewhere | blank |

Any other name (e.g. `'rounded'`) draws no border.

# How to use it

Spacing props (`gap`, `columnGap`, `rowGap`, `padding`, `margin`, and one-side/one-axis forms like `paddingX`, `marginTop`) take a number of cells or a step name. In terminal and VS Code:

| Step | Cells across | Cells down |
| :- | :- | :- |
| `'xs'` | 1 | 0 |
| `'sm'` | 1 | 0 |
| `'md'` | 2 | 1 |
| `'lg'` | 3 | 1 |
| `'xl'` | 4 | 2 |

A step on `gap`, `padding` or `margin` applies across and down at once (`padding: 'md'` is 2 cells at each side, 1 row above and below).

# Limits and defaults

Step names need v2.1.299+; on earlier releases a tree using one does not draw.
