---
type: "Feature"
title: "Command hook fields: exec form and shell form"
description: "Command-hook fields (command, args, async, asyncRewake, shell, onFailure) and the difference between exec form and shell form."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, command, exec-form, shell]
kind: "frontmatter"
maturity: "unlabelled"
since: "2.1.295"
surfaces: [cli]
requires: ""
identifiers:
  - "command"
  - "args"
  - "async"
  - "asyncRewake"
  - "shell"
  - "onFailure"
  - "CLAUDE_PROJECT_DIR"
  - "CLAUDE_PLUGIN_ROOT"
  - "CLAUDE_PLUGIN_DATA"
  - "CLAUDE_PLUGIN_OPTION_<KEY>"
  - "${user_config.*}"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Command hooks add these fields to the common fields.

| Field | Required | What it does |
| :- | :- | :- |
| `command` | yes | Shell command, or with `args` the executable to spawn directly |
| `args` | no | Argument list; when present, exec form (no shell) |
| `async` | no | `true` runs in background without blocking |
| `asyncRewake` | no | `true` runs in background and wakes Claude on exit code 2; stderr (or stdout if stderr empty) is shown to Claude as a system reminder |
| `shell` | no | `"bash"` or `"powershell"`. Default bash, or powershell on Windows when Git Bash is missing. Does not need `CLAUDE_CODE_USE_POWERSHELL_TOOL`. Ignored when `args` is set |
| `onFailure` | no | `"continue"` or `"block"`; requires v2.1.295+. See [onFailure](./p1-onfailure-block-on-hook-failure.md) |

# How to use it

- **Exec form** (`args` present): `command` is resolved as an executable on `PATH` and spawned directly; each `args` element is one argument, no quoting, no shell. Path placeholders are substituted as plain strings into `command` and each `args` element. Example: `{"type":"command","command":"node","args":["${CLAUDE_PLUGIN_ROOT}/scripts/format.js","--fix"]}`.
- **Shell form** (`args` absent): the string goes to `sh -c` (macOS/Linux), Git Bash (Windows) or PowerShell if Git Bash is missing; pipes, `&&`, redirects, globs work. Set `shell` to choose.
- Both forms export `CLAUDE_PROJECT_DIR`, `CLAUDE_PLUGIN_ROOT`, `CLAUDE_PLUGIN_DATA` to the process.
- Plugin hooks substitute `${user_config.*}` in exec form only. A shell-form plugin hook referencing `${user_config.*}` fails with an error; read `$CLAUDE_PLUGIN_OPTION_<KEY>` (e.g. `$CLAUDE_PLUGIN_OPTION_WEBHOOK_URL`) or set `args`. Before v2.1.207, shell-form plugin hooks also substituted `${user_config.*}`.

# Limits and defaults

On Windows, exec form needs a real executable (`.exe`); `.cmd`/`.bat` shims (npm, npx, eslint in `node_modules/.bin`) cannot be spawned without a shell. Use `node` with the script path, or shell form. In exec form a bare `command` containing whitespace alongside `args` logs a warning (spawn will fail); absolute paths with spaces are fine.
