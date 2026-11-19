---
type: "Feature"
title: "Cloud scheduled tasks (routines)"
description: "Saved prompt, repositories and connectors that run as cloud Claude Code sessions on a schedule, API call or GitHub event."
resource: "https://code.claude.com/docs/en/routines"
tags: [scheduled-tasks, routines, cloud, triggers, automation]
kind: "behavior"
maturity: "research-preview"
since: ""
surfaces: [cloud, web, cli, desktop]
requires: "Pro, Max, Ultra, Team or Enterprise; claude.ai login; cloud sessions enabled"
identifiers:
  - "/schedule"
  - "/routines"
  - "claude.ai/code/routines"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "routines"
    resource: "https://code.claude.com/docs/en/routines"
    title: "Automate work with scheduled tasks"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A cloud scheduled task (formerly a routine) packages a prompt, one or more repositories and connectors, and runs them autonomously as full Claude Code cloud sessions on Anthropic-managed infrastructure (or an organization's self-hosted environment), so it keeps working when your laptop is closed. The page labels the feature research preview: behavior, limits and API surface may change. Each task can hold one or more triggers: Schedule (recurring or one-off), API (HTTP POST with a bearer token), GitHub (repo events). A task may have only an API or only a GitHub trigger and then has no next run time.

Tasks belong to the individual claude.ai account, are not shared with teammates, count against that account's usage, and act as you (commits, PRs, Slack, Linear use your linked identities). Created from the web, the Desktop app (Code tab > Scheduled) or the CLI; all write to the same cloud account.

Two other features schedule work on your machine: Desktop scheduled tasks and `/loop`.

# How to use it

- Web: claude.ai/code/routines > New task. Pick prompt, trigger, repositories (cloned each run, `claude/`-prefixed branches), cloud environment, model and effort (Effort appears when the model offers levels), connectors (all connected ones are included by default; remove unneeded ones). "Run now" starts a run immediately.
- The saved prompt is treated as the session's assignment, not as untrusted mid-conversation content, but it is not live user input and cannot act as approval or consent. The prompt must be self-contained.
- Detail page: History of runs (Succeeded / Failed / Cancelled outcomes describe how the session ended, not whether the work was done), on/off switch to pause, Edit, Delete. Each run opens as a full session.
- Self-hosted environments can run tasks; permissions are configured there.

# Limits and defaults

- Team/Enterprise Owners can disable the feature with the "Scheduled tasks (Was Routines)" or "Routines" toggle at Organization settings > Capabilities > Remote sessions; existing tasks then stop. Custom-role orgs also need the scheduled tasks permission.
- Local MCP servers added with `claude mcp add` are not connectors; add them at claude.ai/customize/connectors, or declare in a committed `.mcp.json` (single-repo tasks not run as project threads).
- GitHub connection missing or expired: runs skipped for up to 72 hours, then the task turns off until GitHub is reconnected and it is turned back on.
- A task's runs start from each repo's default branch unless the prompt says otherwise; for a PR event the first repository starts from the PR head commit. Branch push limits come from GitHub branch protection.

# Notes

Where the old name "routines" still appears: some app labels, `claude.ai/code/routines`, the `/routines` alias, the `/fire` endpoint path and beta header, the response `type`, the `<routine-fire-payload>` tag, and the org toggle.
