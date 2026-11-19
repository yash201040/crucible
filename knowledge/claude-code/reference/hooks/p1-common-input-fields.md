---
type: "Reference"
title: "Common hook input fields"
description: "JSON fields every hook receives on stdin or as POST body, plus agent identity fields and environment notes."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, input, json, reference]
kind: "api"
maturity: "unlabelled"
since: "2.1.257"
surfaces: [cli, ide, desktop, cloud]
requires: ""
identifiers:
  - "session_id"
  - "prompt_id"
  - "transcript_path"
  - "cwd"
  - "scratchpad_dir"
  - "permission_mode"
  - "effort"
  - "hook_event_name"
  - "agent_id"
  - "agent_type"
  - "model"
  - "from_model"
  - "to_model"
  - "tool_name"
  - "tool_input"
  - "tool_use_id"
  - "CLAUDE_EFFORT"
  - "ANTHROPIC_MODEL"
  - "CLAUDE_CODE_SUBPROCESS_ENV_SCRUB"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Fields added to every event's JSON, besides event-specific ones (`tool_name`, `tool_input`, `tool_use_id` for tool events).

# How to use it

| Field | Description |
| :- | :- |
| `session_id` | Current session identifier |
| `prompt_id` | UUID of the prompt being processed; matches `prompt.id` on OpenTelemetry events; absent until first user input |
| `transcript_path` | Path to conversation JSON; written asynchronously and may lag; use `last_assistant_message` on `Stop`/`SubagentStop` for the final text |
| `cwd` | Working directory at invocation |
| `scratchpad_dir` | Session scratchpad path; absent without scratchpad or temp dir; requires v2.1.257+ |
| `permission_mode` | `"default"`, `"plan"`, `"acceptEdits"`, `"auto"`, `"dontAsk"`, `"bypassPermissions"`; Manual mode arrives as `"default"`; not on all events |
| `effort` | Object with `level` (`"low"`, `"medium"`, `"high"`, `"xhigh"`, `"max"`); present on `PreToolUse`, `PostToolUse`, `Stop`, `SubagentStop` and other tool-context events, on models with effort; `$CLAUDE_EFFORT` holds the same level |
| `hook_event_name` | Event that fired |
| `agent_id` | Subagent or in-process teammate id |
| `agent_type` | Agent name (e.g. `"Explore"`, `"security-reviewer"`); present with `--agent` or inside a subagent; the subagent's type wins over `--agent` |

# Limits and defaults

- Only `SessionStart` hooks can receive `model`, and not always. `PreModelSwitch`/`PostModelSwitch` receive `from_model` and `to_model`; use `PostModelSwitch` to follow model changes.
- There is no `$CLAUDE_MODEL`. `$ANTHROPIC_MODEL` is read only if set in your shell and does not change on `/model`.
- On macOS/Linux command hooks run in their own session with no controlling terminal: no `/dev/tty`. Windows has none either. Use `systemMessage` or `terminalSequence`.
- The hook inherits the parent environment except `OTEL_*` exporter variables (removed from every subprocess), variables stripped when `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB=1`, and Anthropic credentials in HIPAA-configured sessions.
