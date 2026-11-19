---
type: "Feature"
title: "Connectors, skills and plugins in Desktop"
description: "Connector directory, skill invocation and plugin management in the Code tab, with SSH, WSL and cloud differences."
resource: "https://code.claude.com/docs/en/desktop"
tags: [desktop, connectors, skills, plugins, mcp]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [desktop]
requires: "Claude account for connectors; local or SSH session for plugin browser"
identifiers:
  - "~/.claude/skills/"
  - "claude_desktop_config.json"
  - "claude mcp add-from-claude-desktop"
  - "disableSideloadFlags"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "desktop"
    resource: "https://code.claude.com/docs/en/desktop"
    title: "Desktop application"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Connectors are MCP servers with a graphical setup flow. Skills load automatically or via `/`. Plugins bundle skills, agents, hooks, MCP servers and LSP configurations.

# How to use it

- **Connectors**: **+** next to the prompt box > Add connectors / Browse connectors, or **Customize** / **Plugins** in the sidebar. For other servers use settings files. Servers in `claude_desktop_config.json` load into local Code sessions; the standalone CLI does not read it (macOS and WSL: `claude mcp add-from-claude-desktop`).
- **Skills**: `/` or **+** > Slash commands. Local sessions read `~/.claude/skills/`; SSH sessions read the remote host's. Local and cloud sessions also load skills enabled for the claude.ai account unless `disableSideloadFlags` is set.
- **Plugins**: **+** > Add plugins or Manage plugins; scope user, project or local-only. Managed plugins apply as in the CLI, except those withheld under `disableSideloadFlags`.

# Limits and defaults

Plugins: not in cloud sessions (and desktop-installed plugins do not carry to cloud), not in WSL sessions. Connectors are grayed out in some WSL sessions. In local and SSH sessions connectors are delivered to Claude Code directly, so no MCP setting or `managed-mcp.json` governs them; use organization connector tool controls. Connector calls fail after about 30 seconds if an SSH session's Desktop is disconnected.
