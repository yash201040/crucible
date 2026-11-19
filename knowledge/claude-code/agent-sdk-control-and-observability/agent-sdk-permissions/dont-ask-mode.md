---
type: "Feature"
title: "Don't ask mode"
description: "dontAsk turns every would-be prompt into a denial without calling canUseTool; intended for headless agents."
resource: "https://code.claude.com/docs/en/agent-sdk/permissions"
tags: [permission-modes, dontask, headless, deny]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [sdk, headless]
requires: ""
identifiers:
  - "dontAsk"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-permissions"
    resource: "https://code.claude.com/docs/en/agent-sdk/permissions"
    title: "Configure permissions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Converts any permission prompt into a denial, without calling `canUseTool`. An installed mod can still approve some such calls. Tools pre-approved by `allowed_tools`, settings.json allow rules, or a hook run normally, as do calls needing no approval in `default` (file reads in working directories, `Agent`).

# How to use it

Pair with `allowedTools` for a hard-deny headless agent. Use when you run a headless agent and want a hard deny for each call that would otherwise prompt.

# Limits and defaults

Denied even when an allow rule matches:
- connector tools the organization set to `ask`
- tools needing user interaction: `AskUserQuestion`, MCP tools with `_meta["anthropic/requiresUserInteraction"]`
- custom tools with `permission_policy` `always_ask`
- reads from network paths
- recognized critical-path removals

A `PreToolUse` hook `allow` for a critical-path removal, a network-path read or an `always_ask` tool is still denied. The check that recognizes critical-path removals can miss some commands.
