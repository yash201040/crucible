---
type: "Feature"
title: "includeGitInstructions"
description: "Controls whether Claude gets built-in commit/PR instructions and a git status snapshot, and when the snapshot is dropped in headless and SDK runs."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [settings, git, system-prompt, headless]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk, cloud]
requires: ""
identifiers:
  - "includeGitInstructions"
  - "CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS"
  - "--system-prompt"
  - "--system-prompt-file"
  - "--append-system-prompt"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude Code gives Claude two git context pieces: built-in instructions for writing commits and PRs (in the Bash tool description) and a git status snapshot (current branch, main branch, `git status` output, recent commits, read when the conversation starts). `includeGitInstructions` (any file, Boolean, default `true`) set to `false` leaves both out, for example when you use your own git workflow skills.

# How to use it

`{ "includeGitInstructions": false }`, or per session `CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS`, which takes precedence.

# Limits and defaults

- Cloud sessions never include the snapshot.
- `-p` runs lose the snapshot when you replace the system prompt with `--system-prompt` or `--system-prompt-file`, or run a custom agent with its own prompt (`--agent` or the `agent` setting). Outside bare mode, keep the snapshot by running without a custom agent and using `--append-system-prompt`.
- Agent SDK: a custom system prompt or custom main-thread agent drops the snapshot; with no system prompt the SDK's minimal default also starts without it. Outside bare mode, use the `claude_code` preset without a custom `agent`.
