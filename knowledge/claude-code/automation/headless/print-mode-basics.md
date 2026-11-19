---
type: "Feature"
title: "Non-interactive mode with -p"
description: "claude -p runs Claude Code non-interactively; exit codes, option conflicts and the Agent SDK relationship."
resource: "https://code.claude.com/docs/en/headless"
tags: [headless, print-mode, cli, exit-codes]
kind: "cli_flag"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "-p"
  - "--print"
  - "--bg"
  - "--cloud"
  - "--continue"
  - "--allowedTools"
  - "--output-format"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "headless"
    resource: "https://code.claude.com/docs/en/headless"
    title: "Run Claude Code programmatically"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The Agent SDK gives the same tools, agent loop and context management as Claude Code, as a CLI for scripts and CI/CD or as Python and TypeScript packages. `claude -p "<prompt>"` (or `--print`) runs non-interactively, e.g. `claude -p "Find and fix the bug in auth.py" --allowedTools "Read,Edit,Bash"`.

# How to use it

- Exit code 0 on success, non-zero when the run fails. An invalid flag is reported on stderr before the run starts; a failure inside the run (such as missing authentication) is printed as the result on stdout.
- Not every option combines with `-p`: Claude Code rejects `--bg`, and rejects `--cloud` with a task description, with an error naming the conflict. `--cloud` with a session ID plus `-p` instead queues a message into that cloud session and exits.
- Common companions: `--continue`, `--allowedTools`, `--output-format`.
- Stdin is read, so data can be piped: `cat build-error.txt | claude -p 'explain the root cause' > output.txt`.

# Limits and defaults

- Piped stdin is capped at 10MB; beyond that Claude Code exits with an error and non-zero status (write to a file and reference the path instead).
- If stdin cannot be read (the parent disconnected), a warning goes to stderr and the command-line prompt is used.
- With `--output-format json`, the payload includes `total_cost_usd` and a per-model cost breakdown. With `--continue` or `--resume` it reports the conversation's whole total. Both are client-side estimates and can differ from the bill.
- `-p` working-directory deletion: the session keeps running; a warning message appears in `stream-json` output when a turn starts and shell commands fail until the directory exists again.
