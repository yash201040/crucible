---
type: "Feature"
title: "Worktree base branch and PR checkout"
description: "worktree.baseRef chooses fresh (default branch) or head; --worktree with a PR/MR number or URL branches from that change."
resource: "https://code.claude.com/docs/en/worktrees"
tags: [worktrees, base-branch, pull-request, settings]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "worktree.baseRef"
  - "\"fresh\""
  - "\"head\""
  - "--worktree \"#1234\""
  - ".claude/worktrees/pr-<number>"
  - "origin/HEAD"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "worktrees"
    resource: "https://code.claude.com/docs/en/worktrees"
    title: "Run parallel sessions with worktrees"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

New worktrees branch from the repository's default branch unless `worktree.baseRef` says otherwise. It cannot be a branch name; to start from a specific existing branch use `git worktree add`.

# How to use it

| `worktree.baseRef` | Meaning |
| :- | :- |
| `"fresh"` (default) | Branch from the default branch on the remote (usually `main`), a clean tree matching the remote |
| `"head"` | Branch from current local `HEAD` (carries unpushed commits); inside a worktree it resolves to that worktree's `HEAD`; use for subagents operating on in-progress work |

```json
{"worktree": {"baseRef": "head"}}
```

PR/MR: `claude --worktree "#1234"` (quote it), or pass a GitHub pull request URL or GitLab merge request URL such as `https://gitlab.com/group/repo/-/merge_requests/123`. Claude Code reads only the number, always fetches from `origin` and creates `.claude/worktrees/pr-<number>`. Fetch path by host: github.com `pull/<number>/head`; gitlab.com `merge-requests/<number>/head`; others try `pull/<number>/head` then `merge-requests/<number>/head`.

# Limits and defaults

- For a `"fresh"` base, if not fetched within 24 hours it fetches the default branch with a 5-second cap and falls back to the cached ref on failure; with no remote or no cached `origin/HEAD` it falls back to local `HEAD`.
- Fetches never wait for terminal input: a password, passphrase or new-SSH-host prompt counts as failure. A PR fetch failure exits with `Error creating worktree: Failed to fetch PR/MR #<number>`; load the key in `ssh-agent` and run `git fetch` once to record a new host.
