---
type: "Feature"
title: "Restricting Claude's skill access"
description: "Deny the Skill tool or use Skill(name) allow and deny permission rules, including alias, nested and synced-skill matching."
resource: "https://code.claude.com/docs/en/skills"
tags: [skills, permissions, skill-tool, deny-rules]
kind: "tool"
maturity: "unlabelled"
since: "2.1.260"
surfaces: [cli]
requires: ""
identifiers:
  - "Skill"
  - "Skill(commit)"
  - "Skill(review-pr *)"
  - "Skill(deploy *)"
  - "Skill(anthropic-skills:pdf)"
  - "Skill(anthropic-skills *)"
  - "Skill(skill:deploy)"
  - "/init"
  - "/security-review"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "skills"
    resource: "https://code.claude.com/docs/en/skills"
    title: "Extend Claude with skills"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

By default Claude can invoke any skill without `disable-model-invocation: true`. A few built-in commands, including `/init` and `/security-review`, are available through the Skill tool; others such as `/compact` are not.

# How to use it

- Disable all skills: add `Skill` to deny rules in `/permissions`.
- Allow or deny specific skills: `Skill(name)` exact, `Skill(name *)` prefix with any arguments, e.g. allow `Skill(commit)`, `Skill(review-pr *)`; deny `Skill(deploy *)`. Adding allow rules does not limit Claude to those skills.
- Hide individual skills with `disable-model-invocation: true` (removes the skill from Claude's context). `user-invocable: false` alone does not stop Claude.

| Deny rule names | Example | Also blocks |
| :- | :- | :- |
| An alias | `Skill(review)` | bundled `/code-review` via `/review` |
| An unqualified name | `Skill(deploy)` | nested skill listed `apps/web:deploy` (before v2.1.260 not blocked) |
| A synced skill | `Skill(anthropic-skills:deploy)` | that skill when Claude Desktop delivers it as a plugin |
| Plugin form of a synced skill | `Skill(deploy:deploy)` | the synced skill |
| Parameter form | `Skill(skill:deploy)` | the skill by any of its names, including alias and display name |

# Limits and defaults

An `allow` rule matches only the skill's own name and the name in Claude's invocation. To approve synced skills use `Skill(anthropic-skills:pdf)` or `Skill(anthropic-skills *)`; `Skill(anthropic *)` does not cover them.
