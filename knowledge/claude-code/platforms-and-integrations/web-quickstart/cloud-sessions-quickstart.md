---
type: "Guide"
title: "Cloud sessions quickstart"
description: "How a cloud session runs, how it compares with local and Remote Control sessions, and how to start and review a task from claude.ai/code."
resource: "https://code.claude.com/docs/en/web-quickstart"
tags: [cloud-sessions, quickstart, permission-modes, parallel-tasks]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [web, cloud, mobile, desktop, cli]
requires: "Pro, Max, Ultra, Team; Enterprise with premium seats or Chat + Claude Code seats"
identifiers:
  - "claude --cloud"
  - "claude.ai/code"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "web-quickstart"
    resource: "https://code.claude.com/docs/en/web-quickstart"
    title: "Get started with Claude Code in the cloud"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A cloud session runs Claude Code on an isolated VM (Anthropic-managed by default) instead of your machine. Start from claude.ai/code, the Claude mobile app, the Desktop app with Cloud selected, or `claude --cloud`. Steps: clone the repo and run the setup script; set network access from the environment's access level; Claude works; it pushes a branch to GitHub. The session stays open after the push, so PR creation and further edits happen in the same conversation. Sessions persist across devices; usage counts toward plan limits with no separate VM charge. Suited to parallel independent tasks (each own session and branch), repos not cloned locally, tasks needing little steering, and code questions. In a self-hosted environment the clone and later steps run on the organization's runners.

# How to use it

Comparison:

| | Cloud session | Local session | Local + Remote Control |
|---|---|---|---|
| Runs on | cloud VM | your machine | your machine |
| Uses local config | no, repo only | yes | yes |
| Requires GitHub | yes (unless `--cloud` bundles the local repo) | no | no |
| Keeps running if you disconnect | yes | no | while session stays open |
| Permission modes | Accept edits, Plan, Auto | all in terminal | Manual, Accept edits, Plan, Auto |
| Network | configurable per environment | machine's | machine's |

Start a task: pick repository (multiple allowed) and branch, or "No repository" at claude.ai/code; choose permission mode (Auto, Accept edits, Plan; cloud sessions offer no Manual or Bypass permissions; Auto may be grayed out if the model or org does not support it); describe and submit. Each task gets its own session and branch.

Review: Changes card shows `+N -M`; diff compares to base branch by default (Compare against to change); hover a line and click + to queue inline comments that are bundled with the next message; Create PR (right-click for draft PR). Keep iterating after the PR; Auto-fix pull requests can monitor it.

# Limits and defaults

Closing the tab does not stop a session; it runs to completion of the current task then idles, and can be archived or deleted from the sidebar.
