---
type: "Feature"
title: "Disabling specific subagents"
description: "Deny Agent(name) entries in permissions.deny or --disallowedTools to stop Claude using built-in or custom subagents."
resource: "https://code.claude.com/docs/en/sub-agents"
tags: [subagents, permissions, deny, fork]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless]
requires: ""
identifiers:
  - "permissions.deny"
  - "Agent(Explore)"
  - "Agent(my-custom-agent)"
  - "Agent(fork)"
  - "--disallowedTools"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sub-agents"
    resource: "https://code.claude.com/docs/en/sub-agents"
    title: "Create custom subagents"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Add `Agent(subagent-name)` (matching the `name` field) to `permissions.deny`; works for built-in and custom subagents.

# How to use it

```json
{"permissions": {"deny": ["Agent(Explore)", "Agent(my-custom-agent)"]}}
```

CLI equivalent: `claude --disallowedTools "Agent(Explore)"`. `Agent(fork)` stops only forks.
