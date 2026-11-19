---
type: "Feature"
title: "Filesystem and programmatic hooks in the SDK"
description: "Two hook definition styles run side by side; callback return shape, hook types and TypeScript-only events."
resource: "https://code.claude.com/docs/en/agent-sdk/claude-code-features"
tags: [hooks, callbacks, settings, subagents]
kind: "hook"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "hooks"
  - "HookMatcher"
  - "hookSpecificOutput"
  - "permissionDecision"
  - "permissionDecisionReason"
  - "PreToolUse"
  - "SessionStart"
  - "SessionEnd"
  - "TeammateIdle"
  - "TaskCompleted"
  - "agent_id"
  - "agent_type"
  - "command"
  - "http"
  - "mcp_tool"
  - "prompt"
  - "agent"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-claude-code-features"
    resource: "https://code.claude.com/docs/en/agent-sdk/claude-code-features"
    title: "Use Claude Code features in the SDK"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Two ways to define hooks, running side by side:
- Filesystem hooks: defined in `settings.json`, loaded when `settingSources` includes the source. Types: `"command"` (shell), `"http"` (POST to endpoint), `"mcp_tool"` (call a connected MCP server's tool), `"prompt"` (LLM evaluates a prompt), `"agent"` (spawns a verifier agent). Fire in the main agent and its subagents.
- Programmatic hooks: callbacks passed to `query()` via `hooks` (Python `HookMatcher(matcher="Bash", hooks=[fn])`). Run in your process, return structured decisions, also fire inside subagents; the hook input carries `agent_id` and `agent_type`.

# How to use it

Return `{}` to allow. To block, return `hookSpecificOutput` with `hookEventName: "PreToolUse"`, `permissionDecision: "deny"`, `permissionDecisionReason`; the reason goes to Claude as the tool result. Python callback signature `(input_data, tool_use_id, context)`; `context` is reserved for future abort-signal support.

# Limits and defaults

The TypeScript SDK supports additional events beyond Python, including `SessionStart`, `SessionEnd`, `TeammateIdle`, `TaskCompleted`.
