---
type: "Reference"
title: "Command-line flag and argument errors"
description: "Startup errors for conflicting or invalid claude flags: --bg, --print, --agents, --json-schema, --settings, system prompt flag pairs."
resource: "https://code.claude.com/docs/en/errors"
tags: [errors, cli-flags, startup, headless]
kind: "cli_flag"
maturity: "unlabelled"
since: "2.1.198"
surfaces: [cli, headless]
requires: ""
identifiers:
  - "--bg"
  - "--background"
  - "--print"
  - "-p"
  - "--append-subagent-system-prompt"
  - "--append-subagent-system-prompt-file"
  - "--system-prompt"
  - "--system-prompt-file"
  - "--append-system-prompt"
  - "--append-system-prompt-file"
  - "--agents"
  - "--safe-mode"
  - "CLAUDE_CODE_SAFE_MODE"
  - "--json-schema"
  - "--settings"
  - "--restricted"
  - "claude agents"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "errors"
    resource: "https://code.claude.com/docs/en/errors"
    title: "Error reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Errors printed by `claude` at launch when flags conflict or a flag value is invalid. In most cases the process exits with code 1 and starts nothing.

# How to use it

| Error | Cause | Fix |
|---|---|---|
| `--bg and --print conflict ...` (needs v2.1.198+) | `--bg` combined with `-p`/`--print`; `--bg` starts a background session attachable via `claude agents`, `--print` never starts that interactive session. Before v2.1.198 this silently made an unattachable job. | Drop `-p`; use `claude --bg "<task>"`, or drop `--bg` and use `claude -p "<task>"` |
| `Couldn't tell whether --bg is a flag or text here` | `--bg`/`--background` placed where it is ambiguous; nothing started, exit 1 | Put it first: `claude --bg --name nightly-audit "<task>"` |
| `Cannot use both --append-subagent-system-prompt and --append-subagent-system-prompt-file` | Both forms passed; exit 1 | Keep one. Before v2.1.283 the same applied to `--system-prompt` + `--system-prompt-file` and `--append-system-prompt` + `--append-system-prompt-file` (now they combine) |
| `Error: Invalid --agents configuration:` | Bad `--agents` value; exit 1 (since v2.1.242; earlier the session started anyway) | Fix the listed problems |
| `--json-schema is not a valid JSON Schema` | Schema failed compilation in non-interactive mode; exit 1 (since v2.1.205) | Fix the keyword the diagnostic names |
| `Settings file exceeds the 2MiB limit` | File passed to `--settings` over 2 MiB (since v2.1.214) | Use a regular JSON file under 2 MiB |
| `Cloud sessions cannot be created from a --restricted session` | Cloud session requested from a `--restricted` session; refused client-side | Run locally, or start without `--restricted` |

`--agents` details:
- Checks run in order and stop at the first failure: (1) value starts with `{` but is not JSON, or file contents not JSON: one `invalid JSON:` line; (2) schema mismatch for CLI-defined subagents: one line per problem; (3) agent name starting with `-`: `<name>: agent names must not start with '-'`. Over 20 problem lines are cut to 20 plus `...and N more`.
- `--safe-mode` or `CLAUDE_CODE_SAFE_MODE` makes Claude Code ignore `--agents`.
- With `--resume`/`--continue`, inline JSON is not checked; a file value is checked on every launch.
- With `--print`, `--agents` also accepts a JSON file path (since v2.1.281; before, only inline JSON). Without `-p`: `Error: --agents takes a JSON object, or a file path only with --print (-p)`. A missing file: `Error: --agents file not found: <path>` (also appears when the shell mangled inline JSON, since a non-`{` value is read as a path).

`--json-schema`: `format` keyword is accepted as an annotation, not enforced. Two pre-checks: `Error: --json-schema is not valid JSON` and `Error: --json-schema must be a JSON object`.

`--settings`: a path that is not a regular file fails with `Cannot use settings file (Not a regular file (device, FIFO, or socket))`; a directory gives an `EISDIR` reason.

# Limits and defaults

- Settings file limit: 2 MiB.
- `--agents` error lines shown: 20.

# Notes

`--restricted` first appeared in v2.1.248; earlier versions reject it as an unknown option.
