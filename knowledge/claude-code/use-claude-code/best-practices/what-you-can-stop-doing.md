---
type: "Reference"
title: "Advice current models made unnecessary"
description: "Table of old prompting and context-management habits that newer models no longer need, with the reason."
resource: "https://code.claude.com/docs/en/best-practices"
tags: [prompting, habits, context, emphasis, effort]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "ultrathink"
  - "/goal"
  - "Stop"
  - "/clear"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "best-practices"
    resource: "https://code.claude.com/docs/en/best-practices"
    title: "Best practices for Claude Code"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Old workarounds that models have outgrown.

# How to use it

| Old advice | Why it is gone |
| :- | :- |
| Manage the context window aggressively | Most current models have a 1M-token window and compaction is automatic; `/clear` between tasks is still worth it for focus and cost |
| IMPORTANT / ALL CAPS on missed instructions | Current models follow plain wording; emphasis causes over-application. Rules that cannot bend become hooks or deny rules; a long file should be shortened |
| Use subagents to protect context | Rarely the problem now; subagents still help with parallel work, noisy output and independent review, each at extra token cost |
| Delegate to a subagent for a better answer | Same task gives no better answer; a fresh reviewer helps because it has not seen your reasoning |
| `think hard`, `be thorough` | Effort is the control; `ultrathink` still works for one turn |
| Tell Claude to keep going, loop until done | Models carry on by themselves; if a run stops short say `continue`, and for unwatched runs use `/goal` or a `Stop` hook. A check to pass is still worth giving |
| Describe architecture and file layout in CLAUDE.md | Claude reads the repo itself |
