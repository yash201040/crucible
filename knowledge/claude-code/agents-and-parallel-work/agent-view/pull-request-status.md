---
type: "Feature"
title: "Pull request label on rows"
description: "Rows link to the session's pull or merge request with a colour-coded #N or !N label."
resource: "https://code.claude.com/docs/en/agent-view"
tags: [agent-view, pull-request, gh, status]
kind: "ui"
maturity: "research-preview"
since: "2.1.233"
surfaces: [cli]
requires: ""
identifiers:
  - "FORCE_HYPERLINK"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-view"
    resource: "https://code.claude.com/docs/en/agent-view"
    title: "Manage multiple agents with agent view"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

When a session opens a pull request, the row gets a label `#1234` (GitLab merge request: `!1234`, since v2.1.233) linked to it. The link is emitted even without detected hyperlink support (SSH, tmux); `FORCE_HYPERLINK=0` renders plain text. The label stays after a follow-up. More than one linked request shows a count such as `3 PRs`, coloured by the open one needing most attention; peek lists them all.

# How to use it

How the request is found:
- `gh` commands that edit, comment on, close or mark ready link the request named in the command output. A command with no PR in captured output (notably `gh pr merge`) creates no link.
- `gh pr checkout` or a push: Claude Code looks up the branch with `gh pr view`.
- If the request does not exist at push time, the lookup retries after up to five later `git`, `gh`, `glab`, or `curl` commands in the same directory (also finds PRs made via the GitHub REST API).

| Colour | Status |
| :- | :- |
| Yellow | Waiting on checks or review, or checks failed |
| Green | Checks passed, no blocking review |
| Purple | Merged |
| Grey | Draft or closed |

Dispatching `#1234` or a PR/MR URL selects the existing session instead of starting a new one. A session moves to the `Ready for review` group when its PR needs review or has failing checks.
