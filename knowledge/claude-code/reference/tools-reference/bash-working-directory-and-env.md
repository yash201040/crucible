---
type: "Feature"
title: "Bash tool: what persists between commands"
description: "Each Bash command is a separate process; working directory carries over under conditions, environment variables do not."
resource: "https://code.claude.com/docs/en/tools-reference#bash-tool-behavior"
tags: [bash, working-directory, environment, shell]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, sdk]
requires: ""
identifiers:
  - "Bash"
  - "CLAUDE_BASH_MAINTAIN_PROJECT_WORKING_DIR"
  - "CLAUDE_ENV_FILE"
  - "--add-dir"
  - "/add-dir"
  - "additionalDirectories"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "tools-reference"
    resource: "https://code.claude.com/docs/en/tools-reference"
    title: "Tools reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The Bash tool runs each command in a separate process.

# How to use it

- A `cd` in the main session carries over while the result stays inside the project directory or an additional working directory (`--add-dir`, `/add-dir`, `additionalDirectories`). Outside them, Claude Code resets to the project directory and appends `Shell cwd was reset to <dir>`. Subagent sessions never carry over directory changes.
- `CLAUDE_BASH_MAINTAIN_PROJECT_WORKING_DIR=1` makes every command start in the project directory.
- Environment variables do not persist (`export` is lost). To persist them set `CLAUDE_ENV_FILE` to a shell script before launch, or populate it with a SessionStart hook.
- Claude Code starts a non-interactive shell, sources `~/.zshrc` or `~/.bashrc`, and applies captured aliases, functions and options. Activate virtualenv or conda before launching.
