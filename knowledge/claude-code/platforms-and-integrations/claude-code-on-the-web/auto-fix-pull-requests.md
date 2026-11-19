---
type: "Feature"
title: "Auto-fix pull requests"
description: "Claude watches a PR in a cloud session and responds to CI failures and review comments, pushing fixes when clear."
resource: "https://code.claude.com/docs/en/claude-code-on-the-web"
tags: [auto-fix, pull-request, ci, github]
kind: "slash_command"
maturity: "unlabelled"
since: ""
surfaces: [cli, web, mobile, cloud]
requires: "Claude GitHub App installed on the repository"
identifiers:
  - "/autofix-pr"
  - "Auto-fix"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "claude-code-on-the-web"
    resource: "https://code.claude.com/docs/en/claude-code-on-the-web"
    title: "Use Claude Code in the cloud"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude subscribes to GitHub activity on a pull request; on a failed check or reviewer comment it investigates and pushes a fix when one is clear. Clear fixes are made and explained; ambiguous or architecturally significant requests are asked about first; duplicates and no-action events are noted.

# How to use it

- PR from a cloud session: in the **Changes** card, the PR's menu, turn on **Auto-fix**.
- Terminal: `/autofix-pr` on the PR's branch; it detects the PR with `gh`, spawns a cloud session and turns auto-fix on.
- Mobile: tell Claude to auto-fix the PR. Any existing PR: paste its URL and ask.
- Stop: turn off Auto-fix in the menu or tell Claude to stop watching.

# Limits and defaults

- GitHub sends no webhook when the base branch advances into a merge conflict, so auto-fix cannot react to conflicts; ask Claude to rebase.
- Claude may reply to review threads using the user's GitHub account, labelled as from Claude Code. Warning: replies can trigger comment-triggered automation (Atlantis, Terraform Cloud, GitHub Actions on `issue_comment`); consider disabling for such repos.
