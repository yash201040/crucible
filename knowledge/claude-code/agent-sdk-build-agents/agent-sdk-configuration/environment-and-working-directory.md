---
type: "Feature"
title: "env option and working directory"
description: "How env replaces (TypeScript) or merges (Python) the subprocess environment, and how cwd and additionalDirectories scope file access."
resource: "https://code.claude.com/docs/en/agent-sdk/configuration"
tags: [env, cwd, isolation, directories]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "env"
  - "ANTHROPIC_BASE_URL"
  - "cwd"
  - "additionalDirectories"
  - "add_dirs"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-configuration"
    resource: "https://code.claude.com/docs/en/agent-sdk/configuration"
    title: "Configure your agent"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`env` sets environment variables for the Claude Code process running the session. `cwd` sets its working directory.

# How to use it

- TypeScript: `env` replaces the subprocess environment; spread `process.env` to keep `PATH`, `HOME`, `ANTHROPIC_API_KEY`.
- Python: values are merged over the inherited environment and override it.
- With `env` unset the subprocess inherits your environment in both languages.
- Example gateway: `ANTHROPIC_BASE_URL: "https://gateway.example.com"`.
- Variables can also configure Claude Code itself (see the Environment variables page). API timeout and stall detection tuning is under Handle slow or stalled API responses in each reference.
- `cwd` unset means the process's working directory. Neither SDK has a `cwd` setter: start another session with a different `cwd`. The working directory determines which project's settings and hooks load, where session skills are discovered, and which project a stored session belongs to.
- Extra file access outside the cwd: `additionalDirectories` (TypeScript) / `add_dirs` (Python); this grants file access, not configuration.
