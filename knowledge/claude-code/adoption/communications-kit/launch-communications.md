---
type: "Guide"
title: "Launch communications and rollout checklist"
description: "Pre-send checklist and announcement templates (standard, executive sponsor, pilot, champion DM) for rolling out Claude Code."
resource: "https://code.claude.com/docs/en/communications-kit"
tags: [rollout, announcement, launch, adoption]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "curl -fsSL https://claude.ai/install.sh | bash"
  - "/init"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "communications-kit"
    resource: "https://code.claude.com/docs/en/communications-kit"
    title: "Communications kit"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Copy-ready draft announcements for administrators and engineering leads; treat as drafts to rewrite in your voice and replace `[bracketed placeholders]`.

# How to use it

Before sending: create a `#claude-code` channel, test the install command on a machine in your environment, have the security/data-usage link ready, choose one concrete first task, name a channel owner for the first 48 hours, line up a C-suite sponsor (exec-sent launches see higher first-week adoption per the page).

Templates provided: standard announcement (email and Slack/Teams: install, `cd <your-repo>`, `claude`, run `/init`, example prompts, data-handling statement, VS Code and JetBrains mention); executive sponsor variant (single ask of ten minutes); pilot group variant (feedback to `#claude-code-pilot`, suggests Shift+Tab into plan mode on the first multi-file change); champion recruitment DM.

# Notes

The standard message states that Claude Code runs in the terminal and talks directly to Anthropic's API, and that on Team or Enterprise plans Anthropic does not use code or prompts to train models.
