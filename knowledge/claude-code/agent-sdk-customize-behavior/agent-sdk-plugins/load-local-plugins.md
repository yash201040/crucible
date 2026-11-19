---
type: "Feature"
title: "Load local plugins in the SDK"
description: "Pass local plugin directories in the plugins option of query() so a session gets their skills, agents, hooks and MCP servers."
resource: "https://code.claude.com/docs/en/agent-sdk/plugins"
tags: [plugins, sdk, options, local]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "plugins"
  - "type: \"local\""
  - "path"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-plugins"
    resource: "https://code.claude.com/docs/en/agent-sdk/plugins"
    title: "Plugins in the SDK"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A plugin bundles skills, agents (subagents), hooks and MCP servers that can be shared across projects. In the Agent SDK you load plugins programmatically from local directories to add these to a session.

# How to use it

Give a list of `{ type: "local", path }` objects in the `plugins` option (TypeScript `options.plugins`, Python `ClaudeAgentOptions(plugins=[...])`). Several plugins from different places can be combined.

- `type` must be `"local"`; it is the only value the SDK accepts.
- `path` may be relative (resolved against the `cwd` option) or absolute.
- The path must be the plugin root: the parent of `skills/`, `agents/`, `hooks/`, `commands/` or `.claude-plugin/`.
- A plugin from a marketplace or remote repo must be downloaded first; give its local directory.
- A plugin installed through the CLI (`/plugin install my-plugin@marketplace`) can be used by giving its install path; look under `~/.claude/plugins/`.

# Limits and defaults

- The SDK does not expand tilde paths such as `~/plugins`; build the path (for example with `os.homedir()`).
- If a path does not exist, the SDK skips that plugin and the session continues. Check the `plugins` list of the init message to confirm each loaded.

# Notes

Plugin skills are namespaced; see [plugin skills](./use-plugin-skills.md). To change plugins in a running session see [reload and add plugins](./reload-and-add-plugins.md).
