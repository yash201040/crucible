---
type: "Feature"
title: "Claude Tag for Slack"
description: "Slack integration running @Claude as an organization's shared identity with admin-configured access, on Team and Enterprise plans."
resource: "https://code.claude.com/docs/en/claude-tag"
tags: [slack, claude-tag, team, integration]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cloud]
requires: "Team or Enterprise plan"
identifiers:
  - "@Claude"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "claude-tag"
    resource: "https://code.claude.com/docs/en/claude-tag"
    title: "Claude Tag"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude Tag runs `@Claude` in a team's Slack channels as the organization's shared identity, with admin-configured access. Anyone in a channel can tag `@Claude` into a thread and assign a task. Setup and usage docs live at claude.com/docs/claude-tag/overview, not in the Claude Code docs.

# Limits and defaults

- Available on Team and Enterprise plans only. Not available on Pro, Max or Ultra; for those, set up the separate Claude Code in Slack (each session runs under an individual user's account) for Slack workspaces no organization has connected to Claude Tag.
