---
type: "Reference"
title: "Load a plugin for one session"
description: "--plugin-dir, --plugin-url and CLAUDE_CODE_PLUGIN_DIRS load plugins from disk, zip or URL without a marketplace."
resource: "https://code.claude.com/docs/en/plugins/create"
tags: [plugins, plugin-dir, plugin-url, development]
kind: "cli_flag"
maturity: "unlabelled"
since: "2.1.265"
surfaces: [cli]
requires: ""
identifiers:
  - "--plugin-dir"
  - "--plugin-url"
  - "CLAUDE_CODE_PLUGIN_DIRS"
  - "/reload-plugins"
  - ".claude-plugin/marketplace.json"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-create"
    resource: "https://code.claude.com/docs/en/plugins/create"
    title: "Create a Claude Code plugin"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Ways to load a plugin you are writing, without a marketplace, for a single session.

# How to use it

| Name | Kind | What it does |
| :- | :- | :- |
| `--plugin-dir <path>` | flag | Plugin root directory or `.zip`; repeat to load several (`--plugin-dir ./a --plugin-dir ./b.zip`) |
| `--plugin-url <url>` | flag | Downloads a `.zip` at startup (e.g. CI build artifact); repeat or pass space-separated in one quoted argument |
| `CLAUDE_CODE_PLUGIN_DIRS` | env var | Absolute paths loaded like `--plugin-dir`, in addition to flag paths; for sessions where no flag can be added. Requires v2.1.280 or later |

Run `/reload-plugins` to pick up edits during the session.

# Limits and defaults

- Folder of plugins (`--plugin-dir ./plugins`) requires v2.1.265 or later: if the folder has no `.claude-plugin/` and no components at top level, each immediate subfolder with `.claude-plugin/plugin.json` loads as a plugin; others are skipped silently. A folder with a `.claude-plugin/marketplace.json` but no `plugin.json` also loads its plugin folders (v2.1.281 or later); nothing is installed from the marketplace file.
- In an interactive session, subfolders added or removed later load or unload with a message; if that would invalidate the prompt cache, the change is held until `/reload-plugins`.
- `--plugin-url` with an unfetchable or invalid archive: Claude Code starts without the plugin and records an error in the `/plugin` Errors tab. Point only at archives you trust.
- Project and local settings cannot set `CLAUDE_CODE_PLUGIN_DIRS`. Managed settings can turn off `--plugin-dir` and `CLAUDE_CODE_PLUGIN_DIRS`.
- Pointing `--plugin-dir` at a marketplace root does not load plugins under `plugins/` and shows no error.
- Name conflicts between plugins loaded different ways: see loading docs.
