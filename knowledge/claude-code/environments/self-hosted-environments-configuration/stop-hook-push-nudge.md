---
type: "Guide"
title: "Stop hook that prompts sessions to push work"
description: "Reference Stop hook for runners that nudges Claude to commit and push, since the runner installs none."
resource: "https://code.claude.com/docs/en/self-hosted-environments-configuration"
tags: [self-hosted, stop-hook, git, push, resume]
kind: "hook"
maturity: "beta"
since: ""
surfaces: [cloud]
requires: "Self-hosted environments (Team or Enterprise); git identity and push credentials"
identifiers:
  - "Stop"
  - "~/.claude/hooks/stop-hook-nudge.sh"
  - "stop_hook_active"
  - "--configure-git"
  - "--push-outcome-on-release"
  - "CLAUDE_PROJECT_DIR"
  - "GIT_OPTIONAL_LOCKS"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "self-hosted-environments-configuration"
    resource: "https://code.claude.com/docs/en/self-hosted-environments-configuration"
    title: "Customize sessions in self-hosted environments"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Anthropic-hosted sessions run a `Stop` hook prompting Claude to commit and push; the runner installs none, so uncommitted work stays on the runner disk and the Create PR button in claude.ai/code stays inactive until the branch is on the remote. The page gives a reference implementation.

# How to use it

Merge a `hooks.Stop` entry (`type: command`, `timeout: 10`, command `"$CLAUDE_CONFIG_DIR/hooks/stop-hook-nudge.sh"`) into `~/.claude/settings.json` on the runner host and save the script as `~/.claude/hooks/stop-hook-nudge.sh` (executable); the runner seeds both into every session. The script reads the hook JSON on stdin, exits if `"stop_hook_active":true` (nudges once per turn), checks `$CLAUDE_PROJECT_DIR` for uncommitted changes (excluding `.claude/`) or unpushed commits, and prints `{"decision":"block","reason":"..."}`. Silent when not a git repo or no remote.

Prerequisites: a git identity (image `user.name`/`user.email` or `--configure-git`); push credentials (Anthropic-managed git or image config); for resumed sessions set `--push-outcome-on-release` on every runner in the environment.

# Limits and defaults

- Prompts at most once per turn; a failed push still ends the turn. A hook that exceeds `timeout` ends the turn with no prompt: raise it on large checkouts (the script's `git status` skips `core.fsmonitor`).
- Submodules: checks commit identity only; uncommitted submodule files and unpushed submodule commits are not caught. Older script copies lacking `GIT_OPTIONAL_LOCKS` should be replaced (now if the Bash sandbox is on).
- Hooks run outside the Bash sandbox; the script hardens git with `core.fsmonitor=` and `core.hooksPath=/dev/null` but the sandbox alone should not be relied on.

# Notes

In multi-repo sessions with `--capacity` above one or a `checkout` hook, `$CLAUDE_PROJECT_DIR` is the per-session directory, not a checkout.
