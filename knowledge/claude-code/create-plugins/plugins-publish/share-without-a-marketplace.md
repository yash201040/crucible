---
type: "Guide"
title: "Share a plugin without a marketplace"
description: "Send the folder or zip, or point --plugin-url at a release zip; users load it per session or from ~/.claude/skills/."
resource: "https://code.claude.com/docs/en/plugins/publish"
tags: [plugins, sharing, plugin-url, installer]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "claude --plugin-dir"
  - "--plugin-url"
  - "~/.claude/skills/"
  - "claude plugin marketplace add <source>"
  - "claude plugin install <name>@<marketplace>"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-publish"
    resource: "https://code.claude.com/docs/en/plugins/publish"
    title: "Publish and distribute a plugin"
stale_after: "2027-01-19T00:00:00Z"
---

# How to use it

From a git repo people can clone and load the checkout, or run `--plugin-url` at a `.zip` attached to a release. Otherwise send the directory or zip. Recipients load it for one session (`claude --plugin-dir ./deploy-helper`, path being clone, unzipped folder or the `.zip`) or for every session by moving the directory with its `.claude-plugin/plugin.json` under `~/.claude/skills/` (unless an administrator blocked skills-directory plugins). Updates require pulling or downloading again.

# Notes

Ship with your own CLI or SDK: publish in a marketplace and have the installer or post-install message run or print `claude plugin marketplace add <source>` then `claude plugin install <name>@<marketplace>`; for in-session discovery see the cli-hints page.
