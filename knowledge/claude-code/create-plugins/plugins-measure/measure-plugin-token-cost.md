---
type: "Feature"
title: "Measure plugin cost with plugin details"
description: "claude plugin details prints the component inventory and projected always-on and on-invoke token cost of a loaded plugin."
resource: "https://code.claude.com/docs/en/plugins/measure"
tags: [plugins, cost, tokens, context]
kind: "slash_command"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "claude plugin details"
  - "--plugin-dir"
  - "/context"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-measure"
    resource: "https://code.claude.com/docs/en/plugins/measure"
    title: "Measure plugin cost and usage"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

In every session where a plugin is enabled, the names and descriptions of its skills, agents and commands are in Claude's context and count against usage whether or not the plugin is used. `claude plugin details <name>` (a shell command, not a session prompt) shows the number. The plugin must be loaded: installed, in a skills directory, or passed in the same command (`claude --plugin-dir ./formatter plugin details formatter`).

# How to use it

Output sections: Component inventory (commands counted with skills; hooks marked harness-only with no model context cost; MCP servers get no estimate, tool schemas resolved at runtime), Projected token cost (`Always-on: ~146 tok added to every session`), and a Per-component table with always-on and on-invoke columns. On-invoke is the body loaded each time a skill or agent fires. Token counts are estimates.

To see what a plugin's MCP tools add, run `/context` in a session with the plugin enabled and read the `MCP tools` category.

# Notes

The always-on figure counts each component's name plus its `description` and `when_to_use` frontmatter. In the official marketplace, `/plugin` shows a **Context cost** section (`Every turn:` and `When invoked:`) before install, highlighting `Every turn:` at 2,000 tokens or more; plugins in your own marketplace have no such section. Lowering the figure: shorten descriptions, split a large plugin; check skill triggering afterwards with a `tool_used: Skill` grader in an eval suite.
