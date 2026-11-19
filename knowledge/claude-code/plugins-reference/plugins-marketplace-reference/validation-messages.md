---
type: "Reference"
title: "claude plugin validate marketplace messages"
description: "Errors and warnings printed by claude plugin validate for marketplace.json, mapped to the field they name, plus failures validation misses."
resource: "https://code.claude.com/docs/en/plugins/marketplace-reference"
tags: [validation, marketplace, errors, warnings]
kind: "cli_flag"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "claude plugin validate"
  - "claude plugin list"
  - "plugins[i].name"
  - "plugins[i].source"
  - "plugins[i].engines.claude-code"
  - "renames"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-marketplace-reference"
    resource: "https://code.claude.com/docs/en/plugins/marketplace-reference"
    title: "Marketplace reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`claude plugin validate <path>` takes the marketplace root or the file itself; name the file `marketplace.json` to have it validated as a marketplace rather than a plugin manifest. Messages name entries by index (`plugins.1.source` or `plugins[1].source`). A prefix such as `plugins[2] plugin.json →` concerns that plugin's own files.

# How to use it

| Message (abridged) | Level | Field |
| :- | :- | :- |
| `Marketplace must have a name` | Error | `name` empty |
| `Marketplace name cannot contain spaces...` / `path separators`, `..` / control or bidi characters | Error | `name` |
| `Marketplace name impersonates an official Anthropic/Claude marketplace` | Error | `name` |
| `Marketplace name "inline" is reserved for --plugin-dir session plugins` (and `builtin`, `skills-dir`, `synced`, `claude-plugin-test`) | Error | `name` |
| `Author name cannot be empty` | Error | `owner.name` |
| `Plugin name cannot contain spaces...` / control or bidi characters | Error | `plugins[i].name` |
| `Plugin name "x" is reserved: it passes as one of Anthropic's own` | Error | `plugins[i].name` |
| `Plugin name "x" reads as one of Anthropic's own` | Warning | `plugins[i].name` |
| `Claude Code cannot install plugins from marketplace "x"...` / `plugin "x"...` (id characters a-z A-Z 0-9 `.` `_` `-`, starting alphanumeric) | Error | `name` / `plugins[i].name` |
| `Duplicate plugin name "x" found in marketplace` | Error | two entries share a name |
| `Must be a version range such as ">=2.1.0"; got "<value>"...` | Error | `plugins[i].engines.claude-code` |
| `plugins.i.source: Invalid input` | Error | source matches no type |
| `plugins.i.source: Invalid string: must start with "./"` | Error | relative source without `./` (before v2.1.285 printed `Invalid input`) |
| `plugins[i].source: Path contains "..": <path>` | Error | relative source escaping the root |
| `source.source: 'unsupported' is a parse-time placeholder and cannot be authored` | Error | `plugins[i].source` |
| `Plugin "x" sets headersHelper but is not "strict": false` | Error | archive entry |
| `chain does not resolve (<reason>)...` / `target "x" is not a valid plugin name (PluginIdSchema)` | Error | `renames.<old>` |
| `Unknown field 'x'. Claude Code ignores it at load time.` | Warning | top level, `metadata`, entry, `relevance` |
| `'engines' must be an object such as { "claude-code": ">=2.1.0" }...` | Warning | `plugins[i].engines` |
| `Marketplace has no plugins defined` | Warning | `plugins` empty |
| `Plugin "x" sets headers/headersHelper, which only apply to "archive" sources...` | Warning | non-archive entry |
| `Plugin "x" fetches its archive with a headersHelper but sets no sha256 pin` | Warning | `plugins[i].source.sha256` |
| `Header "x" is a request-routing/identity header that catalog entries may not set; Claude Code drops it at download time.` | Warning | `plugins[i].headers.<name>` |
| `Local source "x" is or traverses a symlink, so <path> was not read` | Warning | `plugins[i].source` |
| `No marketplace description provided...` | Warning | `description` |
| `Entry declares version "x" but <path>/plugin.json says "y". At install time, plugin.json wins` | Warning | `plugins[i].version` |
| `'relevance'`, `'metadata'`, `'experimental'` wrong type, ignored at load | Warning | those entry fields |
| Claude Desktop name warnings (`org`, `org-provisioned`, `unknown` reserved; letters/digits/`.`/`_`/`-`, alphanumeric start, max 128 chars) | Warning | `name`, `plugins[i].name` |

# Limits and defaults

`Invalid input` on a source means no source type matched: an `npm` `package` containing `..`, an unknown `source` type, or a known type missing a required field (e.g. `github` without `repo`).

# Notes

Validation does not catch everything. An entry `hooks` as a path or array passes but fails at load; errors fetching a `source` appear only after install. `claude plugin list` shows a plugin that failed to load with its error.
