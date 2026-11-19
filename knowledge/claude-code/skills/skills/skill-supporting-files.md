---
type: "Guide"
title: "Supporting files in a skill"
description: "A skill directory can hold reference files and scripts loaded on demand; keep SKILL.md under 500 lines."
resource: "https://code.claude.com/docs/en/skills"
tags: [skills, supporting-files, scripts, context]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "SKILL.md"
  - "reference.md"
  - "examples.md"
  - "scripts/"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "skills"
    resource: "https://code.claude.com/docs/en/skills"
    title: "Extend Claude with skills"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Skills can hold several files so `SKILL.md` stays focused: `SKILL.md` (required overview), reference docs and examples loaded when needed, and `scripts/` utilities that are executed, not loaded.

# How to use it

Link supporting files from `SKILL.md` and say what each contains and when to load it. Keep `SKILL.md` under 500 lines. Use `${CLAUDE_SKILL_DIR}` to reference bundled scripts. Skills can bundle scripts in any language; one example generates an interactive HTML codebase map via a Python script and `allowed-tools: Bash(python3 *)`.
