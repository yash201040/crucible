---
type: "Guide"
title: "Ship updates, renames and removals"
description: "Increment version to release, tag git releases for dependents, and use the marketplace renames map instead of changing a published name."
resource: "https://code.claude.com/docs/en/plugins/publish"
tags: [plugins, versioning, renames, tags]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "claude plugin tag"
  - "--push"
  - "renames"
  - "displayName"
  - "{name}--v{version}"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-publish"
    resource: "https://code.claude.com/docs/en/plugins/publish"
    title: "Publish and distribute a plugin"
stale_after: "2027-01-19T00:00:00Z"
---

# How to use it

- Release: if `plugin.json` sets `version`, increment and push; users who run `claude plugin update` or have auto-update get it.
- Tag: when other plugins declare a range on yours, run `claude plugin tag` from the plugin directory to create a `{name}--v{version}` tag; `--push` sends it to `origin`.
- Rename or remove: never change a published `name`; installs are recorded under the old name and are lost. Use the marketplace file's `renames` map so existing installs migrate instead of failing with `Plugin "<name>" not found in marketplace`. Change `displayName` for a different label.

# Notes

Dependencies: list other plugins from the same marketplace in the `dependencies` array of `plugin.json` (bare name or object with a semver `version` range); installing yours installs and enables them. See [declare dependencies](../plugins-dependencies/declare-plugin-dependencies.md).
