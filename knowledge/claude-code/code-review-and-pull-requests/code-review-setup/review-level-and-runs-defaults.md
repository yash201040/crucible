---
type: "Feature"
title: "Review level, review runs and organization coverage"
description: "Owner settings for Code Review: default review level, per-repository Review runs, and covering a whole github.com GitHub organization (needs a spend limit)."
resource: "https://code.claude.com/docs/en/code-review-setup"
tags: [code-review, review-level, admin, github-organization]
kind: "ui"
maturity: "unlabelled"
since: ""
surfaces: [cloud]
requires: "Owner role; for whole-organization coverage, a github.com organization you own and a monthly spend limit"
identifiers:
  - "Review level"
  - "Review runs"
  - "Change level"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "code-review-setup"
    resource: "https://code.claude.com/docs/en/code-review-setup"
    title: "Set up Code Review"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Review level: **Quick**, **Standard** (default), **Deep**. One organization default (select under **Review level**, confirm **Change level**); per-repository override via **Edit** (first option **Default** follows the org, saves immediately). A new level applies to reviews started after the change.

**Review runs** per repository: **Once after PR creation** (opened, reopened, marked ready), **After every push** (also auto-resolves threads when flagged issues are fixed), **Manual (@claude review)**. Table shows Once per PR, Every push, Manual. Drafts and forks are always skipped by automatic reviews.

# How to use it

Cover a whole GitHub organization: **Edit** its row in the Repositories table, select a **Review runs** option (the three plus **Off**) and confirm. Covers every repository the GitHub App can access, including later ones, from its next PR; can raise spend significantly; overrides individually set repositories (one set differently afterward is marked **Custom**; repositories turned off on their own rows stay off); an organization row has no review level.

# Limits and defaults

Requirements for whole-organization coverage: the connected GitHub account owns the organization; the organization is on github.com (GitHub Enterprise Server instances and personal accounts are not eligible); a monthly spend limit exists for the Claude organization or for Code Review. New repositories take the organization row's setting when it is covered as a whole, else After every push.
