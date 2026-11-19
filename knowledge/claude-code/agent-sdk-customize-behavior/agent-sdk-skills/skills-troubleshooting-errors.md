---
type: "Reference"
title: "Skills troubleshooting and name errors"
description: "Why SDK skills are not found or used, and the validation errors raised for invalid names in the skills list."
resource: "https://code.claude.com/docs/en/agent-sdk/skills"
tags: [skills, troubleshooting, errors, validation]
kind: "behavior"
maturity: "unlabelled"
since: "0.3.221"
surfaces: [sdk]
requires: ""
identifiers:
  - "settingSources: []"
  - "Invalid skill name \"docs:*\": wildcard-suffix names are not allowed; list each skill by its exact name."
  - "Skill names must be non-empty strings."
  - "ValueError"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-skills"
    resource: "https://code.claude.com/docs/en/agent-sdk/skills"
    title: "Extend agents with skills"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Checks for skills that do not load or run, and the pre-flight rejection of bad names.

# How to use it

| Symptom | Cause / fix |
| --- | --- |
| Skills not found | `settingSources`/`setting_sources` set explicitly without `user` and `project` (e.g. `[]`); `cwd` not at or below the directory with `.claude/skills/` in the same repo |
| Skill not used | Name missing from `skills` list (Skill tool returns the allowlist error) or vague `description`; dispatching `/<name>` works without listing |
| Invalid name | `query()` rejects the list before starting the Claude Code process |

Names rejected: empty, containing parentheses, commas or control characters, padded with whitespace, or wildcard forms (bare `*` or `:*` suffix).

# Limits and defaults

- TypeScript throws an `Error`; before TypeScript Agent SDK 0.3.221 the check did not run.
- Python raises `ValueError`; before Python Agent SDK 0.2.129 the check did not run.
- Empty name message: `Skill names must be non-empty strings` (Python without the period).
