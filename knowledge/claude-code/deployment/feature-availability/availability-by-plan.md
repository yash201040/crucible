---
type: "Reference"
title: "Features requiring a Claude subscription, by plan"
description: "Features reachable only with a claude.ai login and their per-plan availability across Pro, Max, Ultra, Team and Enterprise."
resource: "https://code.claude.com/docs/en/feature-availability"
tags: [plans, subscription, availability, enterprise]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop, web, mobile]
requires: "claude.ai account"
identifiers:
  - "/schedule"
  - "/voice"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "feature-availability"
    resource: "https://code.claude.com/docs/en/feature-availability"
    title: "Feature availability"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

These require a claude.ai sign-in and are not reachable with a Console API key or a third-party provider: cloud sessions and mobile, Claude Code in Slack (Pro, Max, Ultra), Desktop, cloud scheduled tasks (`/schedule`), Ultrareview, Code Review (Team, Enterprise), Remote Control, Chrome extension, computer use (Pro, Max, Ultra), Artifacts, voice dictation. Desktop is a partial exception through gateway routing or Claude Desktop on 3P.

# How to use it

| Feature | Pro | Max | Ultra | Team | Enterprise |
|---|---|---|---|---|---|
| Cloud sessions | yes | yes | yes | yes | yes (premium seat or Chat + Claude Code seat) |
| Cloud scheduled tasks | yes | yes | yes | yes | yes |
| Remote Control | yes | yes | yes | admin-enabled | admin-enabled |
| Channels | yes | yes | yes | admin-enabled | admin-enabled |
| Computer use | yes | yes | yes | no | no |
| Dispatch (Desktop) | yes | yes | yes | no | no |
| Code Review | no | no | no | yes | yes |
| Artifacts | yes | yes | yes | yes | yes |
| Analytics dashboard, contribution metrics | no | no | no | yes | yes |
| Enterprise Analytics API | no | no | no | no | yes |
| Server-managed settings | no | no | no | yes | yes |
| SSO | no | no | no | yes | yes |
| SCIM, Compliance API | no | no | no | no | yes |
| Zero Data Retention | no | no | no | no | yes, separate enablement for qualified accounts |

# Notes

Ultra is the new name for Max 20x; Max is the new name for Max 5x; Max and Ultra have the same Claude Code features. Enterprise organizations with the HIPAA configuration have some of these features turned off. The plan section does not apply to cloud-provider or Console API key users.
