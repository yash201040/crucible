---
type: "Concept"
title: "Dependencies for plugins synced from claude.ai"
description: "A plugin turned on in claude.ai loads as <name>@synced, and a marketplace-named dependency is met by an installed copy or a same-name claude.ai plugin."
resource: "https://code.claude.com/docs/en/plugins/dependencies"
tags: [plugins, dependencies, claude-ai, sync]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, web]
requires: ""
identifiers:
  - "<name>@synced"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-dependencies"
    resource: "https://code.claude.com/docs/en/plugins/dependencies"
    title: "Plugin dependencies"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

When a user enables your plugin in claude.ai, Claude Code loads it as `<name>@synced` with no marketplace. A dependency entry naming a marketplace counts as met when the user has (a) the dependency installed from that marketplace and enabled (a `version` range is checked against the installed copy), or (b) an enabled claude.ai plugin of the same name (range checked against its `version`; a plugin stating no `version` passes). A claude.ai plugin meets the entry only when your plugin also loads from claude.ai. Tell users to turn the dependency on there too or install it from its marketplace.
