---
type: "Reference"
title: "settingSources and what it loads"
description: "Which filesystem settings each setting source loads and the default of all three when omitted."
resource: "https://code.claude.com/docs/en/agent-sdk/claude-code-features"
tags: [setting-sources, settings, claude-md, skills]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "settingSources"
  - "setting_sources"
  - "cwd"
  - "additionalDirectories"
  - "add_dirs"
  - "--add-dir"
  - "~/.claude/"
  - ".claude/settings.json"
  - ".claude/settings.local.json"
  - "CLAUDE.local.md"
  - ".claude/rules/*.md"
  - ".claude/skills/"
  - ".claude/commands/"
  - ".claude/agents/"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-claude-code-features"
    resource: "https://code.claude.com/docs/en/agent-sdk/claude-code-features"
    title: "Use Claude Code features in the SDK"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`settingSources` (TypeScript) / `setting_sources` (Python) selects which filesystem settings the SDK loads. Omitting it equals `["user", "project", "local"]`, the same as the CLI. Pass `[]` to disable user, project and local settings and limit the agent to what you configure programmatically.

# How to use it

| Source | Loads | Location |
| :- | :- | :- |
| `"project"` | Project `settings.json` and hooks; CLAUDE.md and `.claude/rules/*.md`; project skills, commands, subagents | `<cwd>/.claude/` for settings and hooks; `<cwd>` and parents for CLAUDE.md and rules; `<cwd>` and parents up to the repo root for skills/commands/subagents, plus `.claude/skills/`, `.claude/commands/`, `.claude/agents/` of each `additionalDirectories`/`add_dirs` dir (passed as `--add-dir`) |
| `"user"` | User `settings.json`, CLAUDE.md, `~/.claude/rules/*.md`, skills, commands, subagents | `~/.claude/` |
| `"local"` | `CLAUDE.local.md`, `.claude/settings.local.json` | `<cwd>/.claude/` (settings.local.json can also load from the repo root inside a git repo); `<cwd>` and parents for CLAUDE.local.md |

`cwd` determines where project-level inputs are looked up; project `settings.json` loads from `<cwd>/.claude/` with no parent fallback.

# Notes

Example: `settingSources: ["user", "project"]` with `allowedTools: ["Read", "Edit", "Bash"]`.
