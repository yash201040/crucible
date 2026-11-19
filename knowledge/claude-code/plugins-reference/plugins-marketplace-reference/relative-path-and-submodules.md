---
type: "Feature"
title: "Relative path sources, pluginRoot and submodules"
description: "How relative plugin paths resolve, the bare-name pluginRoot shortcut, and which git submodules Claude Code fetches."
resource: "https://code.claude.com/docs/en/plugins/marketplace-reference"
tags: [marketplace, relative-path, submodules, pluginroot]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.295"
surfaces: []
requires: ""
identifiers:
  - "metadata.pluginRoot"
  - "--sparse"
  - "sparsePaths"
  - "SKILL.md"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-marketplace-reference"
    resource: "https://code.claude.com/docs/en/plugins/marketplace-reference"
    title: "Marketplace reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A relative-path source such as `./plugins/formatter` resolves from the marketplace root (`<root>/plugins/formatter`), even though the file sits in `<root>/.claude-plugin/`.

# How to use it

- A path containing `..` fails validation. On macOS and Linux a backslash after the leading `./` is refused; use forward slashes.
- Relative paths work only when Claude Code has the marketplace's files: `github`, `git`, `file`, `directory` marketplace sources work; `url` fetches only `marketplace.json` so relative paths cannot resolve (use `github` or `git-subdir` objects); `settings` rejects relative paths outright.
- **Bare names**: set `metadata.pluginRoot` (e.g. `"./plugins"`) and write `"source": "formatter"` to get `./plugins/formatter`. Needs v2.1.239 or later. The root must be a relative path inside the marketplace, has no effect on sources already starting `./`, and a source containing `/` (such as `team-a/formatter`) is not a bare name and still needs `./`.

# Limits and defaults

**Submodules (v2.1.295 or later)**: cloning a marketplace fetches only submodules that hold plugin files; earlier versions fetch all, nested included, which can exceed the clone timeout. For a subdirectory plugin a submodule is fetched when the plugin is inside it, it is inside the plugin, or a committed symlink targets it. A root plugin (`"source": "./"`) gets all submodules or none; all are fetched if a root component directory (`skills/`, `hooks/`, `bin/`), a configured path (entry, `plugin.json`, `.mcp.json`, `hooks/hooks.json`), a symlink, or text naming a submodule path (such as `vendor/tool`) points into any submodule. All are also fetched when Claude Code cannot tell (a root `SKILL.md`, or an unreadable marketplace file, config file or `.gitmodules`). With `--sparse` or `sparsePaths`, only the named directories are checked out and no submodule is fetched.
