---
type: "Feature"
title: "Skills option and allowlist"
description: "The skills option of query() controls which discovered skills Claude may invoke: all, a list of names, or none."
resource: "https://code.claude.com/docs/en/agent-sdk/skills"
tags: [skills, sdk, allowlist, options]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "skills"
  - "\"all\""
  - "settingSources"
  - "setting_sources"
  - "additionalDirectories"
  - "add_dirs"
  - "Skill"
  - "Skill <name> is not in this session's skills allowlist"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-skills"
    resource: "https://code.claude.com/docs/en/agent-sdk/skills"
    title: "Extend agents with skills"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

In the SDK, skills are `SKILL.md` files on disk (for example `.claude/skills/<name>/SKILL.md`), discovered at startup from filesystem setting sources; full content loads when Claude invokes the skill. There is no programmatic API to register skills (unlike subagents, which have the `agents` option). Skills are model-invoked, and also user-invoked by sending `/<name>`.

# How to use it

| `skills` value | Effect |
| --- | --- |
| omitted | Discovered skills enabled and Skill tool available (matches CLI) |
| `"all"` | Claude may invoke every discovered skill (no wildcard syntax) |
| `["pdf", "docx"]` | Only the named skills |
| `[]` | Claude may invoke none |

- Names: your own skill = its directory name; plugin skill = `plugin:skill`; a skill from `additionalDirectories`/`add_dirs` with a clashing name gets a prefixed name (with `verify` in `../api` and `../web`, list `verify` and `web:verify`; needs Claude Code v2.1.309 or later).
- Setting `skills` adds the Skill tool to `allowedTools` automatically. With an explicit `tools` list, include `"Skill"`.
- Default `query()` options load user and project sources: `~/.claude/skills/`, `<cwd>/.claude/skills/` and parents up to the repo root, plus `<dir>/.claude/skills/` for each added directory (passed as `--add-dir`). If you set `settingSources` explicitly, include `'project'` and `'user'`, or use the `plugins` option.

# Limits and defaults

- Unlisted skills are invisible to the model and the Skill tool rejects them (`Skill <name> is not in this session's skills allowlist`), but files stay reachable via Read and Bash.
- Restricting the list does not restrict [dispatch by name](./commands-in-sdk-sessions.md).

# Notes

The init message `skills` array lists user-invocable skills with a `description` or `when_to_use` field, plus bundled skills; skills with `user-invocable: false` load but do not appear. The array is the same whether or not they are in your `skills` list.
