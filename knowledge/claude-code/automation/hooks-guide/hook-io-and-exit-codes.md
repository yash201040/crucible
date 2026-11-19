---
type: "Reference"
title: "Hook input, output, exit codes and JSON control"
description: "stdin JSON fields, exit 0 vs 2, structured hookSpecificOutput decisions, defer, and how multiple hooks combine."
resource: "https://code.claude.com/docs/en/hooks-guide"
tags: [hooks, exit-codes, json-output, decisions]
kind: "hook"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "session_id"
  - "cwd"
  - "hook_event_name"
  - "tool_name"
  - "tool_input"
  - "hookSpecificOutput"
  - "permissionDecision"
  - "permissionDecisionReason"
  - "additionalContext"
  - "decision"
  - "onFailure"
  - "defer"
  - "updatedInput"
  - "stop_hook_active"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks-guide"
    resource: "https://code.claude.com/docs/en/hooks-guide"
    title: "Automate actions with hooks"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Hooks talk to Claude Code through stdin, stdout, stderr and exit codes. Every event passes JSON on stdin with common fields `session_id` and `cwd` plus event-specific data (`PreToolUse`: `hook_event_name`, `tool_name`, `tool_input`, where Bash's `command` is the shell command; `UserPromptSubmit`: `prompt`; `SessionStart`: `source` of `startup`, `resume`, `clear`, `compact` or `fork`).

# How to use it

- Exit 0: no objection. From a `PreToolUse` hook the call still goes through the normal permission flow (exit 0 does not approve). For `UserPromptSubmit`, `UserPromptExpansion`, `SessionStart` and `PostModelSwitch`, plain-text stdout is added to Claude's context.
- Exit 2: block; stderr is the reason (feedback to Claude, shown to the user, or nothing, as with `ConfigChange` and `Elicitation`). Some events cannot be blocked (e.g. `SessionStart`: stderr shown, execution continues).
- Any other exit code with no valid JSON: the action proceeds on most events, unless the hook is one whose failure blocks (e.g. `onFailure: "block"`).
- Structured control: exit 0 and print JSON. Use exit 2 or JSON per hook, not both. Example `PreToolUse` deny: `{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"..."}}`; `"ask"` shows the normal prompt; `"allow"` skips the interactive prompt but deny and ask rules (including enterprise managed deny lists) and prompts for network-path reads, MCP tools marked `requiresUserInteraction`, Agent SDK `always_ask` tools and org-`ask` connector tools still apply.
- `"defer"` is available only in `-p` mode: it ends the turn with the tool call preserved so an SDK wrapper can collect input and resume.
- `PreModelSwitch` uses `permissionDecision`: `allow` proceeds, `deny` cancels, `ask` confirms only for interactive `/model` (a refusal elsewhere).
- Other decision shapes: `PostToolUse` and `Stop` use top-level `decision: "block"`; `PermissionRequest` uses `hookSpecificOutput.decision.behavior`. `UserPromptSubmit` injects text via `hookSpecificOutput.additionalContext`; a top-level `additionalContext` is silently ignored.

# Limits and defaults

When several hooks match one event, every command runs to completion before results merge; a `deny` does not stop sibling hooks' side effects. For `PreToolUse` permission decisions the most restrictive wins in order `deny`, `defer`, `ask`, `allow`; `additionalContext` from all hooks is kept and passed together. When multiple `PreToolUse` hooks return `updatedInput`, rewrites are not merged and which one the tool runs with is not guaranteed.
