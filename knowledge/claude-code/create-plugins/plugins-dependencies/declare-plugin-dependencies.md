---
type: "Feature"
title: "Declare plugin dependencies"
description: "List dependencies in plugin.json as names or objects with a semver version range and optional marketplace."
resource: "https://code.claude.com/docs/en/plugins/dependencies"
tags: [plugins, dependencies, semver, manifest]
kind: "setting"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "dependencies"
  - "dependencies[].name"
  - "dependencies[].version"
  - "dependencies[].marketplace"
  - "name@marketplace"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-dependencies"
    resource: "https://code.claude.com/docs/en/plugins/dependencies"
    title: "Plugin dependencies"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A dependency is another plugin yours relies on. Without a version constraint a dependency moves to each new release its marketplace publishes. With one (a semver range such as `~2.1.0`) users of a git-backed dependency keep receiving only matching patches.

# How to use it

`dependencies` array in `.claude-plugin/plugin.json`. An entry is a string (`"audit-logger"` or `"name@marketplace"`) or an object:

| Field | Description |
| :- | :- |
| `name` | Required. Dependency name as in its marketplace entry; looked up in the declaring plugin's marketplace unless `marketplace` is set |
| `version` | Semver range such as `~2.1.0`, `^2.0`, `>=1.4`, `=2.1.0`; installs at the highest git tag satisfying it, so the dependency's maintainer must tag releases |
| `marketplace` | A different marketplace to resolve `name` in (needs allowlist) |

# Limits and defaults

A range does not match pre-release versions such as `2.0.0-beta.1` unless you opt in with a suffix such as `^2.0.0-0`.
