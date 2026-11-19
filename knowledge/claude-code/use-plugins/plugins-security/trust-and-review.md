---
type: "Guide"
title: "Review, warn, refuse and remove a plugin"
description: "Steps to review a plugin before install, the trust warning and pluginTrustMessage, refusal cases, and removing a plugin."
resource: "https://code.claude.com/docs/en/plugins/security"
tags: [plugins, security, review, uninstall]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "claude plugin marketplace list"
  - "claude plugin details"
  - "claude --plugin-dir <plugin directory> plugin details <plugin name>"
  - "claude plugin uninstall"
  - "--keep-data"
  - "pluginTrustMessage"
  - "hooks/hooks.json"
  - ".mcp.json"
  - "~/.claude/plugins/cache/"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-security"
    resource: "https://code.claude.com/docs/en/plugins/security"
    title: "Plugin security and trust"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A four-step review before installing, a fixed trust warning shown in the details pane, and refusal rules for untrusted sources and failed integrity checks.

# How to use it

1. `claude plugin marketplace list` prints each marketplace's source.
2. In `/plugin`, the details pane's **Will install** section lists commands, agents, skills, hooks, MCP and LSP servers; for a plugin with no published component data it shows the entry's declaration or `Components will be discovered at installation` (stored in the marketplace) or `Component summary not available for remote plugin` (fetched elsewhere).
3. Read the source via **Open homepage** or **View on GitHub**: `hooks/hooks.json` (hook commands), `.mcp.json` (server command or URL), every file in `bin/`.
4. `claude --plugin-dir <plugin directory> plugin details <plugin name>` (on a clone) prints a `Component inventory` (skills and commands, agents, hooks with event, MCP and LSP servers) without starting a session; after install, `claude plugin details <plugin name>` prints it for the copy under `~/.claude/plugins/cache/<marketplace>/<plugin>/<version>/`.

**Trust warning**: the same text for every marketplace says plugins can run code with access to files and shell and Anthropic cannot verify them. If managed settings set `pluginTrustMessage`, that text is appended.

**Refusals**: a marketplace using an official or community name with a source outside `github.com/anthropics/` stops loading along with its installed plugins (error `Marketplace is registered from an untrusted source`); an `archive` source pinned to `sha256` with a mismatching download is refused (error `Plugin archive integrity check failed`). The `sha256` pin is separate from the community catalog's commit SHA pin.

# Limits and defaults

**Removal**: `claude plugin uninstall <plugin>` with the `--scope` used at install. When it was the last scope, the persistent data directory is deleted by default (`--keep-data` and other cases are on the CLI reference). Cached files stay under `~/.claude/plugins/cache/` for 14 days before a background sweep; after your last plugin is uninstalled, orphan directories stay until you install another; delete `~/.claude/plugins/cache/<marketplace>/<plugin>/` to remove now. Removing the marketplace uninstalls all its plugins.
