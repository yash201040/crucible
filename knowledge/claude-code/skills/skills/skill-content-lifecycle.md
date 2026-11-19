---
type: "Limit"
title: "Skill content lifecycle and compaction"
description: "Invoked skill content stays in context, is not re-read, and is re-attached after compaction within 5,000 tokens each and 25,000 combined."
resource: "https://code.claude.com/docs/en/skills"
tags: [skills, context, compaction, tokens]
kind: "limit"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers: []
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "skills"
    resource: "https://code.claude.com/docs/en/skills"
    title: "Extend Claude with skills"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

On invocation, the rendered `SKILL.md` enters the conversation as one message and stays across turns. Claude Code does not re-read the file later. The `allowed-tools` grant does not persist: it clears on your next message.

# How to use it

- Write guidance meant to apply throughout a task as standing instructions.
- Re-invoking with identical rendered content adds a short "already loaded" note; differing content (new arguments or new dynamic-context output) appends the full content again.
- A rule that must hold every time belongs in a hook (or the skill's `hooks` frontmatter), not prose.

# Limits and defaults

- Auto-compaction re-attaches the most recent invocation of each skill after the summary, keeping the first 5,000 tokens of each.
- Re-attached skills share a 25,000-token budget, filled from the most recently invoked skill, so older skills can be dropped after many invocations.
- Put the most important instructions near the top of `SKILL.md`; invoke again after compaction to restore full content.
- Keep the body concise: every line is a recurring token cost.
