---
type: "Limit"
title: "Frontmatter portability outside Claude Code"
description: "claude.ai uploads, the Skills API and package_skill.py accept only six frontmatter fields and fail hard on others."
resource: "https://code.claude.com/docs/en/skills"
tags: [skills, frontmatter, claude-ai, skills-api]
kind: "limit"
maturity: "unlabelled"
since: ""
surfaces: [cli, web, cloud]
requires: ""
identifiers:
  - "package_skill.py"
  - "allowed-tools"
  - "compatibility"
  - "license"
  - "metadata"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "skills"
    resource: "https://code.claude.com/docs/en/skills"
    title: "Extend Claude with skills"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude Code accepts every frontmatter field. Claude.ai skill uploads, the Skills API and packaging with `package_skill.py` (from anthropics/skills) allow only `name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`. Enabling a personal skill for your claude.ai account (for Cowork, cloud and scheduled tasks) uploads it, so the same rules apply.

# Limits and defaults

Any other field causes a hard error, for example: `Unexpected key(s) in SKILL.md frontmatter: argument-hint. Allowed properties are: allowed-tools, compatibility, description, license, metadata, name`. Claude Code-only body features such as dynamic context injection do not function in claude.ai chat or via the API. Spec-only frontmatter loads in Claude Code unchanged.
