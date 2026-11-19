---
type: "Reference"
title: "Component path forms"
description: "Accepted shapes for agents, skills, outputStyles, workflows, commands, hooks and mcpServers entries in plugin.json, with merge behavior."
resource: "https://code.claude.com/docs/en/plugins/manifest-reference"
tags: [plugins, manifest, hooks, mcp]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "source"
  - "content"
  - "argumentHint"
  - "model"
  - "allowedTools"
  - ".mcpb"
  - ".dxt"
  - "hooks/hooks.json"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-manifest-reference"
    resource: "https://code.claude.com/docs/en/plugins/manifest-reference"
    title: "Plugin manifest reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Every component key accepts a path relative to the plugin root. `hooks`, `mcpServers`, `lspServers` and `experimental.monitors` also accept inline config; `commands` also accepts an object map; `mcpServers` also accepts MCP bundle paths and URLs.

# How to use it

- **Path-only fields** (`agents`, `skills`, `outputStyles`, `workflows`, `experimental.themes`): one path or an array. `agents` entries must be `.md` files; `skills` entries must be directories; the other three accept a directory or a file.
- **`commands`**: a path (flat `.md` file or directory), array, or object map where each key becomes the command name after the plugin prefix (`"about"` in `deploy-tools` runs `/deploy-tools:about`). Each value sets exactly one of `source` or `content`; both or neither fails validation.

| Command field | Type | Description |
| :- | :- | :- |
| `source` | string | Markdown file path relative to plugin root |
| `content` | string | Inline Markdown body, instead of `source` |
| `description` | string | Description shown |
| `argumentHint` | string | Hint after the command name, e.g. `[file]` |
| `model` | string | Default model for the command |
| `allowedTools` | array of strings | Tools the command may use without prompting |

- **`hooks`**: a `.json` file path, an inline hooks object (same shape as `hooks` in `settings.json`), or an array mixing both. A hooks file must wrap the event map in a top-level `"hooks"` key (as `hooks/hooks.json`); a file with only the event map fails to load. An inline object is the event map itself with no wrapper. Merged with `hooks/hooks.json` when it exists.
- **`mcpServers`**: `.json` file path, MCP bundle path or URL, inline map, or array. `.mcp.json` at the plugin root loads first, then each declared shape in order; a later server name replaces an earlier one.

| `mcpServers` shape | Example | What Claude Code does |
| :- | :- | :- |
| `.json` path | `"./mcp/servers.json"` | Reads as an `mcpServers` map |
| Bundle path | `"./bundle.mcpb"` | Extracts the `.mcpb`/`.dxt` bundle into `mcpb/` under the plugins root and reads its config |
| Bundle URL | `"https://example.com/server.mcpb"` | Downloads, extracts, reads |
| Inline map | `{ "deploy-api": { "command": "node", "args": [...] } }` | Server configs keyed by name |

# Limits and defaults

A bundle path or URL must end in `.mcpb` or `.dxt`; other extensions fail validation.
