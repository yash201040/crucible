---
type: "Concept"
title: "What an installed plugin can do"
description: "Plugins run code with user privileges through hooks, monitors, mods, MCP/LSP servers and bin/, mostly outside permission rules and sandbox."
resource: "https://code.claude.com/docs/en/plugins/security"
tags: [plugins, security, hooks, sandbox]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "bin/"
  - "defaultEnabled"
  - "PowerShell"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-security"
    resource: "https://code.claude.com/docs/en/plugins/security"
    title: "Plugin security and trust"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

An installed plugin can execute arbitrary code on your machine with your user privileges. Capabilities:

- **Hooks**: run as shell commands at lifecycle points.
- **Monitors**: background shell commands Claude Code starts on session start, plugin reload, or the first time a named skill runs.
- **Mods**: run JavaScript inside Claude Code with your permissions.
- **MCP and LSP servers**: Claude Code connects to declared MCP servers (a stdio server is a process started on your machine) and starts declared language servers.
- **`bin/` directory**: each enabled plugin's `bin/` is added to the `PATH` of the Bash tool's shell. For the PowerShell tool, `PATH` includes those directories only when the command runs outside the sandbox.
- **Skills, commands, agents**: enter Claude's context as instructions.
- **Updates**: with auto-update on, reviewed files can change on disk in the background.

# Limits and defaults

- Permission rules and the sandbox cover the tool calls Claude makes, not code a plugin runs by itself. Hooks, monitors, MCP servers, LSP servers and processes a mod starts run outside the sandbox; command hooks and monitors have full user permissions.
- A call to a plugin's MCP tool, or a Bash command running a `bin/` executable, is a tool call and permission rules apply.
- Installing a plugin also enables it unless its manifest or marketplace entry sets `defaultEnabled: false` and you have not enabled it.
