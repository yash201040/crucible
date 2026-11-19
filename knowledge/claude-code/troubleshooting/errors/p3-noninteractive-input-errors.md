---
type: "Reference"
title: "Non-interactive and stdin input errors"
description: "Errors for claude -p / stream-json input: missing prompt, whitespace-only prompt, 256M no-newline stream, no keyboard, disk full on transcript save."
resource: "https://code.claude.com/docs/en/errors"
tags: [errors, headless, stream-json, stdin, transcripts]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "--print"
  - "-p"
  - "--input-format stream-json"
  - "--output-format"
  - "--continue"
  - "--resume"
  - "CLAUDE_CODE_TMPDIR"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "errors"
    resource: "https://code.claude.com/docs/en/errors"
    title: "Error reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Errors a script or harness hits when driving `claude` non-interactively or through stdin.

# How to use it

| Message | When | Fix |
|---|---|---|
| `Input must be provided either through stdin or as a prompt argument when using --print` | `-p` with no prompt and nothing piped; also bare `claude` when stdout is redirected or the console is not a real terminal (it falls back to non-interactive mode) | Pass the prompt: `claude -p "q"` or `echo "q" \| claude -p` |
| `Input contained only whitespace` | Prompt of only spaces/tabs/newlines. For `claude -p`: exits with `Error: Input contained only whitespace. Provide a prompt ...`. For a running `--input-format stream-json` or Agent SDK session: turn ends without calling the model, session stays usable, result text `Blank prompt — the message was only whitespace, so nothing was sent to the model.` | Send visible text. Before v2.1.229 the API rejected it with a 400 |
| `stream-json input carried over 256M characters with no newline` | More than 268,435,456 characters on stdin with no newline to `claude -p --input-format stream-json`; stderr error, exit 1. Before v2.1.257 input was buffered without limit | Each message must be one newline-terminated JSON line; for plain text drop `--input-format stream-json` |
| `Claude Code can't read the keyboard here` | Interactive `claude` (no `-p`) with stdin not a terminal. Windows: prints the message, exit 1. macOS/Linux: reads `/dev/tty` and starts, using piped text as first prompt; message only if `/dev/tty` cannot be opened. Before v2.1.287 it started and failed with `Raw mode is not supported` | Add `-p`; works with `--continue` and `--resume <session-id>` (example: `type notes.md \| claude -p --continue`) |
| `Claude Code could not save all of this session's transcript under ... because the disk is full (ENOSPC)` | Disk full or quota used up (`EDQUOT`) during `claude -p`. Text and `json` output: exit 1 (answer already printed). `stream-json`: usual exit code, answer still arrives | Free space before the next run; resuming may miss part of the conversation |

# Limits and defaults

- stream-json no-newline budget: 268,435,456 characters (shown as `256M`).

# Notes

Related: the startup temp directory `claude-<uid>` can be overridden with `CLAUDE_CODE_TMPDIR`; see [startup and config file errors](./p3-startup-and-config-file-errors.md).
