---
type: "Feature"
title: "onFailure block for failing callbacks"
description: "By default a failing callback lets the action proceed with a warning; onFailure block makes the action blocked instead."
resource: "https://code.claude.com/docs/en/agent-sdk/hooks"
tags: [hooks, failure, security, fail-closed]
kind: "api"
maturity: "unlabelled"
since: "0.3.317"
surfaces: [sdk]
requires: "TypeScript Agent SDK v0.3.317 or later, or Python Agent SDK v0.2.177 or later"
identifiers:
  - "onFailure"
  - "on_failure"
  - "hook_callback_failed"
  - "SDKInformationalMessage"
  - "does not honor"
  - "did not register your hooks"
  - "failed; blocking because onFailure is \"block\""
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-hooks"
    resource: "https://code.claude.com/docs/en/agent-sdk/hooks"
    title: "Intercept and control agent behavior with hooks"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

On most events, if a callback throws or returns output failing validation, the action goes ahead and your app gets an `SDKInformationalMessage` warning with `tag` `hook_callback_failed` (Python: read `tag` from `SystemMessage.data`). So a crashing `PreToolUse` guard lets the call reach the normal permission flow. A callback that returns nothing (a path with no `return`) also counts as failing.

# How to use it

Set `onFailure: "block"` (TypeScript) or `on_failure="block"` (Python) on the matcher: `HookMatcher(matcher="Bash", hooks=[check_policy], on_failure="block")`. The tool result then includes `failed; blocking because onFailure is "block"` and Claude does not see your error text. Return `{}` when the callback has no opinion; a callback that catches its own error and returns `{}` is not failing, so let errors propagate from a guard.

# Limits and defaults

- `Stop`, `SubagentStop`, `TaskCompleted`, `TeammateIdle` ignore the option.
- `PermissionRequest`: the block counts only if it arrives before your `canUseTool` callback answers.
- `PostToolUse`: the tool already ran, so Claude receives the failure as feedback.
- A timeout with `"block"` also blocks `PreCompact`, `Elicitation`, `WorktreeCreate`.
- Startup errors with `"block"` (query fails, no prompt sent): Claude Code lacks support (error includes `does not honor`; update or remove the option), or the session was already running and did not register your hooks (error includes `did not register your hooks`; start a new session).
