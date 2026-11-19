---
type: "Reference"
title: "Subagent scopes and priority"
description: "Where subagent definitions live (managed, --agents, project, user, plugin), their priority order and discovery rules."
resource: "https://code.claude.com/docs/en/sub-agents"
tags: [subagents, scope, priority, plugins, managed]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "--agents"
  - ".claude/agents/"
  - "~/.claude/agents/"
  - "--add-dir"
  - "/add-dir"
  - "/doctor"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sub-agents"
    resource: "https://code.claude.com/docs/en/sub-agents"
    title: "Create custom subagents"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

When several subagents share a name, the higher-priority location wins.

# How to use it

| Location | Scope | Priority |
| :- | :- | :- |
| Managed settings (`.claude/agents/` inside the managed settings directory) | Organization-wide | 1 (highest) |
| `--agents` CLI flag | Current session | 2 |
| `.claude/agents/` | Current project | 3 |
| `~/.claude/agents/` | All your projects | 4 |
| Plugin `agents/` directory | Where plugin enabled | 5 (lowest) |

- Project subagents are found by walking up from the working directory to the repository root; the definition closest to the working directory wins on a name clash.
- `--add-dir` / `/add-dir` also loads that directory's `.claude/agents/`.
- Both `.claude/agents/` and `~/.claude/agents/` are scanned recursively; subfolders do not affect identity (only `name` does). Two files in the same tree with the same `name`: only one loads, by filesystem read order. `/doctor` reports such duplicates.
- Plugin `agents/` is also scanned recursively, but a subfolder becomes part of the scoped identifier: `agents/review/security.md` in plugin `my-plugin` registers as `my-plugin:review:security`.
- Plugin subagents appear in @-mention typeahead under their scoped name.

# Notes

- Plugin subagents ignore `hooks`, `mcpServers` and `permissionMode` for security. Copy the file into `.claude/agents/` or `~/.claude/agents/` if you need them, or ship hooks in the plugin's `hooks/hooks.json` and servers in `.mcp.json`.
- A subagent definition can be reused as an agent team teammate by naming the subagent type when spawning.
