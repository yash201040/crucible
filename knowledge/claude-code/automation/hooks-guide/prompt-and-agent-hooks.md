---
type: "Feature"
title: "Prompt-based and agent-based hooks"
description: "type prompt hooks make a single model call returning ok/reason; type agent hooks (experimental) run a subagent with tools."
resource: "https://code.claude.com/docs/en/hooks-guide"
tags: [hooks, prompt-hooks, agent-hooks, stop-hook]
kind: "hook"
maturity: "experimental"
since: ""
surfaces: [cli, headless]
requires: ""
identifiers:
  - "type: prompt"
  - "type: agent"
  - "ok"
  - "reason"
  - "impossible"
  - "continueOnBlock"
  - "model"
  - "timeout"
  - "$ARGUMENTS"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks-guide"
    resource: "https://code.claude.com/docs/en/hooks-guide"
    title: "Automate actions with hooks"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Prompt hooks (`type: "prompt"`) send your prompt and the hook input to a Claude model for a judgment decision; the optional `model` field picks a more capable model. The model returns JSON `{"ok": true|false, "reason": "..."}`. Agent hooks (`type: "agent"`, labeled experimental, behavior and configuration may change; prefer command hooks for production) spawn a subagent that can read files, search code and use tools before deciding.

# How to use it

Handling of `"ok": false` for prompt hooks:

| Event | Result |
| --- | --- |
| `Stop`, `SubagentStop` | `reason` fed back so Claude keeps working; if the response sets `"impossible": true` the stop is allowed and the turn ends |
| `PreToolUse` | Call denied; by default the turn ends with the reason as a warning line. `continueOnBlock: true` returns the reason to Claude as the tool error so it can continue |
| `PostToolUse` | Turn ends with a warning by default; `continueOnBlock: true` feeds the reason back and continues |
| `PostToolBatch`, `UserPromptSubmit`, `UserPromptExpansion` | Turn ends, reason shown as a warning line |

Stop prompt hook: `{"type":"prompt","prompt":"Check if all tasks are complete. If not, respond with {\"ok\": false, \"reason\": \"what remains to be done\"}."}`. Agent hook example: `{"type":"agent","prompt":"Verify that all unit tests pass. Run the test suite and check the results. $ARGUMENTS","timeout":120}`.

# Limits and defaults

Agent hooks: `ok`/`reason` format, default timeout 60 seconds, up to 50 tool-use turns, no `impossible` field and no `continueOnBlock` field; on `ok: false` they behave like a prompt hook with `continueOnBlock: true` (so on `PreToolUse` and `PostToolUse` the turn continues). `$ARGUMENTS` is replaced with the hook's JSON input. Use prompt hooks when input data suffices, agent hooks when verifying against real codebase state.
