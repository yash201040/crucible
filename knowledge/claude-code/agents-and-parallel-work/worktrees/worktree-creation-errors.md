---
type: "Reference"
title: "Worktree creation errors and recoveries"
description: "Error messages for symlinks, replaced objects, Git LFS filter drivers, partial clones, non-git directories and wrong-repository worktrees."
resource: "https://code.claude.com/docs/en/worktrees"
tags: [worktrees, errors, git-lfs, troubleshooting]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.247"
surfaces: [cli]
requires: ""
identifiers:
  - "GIT_NO_REPLACE_OBJECTS"
  - "git replace"
  - "git lfs install --local"
  - "git lfs pull"
  - "Could not read the repository git config to neutralize filter drivers"
  - "The repository git config defines a filter driver whose name cannot be neutralized (contains \"=\" or a newline)"
  - "The repository git config has a conditional include (includeIf)"
  - "Git was not run: the repository's own git config sets <key>"
  - "This repository is a partial clone"
  - "Can only use --worktree in a git repository"
  - "belongs to a different repository"
  - "is a leftover worktree"
  - "is already checked out elsewhere in this repository"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "worktrees"
    resource: "https://code.claude.com/docs/en/worktrees"
    title: "Run parallel sessions with worktrees"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Errors when Claude Code creates a worktree, enters one at startup, or returns a resumed session to one.

# How to use it

| Situation | Behavior and fix |
| :- | :- |
| Cannot enter worktree at startup | Prints error naming the path, exits code 1 (e.g. hook printed something else, or directory deleted) |
| Symlinked path | Refuses when `.claude`, `.claude/worktrees` or the worktree directory is a symlink; remove it and retry. Before v2.1.212 a committed symlink could be followed to create files outside the repo |
| `git replace` objects | Worktree holds original objects' content; checkout runs with `GIT_NO_REPLACE_OBJECTS=1` (overrides your value). Use `git worktree add` yourself |
| Git LFS pointer files | With `git lfs install --local` (repo `.git/config` filter), a Claude-created worktree has pointer files because repo-own filter drivers are skipped (before v2.1.247 they ran); run `git lfs pull` in the worktree. Plain `git lfs install` (global) is unaffected |
| `Could not read the repository git config to neutralize filter drivers` | No worktree; fix `.git/config` permissions and retry |
| `The repository git config defines a filter driver whose name cannot be neutralized (contains "=" or a newline)` | Rename or remove that driver |
| `The repository git config has a conditional include (includeIf)` | Inline the included settings and remove the `includeIf` in `.git/config` (a global-config `includeIf` is fine) |
| `Git was not run: the repository's own git config sets <key>` | Key points Git LFS at a program (e.g. `lfs.customtransfer.<name>.path`, `lfs.standalonetransferagent`); move yours to global config, or remove it if unrecognized |
| `This repository is a partial clone` | Take the step in the message's sentence ending `try again`, then rerun from that shell |
| `Can only use --worktree in a git repository` | No git checkout and no `WorktreeCreate` hook: `git init` and make a first commit, set up the hook for another VCS, or run without `--worktree` |
| `belongs to a different repository` / `is a leftover worktree` | Directory tied to another location (after copy or move); use a different name; if nothing to keep and no move, remove it and retry (after a move this may give `is already checked out elsewhere in this repository`) |

# Notes

The four filter-driver cases (the four rows beginning `Could not read` through `Git was not run`) create no worktree at all.
