---
type: "Concept"
title: "Hook security and workspace trust"
description: "Hooks run with your full user permissions; settings-file hooks run only after workspace trust, but -p and SDK sessions treat folders as trusted."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, security, workspace-trust, headless]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "--bare"
  - "--settings"
  - "disableAllHooks"
  - "CLAUDE_PROJECT_DIR"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Command hooks execute shell commands with your full user permissions and can modify, delete or access anything your account can. Claude Code checks workspace trust before running any hook from a settings file.

# How to use it

- Interactive session: hooks from every settings file, including your own `~/.claude/settings.json`, are held back until you accept the workspace trust dialog for the folder (or a parent whose trust extends to it).
- `-p` or SDK session: no dialog is ever shown and the folder is treated as trusted, so hooks committed in a repository's `.claude/settings.json` run in a folder you never trusted.

Before scripting `claude -p` over a repository you did not write, review its `.claude/` settings files, start with `--bare`, or turn hooks off for the run with `--settings '{"disableAllHooks": true}'`. Frontmatter hooks in a project subagent follow a stricter rule than settings-file hooks.

Practices: validate and sanitize inputs; always quote shell variables (`"$VAR"`); block path traversal (check for `..`); use absolute paths (in exec form use `${CLAUDE_PROJECT_DIR}` with no quoting, in shell form wrap in double quotes); skip sensitive files (`.env`, `.git/`, keys).
