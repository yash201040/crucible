---
type: "Feature"
title: "Diff view, code review and PR monitoring"
description: "Line comments on diffs, the /code-review card, and Auto-fix or Merge when ready for pull requests in Desktop."
resource: "https://code.claude.com/docs/en/desktop"
tags: [desktop, diff, code-review, pull-request, ci]
kind: "ui"
maturity: "unlabelled"
since: ""
surfaces: [desktop]
requires: "GitHub CLI (gh) installed and authenticated for PR monitoring"
identifiers:
  - "/code-review"
  - "Auto-fix"
  - "Merge when ready"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "desktop"
    resource: "https://code.claude.com/docs/en/desktop"
    title: "Desktop application"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Review Claude's changes file by file, comment on lines, have Claude review its own work, and let it watch a PR through CI.

# How to use it

- **Diff view**: click the `+12 -1` counts in the Changes card. Hover a line, click **+**, Enter to comment; submit all with Cmd+Enter (Ctrl+Enter on Windows). Claude revises and shows a new diff.
- **`/code-review`**: findings arrive as a **Code review** card (local, SSH, WSL sessions) with **Walk through in Changes**, **Fix this one** and **Apply fixes**.
- **PR monitoring**: after opening a PR the Changes card shows CI status; the menu has **Auto-fix** (also addresses new review comments from the repo owner, org members, collaborators or GitHub Apps, in local sessions) and **Merge when ready** (GitHub auto-merge; squash unless a merge queue is used).
- **Auto-archive after PR merge or close** in Settings archives sessions automatically (not cloud or running sessions).

# Limits and defaults

- **Merge when ready** is disabled in SSH and WSL sessions, and does not turn on if the repo disallows auto-merge.
- In SSH sessions install and authenticate `git` and `gh` on the remote machine; Desktop does not prompt to install `gh` there.
- A cloud session's diff can omit unpushed changes.
