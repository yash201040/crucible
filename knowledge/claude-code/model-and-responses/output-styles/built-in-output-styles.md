---
type: "Reference"
title: "Built-in output styles"
description: "The Default style plus Proactive, Concise, Explanatory and Learning: what each changes and when it fits."
resource: "https://code.claude.com/docs/en/output-styles#built-in-output-styles"
tags: [output-styles, proactive, concise, explanatory, learning]
kind: "setting"
maturity: "unlabelled"
since: "2.1.237"
surfaces: [cli]
requires: "Concise needs Claude Code v2.1.237+"
identifiers:
  - "Default"
  - "Proactive"
  - "Concise"
  - "Explanatory"
  - "Learning"
  - "TODO(human)"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "output-styles"
    resource: "https://code.claude.com/docs/en/output-styles"
    title: "Output styles"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

An output style is a set of instructions that sets Claude's role, tone and response format for every response in a session. Claude Code starts in Default (standard software engineering system prompt; no style instructions added). Each of the four other built-in styles keeps those instructions and adds its own. It is an instruction Claude follows, not a guarantee.

# How to use it

| Style | What changes | Use when |
| :- | :- | :- |
| Proactive | Starts work at once, makes reasonable assumptions on routine decisions, does not enter plan mode unless asked | Keep working through routine decisions |
| Concise | Leads with the result; no preamble, narration or recap; simple answers in one to three sentences; engineering as thorough as Default | Default is too long |
| Explanatory | Adds short `Insight` blocks (two or three points) explaining choices; not written into files | Learning a codebase |
| Learning | Same `Insight` blocks, plus leaves pieces of code for you marked `TODO(human)` and a "Learn by Doing" request, then waits | Hands-on coding practice |

# Limits and defaults

- Proactive's instructions tell Claude to check in conversation before deleting data or changing shared or production systems; that is separate from permission prompts, and switching to Proactive does not change your permission mode.
- Concise still writes at full length for anything you ask to be explained and for safety-relevant content (error reports, failing test output, security warnings, destructive-action confirmations). Requires v2.1.237+.
- Explanatory and Learning produce longer responses by design (more output tokens); Concise does the opposite.
