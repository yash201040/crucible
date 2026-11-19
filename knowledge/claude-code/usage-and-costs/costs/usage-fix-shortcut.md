---
type: "Feature"
title: "Fix shortcut in /usage"
description: "Pressing f in /usage runs recommended /effort commands and prompts Claude to apply other recommendations."
resource: "https://code.claude.com/docs/en/costs"
tags: [usage, recommendations, effort, shortcut, remote-control]
kind: "ui"
maturity: "unlabelled"
since: "2.1.305"
surfaces: [cli]
requires: "Claude Code v2.1.305 or later"
identifiers:
  - "/usage"
  - "/effort"
  - "/compact"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "costs"
    resource: "https://code.claude.com/docs/en/costs"
    title: "Manage costs effectively"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

When the `/usage` footer shows a hint such as `f to fix 2 of 3`, pressing `f` acts on the recommendations Claude Code can apply.

# How to use it

After any turn in progress ends, Claude Code runs each `/effort` command shown in a row without `run`. Claude then gets one prompt with a step for each other actionable row, asking it to show each change before making it.

| Row shape | Example | On `f` |
| - | - | - |
| Ends in `/effort` command with no `run` | `40%  Switch from max to high effort · /effort high` | Command is run |
| Ends in `run` and a command | `30%  Compact before you step away · run /compact` | Nothing; run it yourself |
| Anything else | `25%  Trim ~/code/api/CLAUDE.md · 49k tokens per request` | Claude gets a step for some; nothing for the rest |

In `2 of 3` the first number is rows acted on, the second rows shown. A hint like `f to fix both` means all rows.

# Limits and defaults

- While Remote Control is connected the footer shows no `f` hint. If `f` closes /usage with `Nothing was sent. Turn off Remote Control to use fixes.`, disconnect Remote Control, rerun `/usage`, press `f` again.
