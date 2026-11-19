---
type: "Feature"
title: "strictPluginOnlyCustomization"
description: "Managed key that blocks skills, agents, hooks and MCP servers from user and project sources, leaving only plugin and managed sources."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [settings, plugins, managed, lockdown]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: "Managed settings"
identifiers:
  - "strictPluginOnlyCustomization"
  - "strictPluginOnlyCustomization.skills"
  - "strictPluginOnlyCustomization.agents"
  - "strictPluginOnlyCustomization.hooks"
  - "strictPluginOnlyCustomization.mcp"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Managed-scope key, `true` to lock all four surfaces or an array from `"skills"`, `"agents"`, `"hooks"`, `"mcp"`. Default unset (nothing locked). Locking any surface also stops loading skills-directory plugins (folders users keep in `~/.claude/skills/` or `.claude/skills/`). Unknown surface names are ignored, not errors. Pair with `strictKnownMarketplaces`, and `disableSideloadFlags` to reject sideload CLI flags.

# How to use it

`{ "strictPluginOnlyCustomization": ["skills", "hooks"] }`

| Surface | Stops loading | Keeps loading |
| :- | :- | :- |
| `skills` | skills in `~/.claude/skills/` and `.claude/skills/`, commands in `~/.claude/commands/` and `.claude/commands/`, skills and commands under `--add-dir`, skills synced from claude.ai | bundled skills, managed policy directory skills, plugin skills (not skills-directory plugins) |
| `agents` | agents in `~/.claude/agents/`, `.claude/agents/`, `--add-dir` dirs | built-in agents, managed policy directory agents, plugin agents |
| `hooks` | user, project, local `settings.json` hooks; frontmatter hooks in skills, commands, agents from blocked sources | managed settings hooks, plugin hooks |
| `mcp` | MCP servers from `~/.claude.json` and `.mcp.json` | `managed-mcp.json` servers, `managedMcpServers`, plugin MCP servers |

# Notes

With `hooks` locked, a personal or project skill that declares `hooks` in frontmatter loses its `allowed-tools` pre-approval (users get permission prompts), except when it runs in a subagent via `context: fork`. A skill without `hooks` keeps pre-approval. Skills, commands and agents whose frontmatter hooks stop still load while their own surface is not locked.
