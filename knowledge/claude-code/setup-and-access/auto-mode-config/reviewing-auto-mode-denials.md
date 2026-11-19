---
type: "Guide"
title: "Reviewing and fixing auto mode denials"
description: "Recently blocked tab, PermissionDenied hook, policy-category denials and how to fix repeated blocks."
resource: "https://code.claude.com/docs/en/auto-mode-config#review-denials"
tags: [auto-mode, denials, hooks, permissions]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "/permissions"
  - "PermissionDenied"
  - "Recently blocked"
  - "Ctrl+O"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "auto-mode-config"
    resource: "https://code.claude.com/docs/en/auto-mode-config"
    title: "Configure auto mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

How to see why auto mode blocked an action and let a legitimate one through.

# How to use it

- **Recently blocked** tab in `/permissions`: highlight a row, check the real command, press `r` to approve and let Claude retry, `Esc` to apply; `Enter` then `Esc` approves for later; `Ctrl+C` twice discards. Not in the desktop app.
- Approving adds no rule; the retry is re-checked and can be blocked again. Fix permanently with an `allow` rule or `autoMode.environment` entry.
- Programmatic capture: a `PermissionDenied` hook receives the input as `tool_input`; its `reason` has no `Auto mode:` prefix and may read `Blocked by classifier`.
- Notices look like `bash blocked by auto mode · /permissions · Auto mode: [Data Exfiltration]`. Bracketed text is a built-in rule name for `claude auto-mode defaults --label`.
- `Not run · auto mode's check had no usable answer` means no classifier verdict (see errors page), not a policy block.

# Limits and defaults

- Server-side classifier policy categories (`[Destructive or Unwanted Actions]`, `[Unauthorized Access]`, `[Undermining Oversight]`, `[Unsanctioned Communication]`) are not listed by `claude auto-mode defaults`. Give context: name the action and target in a message, add the destination to `autoMode.environment`, or add an `autoMode.allow` entry.
- Rows that cannot show the full command read `This row can't be approved here`.
