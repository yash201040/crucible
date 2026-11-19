---
type: "Reference"
title: "Plugin component path and symlink errors"
description: "Errors for plugin paths that escape the plugin directory, server file paths, unreadable manifests, uncheckable paths and marketplace entry paths."
resource: "https://code.claude.com/docs/en/errors"
tags: [errors, plugins, symlinks, paths]
kind: "file"
maturity: "unlabelled"
since: "2.1.251"
surfaces: [cli]
requires: ""
identifiers:
  - "plugin.json"
  - ".claude-plugin/plugin.json"
  - "hooks/hooks.json"
  - "monitors/monitors.json"
  - "SKILL.md"
  - "mcp-servers"
  - "/reload-plugins"
  - "claude plugin list"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "errors"
    resource: "https://code.claude.com/docs/en/errors"
    title: "Error reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Checks Claude Code applies to file paths named by plugins and marketplace entries; a failing path is dropped and the rest of the plugin loads (except where noted).

# How to use it

| Error | What it means | Fix |
|---|---|---|
| `<component> path escapes plugin directory` | A component path (`commands`, `hooks`, `monitors`, `skills`, ...) leads outside the plugin directory, or a symlink does (not allowed by marketplace symlink rules). Own files such as `hooks/hooks.json`, `monitors/monitors.json`, root `SKILL.md` are skipped when not confirmed inside the plugin (or its local marketplace). On macOS/Linux any backslash in a component path is rejected | Use `./` relative paths inside the plugin with forward slashes; replace outbound symlinks with copies. `EACCES` means restore execute permission on directories |
| `mcp-servers path not read: ... is absolute or has a ".." part` | MCP or LSP server file path with `..` or absolute; plugin loads without those servers | Use `./servers/x.json` style |
| `Plugin not loaded: its manifest ... was not read` | Cannot confirm `.claude-plugin/plugin.json` is inside the plugin (or marketplace); nothing loads from it | Replace symlinked `.claude-plugin` or `plugin.json` with a copy |
| `<component> path couldn't be checked: <path> (ELOOP)` | OS returned an error other than not-found (`ELOOP`, `EIO`, `ESTALE`, `EACCES`); default component folders skip, plugin's own directory failing loads nothing. `claude plugin list` shows `Path not found: ... (skills, ELOOP)`. Before v2.1.265 a default folder that could not be checked loaded silently without the component | Fix symlink loop or mount; `/reload-plugins` or restart |
| `Cannot install <plugin>@<marketplace>: its marketplace entry path does not stay inside the marketplace directory` | Absolute, `..`, network-shaped, backslash-containing (macOS/Linux), link-traversing entry, or relative entry in a direct-URL `marketplace.json` marketplace. Installed plugins show `Plugin source path refused ...` as `failed to load` | Plain relative path with forward slashes, e.g. `./plugins/my-plugin`; use another plugin source or add from git |

# Notes

Before v2.1.251 a `commands` path in a marketplace entry could point outside the plugin; before v2.1.257 the check looked only at path spelling, not symlink targets.
