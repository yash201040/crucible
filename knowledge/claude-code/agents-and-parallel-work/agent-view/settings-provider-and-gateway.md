---
type: "Concept"
title: "Settings, provider and LLM gateway in background sessions"
description: "Which settings, environment, PATH, provider variables and gateway endpoints reach a background session."
resource: "https://code.claude.com/docs/en/agent-view"
tags: [agent-view, gateway, provider, environment]
kind: "behavior"
maturity: "research-preview"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "ANTHROPIC_BASE_URL"
  - "ANTHROPIC_CUSTOM_HEADERS"
  - "CLAUDE_CODE_USE_BEDROCK"
  - "CLAUDE_CODE_USE_VERTEX"
  - "CLAUDE_CODE_EXTRA_BODY"
  - "ANTHROPIC_VERTEX_BASE_URL"
  - "CLAUDE_CODE_SKIP_VERTEX_AUTH"
  - "ANTHROPIC_MODEL"
  - "claude respawn <id>"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-view"
    resource: "https://code.claude.com/docs/en/agent-view"
    title: "Manage multiple agents with agent view"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A background session reads settings from the directory it runs in, as if `claude` started there with the carried-over flags; project `env` values (for example `ANTHROPIC_MODEL`) apply to every session there. It runs with the `PATH` of the dispatching shell and keeps that shell's provider selection (`CLAUDE_CODE_USE_BEDROCK`, `CLAUDE_CODE_USE_VERTEX`), its `ANTHROPIC_DEFAULT_*_MODEL` aliases and any exported `CLAUDE_CODE_EXTRA_BODY`.

# How to use it

For an LLM gateway, put the variables in a settings file `env` block (not only the shell). A shell-exported `ANTHROPIC_BASE_URL`, with `ANTHROPIC_CUSTOM_HEADERS` and credential, reaches a session only when the supervisor itself started from a shell exporting the same gateway, and only when you: background with `←`/`/background`; dispatch into the current directory; wake a stopped session in the current directory by attach/reply; or run `claude respawn`. Gateways in front of a cloud provider forward as endpoint-plus-auth-bypass pair, for example `CLAUDE_CODE_USE_VERTEX=1` with `ANTHROPIC_VERTEX_BASE_URL` and `CLAUDE_CODE_SKIP_VERTEX_AUTH=1`.

# Limits and defaults

A forwarded gateway applies only to that session's running process and is never written to disk. Since v2.1.174 sessions do not inherit gateway variables from the supervisor's launch shell.
