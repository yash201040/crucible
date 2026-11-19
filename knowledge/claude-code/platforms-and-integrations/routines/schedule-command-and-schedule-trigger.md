---
type: "Feature"
title: "/schedule command and schedule triggers"
description: "Create, list, update and run cloud scheduled tasks from the CLI, with recurring cadence, custom cron and one-off runs."
resource: "https://code.claude.com/docs/en/routines"
tags: [schedule, cron, cli, one-off, scheduled-tasks]
kind: "slash_command"
maturity: "research-preview"
since: "2.1.225"
surfaces: [cli, web, desktop]
requires: "claude.ai subscription login (not API key, profile, or cloud provider login)"
identifiers:
  - "/schedule"
  - "/schedule list"
  - "/schedule update"
  - "/schedule run"
  - "/routines"
  - "CRON_TZ="
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "routines"
    resource: "https://code.claude.com/docs/en/routines"
    title: "Automate work with scheduled tasks"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`/schedule` (alias `/routines`) creates a cloud scheduled task conversationally; Claude asks about schedule, repositories and prompt, then saves it. A CLI-created task has a schedule trigger. API triggers and their tokens cannot be added or managed from the CLI (web only). A GitHub trigger can be added by asking Claude in the CLI (needs v2.1.225+) after installing the Claude GitHub App.

# How to use it

```text
/schedule daily PR review at 9am
/schedule tomorrow at 9am, summarize yesterday's merged PRs
/schedule in 2 weeks, open a cleanup PR that removes the feature flag
/schedule list
/schedule update
/schedule run
/schedule why did my nightly review do nothing this morning?
```

The last form lists recent runs with status and links and reads a run's log (tool errors, permission denials, final result); requires v2.1.227+.

Schedule trigger details:
- Presets: hourly, daily, weekly. Preset times are entered in local time zone.
- Runs exactly on the hour can start several minutes late; pick e.g. 9:07.
- Custom: choose Custom in the edit dialog and enter a cron expression such as `0 */2 * * *`. Expressions running more often than once per hour are rejected. A bare five-field expression is in UTC (`0 9 * * 1-5` = 9:00 UTC weekdays); a leading `CRON_TZ=` prefix sets the zone.
- One-off: runs once at a timestamp, then turns itself off and shows Completed. Re-arm via the edit dialog (One-time/Once). One-off runs count against the same hourly limits.

# Limits and defaults

`/schedule` is hidden (`Unknown command: /schedule`) when: authenticated with a Console API key, profile/federation credential or cloud provider (Bedrock, Agent Platform, Foundry); `ANTHROPIC_API_KEY`/`ANTHROPIC_AUTH_TOKEN`/`apiKeyHelper` take precedence; inside a cloud session; cloud sessions disabled by org policy (answers `Cloud sessions are disabled by your organization's policy` from v2.1.268); org Owner disabled scheduled tasks (hidden from v2.1.227); or a custom role lacks the permission. Signed-out answers `/schedule requires a claude.ai subscription. Run /login to sign in with your claude.ai account.` With a Console key and flag fetching it shows `/schedule is available with Claude for Enterprise`. Manage tasks at the web UI in those cases.
