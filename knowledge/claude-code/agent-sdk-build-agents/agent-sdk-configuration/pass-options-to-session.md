---
type: "Feature"
title: "Pass options to a session"
description: "Every query() accepts an Options (TypeScript) or ClaudeAgentOptions (Python) object; allowedTools pre-approves rather than restricts."
resource: "https://code.claude.com/docs/en/agent-sdk/configuration"
tags: [options, query, allowed-tools, configuration]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "Options"
  - "ClaudeAgentOptions"
  - "model"
  - "allowedTools"
  - "allowed_tools"
  - "maxTurns"
  - "max_turns"
  - "cwd"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-configuration"
    resource: "https://code.claude.com/docs/en/agent-sdk/configuration"
    title: "Configure your agent"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A session reads configuration from settings files, environment variables and the options object. Each field is optional; with no options the session uses SDK defaults. Full types and defaults are in the TypeScript `Options` and Python `ClaudeAgentOptions` references.

# How to use it

Example fields (TypeScript / Python): `model`, `allowedTools` / `allowed_tools`, `maxTurns` / `max_turns`, `cwd`. Example: `model: "claude-sonnet-5"`, `allowedTools: ["Read","Glob","Grep"]`, `maxTurns: 8`, `cwd: "/path/to/repo"`. The final output is the result message (`type === "result"`, `subtype === "success"`, `is_error` false).

# Limits and defaults

`allowedTools` pre-approves the listed tools so calls run without stopping for approval. Tools outside the list stay available; for an unlisted tool the permission mode decides whether the call runs.
