---
type: "Feature"
title: "Disable session-scoped scheduling"
description: "CLAUDE_CODE_DISABLE_CRON=1 turns off the scheduler, CronCreate and /loop."
resource: "https://code.claude.com/docs/en/scheduled-tasks"
tags: [env-var, cron, disable, scheduling]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "CLAUDE_CODE_DISABLE_CRON"
  - ".claude/scheduled_tasks.json"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "scheduled-tasks"
    resource: "https://code.claude.com/docs/en/scheduled-tasks"
    title: "Run prompts on a schedule"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Setting `CLAUDE_CODE_DISABLE_CRON=1` disables the scheduler entirely.

# How to use it

```bash
CLAUDE_CODE_DISABLE_CRON=1 claude
```

Effects: `CronCreate` and `/loop` become unavailable and already-scheduled tasks stop firing. While the project's `.claude/scheduled_tasks.json` holds tasks, `CronList` and `CronDelete` stay available so you can still list or cancel them.

# Notes

The full list of disable flags is on the Environment variables page.
