---
type: "Reference"
title: "Remote Control server startup errors"
description: "Errors from claude remote-control / claude rc: untrusted workspace, unanswered prompts, global flags not carried over, --settings file, removed sandbox flags."
resource: "https://code.claude.com/docs/en/errors"
tags: [errors, remote-control, startup, settings]
kind: "cli_flag"
maturity: "unlabelled"
since: "2.1.248"
surfaces: [cli]
requires: ""
identifiers:
  - "claude remote-control"
  - "claude rc"
  - "--spawn=same-dir"
  - "--spawn=worktree"
  - "--settings"
  - "--setting-sources"
  - "--permission-mode"
  - "--disallowed-tools"
  - "--mcp-config"
  - "--sandbox"
  - "--no-sandbox"
  - "sandbox.enabled"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "errors"
    resource: "https://code.claude.com/docs/en/errors"
    title: "Error reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Refusals when starting `claude remote-control` (alias `claude rc`), the server mode that starts sessions on request. Matters for scripts and services that launch it.

# How to use it

| Error | Cause | Fix |
|---|---|---|
| `Error: Workspace not trusted. Please run claude in <dir> first ...` (exit 1) | Directory untrusted and the command cannot ask (stdin/stdout not a terminal, small terminal). Before v2.1.284 it never asked. Answering `n` at `Trust <directory>?` prints `Remote Control did not start` | Run `claude` there and accept the trust dialog |
| Home directory variant | Trust for the home directory is never saved | Start from a project directory |
| `Remote Control did not start: "Enable Remote Control?" got no answer` | First-run question unanswered (script/service stdin ends) | Run once in a terminal as the service's user and answer `y` |
| `Remote Control did not start: "Choose [1/2] (default: 1):" got no answer` | Spawn-mode question unanswered | Pass `--spawn=same-dir` or `--spawn=worktree` |
| `` `--settings` before `remote-control` is not carried over ... `` | A global flag placed before the verb that would restrict or configure sessions (`--settings`, `--setting-sources`, `--permission-mode`, `--disallowed-tools`, `--mcp-config`) | Put options after the verb: `claude remote-control --settings <file>`, `claude remote-control --permission-mode <mode>` |
| `Remote Control did not start, because sessions would skip part or all of the --settings file` | Problem in the file (e.g. invalid JSON) | Fix the file |
| `Session failed: Error: The settings file ... has changed since Remote Control started` | `--settings` file edited while the server runs | Restart `claude remote-control`, or restore the file |
| `--sandbox is not supported by claude remote-control` / `--no-sandbox ...` | Both flags removed in v2.1.300 | Remove the flag; set `sandbox.enabled` to `true` in settings to sandbox sessions |

# Limits and defaults

- Harmless global flags are ignored rather than refused: `--verbose`, `--model`, wrapper-injected `--session-id` or `--plugin-dir`. An unrecognized newer global flag is refused until marked harmless.
- Before v2.1.248, own flags after a global flag failed with `unknown option`.

# Notes

Related unattended-run problem: `Skill usage reports` and `output-style` over Remote Control are in [command-specific errors](./p3-command-specific-errors.md).
