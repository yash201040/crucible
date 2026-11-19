---
type: "Reference"
title: "Common configuration mistakes and fixes"
description: "Symptom, cause and fix table for hooks, settings files, skills, CLAUDE.md, subagents, MCP config and Bash deny rules."
resource: "https://code.claude.com/docs/en/debug-your-config"
tags: [configuration, hooks, skills, mcp, settings]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.191"
surfaces: [cli]
requires: ""
identifiers:
  - "settings.json"
  - "settings.local.json"
  - "~/.claude/settings.json"
  - "~/.claude.json"
  - ".claude/skills/name/SKILL.md"
  - "disable-model-invocation"
  - "omitClaudeMd"
  - "SessionEnd"
  - ".mcp.json"
  - "mcpServers"
  - "claude mcp add --scope user"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "debug-your-config"
    resource: "https://code.claude.com/docs/en/debug-your-config"
    title: "Debug your configuration"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A lookup of frequent location and syntax mistakes. Check these before assuming a bug.

# How to use it

| Symptom | Cause | Fix |
| :- | :- | :- |
| Hook never fires | `matcher` is a JSON array | Single string with `\|`, e.g. `"Edit\|Write"` |
| Hook never fires | `,` separator before v2.1.191 | Use `\|` or upgrade |
| Hook never fires | lowercase tool name like `"bash"` | Matching is case-sensitive: `Bash`, `Edit`, `Write`, `Read` |
| Hook never fires | hooks in a standalone file | Put under `"hooks"` in `settings.json`; only plugins load `hooks/hooks.json` |
| Global permissions/hooks ignored | added to `~/.claude.json` | That file is app state and UI toggles; `permissions`, `hooks`, `env` go in `~/.claude/settings.json` |
| `settings.json` value ignored | same key in `settings.local.json` | Local overrides project, both override user settings |
| Skill missing in `/skills` | file at `.claude/skills/name.md` | Use `.claude/skills/name/SKILL.md` |
| Skill listed but never invoked | `disable-model-invocation: true` or poor description | A "user-only" badge means Claude will not trigger it |
| Subdirectory `CLAUDE.md` ignored | loads on demand | Ask Claude to read a file in that directory |
| Subagent ignores `CLAUDE.md` | built-in Explore and Plan agents skip it; custom subagents load it unless `omitClaudeMd` is set | Restate in the delegating prompt, remove `omitClaudeMd`, or put key rules in the agent body (its system prompt) |
| No cleanup at session end | no `SessionEnd` hook | Add one in `settings.json` |
| `.mcp.json` servers not loading | file under `.claude/`, or top-level `servers` key | Root `.mcp.json`, `mcpServers` key |
| `mcpServers` in `settings.json` ignored | key not read there | Use `.mcp.json` or `claude mcp add --scope user` |
| Project MCP server missing | approval prompt dismissed | `claude mcp reset-project-choices`, restart |
| MCP server fails from some directories | relative path | Absolute paths |
| MCP server lacks env vars | not set in config; Claude Code strips some variables | Per-server `env` in the `.mcp.json` entry |
| `Bash(rm *)` deny does not block `/bin/rm` | rules match the literal string | PreToolUse hook or sandbox |
