---
type: "Concept"
title: "plugin.json manifest file and validation"
description: "The optional .claude-plugin/plugin.json holds metadata, userConfig and component declarations; unrecognized fields are stripped, strict objects reject unknown keys."
resource: "https://code.claude.com/docs/en/plugins/manifest-reference"
tags: [plugins, manifest, validation, plugin-json]
kind: "file"
maturity: "unlabelled"
since: "2.1.281"
surfaces: [cli]
requires: ""
identifiers:
  - ".claude-plugin/plugin.json"
  - "claude plugin validate"
  - "--strict"
  - "${user_config.KEY}"
  - ".mcp.json"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-manifest-reference"
    resource: "https://code.claude.com/docs/en/plugins/manifest-reference"
    title: "Plugin manifest reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The manifest is `plugin.json` in the plugin's `.claude-plugin/` directory. It is optional: without it Claude Code loads components from the standard layout, taking the plugin name from the marketplace entry, or from the directory name with `--plugin-dir`. Write one for metadata, components outside default directories, `userConfig`, or inline component definitions. Put every other plugin file at the plugin root, not inside `.claude-plugin/`.

# How to use it

Run `claude plugin validate ./my-plugin` (authoritative). Results: `Validation passed`; `Validation passed with warnings` (e.g. unknown top-level field stripped, `name` not kebab-case, missing `version`, `description` or `author`; `--strict` turns warnings into failures); `Validation failed` (type mismatch, missing path or one escaping the plugin root, unknown key in a `userConfig` option, `channels` entry, `lspServers` config or `monitors` entry; Claude Code reports the same at load).

It also checks each MCP server entry in `.mcp.json`, a `.json` file named by `mcpServers`, or inline (v2.1.281 or later). Errors: an entry Claude Code would drop, a `${user_config.KEY}` reference to an undeclared option, a remote `url` that is not a valid absolute URL. Warnings: an `http://` or `ws://` URL to a non-loopback host, a header value that looks like a literal credential.

# Limits and defaults

- Unrecognized top-level key: stripped, plugin loads, validate warns.
- Strict objects (`userConfig` options, `channels` entries, `lspServers` configs, `monitors` entries): an unknown key is an error and the plugin does not load.
