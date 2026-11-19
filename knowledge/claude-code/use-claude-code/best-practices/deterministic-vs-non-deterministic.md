---
type: "Concept"
title: "Deterministic vs non-deterministic instructions"
description: "Prompts, CLAUDE.md and skills are decided by the model; hooks, deny rules and managed settings are enforced by the harness."
resource: "https://code.claude.com/docs/en/best-practices"
tags: [hooks, enforcement, claude-md, deny-rules, guardrails]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "--max-turns"
  - "--max-budget-usd"
  - "/goal"
  - "/code-review"
  - "Stop"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "best-practices"
    resource: "https://code.claude.com/docs/en/best-practices"
    title: "Best practices for Claude Code"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Non-deterministic: you write an instruction (prompt, `CLAUDE.md`, skill) and the model decides what to do; no guarantee. Deterministic: you configure it and Claude Code (the harness) must execute it every time (a hook, a deny rule, a managed setting).

# How to use it

| | Non-deterministic (Claude decides) | Deterministic (Claude Code enforces) |
| :- | :- | :- |
| What to do | Prompt, `CLAUDE.md`, skills Claude picks up itself | Hooks, skills only you can start |
| What it can touch | Auto mode's classifier | Deny rules, sandbox in strict mode, managed settings |
| When it's done | Request for evidence, `/goal`, `/code-review` | Tests, typecheck, a `Stop` hook, CI |
| How much it spends | Effort level, Claude's pace | `--max-turns` or `--max-budget-usd` with `-p`, a spend limit |
| Last word | Claude's summary | Branch protection, a person approving the merge |

# Notes

Most of the time let Claude decide. Use the deterministic kind for rules with no exceptions (example: never edit the generated client in `src/gen/`). If you keep adding emphasis to a CLAUDE.md line that Claude misses, it belongs in a hook; hooks for mere preferences should be deleted.
