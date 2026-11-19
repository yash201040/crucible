---
type: "Limit"
title: "Session-scoped scheduling limitations"
description: "Tasks fire only while Claude Code runs and is idle, with no catch-up, specific resume behavior and worktree caveats."
resource: "https://code.claude.com/docs/en/scheduled-tasks"
tags: [limits, resume, background-session, scheduling]
kind: "limit"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "--resume"
  - "--continue"
  - ".claude/scheduled_tasks.json"
  - "CronCreate"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "scheduled-tasks"
    resource: "https://code.claude.com/docs/en/scheduled-tasks"
    title: "Run prompts on a schedule"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Session-scoped scheduling has inherent constraints; for unattended cron-driven work use cloud scheduled tasks (cloud, on a schedule, via API call or GitHub events), GitHub Actions (`schedule` trigger) or Desktop scheduled tasks.

# Limits and defaults

- Tasks fire only while Claude Code is running and idle. Closing the terminal or exiting stops them. Backgrounding the session carries `/loop` tasks to a background session that keeps running without a terminal.
- No catch-up: if a due time passes while Claude is busy, it fires once when Claude becomes idle, not once per missed interval.
- In a background session, a self-paced loop stops if its wakeup comes due while the process is not running (for example after a crash). The transcript then shows a notice that the wakeup will not fire; reply to the session and ask Claude to keep it running.
- `claude --resume` / `--continue` restores `CronCreate` tasks except expired recurring tasks and one-shots whose time has passed. A self-paced `/loop` is not restored; run `/loop` again.
- A restored recurring task does not fire for missed runs; its next run is the first one due after resume, with jitter.
- Resume does not restart background Bash commands and monitors; ask Claude to start them again.
- With feature-flag fetching off, a task kept across sessions is stored in the project's `.claude/scheduled_tasks.json`. If `.claude` or that file is a symlink, Claude Code errors instead of scheduling. A saved task runs only in the folder where it was created; copying the file to another folder (such as a new worktree) lists the tasks there but does not run them, so recreate the task.
