---
type: "Reference"
title: "Plugin entry rules, sources and validation"
description: "Rules for marketplace plugin entries, the main source types, submodule fetching, and what validate catches versus what fails at add or install."
resource: "https://code.claude.com/docs/en/plugins/create-marketplace"
tags: [plugins, marketplace, sources, validation, submodules]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.295"
surfaces: [cli]
requires: "Submodule trimming needs Claude Code v2.1.295 or later"
identifiers:
  - "name"
  - "source"
  - "description"
  - "github"
  - "git-subdir"
  - "url"
  - "archive"
  - "npm"
  - "command"
  - "ref"
  - "sha"
  - "enabledPlugins"
  - "${CLAUDE_PLUGIN_ROOT}"
  - "claude-plugins-official"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-create-marketplace"
    resource: "https://code.claude.com/docs/en/plugins/create-marketplace"
    title: "Create a marketplace"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Each plugin is one object in `plugins`. Core fields: `name` (the text typed before `@`), `source`, `description` (shown in `/plugin`).

# How to use it

| Source | Use when | Minimal value |
|---|---|---|
| Relative path | files inside the marketplace dir | `"./plugins/my-first-plugin"` |
| `github` | plugin is its own GitHub repo | `{ "source": "github", "repo": "your-org/my-first-plugin" }` |
| `git-subdir` | plugin in a subdirectory of another repo | `{ "source": "git-subdir", "url": "your-org/monorepo", "path": "tools/my-first-plugin" }` (`url` takes a git URL or `owner/repo`) |

Other source types: `url` (git repo on any host), `archive` (zip over HTTPS), `npm`, `command` (directory produced by running a command at install time). Pin a git source with `ref` or `sha`.

Rules:
- Relative paths are from the marketplace root (dir containing `.claude-plugin/`). A path with `..` fails `validate` (`Path contains "..": ...`). A missing directory passes `validate` but fails install with `Source path does not exist: <path>`.
- Entry `name` must equal the manifest `name` in `plugin.json`; entry name is the install id and `enabledPlugins` key, manifest name prefixes skills. Installing by manifest name when they differ gives `Plugin "<manifest-name>" not found in marketplace "<marketplace>"`.
- Submodules (v2.1.295+): for a plugin in a subdirectory, only submodules inside it or containing it are fetched. For a plugin at the marketplace root, all submodules are fetched once one plugin file refers to a path inside any; write submodule paths literally (e.g. `${CLAUDE_PLUGIN_ROOT}/vendor/tool/run.sh`) because script-built paths are invisible.

# Limits and defaults

`claude plugin validate` reads only files inside the marketplace dir and reports: JSON syntax errors, missing required fields (`owner: Invalid input`), naming-rule breaks, `..` in relative sources, unknown fields (warnings), and problems in each relative plugin's `plugin.json` (`plugins[N] plugin.json → <field>: <message>`). Not reported until add/install: reserved official names such as `claude-plugins-official` (refused with `The name '<name>' is reserved for official Anthropic marketplaces`), wrong remote `repo`/`path`, missing relative directory.
