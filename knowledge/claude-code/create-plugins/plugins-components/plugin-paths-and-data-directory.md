---
type: "Reference"
title: "Plugin path variables and data directory"
description: "CLAUDE_PLUGIN_ROOT, CLAUDE_PLUGIN_DATA and CLAUDE_PROJECT_DIR substitutions and installing dependencies into the persistent data directory."
resource: "https://code.claude.com/docs/en/plugins/components"
tags: [plugins, paths, env-vars, data-directory]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "CLAUDE_PLUGIN_ROOT"
  - "CLAUDE_PLUGIN_DATA"
  - "CLAUDE_PROJECT_DIR"
  - "~/.claude/plugins/data/<id>/"
  - "NODE_PATH"
  - "SessionStart"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-components"
    resource: "https://code.claude.com/docs/en/plugins/components"
    title: "Add components to a plugin"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Plugins must reference their files through variables, not fixed paths. They are substituted in skill, command and agent content, hook and monitor commands, and MCP and LSP configs, and also exported to hook, MCP and LSP processes.

# How to use it

| Variable | Meaning |
| :- | :- |
| `${CLAUDE_PLUGIN_ROOT}` | Plugin install directory. Each version has its own cache directory so it changes on update; do not write state there |
| `${CLAUDE_PLUGIN_DATA}` | Directory that survives updates (node_modules, venvs, caches); resolves to `~/.claude/plugins/data/<id>/`, created on first reference |
| `${CLAUDE_PROJECT_DIR}` | Project root, same value hooks receive |

`<id>` is the plugin identifier with every character other than letters, digits, `_`, `-` replaced by `-` (`my-plugin@my-marketplace` becomes `my-plugin-my-marketplace`).

Dependencies: for a marketplace-installed plugin, eligible Node.js package dependencies are installed automatically when the plugin is cached. Otherwise a `SessionStart` hook can `diff` `package.json` against the data copy and run `npm install` in `${CLAUDE_PLUGIN_DATA}`; an MCP server then sets `NODE_PATH` to `${CLAUDE_PLUGIN_DATA}/node_modules` in `env`.

# Notes

On Windows most substituted paths use forward slashes (`C:/Users/you/...`); they keep backslashes in an exec-form hook and in hooks run through PowerShell (default shell on Windows without Git Bash).
