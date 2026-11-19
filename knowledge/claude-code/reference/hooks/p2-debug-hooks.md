---
type: "Guide"
title: "Debugging hooks"
description: "Where hook execution is logged (--debug, --debug-file), the log line format for timing, and verbose matcher logging."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, debugging, logs, timing]
kind: "cli_flag"
maturity: "unlabelled"
since: "2.1.296"
surfaces: [cli]
requires: ""
identifiers:
  - "--debug"
  - "--debug-file"
  - "CLAUDE_CODE_DEBUG_LOG_LEVEL"
  - "~/.claude/debug/<session-id>.txt"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Hook execution details go to the debug log file. `--debug` does not print to the terminal.

# How to use it

- `claude --debug-file <path>` writes the log to a known location.
- `claude --debug` writes to `~/.claude/debug/<session-id>.txt`.
- Entries look like `Hook output does not start with {, treating as plain text` and `Hook PostToolUse:Write (PostToolUse) success:` plus the output.
- To find slow hooks, search for `Hooks:` lines ending in a duration. In v2.1.296 or later each command hook on a tool event, `UserPromptSubmit`, `SessionStart`, `Stop` and several other events leaves one when it finishes: event name, a colon, the matched tool name or value, the command in brackets, the plugin if any, how it ended and the time, e.g. `Hooks: PostToolUse:Write [.claude/hooks/log-write.sh] finished with status 0 (31ms)`.
- Possible endings: `timed out after <N>ms`, `cancelled`, `moved to the background`, `failed to start`.
- Set `CLAUDE_CODE_DEBUG_LOG_LEVEL=verbose` for extra lines such as matcher counts and query matching.

# Limits and defaults

- On some events, such as `Notification`, `SessionEnd` and `PreCompact`, a command hook leaves a `completed with status` line without a duration.
- Further troubleshooting (hooks not firing, Stop hooks that keep blocking, config errors) is in the hooks guide; `/context`, `/doctor` and settings precedence are in the debug-your-config page.
