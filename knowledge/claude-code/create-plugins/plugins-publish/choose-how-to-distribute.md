---
type: "Reference"
title: "Plugin distribution routes"
description: "Compare no-marketplace, own marketplace and Anthropic's directory by who can install, requirements, and auto-update."
resource: "https://code.claude.com/docs/en/plugins/publish"
tags: [plugins, distribution, marketplace, directory]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, web]
requires: ""
identifiers:
  - ".claude-plugin/marketplace.json"
  - "--plugin-url"
  - "--plugin-dir"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-publish"
    resource: "https://code.claude.com/docs/en/plugins/publish"
    title: "Publish and distribute a plugin"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Publishing means listing a plugin in a marketplace (a JSON catalog of plugins and where to fetch them) so people install by name and receive updates.

| Route | Who can install | Needs | Auto-updates |
| :- | :- | :- | :- |
| No marketplace | People you send the folder or `.zip` | The plugin folder | None; they load the copy sent |
| Your own marketplace | Anyone who can reach the repo (can be private) | Git repo or other host with `.claude-plugin/marketplace.json` | Off by default |
| Anthropic's directory | People who add it on claude.ai or Cowork; also loads in Claude Code via account sync | GitHub repo with the plugin and a paid claude.ai plan | Yes, after the pushed version is published |

Auto-update is a per-marketplace setting on the user's side that fetches new versions in the background.
