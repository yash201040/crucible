---
type: "Feature"
title: "Desktop local scheduled tasks"
description: "Recurring or one-time local tasks that start a fresh session on a schedule while the app is open, with catch-up, permissions and management."
resource: "https://code.claude.com/docs/en/desktop-scheduled-tasks"
tags: [desktop, scheduling, recurring, cron, unattended]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [desktop]
requires: "Claude Desktop 1.1.5368 or later; app open and computer awake"
identifiers:
  - "~/.claude/scheduled-tasks/<task-name>/SKILL.md"
  - "update_scheduled_task"
  - "requiresUserInteraction"
  - "Run now"
  - "Keep computer awake"
  - "CLAUDE_CONFIG_DIR"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "desktop-scheduled-tasks"
    resource: "https://code.claude.com/docs/en/desktop-scheduled-tasks"
    title: "Schedule recurring tasks in Claude Code Desktop"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The Scheduled tasks page lists local tasks and cloud scheduled tasks (formerly routines; the app may say Routines). A local task runs on your machine with access to files and tools and starts a new session when due; it fires only while the app is open and the computer is awake.

| | Cloud | Desktop | `/loop` |
| - | - | - | - |
| Runs on | cloud | your machine | your machine |
| Needs machine on | no | yes | yes |
| Needs open session | no | no | yes |
| Minimum interval | 1 hour | 1 minute when Claude sets it, 1 hour in forms | 1 minute |
| Permission prompts | auto mode default | configurable per task | inherits |

# How to use it

Code tab > **Scheduled** > **New task** > set up manually; **Name** (lowercased kebab-case, becomes the folder name, unique), instructions, turn on **Only on this computer**, pick a local folder, schedule, permission mode and model, **Create**. Or describe it in any session ("set up a daily code review that runs every morning at 9am"); one-time requests disable themselves after firing.

Schedules: Hourly, Daily, Weekdays, Weekly, Manual (only **Run now**), Custom (cron in local time, numeric days/months, Sunday is `0`, form rejects more often than hourly). **Worktree** checkbox (Edit form, Git repos) gives each run an isolated worktree; default runs on the working directory including uncommitted changes.

Task prompt lives at `~/.claude/scheduled-tasks/<task-name>/SKILL.md` (under `CLAUDE_CONFIG_DIR` if set) with frontmatter `name` and `description`; edits apply next run. Schedule, folder and enabled state are not in the file. A task changes itself with the `update_scheduled_task` MCP tool (approve each call via **Run now**).

# Limits and defaults

- Desktop checks every minute; each task gets a deterministic start delay of a few minutes to stagger API traffic. Runs missed while asleep are skipped, but on app start or wake Desktop runs exactly one catch-up for the most recently missed time within the last seven days.
- Permissions: per-task mode; `~/.claude/settings.json` allow rules apply; use **Run now** and "always allow" to avoid stalls; MCP tools marked `requiresUserInteraction` prompt every call and stall runs. History shows skipped runs with reasons.
- Delete archives sessions but leaves the task folder on disk. **Model** "Default · Set by admin" uses the organization's managed-settings model.
