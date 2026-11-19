---
type: "Concept"
title: "Choosing cwd or repo"
description: "cwd suits identical paths; repo resolves a slug to the clone or worktree where claude last ran, without changing branch."
resource: "https://code.claude.com/docs/en/deep-links"
tags: [deep-links, repo, cwd, worktrees]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "cwd"
  - "repo"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "deep-links"
    resource: "https://code.claude.com/docs/en/deep-links"
    title: "Launch sessions from links"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Two ways to set the working directory of a deep-link session.

# How to use it

- Use `cwd` when everyone clicking has the project at the same absolute path (a standardized devcontainer or VM image).
- Use `repo` for shared links where people clone to different locations. Claude Code opens the clone or worktree of that repository where you most recently ran `claude`: each run in a Git repository records the directory against its GitHub `owner/name`. Clones and worktrees are tracked separately.

# Limits and defaults

The link does not change the checked-out branch; the session opens in whatever state the directory is in. The welcome header shows the chosen path. `repo` resolves only clones Claude Code has already seen: run `claude` inside the clone once, or use `cwd`.
