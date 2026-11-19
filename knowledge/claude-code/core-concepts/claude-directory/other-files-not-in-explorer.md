---
type: "Reference"
title: "Files outside the explorer and choosing the right file"
description: "managed-settings.json, CLAUDE.local.md, AGENTS.md, plugin directories, and a table mapping each customization goal to the right file."
resource: "https://code.claude.com/docs/en/claude-directory"
tags: [claude-directory, managed-settings, plugins, file-choice]
kind: "file"
maturity: "unlabelled"
since: "2.1.229"
surfaces: [cli]
requires: ""
identifiers:
  - "managed-settings.json"
  - "CLAUDE.local.md"
  - "AGENTS.md"
  - "~/.claude/plugins"
  - "installed_plugins.json"
  - "~/.claude/plugins/synced/"
  - "settings.local.json"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "claude-directory"
    resource: "https://code.claude.com/docs/en/claude-directory"
    title: "Explore the .claude directory"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Related files that live elsewhere:

| File | Location | Purpose |
| - | - | - |
| `managed-settings.json` | System-level, varies by OS | Enterprise-enforced settings your own settings files and `--settings` cannot override, apart from narrow exceptions |
| `CLAUDE.local.md` | Project root | Private project preferences, loaded alongside CLAUDE.md; create manually and gitignore |
| `AGENTS.md` | Project root, `.claude/`, or any directory | Instructions for AI coding agents; can be loaded in place of CLAUDE.md |
| Installed plugins | `~/.claude/plugins` | Cloned marketplaces, installed versions, `installed_plugins.json`, per-plugin data, managed by `claude plugin`. Plugins synced from claude.ai go in `~/.claude/plugins/synced/`. A marketplace `command` source in link mode stores links instead of a copy; a `command` source requires v2.1.229 or later. A plugin listed by relative path from a locally added marketplace loads in place |

# How to use it

| You want to | Edit | Scope |
| - | - | - |
| Project context and conventions | `CLAUDE.md` | project or global |
| Allow or block tool calls | `settings.json` `permissions` or `hooks` | project or global |
| Run a script before or after tool calls | `settings.json` `hooks` | project or global |
| Set session environment variables | `settings.json` `env` | project or global |
| Keep personal overrides out of git | `settings.local.json` | project only |
| Add a prompt invoked with `/name` | `skills/<name>/SKILL.md` | project or global |
| Define a specialized subagent | `agents/*.md` | project or global |
| Orchestrate many subagents from a script | `workflows/*.js` | project or global |
| Connect external tools over MCP | `.mcp.json` | project only |
| Change response formatting | `output-styles/*.md` | project or global |

# Notes

Agents shipped in a plugin honor a subset of the subagent frontmatter fields. To debug a setting, hook or file not taking effect, the docs point to the debug-your-config page.
