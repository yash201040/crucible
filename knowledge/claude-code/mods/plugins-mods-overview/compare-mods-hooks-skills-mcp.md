---
type: "Reference"
title: "Compare mods, settings hooks, skills and MCP servers"
description: "Table of what each extension kind is, what it can change and when to pick it."
resource: "https://code.claude.com/docs/en/plugins/mods/overview"
tags: [mods, hooks, skills, mcp]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers: []
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-overview"
    resource: "https://code.claude.com/docs/en/plugins/mods/overview"
    title: "Mods overview"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

| | Mod | Settings hook | Skill | MCP server |
| :- | :- | :- | :- | :- |
| Is | functions in a plugin, called in Claude Code's own process | shell command, HTTP request or prompt on a lifecycle event | `SKILL.md` of instructions | external process/service giving tools |
| Can change | tool calls, prompts, commands, turns, what the interface draws | whether a tool call or prompt proceeds, tool arguments/result, added context | what Claude knows and does | which tools Claude has |
| Draw in interface | Yes | No | No | No |
| You write | JavaScript or TypeScript | script plus a `settings.json` entry | Markdown | server in any language |
| Pick when | you want a pane, band, custom command or to rewrite an event | you want to block, allow or log with an existing script | you keep pasting the same instructions | Claude needs an external system |

# Notes

A plugin can hold all of them, so a mod can ship with a skill and an MCP server.
