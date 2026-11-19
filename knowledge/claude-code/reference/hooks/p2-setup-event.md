---
type: "Feature"
title: "Setup hook event"
description: "Fires only with --init-only, or --init/--maintenance under -p, for explicit one-time install or cleanup runs."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, setup, ci, init]
kind: "hook"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless]
requires: ""
identifiers:
  - "Setup"
  - "--init-only"
  - "--init"
  - "--maintenance"
  - "init"
  - "maintenance"
  - "trigger"
  - "--debug-file"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Setup fires only when Claude Code is launched with `--init-only`, or with `--init` or `--maintenance` in non-interactive mode (`-p`). It does not fire on normal startup. Use for one-time dependency installs or scheduled cleanup triggered from CI or scripts; use SessionStart for per-session init.

# How to use it

| Matcher | Fires on |
| :- | :- |
| `init` | `claude --init-only` or `claude -p --init` |
| `maintenance` | `claude -p --maintenance` |

- `claude --init-only` runs Setup hooks and `SessionStart` hooks with the `startup` matcher, then exits without a conversation. It prints nothing on success; check with `claude --debug-file <path> --init-only`.
- Starting or continuing with `-p` still needs a prompt (argument or stdin), unless a SessionStart hook supplies `initialUserMessage` or you resume a session with a deferred tool call.
- Input adds `trigger`: `"init"` or `"maintenance"`.

# Limits and defaults

- Cannot block; execution continues on any exit code. All JSON output fields (`systemMessage`, `continue`, `additionalContext`) are discarded.
- With `-p`, stdout, stderr and exit code appear only as `hook_response` events with `--output-format stream-json --verbose`.
- Only `type: "command"` hooks run; a `mcp_tool` hook on Setup is always skipped.
- Has access to `CLAUDE_ENV_FILE`.
- Because Setup does not run every launch, plugins needing dependencies should check on first use (for example test `${CLAUDE_PLUGIN_DATA}/node_modules`, run `npm install` on miss). Marketplace plugins may get eligible Node.js dependencies installed automatically when cached.
