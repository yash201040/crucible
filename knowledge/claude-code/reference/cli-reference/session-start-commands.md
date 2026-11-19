---
type: "Reference"
title: "Core claude launch and print commands"
description: "The basic claude invocations: interactive start, one-shot -p queries, piping, continue, resume, update and install."
resource: "https://code.claude.com/docs/en/cli-reference"
tags: [cli, print-mode, resume, install]
kind: "cli_flag"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless]
requires: ""
identifiers:
  - "claude"
  - "claude \"query\""
  - "claude -p \"query\""
  - "claude -c"
  - "claude -c -p \"query\""
  - "claude -r \"<session>\" \"query\""
  - "claude update"
  - "claude install [version]"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "cli-reference"
    resource: "https://code.claude.com/docs/en/cli-reference"
    title: "CLI reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The top-level `claude` command forms for starting, piping, continuing and resuming sessions, and for updating the binary.

# How to use it

| Command | What it does |
| :- | :- |
| `claude` | Start an interactive session |
| `claude "query"` | Interactive session with an initial prompt |
| `claude -p "query"` | Query through the SDK, print the answer, exit |
| `cat file \| claude -p "query"` | Process piped content |
| `claude -c` | Continue the most recent conversation in the current directory |
| `claude -c -p "query"` | Continue via the SDK |
| `claude -r "<session>" "query"` | Resume a session by ID or name |
| `claude update` | Update to the latest version |
| `claude install [version]` | Install or reinstall the native binary; takes a version such as `2.1.118`, or `stable` or `latest` |

# Notes

A mistyped subcommand gets a closest-match suggestion (for example `Did you mean claude update?`) and exits without starting a session. `claude --help` does not list every flag.
