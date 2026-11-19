---
type: "Reference"
title: "Glossary: extensions, hooks, MCP, commands"
description: "Definitions of hook, skill, plugin, command, frontmatter, MCP, MCP Tool Search, connector, output style and artifact terms."
resource: "https://code.claude.com/docs/en/glossary"
tags: [glossary, hooks, skills, plugins, mcp]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "SKILL.md"
  - ".claude/commands/"
  - ".claude/skills/"
  - ".mcp.json"
  - "claude mcp add"
  - "/mcp"
  - "/plugin"
  - "plugin-name:skill-name"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "glossary"
    resource: "https://code.claude.com/docs/en/glossary"
    title: "Glossary"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Glossary terms about extension points and configuration formats.

# How to use it

| Term | Definition |
| :- | :- |
| Hook | A user-defined handler fired at a fixed lifecycle point (before a tool, after an edit, session start). Handler types: shell command, HTTP endpoint, MCP tool, LLM prompt, or subagent. Three levels: hook event, matcher, hook handler. Deterministic rather than at the model's discretion. |
| Skill | A `SKILL.md` file of instructions Claude loads when relevant or you invoke with `/skill-name`. Follows the Agent Skills open standard, extended with invocation control and subagent execution. Recommended successor to custom commands: `.claude/commands/deploy.md` and `.claude/skills/deploy/SKILL.md` both create `/deploy`. |
| Command | A `/name` instruction; built-ins (`/clear`, `/model`, `/compact`), custom files in `.claude/commands/`, or from plugins. Unrelated senses: `claude` CLI subcommands such as `claude mcp add`, and the `command` field of a stdio MCP server entry. |
| Plugin | A bundle of skills, hooks, subagents and MCP servers as one installable unit; plugin skills are namespaced `plugin-name:skill-name`; distributed via a marketplace. |
| Frontmatter | YAML block between `---` lines at the top of a Markdown file (skills, subagents, output styles, rules); the opening `---` must be the first line; each file type accepts its own fields. |
| MCP | An open standard for connecting tools to external data and services; connect via `/mcp` or `.mcp.json`. |
| MCP server | A program providing tools, prompts or resources over MCP; added with `claude mcp add`, `.mcp.json`, a plugin or a claude.ai connector; a local stdio server runs from its `command` and `args`. |
| MCP Tool Search | Defers MCP tool schemas: only names and server instructions load at startup; the full schema is fetched on demand. |
| Connector | An MCP server added to your claude.ai account; appears in `/mcp` when signed in with that account; organizations can provision connectors with per-tool controls. |
| Output style | Changes the instructions given to Claude (tone, format); a custom style adds its own instructions and can drop the default software-engineering ones, unlike CLAUDE.md which adds context alongside the defaults. |
| Artifact | A live web page published from the session to a private URL on claude.ai, updated in place on republish; shares a gallery with claude.ai artifacts; sharing depends on plan. |
