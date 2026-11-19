---
type: "Limit"
title: "Hook limitations, timeouts and block cap"
description: "Default timeouts by hook type, SessionEnd budget, Stop block cap of eight, and behavior of hooks in -p mode."
resource: "https://code.claude.com/docs/en/hooks-guide"
tags: [hooks, timeouts, limits, stop-hook]
kind: "limit"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless]
requires: ""
identifiers:
  - "timeout"
  - "CLAUDE_CODE_STOP_HOOK_BLOCK_CAP"
  - "stop_hook_active"
  - "StopFailure"
  - "args"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks-guide"
    resource: "https://code.claude.com/docs/en/hooks-guide"
    title: "Automate actions with hooks"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Constraints for hook design. Command hooks speak only through stdout, stderr and exit codes and cannot trigger `/` commands or tool calls; `additionalContext` text becomes a system reminder Claude reads as plain text. `PostToolUse` hooks cannot undo actions.

# Limits and defaults

| Hook type | Default timeout (override with `timeout`, in seconds) |
| --- | --- |
| `command`, `http`, `mcp_tool` | 10 minutes; 30 seconds for `UserPromptSubmit`, `PreModelSwitch`, `PostModelSwitch`; 10 seconds for `MessageDisplay` |
| `prompt` | 30 seconds |
| `agent` | 60 seconds |
| `SessionEnd` (any type) | Shared 1.5-second budget; raised to match a longer per-hook `timeout`, up to 60 seconds |

- `PermissionRequest` hooks fire when Claude Code would ask or would auto-deny a call that cannot prompt. In `-p` mode they still run outside `dontAsk` mode, and a call that no hook decides and nothing else can answer is denied.
- `Stop` hooks fire whenever Claude finishes responding, not only at task completion; not on user interrupts; API errors fire `StopFailure` instead.
- Stop block cap: Claude Code overrides a Stop hook after it blocks eight times in a row with no tool call between, ending the turn with a warning. The script should check `stop_hook_active` in the input JSON and exit 0 if `true`. Raise the cap with `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP` if the hook legitimately needs more iterations.
