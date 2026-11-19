---
type: "Feature"
title: "One-time reminders"
description: "Natural-language one-shot tasks that fire once at a pinned minute and delete themselves."
resource: "https://code.claude.com/docs/en/scheduled-tasks"
tags: [reminders, one-shot, scheduling]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers: []
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "scheduled-tasks"
    resource: "https://code.claude.com/docs/en/scheduled-tasks"
    title: "Run prompts on a schedule"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

For a single reminder, describe it in plain language instead of using `/loop`. Claude schedules a single-fire task that deletes itself after running.

# How to use it

```text
remind me at 3pm to push the release branch
in 45 minutes, check whether the integration tests passed
```

Claude pins the fire time to a specific minute and hour with a cron expression and confirms when it will fire.

# Notes

One-shot tasks on `:00` or `:30` can run early; see [jitter](./jitter-and-timing.md).
