---
type: "Guide"
title: "Per-directory skills"
description: "Place skills under .claude/skills/ in a subdirectory, or scope root skills with the paths frontmatter field."
resource: "https://code.claude.com/docs/en/large-codebases"
tags: [skills, monorepo, frontmatter, paths]
kind: "frontmatter"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - ".claude/skills/"
  - "SKILL.md"
  - "paths"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "large-codebases"
    resource: "https://code.claude.com/docs/en/large-codebases"
    title: "Set up Claude Code in a monorepo or large codebase"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Any subdirectory can define skills for its own stack under `.claude/skills/` (for example `packages/api/.claude/skills/api-testing/SKILL.md`, or `src/db/.claude/skills/` in a single tree). Commit them with the code. A skill loads on demand when Claude judges it relevant: working in `packages/api/` loads `api-testing`, in `packages/web/` loads `component-patterns`.

# How to use it

`SKILL.md` has frontmatter `name` and `description` (for example "Testing patterns for the API package. Use when writing or modifying tests in packages/api/.") followed by instructions.

The `paths` frontmatter field takes globs; Claude loads the skill only when working with matching files. Use it for a root-level skill that applies to certain files, such as migrations scoped to `**/migrations/**`.

# Notes

See [keeping skills discoverable](./skill-discoverability.md).
