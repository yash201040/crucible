---
type: "Feature"
title: "MCP prompts as slash commands"
description: "Server prompts appear as /servername:promptname (MCP) or /mcp__servername__promptname, with space-separated arguments."
resource: "https://code.claude.com/docs/en/mcp"
tags: [mcp, prompts, slash-commands, naming]
kind: "slash_command"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "/servername:promptname"
  - "/mcp__servername__promptname"
  - "anthropic-skills"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "mcp"
    resource: "https://code.claude.com/docs/en/mcp"
    title: "Connect Claude Code to tools via MCP"
stale_after: "2027-01-19T00:00:00Z"
---

# How to use it

Type `/` to list prompts as `/servername:promptname (MCP)`; `/mcp__servername__promptname` also runs one. Pass arguments space-separated after the command, for example `/mcp__github__pr_review 456` or `/mcp__jira__create_issue login-bug high`. Claude Code splits on whitespace, so each argument is one token; arguments follow the prompt's defined parameters, and the result is injected into the conversation. Prompts are discovered dynamically from connected servers.

# Limits and defaults

In the `/mcp__servername__promptname` form, characters of the server name outside `A-Z a-z 0-9 _ -` become `_`; the prompt name is used as declared. A server named `anthropic-skills` has its prompts hidden (name reserved for skills synced from claude.ai); its tools still work, so rename the server to list prompts.
