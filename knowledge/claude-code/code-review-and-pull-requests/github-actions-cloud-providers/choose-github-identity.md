---
type: "Concept"
title: "Choosing a GitHub identity for cloud provider runs"
description: "Three identities the action can use to push and comment with a cloud provider: official Claude App, custom app, or GITHUB_TOKEN, and how workflow examples change."
resource: "https://code.claude.com/docs/en/github-actions-cloud-providers"
tags: [github-actions, github-app, identity, ci]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [headless, cloud]
requires: ""
identifiers:
  - "github_token"
  - "GITHUB_TOKEN"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "github-actions-cloud-providers"
    resource: "https://code.claude.com/docs/en/github-actions-cloud-providers"
    title: "Use Claude Code GitHub Actions with cloud providers"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The action pushes commits and posts comments through a GitHub identity you choose.

# How to use it

| Identity | Notes | Workflow change from the page's custom-app examples |
| :- | :- | :- |
| Official Claude GitHub App | Full permission set | Delete the Generate GitHub App token step and the `github_token` line |
| Custom GitHub App | Only Contents, Issues, Pull requests | Examples use this |
| Automatic `GITHUB_TOKEN` | No app to create; GitHub will not trigger CI workflows on its commits | Delete token step; `github_token: ${{ secrets.GITHUB_TOKEN }}` |

# Notes

Example workflows trigger on `issue_comment` (created), `pull_request_review_comment` (created) and `issues` (opened), with an `if` guard checking for `@claude`, permissions `contents`, `pull-requests`, `issues` write and `id-token: write`.
