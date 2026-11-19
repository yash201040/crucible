---
type: "Guide"
title: "Create your first skill"
description: "Minimal SKILL.md in ~/.claude/skills/<name>/ with frontmatter and an injected git diff, invoked by /name or automatically."
resource: "https://code.claude.com/docs/en/skills"
tags: [skills, skill-md, getting-started]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "SKILL.md"
  - "~/.claude/skills/<skill-name>/SKILL.md"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "skills"
    resource: "https://code.claude.com/docs/en/skills"
    title: "Extend Claude with skills"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A skill is a `SKILL.md` file: YAML frontmatter between `---` markers saying when to use it, plus markdown instructions. Create one when you keep pasting the same checklist or procedure, or a CLAUDE.md section has become a procedure. Unlike CLAUDE.md, a skill's body loads only when used. Skills follow the Agent Skills open standard (agentskills.io); Claude Code adds invocation control, subagent execution and dynamic context injection.

# How to use it

1. `mkdir -p ~/.claude/skills/summarize-changes`
2. Save `~/.claude/skills/summarize-changes/SKILL.md` with a `description:` line and a body. The example body contains the line `` !`git diff HEAD` ``, which Claude Code runs and replaces with output before Claude reads it.
3. Test: ask something matching the description ("What did I change?") or run `/summarize-changes`.

The directory name (or frontmatter `name`) becomes the command; `description` lets Claude decide when to load it.

# Notes

Custom commands are merged into skills: existing `.claude/commands/` files keep working and Claude can invoke them. Add `disable-model-invocation: true` to stop that, or convert to a skill directory to add supporting files. See [locations](./skill-locations.md) and [frontmatter](./skill-frontmatter-fields.md).
