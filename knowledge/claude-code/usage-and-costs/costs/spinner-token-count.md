---
type: "Concept"
title: "Token count beside the spinner"
description: "The live approximate output-token count shown next to the working spinner, what it covers and when it resets."
resource: "https://code.claude.com/docs/en/costs"
tags: [spinner, tokens, output, ui, subagents]
kind: "ui"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers: []
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "costs"
    resource: "https://code.claude.com/docs/en/costs"
    title: "Manage costs effectively"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

While Claude works in the main conversation, the spinner line can end with elapsed time and a count, e.g. `Deciphering… (10m 27s · ↓ 5.5k tokens)`. It is a live, approximate count of output the current turn has produced so far.

# Limits and defaults

- Covers: streamed text and tool calls, thinking, and output of foreground subagents.
- Leaves out: what is sent to the model (prompt, history, context).
- Resets at the start of each turn and on compaction.
- Hidden until output starts, when the row is too narrow, and in screen reader mode.
- Does not match the `Usage by model` output figures (whole session), nor the verbose-mode count (which measures context size).
