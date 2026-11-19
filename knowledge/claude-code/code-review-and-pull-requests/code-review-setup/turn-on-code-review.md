---
type: "Guide"
title: "Turn on Code Review"
description: "Owner steps in Admin settings > Claude Code: Allow code review, connect GitHub, install the Claude GitHub App, choose repositories, verify with a test PR."
resource: "https://code.claude.com/docs/en/code-review-setup"
tags: [code-review, admin, github-app, setup]
kind: "ui"
maturity: "unlabelled"
since: ""
surfaces: [cloud]
requires: "Owner role in the Claude organization; GitHub organization owner to install the app; write access to each repository added"
identifiers:
  - "Allow code review"
  - "Install GitHub App"
  - "Show tips on pull requests"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "code-review-setup"
    resource: "https://code.claude.com/docs/en/code-review-setup"
    title: "Set up Code Review"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Reviews run on Anthropic infrastructure, so no workflow files go into repositories. Steps at claude.ai/admin-settings/claude-code (Code review section): click the **Allow code review** switch; connect GitHub (select your instance first for GitHub Enterprise Server); install the Claude GitHub App (broader permission set shared with other Claude features); choose repositories; click **Finish**; verify with a non-draft test PR (a **Claude Code Review** check run appears within a few minutes, or comment `@claude review` for a Manual repo).

# How to use it

Repositories start at **After every push**, which runs the most reviews. Add repositories later with **Add** above the Repositories table; a repository is listed only if the GitHub App can access it. If the dialog closes early, repositories stay added but **Allow code review** stays off.

**Show tips on pull requests** (default on) makes Claude post a tip comment when no review starts: repository set to Manual, PR from a fork, a bot or non-write non-author commenting `@claude review`, or the GitHub organization not linked to the Claude organization.

# Limits and defaults

Developers without Owner role can: comment `@claude review` (needs write access; works on drafts and forks), comment `@claude review always` on a non-draft non-fork PR, and commit `REVIEW.md` and `CLAUDE.md`. Developer-requested reviews are billed to the organization.

# Notes

Turn off: per repository (**Edit**, turn off **Code review**), remove a repository (**Remove repository**, not possible while its GitHub organization is covered as a whole), a whole GitHub organization (select **Off**, which also turns off its individually added repositories), or everything (turn off **Allow code review**; the repository list stays).
