---
type: "Reference"
title: "Referencing hook scripts by path"
description: "Placeholders for project and plugin directories in hook commands, and how they behave inside worktrees."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, paths, worktrees, plugins]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop]
requires: ""
identifiers:
  - "${CLAUDE_PROJECT_DIR}"
  - "${CLAUDE_PLUGIN_ROOT}"
  - "${CLAUDE_PLUGIN_DATA}"
  - "hooks/hooks.json"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Placeholders that locate hook scripts regardless of working directory.

# How to use it

| Placeholder | Meaning |
| :- | :- |
| `${CLAUDE_PROJECT_DIR}` | Project root where the session started; also set in the environment of stdio MCP servers and plugin LSP servers |
| `${CLAUDE_PLUGIN_ROOT}` | Plugin installation directory |
| `${CLAUDE_PLUGIN_DATA}` | Plugin persistent data directory, survives plugin updates |

Prefer exec form for hooks using a placeholder; in shell form wrap each placeholder in double quotes. Plugin hooks go in `hooks/hooks.json` with an optional top-level `description`; when the plugin is enabled they merge with user and project hooks.

# Limits and defaults

Worktrees: if Claude enters a worktree mid-session, `${CLAUDE_PROJECT_DIR}` stays at the original project root, so a script under it still runs from the main checkout. The `cwd` field in the hook input JSON follows Claude (worktree root, or the new directory after `cd`). Worktree sessions started from the desktop app have separate rules (see the worktrees page).
