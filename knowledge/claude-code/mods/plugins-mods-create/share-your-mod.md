---
type: "Guide"
title: "Share and version a mod"
description: "A mod is a plugin: share by folder, marketplace, managed settings or directory; develop against --plugin-dir not the installed copy."
resource: "https://code.claude.com/docs/en/plugins/mods/create"
tags: [mods, sharing, marketplace, versioning]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "claude plugin validate"
  - "--plugin-dir"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-create"
    resource: "https://code.claude.com/docs/en/plugins/mods/create"
    title: "Create a mod"
stale_after: "2027-01-19T00:00:00Z"
---

# How to use it

A mod is versioned in the manifest and installed and updated with `/plugin` commands. Audiences: a few people (send the directory or `.zip`); your team (your own marketplace, possibly registered in repository settings); your organization (an administrator installs the organization's mods through managed settings); anyone (public marketplace repo or Anthropic's directory).

# Limits and defaults

`claude plugin validate` fails a plugin `name` that looks like one of Anthropic's own, such as one starting with `claude-`. Events and methods change between releases, so state the tested Claude Code version in the README. Claude Code caches an installed plugin by version, so edits do not reach an installed copy until you increment the version and reinstall; develop against the directory with `--plugin-dir`.
