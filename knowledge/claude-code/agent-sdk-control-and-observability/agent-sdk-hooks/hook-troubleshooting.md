---
type: "Guide"
title: "Hook troubleshooting"
description: "Fixes for hooks not firing, over-broad matchers, ignored modified input, Python session hooks, permission prompt multiplication and loops."
resource: "https://code.claude.com/docs/en/agent-sdk/hooks"
tags: [hooks, troubleshooting, subagents, python]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.227"
surfaces: [sdk]
requires: ""
identifiers:
  - "includeHookEvents"
  - "include_hook_events"
  - "max_turns"
  - "returned updatedInput that failed schema validation"
  - "returned updatedInput that the tool refused"
  - "SessionStart"
  - "SessionEnd"
  - "UserPromptSubmit"
  - "systemMessage"
  - "additionalContext"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-hooks"
    resource: "https://code.claude.com/docs/en/agent-sdk/hooks"
    title: "Intercept and control agent behavior with hooks"
stale_after: "2027-01-19T00:00:00Z"
---

# How to use it

| Symptom | Checks and fixes |
| - | - |
| Hook not firing | event name case-sensitive; matcher matches tool name exactly; hook under the right event key; `Stop` ignores matchers; hooks may not fire when the agent hits `max_turns` because the session ends first |
| Matcher not filtering | matchers match tool names only; filter paths inside the hook via `tool_input.file_path` |
| Tool blocked unexpectedly | look for `permissionDecision: "deny"` in all `PreToolUse` hooks; log `permissionDecisionReason`; empty matcher matches all tools; if the result says `returned updatedInput that failed schema validation` or `...that the tool refused`, include the unchanged `tool_input` fields because `updatedInput` replaces the whole input |
| Modified input not applied | `updatedInput` must be inside `hookSpecificOutput`; do not pair with `defer`; include `hookEventName` |
| Session hooks missing in Python | `SessionStart` and `SessionEnd` callbacks are TypeScript-only (Python `HookEvent` omits them); in Python use shell command hooks in settings files such as `.claude/settings.json` with `setting_sources=["project"]` (or the source holding the hooks); or trigger on the first message from `client.receive_response()` |
| Subagent permission prompts multiplying | each subagent may prompt separately; auto-approve with `PreToolUse` hooks or permission rules (subagents inherit them from the parent) |
| Recursive hook loops | a `UserPromptSubmit` hook that spawns subagents can loop if they trigger it; track subagent state in a shared variable or scope hooks to the top-level session |
| `systemMessage` missing | it shows to the user, not the model; on Claude Code v2.1.227 or later it can surface as an `SDKInformationalMessage` depending on the event; before v2.1.227 only `SessionStart` and `Setup` hook output surfaced in the stream, others only in lifecycle events added by `includeHookEvents` / `include_hook_events`; pass context to the model with `additionalContext`; log decisions separately if you need reliability |
