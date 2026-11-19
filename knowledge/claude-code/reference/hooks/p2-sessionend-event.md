---
type: "Feature"
title: "SessionEnd hook event and timeout"
description: "Cleanup hook at session end with reason matchers and a 1.5 second default budget."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, sessionend, cleanup, timeout]
kind: "hook"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless]
requires: ""
identifiers:
  - "SessionEnd"
  - "reason"
  - "clear"
  - "resume"
  - "logout"
  - "prompt_input_exit"
  - "other"
  - "bypass_permissions_disabled"
  - "CLAUDE_CODE_SESSIONEND_HOOKS_TIMEOUT_MS"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Runs when a session ends: cleanup, logging session statistics, saving state. Matches on exit reason. No decision control; cannot block termination; JSON fields such as `systemMessage` are discarded. Input adds `reason`.

# How to use it

| `reason` | Meaning |
| :- | :- |
| `clear` | `/clear` |
| `resume` | Interactive `/resume` switch |
| `logout` | User logged out |
| `prompt_input_exit` | User exited while prompt input was visible |
| `other` | Other exit reasons |
| `bypass_permissions_disabled` | Removed in v2.1.234; not sent; drop it from matchers |

Example of raising the budget: `CLAUDE_CODE_SESSIONEND_HOOKS_TIMEOUT_MS=5000 claude`.

# Limits and defaults

- Default timeout 1.5 seconds, applied on exit, `/clear`, and interactive `/resume` switch.
- Per-hook `timeout` raises the overall budget automatically to the highest per-hook `timeout` in your settings files, up to 60 seconds; a hook with no `timeout` of its own keeps the default. Timeouts on plugin-provided hooks do not raise the budget.
- `CLAUDE_CODE_SESSIONEND_HOOKS_TIMEOUT_MS` (milliseconds) overrides the budget explicitly and also becomes the timeout of each hook without its own. Before v2.1.268 it raised only the overall budget, and a hook without `timeout` was still cancelled after 1.5 s.
