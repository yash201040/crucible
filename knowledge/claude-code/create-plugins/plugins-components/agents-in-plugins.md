---
type: "Feature"
title: "Subagents in a plugin"
description: "Ship subagents as agents/*.md, with scoped names, subfolder naming, and which frontmatter fields plugin agents support or ignore."
resource: "https://code.claude.com/docs/en/plugins/components"
tags: [plugins, subagents, frontmatter, naming]
kind: "frontmatter"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "agents/"
  - "agents"
  - "name"
  - "description"
  - "model"
  - "effort"
  - "maxTurns"
  - "autoCompactWindow"
  - "tools"
  - "disallowedTools"
  - "skills"
  - "memory"
  - "background"
  - "omitClaudeMd"
  - "isolation"
  - "color"
  - "experimental.cacheTtl"
  - "permissionMode"
  - "hooks"
  - "mcpServers"
  - "initialPrompt"
  - "@agent-<plugin>:<name>"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-components"
    resource: "https://code.claude.com/docs/en/plugins/components"
    title: "Add components to a plugin"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Each Markdown file under `agents/` defines a subagent with its own instructions and context window. The frontmatter names it and says when to use it; the body is its system prompt. It is named `<plugin>:<name>` where `<name>` is the frontmatter `name` or the file name if missing. The user can invoke it with `@agent-my-plugin:security-reviewer`. The `agents` manifest key replaces the `agents/` scan.

# How to use it

Subfolders are loaded recursively. Names join plugin, subfolders and file name with colons: `agents/review/security.md` in `my-plugin` is `my-plugin:review:security`.
- Frontmatter `name: audit` replaces only the file name: `my-plugin:review:audit`.
- A file listed in the manifest `agents` field loads without subfolder names: `"agents": "./custom/review/security.md"` gives `my-plugin:security`.

# Limits and defaults

| Frontmatter | Status in plugin agents |
| :- | :- |
| `name`, `description`, `model`, `effort`, `maxTurns`, `autoCompactWindow`, `tools`, `disallowedTools`, `skills`, `memory`, `background`, `omitClaudeMd`, `isolation`, `color`, `experimental.cacheTtl` | Supported |
| `permissionMode`, `hooks`, `mcpServers`, `initialPrompt` | Ignored |

- The only valid `isolation` value is `"worktree"`.
- An agent file cannot add hooks or MCP servers; add them as plugin hooks and MCP servers.
- A `name` over 256 characters is ignored and the file name is used.
- Frontmatter that does not parse: the agent still loads with all fields ignored, named after the file, with description `Agent from my-plugin plugin`. `claude plugin validate` finds these.
