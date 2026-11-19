---
type: "Concept"
title: "Claude Tag as Slack successor"
description: "Claude Tag runs @Claude as an organization's shared identity and replaces this per-user Slack integration for Team and Enterprise."
resource: "https://code.claude.com/docs/en/slack"
tags: [slack, claude-tag, migration, enterprise]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cloud]
requires: "Team or Enterprise plan for Claude Tag"
identifiers:
  - "@Claude connect"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "slack"
    resource: "https://code.claude.com/docs/en/slack"
    title: "Claude Code in Slack"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude Tag is the organization-managed @Claude in Slack with admin-configured access, run under a shared identity rather than each user's account. It is not available on individual (Pro/Max/Ultra) plans, where the earlier per-user version on this page is used in a workspace not connected to Claude Tag.

# How to use it

On Team/Enterprise, set up Claude Tag for a new workspace; existing Slack app and @Claude handle stay. To migrate a workspace already on the earlier version, follow "Migrate from the earlier Claude in Slack" in the Claude Tag docs. The `@Claude connect` command is named in the "not set up" notice.
