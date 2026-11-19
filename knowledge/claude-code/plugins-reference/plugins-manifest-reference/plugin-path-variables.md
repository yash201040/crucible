---
type: "Reference"
title: "Plugin path variables"
description: "CLAUDE_PLUGIN_ROOT, CLAUDE_PLUGIN_DATA and CLAUDE_PROJECT_DIR: where they resolve, are exported, and how to quote them."
resource: "https://code.claude.com/docs/en/plugins/manifest-reference"
tags: [plugins, env-vars, paths, hooks]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "${CLAUDE_PLUGIN_ROOT}"
  - "${CLAUDE_PLUGIN_DATA}"
  - "${CLAUDE_PROJECT_DIR}"
  - "CLAUDE_PLUGIN_ROOT"
  - "CLAUDE_PLUGIN_DATA"
  - "CLAUDE_PROJECT_DIR"
  - "shell"
  - "powershell"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-manifest-reference"
    resource: "https://code.claude.com/docs/en/plugins/manifest-reference"
    title: "Plugin manifest reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Three path variables are provided to plugin components, referenced as `${NAME}` in specific fields and exported as environment variables to some processes.

# How to use it

| Variable | Resolves to | Use for |
| :- | :- | :- |
| `${CLAUDE_PLUGIN_ROOT}` | Absolute path of the plugin's installed version; changes on update, so do not write state there | Bundled scripts, binaries, config |
| `${CLAUDE_PLUGIN_DATA}` | `~/.claude/plugins/data/<id>/`, created on first reference, kept across updates; `<id>` is the plugin identifier with every character other than letter, digit, `_`, `-` replaced by `-` | `node_modules`, generated code, caches |
| `${CLAUDE_PROJECT_DIR}` | The project root | Project-local scripts and config |

| Plugin component | Where `${...}` resolves | Exported to process |
| :- | :- | :- |
| Hook commands | Anywhere in `command` and `args` | `CLAUDE_PLUGIN_ROOT`, `CLAUDE_PLUGIN_DATA`, `CLAUDE_PROJECT_DIR`, `CLAUDE_PLUGIN_OPTION_<KEY>` |
| Monitor commands | Anywhere in `command` | Not exported |
| MCP `stdio` servers | `command`, `args`, `env` | The three path variables |
| MCP `http`, `sse`, `ws` servers | `url`, `headers`, `headersHelper` | Not applicable |
| LSP servers | `command`, `args`, `env`, `workspaceFolder` | The three path variables |
| Skill, command, agent content | Anywhere in the Markdown body | Not applicable |

# Limits and defaults

- The variables are not in the environment of commands Claude runs through the Bash tool, in the main session or a subagent; in skill, command and agent content write the `${...}` reference in the body and it is substituted inline.
- The data directory is deleted when the plugin is uninstalled from its last place, unless `--keep-data` (see `plugin uninstall`).
- Quoting: use exec form with `args` for hooks so each path is one argument; in shell-form hooks and monitor commands wrap the variable in double quotes (`"\"${CLAUDE_PLUGIN_ROOT}\"/scripts/process.sh"`). Unquoted use in a shell-form hooks-file command makes validate warn, unless the hook sets `shell` to `"powershell"`.
- Windows: most substituted paths use forward slashes (`C:/Users/you/...`); exec-form hooks and PowerShell hooks (default shell on Windows without Git Bash) keep native backslashes.
