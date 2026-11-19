---
type: "Guide"
title: "Set environment variables in a shell or settings file"
description: "How to set Claude Code environment variables per shell session or through the env key of a settings file, and which file reaches whom."
resource: "https://code.claude.com/docs/en/env-vars"
tags: [env, settings, configuration, shell]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "env"
  - "~/.claude/settings.json"
  - ".claude/settings.json"
  - ".claude/settings.local.json"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "env-vars"
    resource: "https://code.claude.com/docs/en/env-vars"
    title: "Environment variables"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Two ways to set a variable. A shell variable lasts for that terminal session. A variable under the `env` key of a `settings.json` applies every time `claude` runs, however it was launched.

# How to use it

Shell (set before launching `claude`):
- macOS, Linux, WSL: `export API_TIMEOUT_MS="1200000"` (persist in `~/.bashrc` or `~/.zshrc`).
- PowerShell: `$env:API_TIMEOUT_MS = "1200000"`; persist with `[Environment]::SetEnvironmentVariable("API_TIMEOUT_MS", "1200000", "User")`.
- CMD: `set API_TIMEOUT_MS=1200000`; persist with `setx`.

Settings file:

```json
{ "env": { "API_TIMEOUT_MS": "1200000", "BASH_DEFAULT_TIMEOUT_MS": "300000" } }
```

| File | Applies to |
| :- | :- |
| `~/.claude/settings.json` | You, in every project |
| `.claude/settings.json` | Everyone in the project (checked in) |
| `.claude/settings.local.json` | You, this project only (gitignored when Claude Code saves to it; add to gitignore yourself if hand-made) |
| Managed settings | Whole organization, deployed by an admin |

# Limits and defaults

- Values are copied as written. No shell expands them, so `~` or `$HOME` stay literal. Write absolute paths, for example `"CLAUDE_CONFIG_DIR": "/home/you/.claude-work"`.
- A running session applies new or changed `env` values when the file is saved. Features that read variables once at startup (such as OpenTelemetry monitoring) keep startup values until relaunch.
- Removing a variable from the file does not unset it in a running session; it takes effect on the next launch.
- Shell variables are read only at startup.
