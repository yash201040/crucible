---
type: "Concept"
title: "Tools sets and allowedTools versus tools"
description: "Which built-in tool combinations give read-only, edit or full automation, and how allowedTools pre-approves rather than restricts."
resource: "https://code.claude.com/docs/en/agent-sdk/quickstart"
tags: [tools, permissions, allowed-tools, permission-modes]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "tools"
  - "allowedTools"
  - "permissionMode"
  - "acceptEdits"
  - "Read"
  - "Edit"
  - "Glob"
  - "Grep"
  - "Bash"
  - "WebSearch"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-quickstart"
    resource: "https://code.claude.com/docs/en/agent-sdk/quickstart"
    title: "Quickstart"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Tool lists control what the agent can do; permission modes control how much human oversight there is. The active mode is evaluated together with allow and deny rules in a fixed order (see the permissions docs).

# How to use it

| Tools | What the agent can do |
| - | - |
| `Read`, `Glob`, `Grep` | Read-only analysis |
| `Read`, `Edit`, `Glob` | Analyze and modify code |
| `Read`, `Edit`, `Bash`, `Glob`, `Grep` | Full automation |

To limit the built-in tools to one of these sets, pass the set as `tools`. Listing them in `allowedTools` instead only pre-approves them: the agent can still call other tools, subject to the permission mode. `permissionMode: "acceptEdits"` auto-approves file edits.
