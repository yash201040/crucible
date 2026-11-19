---
type: "Reference"
title: "Using userConfig values in a plugin"
description: "${user_config.KEY} substitution and CLAUDE_PLUGIN_OPTION_<KEY> variables; shell-form fields reject ${user_config.*}."
resource: "https://code.claude.com/docs/en/plugins/manifest-reference"
tags: [plugins, userconfig, hooks, shell-safety]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "${user_config.*}"
  - "CLAUDE_PLUGIN_OPTION_<KEY>"
  - "CLAUDE_PLUGIN_OPTION_API_TOKEN"
  - "headersHelper"
  - "CLAUDE_CODE_MCP_SERVER_NAME"
  - "CLAUDE_CODE_MCP_SERVER_URL"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-manifest-reference"
    resource: "https://code.claude.com/docs/en/plugins/manifest-reference"
    title: "Plugin manifest reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Two ways to read a saved `userConfig` value, and the fields that refuse one.

# How to use it

- **`${user_config.KEY}`**: substituted in MCP server config, LSP server config, exec-form hook `args`, and skill and agent content. In skill and agent content only non-sensitive values are substituted; a sensitive value becomes a placeholder.
- **`CLAUDE_PLUGIN_OPTION_<KEY>`**: exported to hook processes for every option, `<KEY>` uppercased; a shell-form hook reads `$CLAUDE_PLUGIN_OPTION_API_TOKEN` for `api_token`.

Shell-form hook commands, monitor commands and MCP `headersHelper` reject `${user_config.*}`: a component referencing it there fails with an error instead of running, because the shell would re-parse the substituted value.

| Field | How the value can reach it |
| :- | :- |
| Shell-form hook commands | Use exec form with `args`, or read `CLAUDE_PLUGIN_OPTION_<KEY>` from the environment |
| Monitor commands | Not through Claude Code; monitor processes do not receive `CLAUDE_PLUGIN_OPTION_<KEY>` |
| MCP `headersHelper` | Not through Claude Code; its environment has `CLAUDE_PLUGIN_ROOT`, `CLAUDE_CODE_MCP_SERVER_NAME`, `CLAUDE_CODE_MCP_SERVER_URL` but no option values |
