---
type: "Feature"
title: "GitHub trigger and PR filters"
description: "Start a fresh cloud session on pull request, release or issue events, with filters on PR fields."
resource: "https://code.claude.com/docs/en/routines"
tags: [github, trigger, webhook, pull-request, filters]
kind: "behavior"
maturity: "research-preview"
since: "2.1.225"
surfaces: [cloud, web, cli]
requires: "Claude GitHub App installed on the repository"
identifiers:
  - "pull_request.opened"
  - "pull_request.closed"
  - "/web-setup"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "routines"
    resource: "https://code.claude.com/docs/en/routines"
    title: "Automate work with scheduled tasks"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A GitHub trigger starts a new session when a matching event occurs on a connected repo. Sessions are never reused across events: two PR updates give two independent sessions. Events are Pull request, Release (created, published, edited, deleted) and Issue; each can be narrowed to a specific action (for example `pull_request.opened`) or all actions. Webhook events are capped per task and per account per hour; events over the cap are dropped until the window resets.

# How to use it

- Web: task edit dialog > Trigger row > + > GitHub event, choose repo, event, filters, Save changes. The web prompts to install the app. From the CLI, install the app from the GitHub App page first, then ask Claude, e.g. `/schedule add a GitHub trigger to my nightly review for pull requests opened in acme/webapp` (v2.1.225+).
- `/web-setup` grants repo access for cloning but does not install the GitHub App or enable webhooks.
- PR filter fields (all must match): Author, Title, Body, Base branch, Head branch, Labels, Is draft, Is merged.
- Operators: equals, contains, starts with, is one of, is not one of, matches regex. Regex tests the entire value, so use `.*hotfix.*` for a substring match.
- Example filter combinations: base `main` + head contains `auth-provider`; is draft = false; labels include `needs-backport`.

# Notes

The GitHub trigger is unavailable in the main-view dialog until a repository is selected.
