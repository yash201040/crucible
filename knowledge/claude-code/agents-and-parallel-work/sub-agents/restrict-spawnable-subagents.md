---
type: "Feature"
title: "Restricting which subagents can be spawned"
description: "Agent(agent_type) allowlist syntax in tools for an agent running as the main thread with --agent; Task was renamed Agent in 2.1.63."
resource: "https://code.claude.com/docs/en/sub-agents"
tags: [subagents, spawning, allowlist, coordinator]
kind: "frontmatter"
maturity: "unlabelled"
since: "2.1.63"
surfaces: [cli]
requires: ""
identifiers:
  - "Agent(worker, researcher)"
  - "Agent"
  - "Task"
  - "--agent"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sub-agents"
    resource: "https://code.claude.com/docs/en/sub-agents"
    title: "Create custom subagents"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

An agent running as the main thread via `claude --agent` can restrict spawnable subagent types with `Agent(type, ...)` in `tools`.

# How to use it

```yaml
name: coordinator
tools: Agent(worker, researcher), Read, Bash
```

- Allowlist: only `worker` and `researcher` can be spawned; other types fail and the agent sees only the allowed types.
- `tools: Agent, Read, Bash` allows any subagent.
- Omit `Agent` entirely: the agent cannot spawn any subagent.
- To block specific agents but allow the rest use `permissions.deny` (`Agent(name)`).

# Limits and defaults

- The type list only applies to an agent running as the main thread with `claude --agent`. In a subagent definition, listing `Agent` lets it spawn subagents within the depth limit, but any type list in parentheses is ignored.
- Version 2.1.63 renamed the Task tool to Agent; existing `Task(...)` references still work as aliases.
