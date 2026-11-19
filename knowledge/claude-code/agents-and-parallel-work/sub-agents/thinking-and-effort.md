---
type: "Feature"
title: "Thinking and effort in subagents"
description: "Subagents inherit extended thinking; effort comes from the effort field, a per-invocation parameter or the session level."
resource: "https://code.claude.com/docs/en/sub-agents"
tags: [subagents, effort, thinking, model]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.292"
surfaces: [cli]
requires: ""
identifiers:
  - "effort"
  - "CLAUDE_CODE_EFFORT_LEVEL"
  - "/effort"
  - "--effort"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sub-agents"
    resource: "https://code.claude.com/docs/en/sub-agents"
    title: "Create custom subagents"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Subagents inherit the main conversation's extended thinking configuration; there is no per-subagent thinking setting. Effort can be set per subagent.

# How to use it

- Set the `effort` frontmatter field.
- Claude can also pass an `effort` parameter for one non-fork invocation; it overrides the field and persists across resume. Requires v2.1.292 or later.
- `CLAUDE_CODE_EFFORT_LEVEL` takes precedence over both.

# Limits and defaults

With no field or parameter: on the main conversation's model the subagent runs at the session's level (from `/effort` or `--effort`); on another model the session level does not apply.
