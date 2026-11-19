---
type: "Guide"
title: "Install a plugin (terminal, desktop, VS Code, cloud)"
description: "How to install a plugin per surface, read the install summary, and what each surface supports."
resource: "https://code.claude.com/docs/en/plugins/install"
tags: [plugins, install, surfaces, reload-plugins]
kind: "slash_command"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop, ide, cloud]
requires: ""
identifiers:
  - "/plugin install"
  - "/plugin"
  - "/plugins"
  - "/reload-plugins"
  - "/reload-plugins --force"
  - "claude plugin list"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-install"
    resource: "https://code.claude.com/docs/en/plugins/install"
    title: "Install and manage plugins"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Installing adds a plugin's skills, agents, hooks and MCP servers to Claude Code. The example installs `commit-commands` from `claude-plugins-official`.

# How to use it

**Terminal**: `/plugin install commit-commands@claude-plugins-official` does not install immediately in a session; it opens the `/plugin` panel on the plugin's details. `/plugin` alone opens **Discover** (type to search, Enter for details). The details pane shows description, **Will install** (commands, agents, skills, hooks, MCP and LSP servers), **Last updated** and **Context cost** (official-marketplace plugins only: **Every turn** and **When invoked** token estimates, shown when opened by naming the marketplace or from the **Marketplaces** tab, not from **Discover**). Local or custom marketplaces can show `Components will be discovered at installation`. Then choose a scope; Claude Code installs declared dependencies and prints a summary whose last sentence says:

| Summary | Meaning |
| :- | :- |
| `Plugin is now active.` | No reload needed |
| active plus `Its bundled MCP server needs` | Server cannot start until set up: **Installed** tab, select plugin, **Configure** |
| `Run /reload-plugins to apply.` | Panel closes and Claude Code reloads; if reload would invalidate the prompt cache it warns and leaves the plugin pending; `/reload-plugins --force` activates it at the cost of one uncached request |
| `The plugin couldn't` | Load failed; see the **Errors** tab |

Confirm: skills appear as `/<plugin>:<skill>` (e.g. `/commit-commands:commit`); also the **Installed** tab or `claude plugin list` (prints `Version`, `Scope`, `Status`). Claude Code adds the official marketplace on first interactive terminal session; claude.com/marketplace's **Claude Code** button copies `claude plugin install <name>@claude-plugins-official`.

**Desktop app** (Code tab, local or SSH session): **+** button, **Add plugins** (or **Plugins**, **Browse plugins**, **Manage plugins**), select plugin, choose scope.

**VS Code**: type `/plugins` for **Manage plugins**; on the **Plugins** tab click **Install**; if empty add `anthropics/claude-plugins-official` on **Marketplaces**. Scopes: **Install for you**, **Install for this project**, **Install locally**. Changes apply to open sessions without restart.

**Cloud session**: no plugin browser; does not load plugins installed on your machine or those enabled in the repo's `.claude/settings.json`. Org-distributed plugins come through managed settings.

# Limits and defaults

- **JetBrains**: runs Claude Code in the IDE terminal; use the Terminal steps.
- **`claude -p` and other non-interactive runs**: `/plugin` does not run (Claude replies `/plugin isn't available in this environment.`); already-installed plugins still load; manage them with [shell commands](./install-from-shell.md).
- **Agent SDK**: load plugins through the SDK's plugin option.
- Plugin authors can test a copy with `--plugin-dir` for one session.
