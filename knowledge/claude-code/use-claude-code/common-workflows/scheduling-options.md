---
type: "Reference"
title: "Options for running Claude on a schedule"
description: "Cloud scheduled tasks, desktop scheduled tasks, GitHub Actions and /loop compared by where they run."
resource: "https://code.claude.com/docs/en/common-workflows"
tags: [scheduling, routines, loop, github-actions, desktop]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop, cloud]
requires: ""
identifiers:
  - "/loop"
  - "--resume"
  - "--continue"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "common-workflows"
    resource: "https://code.claude.com/docs/en/common-workflows"
    title: "Common workflows"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Four ways to run a recurring task (PR review each morning, weekly dependency audit, overnight CI checks).

# How to use it

| Option | Where it runs | Best for |
| :- | :- | :- |
| Cloud scheduled tasks | Cloud, Anthropic-managed by default | Runs when your computer is off; can also trigger on API calls or GitHub events; configure at claude.ai/code/routines |
| Desktop scheduled tasks | Your machine, via the desktop app | Direct access to local files, tools, uncommitted changes |
| GitHub Actions | Your CI pipeline | Repo events such as opened PRs, or cron schedules beside workflow config |
| `/loop` | The current CLI session | Quick polling while a session is open; `--resume` and `--continue` restore unexpired fixed-interval loops |

# Notes

A scheduled task runs autonomously and cannot ask clarifying questions, so state what success looks like and what to do with results (example: review open PRs labeled `needs-review`, comment inline, post a summary in a Slack channel).
