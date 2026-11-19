---
type: "Guide"
title: "Auto-approve permission prompts with a hook"
description: "A PermissionRequest hook returns a JSON allow decision, with updatedInput for interactive tools and setMode via updatedPermissions."
resource: "https://code.claude.com/docs/en/hooks-guide"
tags: [hooks, permissionrequest, permissions, plan-mode]
kind: "hook"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "PermissionRequest"
  - "ExitPlanMode"
  - "hookSpecificOutput.decision.behavior"
  - "updatedInput"
  - "updatedPermissions"
  - "setMode"
  - "bypassPermissions"
  - "permissions.disableBypassPermissionsMode"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks-guide"
    resource: "https://code.claude.com/docs/en/hooks-guide"
    title: "Automate actions with hooks"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`PermissionRequest` hooks run when Claude Code is about to ask for permission. If the hook writes JSON with `"behavior": "allow"`, Claude Code answers for you. Auto-approval needs a JSON decision on stdout, not an exit code. For a tool that requires user interaction, such as `ExitPlanMode`, the allow also needs `updatedInput` or Claude Code ignores it and still prompts.

# How to use it

Matcher `ExitPlanMode`, command: `jq -c '{hookSpecificOutput: {hookEventName: "PermissionRequest", decision: {behavior: "allow", updatedInput: .tool_input}}}'`. On approval Claude Code exits plan mode and restores the mode active before plan mode; the transcript shows "Allowed by PermissionRequest hook". The hook path always keeps the current conversation (it cannot clear context for a fresh implementation session as the dialog can).

To set a mode, add `updatedPermissions: [{type: "setMode", mode: "acceptEdits", destination: "session"}]` (mode is any permission mode; `session` applies for this session only).

# Limits and defaults

- `bypassPermissions` applies only if bypass mode was already available at start (`--dangerously-skip-permissions`, `--permission-mode bypassPermissions`, `--allow-dangerously-skip-permissions`, or `permissions.defaultMode: "bypassPermissions"` in user, `--settings` or managed settings). Not if `permissions.disableBypassPermissionsMode` is set or the session started in restricted mode. It is never saved as `defaultMode`.
- Keep the matcher narrow: `.*` or an empty matcher would auto-approve every prompt, including writes and shell commands.
