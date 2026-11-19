---
type: "Feature"
title: "command plugin source"
description: "A plugin source whose directory is printed by a shell command, with timeout, copy and link modes and failure conditions."
resource: "https://code.claude.com/docs/en/plugins/marketplace-reference"
tags: [marketplace, command-source, plugin-source, link-mode]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "command"
  - "timeout"
  - "mode"
  - "copy"
  - "link"
  - "disableCommandPluginSources"
  - "--yes"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-marketplace-reference"
    resource: "https://code.claude.com/docs/en/plugins/marketplace-reference"
    title: "Marketplace reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Used when a tool installed on the user's machine produces the plugin directory (for example an IDE rendering a plugin for the user's toolchain). Claude Code runs the command on install or update, and again once per session, so changed output arrives without reinstalling.

# How to use it

```json
{ "name": "formatter", "source": { "source": "command", "command": "my-tool claude-plugin-path", "timeout": 120 } }
```

| Field | Rule |
| :- | :- |
| `command` | Shell command printing the plugin directory's absolute path as one line and exiting 0. Shown in full to the user for review. Printable ASCII, at most 500 characters, no run of four or more spaces |
| `timeout` | Whole seconds, 1 to 600, default 60 |
| `mode` | `copy` (default) or `link` |

The command runs via `sh` (`cmd.exe` on Windows) from the user's home directory; use an absolute path or a command on `PATH`. In a script, `claude plugin install ... --yes` accepts the command prompt. Administrators turn command sources off with `disableCommandPluginSources`.

# Limits and defaults

Install or update fails if the command exits non-zero, exceeds `timeout`, prints anything but one absolute path, or the printed directory has no plugin content at top level (no `.claude-plugin/`, `skills/`, `commands/`, `agents/`, `hooks/`), is the session's own directory or a parent, is a UNC path on Windows, or (copy mode) exceeds 256 MiB or 20,000 entries.

- **copy**: copied into the plugin cache; version is a hash of the copied files; identical re-run counts as up to date.
- **link**: cache entry links each top-level entry; files load in place; no hashing and no size limits. The directory must stay put while installed; print a different path to signal new content (version comes from the real path and top-level entries); top-level symlinks must stay inside the directory; include `node_modules` because the Node.js dependency install is skipped; a session started inside the directory does not load the plugin; refused on Windows (declare `"mode": "copy"`).
