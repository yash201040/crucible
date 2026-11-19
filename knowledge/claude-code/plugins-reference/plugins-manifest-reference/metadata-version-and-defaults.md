---
type: "Concept"
title: "displayName, version, defaultEnabled, dependencies"
description: "Behavior of version pinning, displayName precedence, defaultEnabled persistence, dependency entry shapes and directory-listing fields."
resource: "https://code.claude.com/docs/en/plugins/manifest-reference"
tags: [plugins, version, dependencies, default-enabled]
kind: "file"
maturity: "unlabelled"
since: "2.1.281"
surfaces: [cli]
requires: ""
identifiers:
  - "enabledPlugins"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-manifest-reference"
    resource: "https://code.claude.com/docs/en/plugins/manifest-reference"
    title: "Plugin manifest reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Detail on fields listed in the [fields table](./manifest-fields-table.md).

# How to use it

- **`displayName`**: may contain spaces and any casing; not used for namespacing or lookup. A `displayName` on the marketplace entry takes precedence.
- **`version`**: any string, not checked against semver. Setting it pins the plugin to that version until you change it. Not pinned by this field: a plugin with a `command` source, a plugin from a marketplace hosted on claude.ai, a plugin loaded in place from a marketplace added from a local path.
- **`metadata`**: free-form; Claude Code does not read it.
- **Directory listing fields** (`icon`, `documentationUrl`, `supportUrl`, `privacyPolicyUrl`, `termsOfServiceUrl`): read by Anthropic's directory at submission, ignored at load. Set only in `plugin.json`; in a marketplace entry validate reports them as unknown. `icon` is an image path inside the plugin such as `./logo.png`; the four URLs are `https://`. On v2.1.281 or later validate does not report them as unknown in `plugin.json`; earlier versions warn, so `--strict` fails there.
- **`defaultEnabled`**: whether the plugin starts enabled when the user has not set it in `enabledPlugins`; default `true`. A plugin that an enabled plugin depends on starts enabled regardless. The marketplace entry's value overrides. Once a user's `enabledPlugins` entry is written it persists across updates, so changing `defaultEnabled` later does not affect existing users.
- **`dependencies`**: each entry is `"name"`, `"name@marketplace"` or `{ "name": "...", "marketplace": "...", "version": "..." }`. Bare names resolve against the plugin's own marketplace.
