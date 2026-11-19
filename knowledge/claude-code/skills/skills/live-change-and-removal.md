---
type: "Feature"
title: "Live skill edits and removing skills"
description: "Skill directories are watched for changes (except bare mode); /reload-skills for new top-level dirs; how to remove each kind of skill."
resource: "https://code.claude.com/docs/en/skills"
tags: [skills, reload, watch, remove]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "/reload-skills"
  - "/reload-plugins"
  - "/plugin uninstall <plugin-name>@<marketplace-name>"
  - "disableBundledSkills"
  - "user-invocable-only"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "skills"
    resource: "https://code.claude.com/docs/en/skills"
    title: "Extend Claude with skills"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude Code watches `~/.claude/skills/`, project `.claude/skills/` and `.claude/skills/` in `--add-dir` directories and picks up add, edit and remove within the session. Not in bare mode.

# How to use it

- A top-level skills directory that did not exist at session start is not watched: run `/reload-skills`, and again after each later change there.
- Watching covers `SKILL.md` text. For a skill folder that is also a plugin, changes to `.mcp.json`, `agents/` and `output-styles/` need `/reload-plugins`; `hooks/` too, except a mod's module file that reloads on its own.
- Remove: personal/project skill, delete its directory; enterprise skill, admin deletes it in the managed settings directory (e.g. `/etc/claude-code/.claude/skills/<skill-name>/` on Linux); plugin skill, disable or uninstall the plugin; claude.ai skill, turn it off on the account (deleting by hand re-downloads while enabled); bundled skill, set `disableBundledSkills` to `true` or `"off"` in `skillOverrides`.
- Keep but stop Claude invoking: `disable-model-invocation: true`, or `"user-invocable-only"` in `skillOverrides`.
