---
type: "Feature"
title: "Session recap and /recap"
description: "A one-line recap shown when you return to an idle terminal, and an on-demand /recap command."
resource: "https://code.claude.com/docs/en/interactive-mode#session-recap"
tags: [recap, session, idle, summary]
kind: "slash_command"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "/recap"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "interactive-mode"
    resource: "https://code.claude.com/docs/en/interactive-mode"
    title: "Interactive mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A recap generates in the background once at least three minutes have passed since the last completed turn and the terminal is unfocused. It appears only after at least three turns and never twice in a row.

# How to use it

`/recap` generates one on demand, only when you run it yourself; relayed from Slack, Teams or a project thread, or inside a cloud scheduled task prompt, you get a notice instead. On by default for every plan and provider; turn off **Session recap** in `/config`.

# Limits and defaults

Automatic and `/recap` output are capped at 400 characters. The automatic recap never appears in non-interactive mode.
