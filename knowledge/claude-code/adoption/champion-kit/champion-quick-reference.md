---
type: "Reference"
title: "Champion quick-reference techniques"
description: "Short list of techniques that move users to daily use: context, plan mode, CLAUDE.md, skills, Stop hook, recovery."
resource: "https://code.claude.com/docs/en/champion-kit#quick-reference-sheet"
tags: [adoption, tips, plan-mode, skills]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "/init"
  - "Shift+Tab"
  - ".claude/skills/<name>/SKILL.md"
  - "@file"
  - "Stop"
  - "/team-onboarding"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "champion-kit"
    resource: "https://code.claude.com/docs/en/champion-kit"
    title: "Champion kit"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Techniques the page recommends pinning for teammates.

# How to use it

| Technique | How |
| :- | :- |
| Provide context | `@file` or `@directory/` references, or paste error/log output |
| Review the plan first | `Shift+Tab` into plan mode; Claude proposes changes without editing source |
| Teach the repo | `/init` generates `CLAUDE.md`; add conventions, test commands, off-limits directories |
| Reuse a workflow | `SKILL.md` in `.claude/skills/<name>/` creates a `/name` skill |
| Long-task awareness | a Stop hook for a desktop notification |
| Recover from a bad result | paste the failing test or stack trace back instead of rephrasing |
| Keep edits surgical | ask for a diff or say "only change X" |

# Notes

Plan mode is described as the trust-building feature. Hallucination complaints are framed as a context problem (use `@`-context, `/init`, real error output).
