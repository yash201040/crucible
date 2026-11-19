---
type: "Limit"
title: "Plugin name rules and reserved names"
description: "name must be non-empty with no spaces, @, : or path separators; validate errors or warns on names that pass as Anthropic's own."
resource: "https://code.claude.com/docs/en/plugins/manifest-reference"
tags: [plugins, naming, reserved-names, validation]
kind: "limit"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "claude-"
  - "anthropic-"
  - "anthropics-"
  - "cc-plugin-"
  - "claude-code"
  - "claude-mods"
  - "claude plugin init"
  - "claude plugin tag"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-manifest-reference"
    resource: "https://code.claude.com/docs/en/plugins/manifest-reference"
    title: "Plugin manifest reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`name` must be non-empty, with no spaces, `@`, `:`, path separators, control characters or bidirectional-formatting characters; use kebab-case. Every component is namespaced under it: agent `reviewer` in plugin `deploy-tools` appears as `deploy-tools:reviewer`.

# How to use it

`claude plugin validate` checks the name does not pass as one of Anthropic's own (case ignored, any run of separators counted as one):

| Name | Result |
| :- | :- |
| Starts with `claude-`, `anthropic-`, `anthropics-` or `cc-plugin-` | Error |
| Is `claude`, `anthropic`, `anthropics`, `claude-code` or `claude-mods` | Error |
| `official` beside `claude` or `anthropic` (e.g. `official-claude-tools`) | Error |
| `claude`, `anthropic` or `anthropics` as a whole word elsewhere (e.g. `mcp-for-claude`) | Warning |

# Limits and defaults

Messages: `Plugin name "<name>" is reserved: it passes as one of Anthropic's own` and `Plugin name "<name>" reads as one of Anthropic's own`. `claude plugin init` and `claude plugin tag` refuse a name that draws the error; Claude Code still installs and loads such a plugin.
