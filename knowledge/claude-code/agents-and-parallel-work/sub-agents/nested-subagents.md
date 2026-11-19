---
type: "Feature"
title: "Nested subagents and depth limit"
description: "Subagents can spawn subagents up to three layers deep by default; the depth is set with CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH."
resource: "https://code.claude.com/docs/en/sub-agents"
tags: [subagents, nesting, limits, depth]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sub-agents"
    resource: "https://code.claude.com/docs/en/sub-agents"
    title: "Create custom subagents"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

By default a subagent can spawn its own subagents up to three layers below the main conversation. At the limit the `Agent` tool is withheld from every subagent except a fork (which keeps it listed but errors), so a subagent at the limit works itself and returns one summary.

# How to use it

Set the layer count: `{"env": {"CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH": "2"}}` caps at two layers; `1` turns nesting off. To stop one subagent spawning, omit `Agent` from its `tools` or add it to `disallowedTools`. Nested subagents are defined in the same scopes as top-level ones and default to the spawner's model.

# Limits and defaults

- Interactive terminal: only the top-level subagent's summary returns to you (a subagent that launches background subagents waits for them).
- `claude -p` and the Agent SDK: the spawner waits only for a foreground nested subagent; a background nested one reports to the main conversation if it outlasts the spawner.
- The terminal subagent panel shows a tree with a `(+N)` descendant count per row.
