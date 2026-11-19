---
type: "Guide"
title: "Sharing skills"
description: "Distribute skills via committed project .claude/skills/, plugins, or managed settings."
resource: "https://code.claude.com/docs/en/skills"
tags: [skills, sharing, plugins, managed-settings]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - ".claude/skills/"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "skills"
    resource: "https://code.claude.com/docs/en/skills"
    title: "Extend Claude with skills"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Three scopes for distributing skills.

# How to use it

- Project skills: commit `.claude/skills/` to version control.
- Plugins: add a `skills/` directory to a plugin.
- Managed: deploy organization-wide through managed settings (enterprise location).

Project skills committed to a repo also load when that repo is used in a Claude Tag channel. See [locations](./skill-locations.md).
