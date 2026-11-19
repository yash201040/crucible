---
type: "Guide"
title: "Test and debug a plugin"
description: "Ordered checks for a plugin that does not load: validate, reload, /plugin tabs, plugin list, plus common failure causes."
resource: "https://code.claude.com/docs/en/plugins/create"
tags: [plugins, debugging, validate, evals]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "claude plugin validate"
  - "--strict"
  - "/reload-plugins"
  - "/plugin"
  - "claude plugin list"
  - "claude plugin eval"
  - "/mcp"
  - "/plugin configure <plugin-name>"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-create"
    resource: "https://code.claude.com/docs/en/plugins/create"
    title: "Create a Claude Code plugin"
stale_after: "2027-01-19T00:00:00Z"
---

# How to use it

1. `claude plugin validate <path>` checks the manifest and frontmatter of every skill, agent and command; exits `0` on pass; `--strict` fails on warnings too.
2. `/reload-plugins` applies edits; prints one `Reloaded:` line with counts.
3. `/plugin`: Installed tab lists components found; Errors tab lists load failures.
4. `claude plugin list` (shell) prints session-only and skills-directory plugins in their own sections with `Status: ✔ loaded` or the error; pass `--plugin-dir <path>` before `plugin list` to include a plugin in development.
5. A skills-directory plugin not listed with no error may be blocked by managed settings.

MCP: `/mcp` shows connection status. Hooks: enable debug logging and trigger the event.

# Notes

Common failures: `<component> path not found: <path>` (for example `commands path not found`) in the Errors tab; `skills/` inside `.claude-plugin/` or a `skills` entry pointing at a file; the `userConfig` dialog never appears with `--plugin-dir` or `claude plugin install` (run `/plugin configure <plugin-name>`). `claude plugin eval` (shell) runs test cases with and without the plugin and scores the difference.
