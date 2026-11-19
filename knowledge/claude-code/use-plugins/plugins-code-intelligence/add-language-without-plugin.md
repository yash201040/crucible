---
type: "Guide"
title: "Add a language without an official plugin"
description: "Connect any language server by writing a plugin with an .lsp.json file and loading it with --plugin-dir or a marketplace."
resource: "https://code.claude.com/docs/en/plugins/code-intelligence"
tags: [lsp, custom-plugin, plugin-dir]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - ".lsp.json"
  - "--plugin-dir"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-code-intelligence"
    resource: "https://code.claude.com/docs/en/plugins/code-intelligence"
    title: "Code intelligence plugins"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

For a language not in the [official table](./language-server-plugins.md), write a plugin containing an `.lsp.json` that names the server command and the file extensions it handles.

# How to use it

Load it for one session with `--plugin-dir` or publish it to a marketplace. The `.lsp.json` fields and a worked example are on the plugin components page (LSP servers section).
