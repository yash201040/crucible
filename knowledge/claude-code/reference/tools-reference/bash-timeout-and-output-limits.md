---
type: "Limit"
title: "Bash timeout and output limits"
description: "Default and maximum foreground timeouts, inline output ceilings, read-back window and the settings that change them."
resource: "https://code.claude.com/docs/en/tools-reference#timeout-and-output-limits"
tags: [bash, timeout, output, limits, truncation]
kind: "limit"
maturity: "unlabelled"
since: "2.1.261"
surfaces: [cli, sdk, headless]
requires: ""
identifiers:
  - "BASH_DEFAULT_TIMEOUT_MS"
  - "BASH_MAX_TIMEOUT_MS"
  - "BASH_MAX_OUTPUT_LENGTH"
  - "bashOutputMaxChars"
  - "timeout"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "tools-reference"
    resource: "https://code.claude.com/docs/en/tools-reference"
    title: "Tools reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude passes a per-call `timeout` when it wants longer than the default; you never set one per command. Output streams to a working file; a command over 5 GB of output is killed.

# How to use it

| Name | Kind | Default | Effect |
| :- | :- | :- | :- |
| `BASH_DEFAULT_TIMEOUT_MS` | env | 2 minutes | Foreground default when Claude passes no timeout |
| `BASH_MAX_TIMEOUT_MS` | env | 10 minutes | Ceiling; effective ceiling is the larger of the two variables |
| `BASH_MAX_OUTPUT_LENGTH` | env | 30,000 chars | Characters read back from the working file; hard ceiling 150,000 |
| `bashOutputMaxChars` | setting | about 30,000 | Sizes inline ceiling and read-back window together, up to 128,000; then `BASH_MAX_OUTPUT_LENGTH` is ignored. Needs v2.1.261+ |

The PowerShell tool follows the same timeout rules and variables.

# Limits and defaults

- Valid result: inline up to roughly 30,000 characters; beyond that Claude gets the path of a file in the session directory (truncated past 64 MiB) plus a preview of up to the first 2,000 characters.
- Failure: inline up to roughly 10,000 characters, a head-and-tail excerpt cut from the read-back window, no file path.
- Exit code 1 counts as valid only for `grep`, `rg`, `egrep`, `fgrep`, `find`, `diff`, `test`, `[`, `git diff`, `git grep`. Other commands exiting 1 (such as `pgrep`, `jq -e`, `cmp`) count as failures.
- Raising `BASH_MAX_OUTPUT_LENGTH` does not raise the inline ceilings.
