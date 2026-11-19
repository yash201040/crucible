---
type: "Reference"
title: "Project config files and when they load"
description: "Project-scope files (CLAUDE.md, .mcp.json, .worktreeinclude, settings, rules, skills, agents, workflows, output styles) with load timing and precedence."
resource: "https://code.claude.com/docs/en/claude-directory"
tags: [claude-directory, project, settings, load-timing]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "CLAUDE.md"
  - ".mcp.json"
  - ".worktreeinclude"
  - ".claude/settings.json"
  - ".claude/settings.local.json"
  - ".claude/rules/"
  - ".claude/skills/"
  - ".claude/commands/"
  - ".claude/output-styles/"
  - ".claude/agents/"
  - ".claude/workflows/"
  - "CLAUDE_CONFIG_DIR"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "claude-directory"
    resource: "https://code.claude.com/docs/en/claude-directory"
    title: "Explore the .claude directory"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude Code reads instructions, settings, skills, subagents and memory from the project directory and `~/.claude`. Commit project files to share with the team; `~/.claude` is personal. On Windows `~/.claude` is `%USERPROFILE%\.claude`; if `CLAUDE_CONFIG_DIR` is set, every `~/.claude` path (and `.claude.json`) lives under it instead.

# How to use it

| File | When it loads | Notes |
| - | - | - |
| `CLAUDE.md` | Session start | Project instructions. `AGENTS.md` can be read in its place |
| `.mcp.json` | Approved servers load at session start in interactive sessions; tool schemas are deferred and load on demand via tool search | Project-scoped MCP servers for the team; personal ones go in `~/.claude.json` |
| `.worktreeinclude` | When a git worktree is created via `--worktree`, the `EnterWorktree` tool, or subagent `isolation: worktree` | Gitignored files to copy into each new worktree (`.gitignore` syntax; must match a pattern and be gitignored) |
| `.claude/settings.json` | Session start; most edits apply to the running session | Permissions and hooks are enforced, unlike CLAUDE.md. Ranks above `~/.claude/settings.json`, below `.claude/settings.local.json`, `--settings` and managed settings. Single-value keys (e.g. `model`) use the highest-ranked value; most lists (e.g. `permissions.allow`) merge |
| `.claude/settings.local.json` | Session start | Personal project overrides, gitignored when Claude Code saves a setting to it. Ranks above `settings.json`, below `--settings` and managed settings |
| `.claude/rules/` | Rules without `paths:` frontmatter at session start; rules with `paths:` when Claude reads, writes or edits a matching file | Guidance, not enforced |
| `.claude/skills/` | `/skill-name` or when Claude matches the task | Folder with `SKILL.md`; `disable-model-invocation: true` blocks Claude invoking it, `user-invocable: false` blocks the user |
| `.claude/commands/` | `/command-name` | Single-file commands (`deploy.md` runs as `/deploy`); new ones should be skills |
| `.claude/output-styles/` | Read at startup in the terminal; restart after edits | Markdown files defining an output style |
| `.claude/agents/` | Each subagent runs in its own context window when invoked | Markdown with `name` and `description` frontmatter |
| `.claude/workflows/` | Loaded at startup when workflows are on; each saved workflow runs as `/<name>` | `.js` dynamic workflow scripts; have Claude write one, run `/workflows` and save it here |

# Limits and defaults

Managed settings beat every settings file and `--settings` value apart from narrow exceptions; CLI flags such as `--permission-mode` or `--settings` override `settings.json` for the session; some environment variables take precedence over equivalent settings (check each in the env var reference).
