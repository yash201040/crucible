---
type: "Feature"
title: "Skills through settingSources and the skills option"
description: "Skills are discovered from the filesystem; the skills option enables all, named or none; no programmatic registration."
resource: "https://code.claude.com/docs/en/agent-sdk/claude-code-features"
tags: [skills, setting-sources, skill-tool]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "skills"
  - "Skill"
  - "allowedTools"
  - "tools"
  - ".claude/skills/<name>/SKILL.md"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-claude-code-features"
    resource: "https://code.claude.com/docs/en/agent-sdk/claude-code-features"
    title: "Use Claude Code features in the SDK"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Skills are markdown files with specialized knowledge and invocable workflows, loaded on demand: the agent receives descriptions at startup and loads full content when relevant.

# How to use it

- Discovered via `settingSources`. If the `skills` option on `query()` is omitted, discovered user and project skills are enabled and the Skill tool is available (CLI behavior).
- `skills` accepts `"all"`, a list of skill names, or `[]` to disable all. When set, the SDK adds the Skill tool to `allowedTools` automatically; with an explicit `tools` list, include `"Skill"`.
- Example: `settingSources: ["user", "project"], skills: "all", allowedTools: ["Read", "Grep", "Glob"]`.

# Limits and defaults

Skills must be filesystem artifacts (`.claude/skills/<name>/SKILL.md`); the SDK has no programmatic API for registering skills.
