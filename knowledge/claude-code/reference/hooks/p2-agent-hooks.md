---
type: "Feature"
title: "Agent-based hooks (type: agent)"
description: "Experimental hooks that spawn a subagent with tools (up to 50 turns) to verify a condition and return ok."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, agent-hooks, verification, experimental]
kind: "hook"
maturity: "experimental"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "agent"
  - "prompt"
  - "$ARGUMENTS"
  - "timeout"
  - "ok"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Agent hooks (`type: "agent"`) are like prompt hooks but with multi-turn tool access: Claude Code spawns a subagent with your prompt and the hook's JSON input, which can use Read, Grep, Glob and similar tools to inspect files or test output. The page labels them experimental: behavior and configuration may change, and for production workflows command hooks are preferred. They support the same events as prompt hooks, except `PermissionRequest`.

# How to use it

Set `"type": "agent"` and a `prompt` (use `$ARGUMENTS` for the hook input). Fields match prompt hooks, with no `continueOnBlock` and a 60-second default `timeout`. Example: a `Stop` hook with prompt "Verify that all unit tests pass. Run the test suite and check the results. $ARGUMENTS" and `"timeout": 120`.

The subagent returns `{ "ok": true }` or `{ "ok": false, "reason": "..." }`.

# Limits and defaults

- Up to 50 turns before the subagent returns its decision.
- On `ok: false`, Claude Code handles it like a prompt hook with `continueOnBlock: true` on that event (see [prompt hooks](./p2-prompt-hooks.md)). The prompt-hook `impossible` field is not supported.
- Default timeout 60 seconds.
