---
type: "Guide"
title: "Test a plugin with its dependency locally"
description: "Load both with --plugin-dir; the local copy satisfies the dependency and version constraints are not checked against it."
resource: "https://code.claude.com/docs/en/plugins/dependencies"
tags: [plugins, dependencies, plugin-dir, testing]
kind: "cli_flag"
maturity: "unlabelled"
since: "2.1.242"
surfaces: [cli]
requires: ""
identifiers:
  - "--plugin-dir"
  - "<name>@inline"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-dependencies"
    resource: "https://code.claude.com/docs/en/plugins/dependencies"
    title: "Plugin dependencies"
stale_after: "2027-01-19T00:00:00Z"
---

# How to use it

`claude --plugin-dir ./my-dependency --plugin-dir ./my-plugin`. The local copy satisfies the dependency entry; no `version` is needed in its `plugin.json` because a constraint is not checked against a local copy. An entry that names a marketplace also matches the local copy on v2.1.242 or later. A parent folder holding both can be passed once (v2.1.265 or later).

# Limits and defaults

Your plugin stops loading while the local copy is disabled or absent: a disabled copy gives an error ending `is disabled — enable it or remove the dependency` (the dependency shown as `<name>@inline`); starting without the dependency's flag reports it as not installed.
