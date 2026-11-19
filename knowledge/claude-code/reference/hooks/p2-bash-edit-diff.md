---
type: "Feature"
title: "bashEditDiff in PostToolUse"
description: "Best-effort list of files a Bash command changed in a Git repo, delivered to PostToolUse in tool_response.bashEditDiff."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, bash, diff, posttooluse]
kind: "setting"
maturity: "beta"
since: "2.1.269"
surfaces: [cli]
requires: "Claude Code v2.1.269 or later"
identifiers:
  - "bashEditDiffEnabled"
  - "tool_response.bashEditDiff"
  - "changedFiles"
  - "files"
  - "moreFiles"
  - "unavailable"
  - "skipped"
  - "shared"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

When a Bash command changes files in a Git repository, Claude Code can record what changed and hand it to your `PostToolUse` hook in `tool_response.bashEditDiff`. The page calls the list best effort and in public beta: it can miss changes, include a file another process changed at the same time, or stop at size limits, and the shape may change. Use it to find what to review, not to enforce policy.

# How to use it

Recording is on in every permission mode when the `bashEditDiffEnabled` setting turns it on; otherwise only in auto mode and `bypassPermissions` mode, and only when Claude Code directs Claude to edit files through Bash. Set `bashEditDiffEnabled` to `false` to turn it off. Background and read-only commands carry no diff.

| Field | Type | Meaning |
| :- | :- | :- |
| `changedFiles` | array | Absolute paths changed, at most 200; present when `files` holds a diff or `moreFiles` > 0 |
| `files` | array | Diffs of up to 5 files (`filePath`, `hunks`, `created`/`deleted` flags) |
| `moreFiles` | number | Changed files with no diff in `files` |
| `unavailable` | boolean | Diff incomplete or could not be taken |
| `skipped` | boolean | Git command that moves the working tree (`git checkout`, `git stash`): no diff taken |
| `shared` | boolean | Another Bash call (e.g. a subagent's) ran in the same repo at the same time |

# Limits and defaults

Files Git ignores and files in submodules are not listed.
