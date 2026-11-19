---
type: "Concept"
title: "What an advisor consultation looks like"
description: "The transcript lines shown while and after the advisor is consulted, and how Claude treats its guidance."
resource: "https://code.claude.com/docs/en/advisor"
tags: [advisor, transcript, ui]
kind: "ui"
maturity: "experimental"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "Advising"
  - "Advisor declined to advise on this request"
  - "Advisor unavailable"
  - "Ctrl+O"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "advisor"
    resource: "https://code.claude.com/docs/en/advisor"
    title: "Escalate hard decisions with the advisor tool"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

When Claude calls the advisor, the transcript shows an `Advising` line with the advisor model name. The finished line reports one of three outcomes.

# How to use it

| Outcome | Line | Detail |
| - | - | - |
| Reviewed | confirms the advisor reviewed the conversation | `Ctrl+O` shows readable guidance |
| Declined | `Advisor declined to advise on this request` | `Ctrl+O` shows a reason if given |
| Unavailable | `Advisor unavailable (<error_code>)` | the call failed; code is the call's error code |

# Notes

Claude generally follows the guidance but surfaces a conflict when its own evidence contradicts a claim (a recommended step fails, file contents disagree). The advisor always gets the full conversation; Claude controls timing.
