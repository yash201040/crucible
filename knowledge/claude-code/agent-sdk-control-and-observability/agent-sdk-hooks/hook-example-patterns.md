---
type: "Guide"
title: "Hook example patterns"
description: "Worked hook patterns: rewrite tool input, block with a reason, auto-approve read-only tools, parallel hooks, subagent tracking, webhooks, Slack."
resource: "https://code.claude.com/docs/en/agent-sdk/hooks"
tags: [hooks, examples, subagents, notifications, webhook]
kind: "behavior"
maturity: "unlabelled"
since: "0.2.139"
surfaces: [sdk]
requires: "permission_prompt notifications need TypeScript Agent SDK v0.3.233+ or Python Agent SDK v0.2.139+"
identifiers:
  - "updatedInput"
  - "permissionDecision"
  - "systemMessage"
  - "agent_transcript_path"
  - "stop_hook_active"
  - "permission_prompt"
  - "elicitation_complete"
  - "elicitation_response"
  - "plugin_notification"
  - "idle_prompt"
  - "auth_success"
  - "elicitation_dialog"
  - "$.ui.notify"
  - "canUseTool"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-hooks"
    resource: "https://code.claude.com/docs/en/agent-sdk/hooks"
    title: "Intercept and control agent behavior with hooks"
stale_after: "2027-01-19T00:00:00Z"
---

# How to use it

- Modify tool input: a `PreToolUse` hook on Write returns `updatedInput` with `file_path` prefixed `/sandbox`, plus `permissionDecision: "allow"`. Use a writable prefix such as `./sandbox` or `/tmp/sandbox` to test (macOS does not allow a root-level `/sandbox`).
- Add context and block: deny `file_path` starting `/etc` with `permissionDecision: "deny"` (reason for the model) and top-level `systemMessage` (shown to the user).
- Auto-approve: return `allow` for `Read`, `Glob`, `Grep`; reads from network paths are still checked; other tools keep normal checks.
- Multiple hooks: matching hooks run in parallel; the most restrictive permission result wins (one `deny` blocks). Completion order is non-deterministic, so make each hook independent.
- Track subagents: a `SubagentStop` hook reads `agent_id`, `agent_transcript_path`, `stop_hook_active` and the tool use ID.
- HTTP requests: hooks may do async work such as webhooks; catch errors inside the hook and pass the `signal` in TypeScript so the request cancels on timeout.
- Notifications to Slack: in SDK sessions `Notification` hooks run for `permission_prompt` (once a request has waited about six seconds on your `canUseTool` callback), `elicitation_complete`, `elicitation_response`, and `plugin_notification` (a mod calls `$.ui.notify`). Other types such as `idle_prompt`, `auth_success`, `elicitation_dialog` come from interactive UI SDK sessions do not run. Each carries `message` and optionally `title`.

# Limits and defaults

Notification hooks do not change agent behavior; return `{}`.
