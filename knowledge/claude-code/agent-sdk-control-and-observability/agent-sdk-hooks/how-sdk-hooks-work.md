---
type: "Feature"
title: "How SDK hooks work"
description: "Hooks are callbacks fired on agent events; matching hooks receive input and return a decision object to allow, block, modify or add context."
resource: "https://code.claude.com/docs/en/agent-sdk/hooks"
tags: [hooks, callbacks, pretooluse, permissions]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "hooks"
  - "HookMatcher"
  - "HookCallback"
  - "options.hooks"
  - "settingSources"
  - "setting_sources"
  - "permissionDecision"
  - "permissionDecisionReason"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-hooks"
    resource: "https://code.claude.com/docs/en/agent-sdk/hooks"
    title: "Intercept and control agent behavior with hooks"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Hooks are callback functions run in response to agent events (a tool call, a session start, execution stopping). Uses: block dangerous operations, log and audit, transform inputs and outputs, require human approval, track session lifecycle.

Flow: (1) an event fires; (2) the SDK collects hooks registered for it, both callback hooks in `options.hooks` and shell command hooks from settings files when the matching `settingSources` / `setting_sources` entry is enabled (it is for default `query()` options); (3) matchers filter by the event's target (for example tool name), and hooks with no matcher run for every event of that type; (4) each callback receives the event input; (5) the callback returns an output object.

# How to use it

Register under the event name in `hooks`:

```
hooks={"PreToolUse": [HookMatcher(matcher="Write|Edit", hooks=[protect_env_files])]}      # Python
hooks: { PreToolUse: [{ matcher: "Write|Edit", hooks: [protectEnvFiles] }] }                // TypeScript
```

Keys are event names; values are arrays of matchers each holding an optional pattern and callbacks. The example denies Write/Edit to `.env` by returning `hookSpecificOutput` with `permissionDecision: "deny"`.

# Notes

- A `Write|Edit` matcher does not cover Bash: Claude writing `.env` via a Bash command does not fire the hook. To block Bash writes to a file, use the sandbox configuration.
- The example's `.env` check allows `C:\project\.env` on Windows because paths use backslashes.
