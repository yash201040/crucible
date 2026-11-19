---
type: "Feature"
title: "Code intelligence plugins"
description: "LSP-backed plugins let Claude find definitions and references without scanning files; install from the official marketplace."
resource: "https://code.claude.com/docs/en/large-codebases"
tags: [plugins, lsp, code-intelligence, marketplace]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, ide, desktop]
requires: "The language server binary on each developer's machine; network access to GitHub for the official marketplace"
identifiers:
  - "/plugin install typescript-lsp@claude-plugins-official"
  - "/plugin marketplace add anthropics/claude-plugins-official"
  - "/plugin marketplace update claude-plugins-official"
  - "enabledPlugins"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "large-codebases"
    resource: "https://code.claude.com/docs/en/large-codebases"
    title: "Set up Claude Code in a monorepo or large codebase"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Code intelligence plugins connect Claude to a language server for jump-to-definition, find-references and type errors, replacing many file reads and greps. The official marketplace has plugins for TypeScript, Python, Go, Rust and others.

# How to use it

In a terminal, at the `claude` prompt: `/plugin install typescript-lsp@claude-plugins-official`. In the VS Code extension or desktop app, use Install a plugin.

| Error | Fix |
| :- | :- |
| `Marketplace "claude-plugins-official" not found` | `/plugin marketplace add anthropics/claude-plugins-official`, retry |
| `Plugin "<name>" not found in marketplace "claude-plugins-official"` | `/plugin marketplace update claude-plugins-official`, retry |

Enable for everyone in the repo with the `enabledPlugins` project setting; each person still installs it.

# Notes

On a restricted network, add the marketplace from an internal Git host or local path. Pairs with `claudeMdExcludes` and Read deny rules (those keep irrelevant content out; this avoids reading the rest to locate definitions).
