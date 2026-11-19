---
type: "Reference"
title: "plugin.json fields"
description: "Every top-level plugin.json key with type and behavior; name is the only required field."
resource: "https://code.claude.com/docs/en/plugins/manifest-reference"
tags: [plugins, manifest, fields, reference]
kind: "file"
maturity: "unlabelled"
since: "2.1.323"
surfaces: [cli]
requires: ""
identifiers:
  - "$schema"
  - "name"
  - "displayName"
  - "version"
  - "description"
  - "author"
  - "homepage"
  - "repository"
  - "license"
  - "keywords"
  - "metadata"
  - "icon"
  - "documentationUrl"
  - "supportUrl"
  - "privacyPolicyUrl"
  - "termsOfServiceUrl"
  - "defaultEnabled"
  - "engines"
  - "dependencies"
  - "userConfig"
  - "types"
  - "channels"
  - "skills"
  - "commands"
  - "agents"
  - "hooks"
  - "mcpServers"
  - "lspServers"
  - "outputStyles"
  - "workflows"
  - "experimental"
  - "experimental.themes"
  - "experimental.monitors"
  - "experimental.evals"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-manifest-reference"
    resource: "https://code.claude.com/docs/en/plugins/manifest-reference"
    title: "Plugin manifest reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The top-level keys of `plugin.json`. `name` is the only required key. In the Type column, a path is a string relative to the plugin root such as `"./custom/commands"`.

# How to use it

| Field | Type | Description |
| :- | :- | :- |
| `$schema` | String | JSON Schema URL for editor autocomplete; ignored at load |
| `name` | String | Identifier, required, kebab-case; components are namespaced under it |
| `displayName` | String | Name shown in UI instead of `name` |
| `version` | String | Version; setting it keeps users on that version until changed |
| `description` | String | Short explanation |
| `author` | Object | `name` (required), optional `email`, `url` |
| `homepage` | String | Documentation URL; must parse as a URL or the plugin fails to load |
| `repository` | String | Source URL; not validated |
| `license` | String | SPDX identifier e.g. `MIT`, `Apache-2.0` |
| `keywords` | Array of strings | Discovery tags |
| `metadata` | Object | Free-form; not read by Claude Code |
| `icon`, `documentationUrl`, `supportUrl`, `privacyPolicyUrl`, `termsOfServiceUrl` | String | Listing fields for Anthropic's directory; ignored by Claude Code |
| `defaultEnabled` | Boolean | Starts enabled when the user has not set it; default `true` |
| `engines` | Object | Claude Code versions the plugin works on as a semver range under `claude-code`, e.g. `"engines": { "claude-code": ">=2.1.400" }`. Requires v2.1.323 or later. Omit it to keep working on v2.0.15 through v2.1.75, which reject the manifest with `Unrecognized key` |
| `dependencies` | Array of strings or objects | Plugins that must be enabled |
| `userConfig` | Object | Values prompted for when enabled |
| `types` | Path | A `.d.ts` declaring `$.state` values and `$` nouns of a mod |
| `channels` | Array of objects | Message channels bound to MCP servers |
| `skills` | Path or array | Skill directories (each of `<name>/SKILL.md` folders or one folder holding `SKILL.md`); `"."` is the plugin root; adds to default `skills/` |
| `commands` | Path, array or object | Flat `.md` files, directories, or name-to-`source`/`content` map; replaces default `commands/` |
| `agents` | Path or array | Agent `.md` files; directories not accepted; replaces default `agents/` |
| `hooks` | Path, object or array | `.json` hook files or inline config; loaded together with `hooks/hooks.json` |
| `mcpServers` | Path, object or array | `.json` files, `.mcpb`/`.dxt` bundles, inline configs; loaded with `.mcp.json`; later name replaces earlier |
| `lspServers` | Path, object or array | `.json` files or inline configs; loaded with `.lsp.json` |
| `outputStyles` | Path or array | Output style files/directories; replaces default `output-styles/` |
| `workflows` | Path or array | Workflow `.js` files or directories; replaces default `workflows/` |
| `experimental` | Object | Container for `themes`, `monitors`, `evals` whose shape may still change |
| `experimental.themes` | Path or array | Theme files/directories; replaces default `themes/`; a top-level `themes` key still loads with a validate warning |
| `experimental.monitors` | Path or inline array | Monitors; default `monitors/monitors.json`; top-level `monitors` still loads with warning; monitors do not start with `-p` |
| `experimental.evals` | Path or array | Directory of eval cases if not `evals/`; `claude plugin eval --eval-dir` overrides |

# Notes

Details: [name rules](./name-rules.md), [metadata fields](./metadata-version-and-defaults.md), [component paths](./component-path-forms.md).
