---
type: "Guide"
title: "Model and effort guidance"
description: "Defaults (Opus 5.5 at medium effort) and when to raise or lower effort, use max, ultrathink, Sonnet, Haiku or Fable."
resource: "https://code.claude.com/docs/en/best-practices"
tags: [effort, model, opus, haiku, ultrathink]
kind: "slash_command"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "/effort"
  - "/effort low"
  - "/effort high"
  - "/effort xhigh"
  - "/model fable"
  - "ultrathink"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "best-practices"
    resource: "https://code.claude.com/docs/en/best-practices"
    title: "Best practices for Claude Code"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A new session runs Claude Opus 5.5 at medium effort on most plans and providers. Claude Fable 5.2, Opus 5.5, Sonnet 5.5 and Haiku 5.5 default to `medium`. Effort is the main control for how long Claude thinks and replaces most prompt wording tricks.

# How to use it

| Setting | When |
| - | - |
| `/effort high` or `/effort xhigh` | Correctness depends on easily missed cases: bug in unfamiliar code, flaky test, schema change needing every reader found |
| `/effort low` | Rapid back-and-forth where you review each result: brainstorming, first sketch, rename across a few files |
| `max` | A hard problem worked without you (e.g. hunting a security vulnerability); on ordinary tasks it tends to overthink |
| `ultrathink` in a prompt | Deeper reasoning for that one message without changing the setting |

Models: default Opus 5.5 handles most coding; Sonnet costs less on routine work; `/model fable` for Claude Fable 5.2; Haiku suits subagents doing simple jobs.
