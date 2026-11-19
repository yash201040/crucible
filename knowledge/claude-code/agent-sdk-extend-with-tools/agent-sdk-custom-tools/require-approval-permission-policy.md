---
type: "Feature"
title: "Per-tool permission policy"
description: "In TypeScript, give an SDK MCP tool permission_policy always_ask or always_deny so allowedTools no longer approves it."
resource: "https://code.claude.com/docs/en/agent-sdk/custom-tools"
tags: [permissions, always-ask, canusetool, typescript]
kind: "setting"
maturity: "unlabelled"
since: "0.3.301"
surfaces: [sdk]
requires: "TypeScript Agent SDK v0.3.301 or later"
identifiers:
  - "permission_policy"
  - "always_ask"
  - "always_deny"
  - "canUseTool"
  - "permissionMode"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-custom-tools"
    resource: "https://code.claude.com/docs/en/agent-sdk/custom-tools"
    title: "Give Claude custom tools"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A `permission_policy` on a custom tool. `always_ask` stops `allowedTools` approving that tool's calls, so they can reach your `canUseTool` callback even though listed. `always_deny` blocks the tool. TypeScript-only; requires Agent SDK v0.3.301 or later.

# How to use it

Put the entry in a `tools` array on the config object `createSdkMcpServer()` returns (not the `tools` option passed into the function):

`mcpServers: { weather: { ...weatherServer, tools: [{ name: "get_temperature", permission_policy: "always_ask" as const }] } }` with `allowedTools`, `permissionMode: "default"` and a `canUseTool` callback.

# Limits and defaults

In `auto` or `plan` permission mode, the auto mode classifier can approve some `always_ask` calls, which then skip your callback. Set `destructiveHint: true` in the annotations to keep calls reaching the callback; an unset `destructiveHint` counts as `false` for `always_ask` calls, not `true`.
