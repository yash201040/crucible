---
type: "Concept"
title: "Slack session flow and access control"
description: "How a Slack mention becomes a cloud session, the action buttons, repository selection and user, workspace and channel access controls."
resource: "https://code.claude.com/docs/en/slack"
tags: [slack, sessions, access-control, pull-requests]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cloud, web]
requires: ""
identifiers:
  - "View session"
  - "Create PR"
  - "Select repository"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "slack"
    resource: "https://code.claude.com/docs/en/slack"
    title: "Claude Code in Slack"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Flow: @mention with a coding request, intent detection, new session at claude.ai/code, status updates in the thread, final message update plus a direct message, then review. Buttons: **View session** (full transcript, continue), **Create PR** (opens GitHub compare page for the session's branch; appears on the start status message after the session finishes), **Switch to code repo...**. If the repository is unclear Claude asks you to click **Select repository**; naming the repo in the request improves selection.

# Limits and defaults

- Access: per-user accounts and plan limits; users reach only repositories they connected themselves.
- Workspace admins control app installation; Enterprise Grid org admins control which workspaces get it; removing the app revokes all users immediately. Channel invitation is an additional gate.
- Use Slack for asynchronous kickoff and teammate visibility; use the web for file uploads, real-time interaction, longer tasks.

# Notes

Troubleshooting entries: "This workspace isn't set up for Claude Tag yet" (no Claude Tag connection and not a Pro/Max/Ultra account); "The legacy Claude in Slack bot is retired" (workspace connected to an org; an Owner enables Claude Tag at admin settings); "Claude Code is not enabled for your account" (no cloud environment yet; finish web onboarding at claude.ai/code individually); sessions not starting (check account connection, cloud sessions, a connected GitHub repo); Claude Tag channel sessions fail when the environment is personal rather than organization-shared (an Owner shares or recreates it as organization-shared, set as org default or per channel).
