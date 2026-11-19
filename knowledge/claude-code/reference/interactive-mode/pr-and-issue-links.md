---
type: "Feature"
title: "PR status badge, GitLab MR badge and issue links"
description: "Footer PR or MR badge with review-state color, and clickable owner/repo#123 issue references."
resource: "https://code.claude.com/docs/en/interactive-mode#pr-review-status"
tags: [pull-request, gitlab, github, links, footer]
kind: "ui"
maturity: "unlabelled"
since: "2.1.234"
surfaces: [cli]
requires: "GitHub token or gh CLI for PRs; glab CLI authenticated for GitLab MRs (v2.1.234+)"
identifiers:
  - "GH_TOKEN"
  - "GITHUB_TOKEN"
  - "GH_HOST"
  - "GH_ENTERPRISE_TOKEN"
  - "GITHUB_ENTERPRISE_TOKEN"
  - "FORCE_HYPERLINK"
  - "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC"
  - "glab auth login"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "interactive-mode"
    resource: "https://code.claude.com/docs/en/interactive-mode"
    title: "Interactive mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

On a branch with an open PR the footer shows a link such as `PR #446` with a colored underline: green approved, yellow pending review, red changes requested, gray draft. It disappears once merged or closed. `Cmd+click` / `Ctrl+click` opens it. It refreshes after a successful `git push` or a `gh pr` command that changes the PR.

# How to use it

- github.com tokens: `GH_TOKEN`, `GITHUB_TOKEN`, or the token from `gh auth login`; footer hints `install gh for PR status` or `gh auth login for PR status` if absent. Enterprise host in `GH_HOST`: `GH_ENTERPRISE_TOKEN`, `GITHUB_ENTERPRISE_TOKEN` or `gh auth login --hostname <host>`. Other hosts: the saved `gh` token, no hint otherwise.
- `FORCE_HYPERLINK=0` renders plain text; `1` forces links on.
- `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` stops PR/MR status checks.
- GitLab: `MR !N` badge (green mergeable, yellow other open, gray draft); needs `glab` on PATH, authenticated with `glab auth login`; `GITLAB_TOKEN` variables are ignored; restart after installing or logging in; refreshes after `glab mr` changes.
- Issue links: only two-part `owner/repo#123` is clickable (not bare `#123`, nested GitLab paths, code spans, or replies over about 1,000 lines or 100,000 characters). Link goes to the host of your git remote: github.com/other hosts `https://<host>/owner/repo/issues/123`, gitlab.com `.../-/issues/123`; bitbucket.org, codeberg.org, gitea.com get no link.
