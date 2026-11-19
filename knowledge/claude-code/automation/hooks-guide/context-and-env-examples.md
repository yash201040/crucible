---
type: "Guide"
title: "Examples: context, audit and environment hooks"
description: "SessionStart compact re-injection, ConfigChange audit log, and direnv reload via CwdChanged, SessionStart and FileChanged with CLAUDE_ENV_FILE."
resource: "https://code.claude.com/docs/en/hooks-guide"
tags: [hooks, sessionstart, configchange, cwdchanged, env-file]
kind: "hook"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: "direnv, devbox or nix for the environment example"
identifiers:
  - "SessionStart"
  - "compact"
  - "ConfigChange"
  - "user_settings"
  - "project_settings"
  - "local_settings"
  - "policy_settings"
  - "skills"
  - "CwdChanged"
  - "FileChanged"
  - "CLAUDE_ENV_FILE"
  - "watchPaths"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks-guide"
    resource: "https://code.claude.com/docs/en/hooks-guide"
    title: "Automate actions with hooks"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

- Re-inject context after compaction: a `SessionStart` hook with matcher `compact` whose stdout text (for example `echo 'Reminder: use Bun, not npm...'` or `git log --oneline -5`) is added to Claude's context. For every session start, CLAUDE.md is suggested instead.
- Audit configuration changes: `ConfigChange` fires when an external process or editor modifies a config file. The matcher filters `user_settings`, `project_settings`, `local_settings`, `policy_settings`, `skills`. Example appends `jq -c '{timestamp: now | todate, source: .source, file: .file_path}'` to `~/claude-config-audit.log`. To block a change, exit 2 or return `{"decision": "block"}`.
- Reload environment: `SessionStart` plus `CwdChanged` hooks each run `direnv export bash > "$CLAUDE_ENV_FILE"`; Claude Code runs `CLAUDE_ENV_FILE` as a preamble before each Bash command. Run `direnv allow` per directory; devbox/nix use `devbox shellenv`. `FileChanged` with a `matcher` like `.envrc|.env` watches specific files; the matcher is split into literal filenames, not a regex.

# How to use it

See `CwdChanged` and `FileChanged` reference entries for input schemas, `watchPaths` output and `CLAUDE_ENV_FILE` details.
