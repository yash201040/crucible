---
type: "Feature"
title: "Skills in Cowork and cloud sessions"
description: "Cowork and cloud sessions, including cloud scheduled tasks, do not read ~/.claude/skills/; they load claude.ai account skills."
resource: "https://code.claude.com/docs/en/skills"
tags: [skills, cloud, cowork, scheduled-tasks]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cloud, desktop]
requires: ""
identifiers:
  - "~/.claude/skills/"
  - ".claude/skills/"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "skills"
    resource: "https://code.claude.com/docs/en/skills"
    title: "Extend Claude with skills"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Cowork and cloud sessions (including cloud scheduled tasks) do not read `~/.claude/skills/` on your machine. Interactive and scheduled Cowork sessions load skills enabled for your claude.ai account, synced at session start (manage at claude.ai/customize/skills/yours).

# How to use it

- A skill existing only in `~/.claude/skills/` is reported as not found when a cloud scheduled task invokes it, because each run starts as a fresh cloud session.
- For Cowork, cloud sessions and cloud threads in a project: enable the skill for your claude.ai account. In a project's cloud thread, skills committed to a repository's `.claude/skills/` are not available. Some self-hosted-environment sessions do not load account skills.
- For cloud sessions other than project threads: alternatively commit the skill to the repo's `.claude/skills/`. Plugins declared in the repo's `.claude/settings.json` and plugins enabled only in user settings do not load in cloud sessions.
- Desktop scheduled tasks run locally, so they do load `~/.claude/skills/`.
