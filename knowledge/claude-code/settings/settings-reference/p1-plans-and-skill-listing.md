---
type: "Reference"
title: "Plans directory and skill listing budget"
description: "plansDirectory, skillListingBudgetFraction, skillListingMaxDescChars, and the removed taskOutputMaxChars."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [plan-mode, skills, context, settings]
kind: "setting"
maturity: "unlabelled"
since: "2.1.277"
surfaces: []
requires: ""
identifiers:
  - "plansDirectory"
  - "skillListingBudgetFraction"
  - "skillListingMaxDescChars"
  - "taskOutputMaxChars"
  - "TaskOutput"
  - "/doctor"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Memory-and-context keys, scope `Any file`.

# How to use it

| Key | Type | Default | What it does |
| :- | :- | :- | :- |
| `plansDirectory` | string path relative to project root | unset (`~/.claude/plans`) | Where plan mode writes plan files. Falls back to `~/.claude/plans` if the path resolves outside the project root (e.g. `"../plans"`) or contains a backslash on macOS, Linux, WSL (`"docs\\plans"`; write `"docs/plans"`) |
| `skillListingBudgetFraction` | number greater than 0, at most 1 | `0.01` (1% of context window) | Share of context for the per-turn skill listing. Over the cap, Claude Code keeps every skill name but drops descriptions of the least-used skills (still invocable, less likely chosen). `/doctor` shows listing use |
| `skillListingMaxDescChars` | positive integer | `1536` | Cap on characters of each skill's `description` plus `when_to_use` text in the listing; longer text is cut |
| `taskOutputMaxChars` | number | n/a | Removed in v2.1.277 together with the `TaskOutput` tool it sized; setting it has no effect. Through v2.1.276 it capped inline output of a background task read with `TaskOutput`; now Claude reads a background task's output file with `Read` |

```json
{ "plansDirectory": "./plans", "skillListingBudgetFraction": 0.02, "skillListingMaxDescChars": 2048 }
```

# Notes

Raising the skill listing keys keeps more descriptions visible at the cost of more context per turn; lowering `skillListingMaxDescChars` fits more skills under the budget.
