---
type: "Feature"
title: "Pre-approve tools for skills"
description: "Skills run with session tools; pre-approve them via skill allowed-tools frontmatter or the allowedTools option, unless managed settings forbid it."
resource: "https://code.claude.com/docs/en/agent-sdk/skills"
tags: [skills, permissions, allowed-tools, managed-settings]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "allowed-tools"
  - "allowedTools"
  - "allowed_tools"
  - "allowManagedPermissionRulesOnly"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-skills"
    resource: "https://code.claude.com/docs/en/agent-sdk/skills"
    title: "Extend agents with skills"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Skills run with the session's tools. To let a skill work without approval stops, pre-approve tools for a project or personal skill with its `allowed-tools` frontmatter or with the `allowedTools` (`allowed_tools` in Python) query option, for example `["Read", "Grep", "Glob"]`.

# Limits and defaults

- If the organization sets `allowManagedPermissionRulesOnly` in managed settings, Claude Code ignores both mechanisms.
- Skills synced from claude.ai follow their own frontmatter rules.
- The list pre-approves the named tools; it does not restrict others. The permission flow (modes, `canUseTool`) is on the Permissions page.
- In the stream a skill invocation appears as a Skill tool use.
