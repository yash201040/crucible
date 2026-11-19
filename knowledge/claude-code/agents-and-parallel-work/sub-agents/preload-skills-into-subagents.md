---
type: "Feature"
title: "Preloading skills into subagents"
description: "The skills field injects full skill content into a subagent's context at startup, up to 32 names."
resource: "https://code.claude.com/docs/en/sub-agents"
tags: [subagents, skills, context]
kind: "frontmatter"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "skills"
  - "disable-model-invocation"
  - "context: fork"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sub-agents"
    resource: "https://code.claude.com/docs/en/sub-agents"
    title: "Create custom subagents"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The `skills` list injects the full content of each named skill into the subagent's context at startup, giving domain knowledge without discovery.

# How to use it

```yaml
skills:
  - api-conventions
  - error-handling-patterns
```

# Limits and defaults

- Up to the first 32 distinct names are preloaded.
- The field controls preloading, not access: without it the subagent can still invoke project, user and plugin skills via the Skill tool. To block skill use, omit `Skill` from `tools` or add it to `disallowedTools`.
- Skills with `disable-model-invocation: true` cannot be preloaded (includes the bundled `/verify` skill).
- Missing or disabled skills are skipped with a debug-log warning.

# Notes

Inverse of a skill with `context: fork`: with `skills`, the subagent controls the system prompt and loads skill content; with `context: fork`, skill content is injected into the named agent. Both start without conversation history.
