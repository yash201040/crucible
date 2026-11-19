---
type: "Guide"
title: "Debug hooks and MCP servers that do not load"
description: "Causes when hooks do not register or fire and when MCP servers show no tools, with the matcher rules and the project approval reset."
resource: "https://code.claude.com/docs/en/debug-your-config"
tags: [hooks, mcp, matcher, debugging, approval]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.191"
surfaces: [cli]
requires: ""
identifiers:
  - "claude mcp reset-project-choices"
  - "claude --debug=mcp"
  - "claude --debug"
  - "~/.claude/debug/<session-id>.txt"
  - ".mcp.json"
  - "matcher"
  - "mcpServers"
  - "hooks"
  - "hooks/hooks.json"
  - "SessionEnd"
  - "PreToolUse"
  - "PermissionRequest"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "debug-your-config"
    resource: "https://code.claude.com/docs/en/debug-your-config"
    title: "Debug your configuration"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Checks for two common failure classes: hooks that are not listed or never fire, and MCP servers that provide no tools.

# How to use it

Hooks (`/hooks` lists every registered hook):
- Hooks belong under the `"hooks"` key of a settings file, not a standalone file. Only plugins load a separate `hooks/hooks.json`.
- A `matcher` that is a JSON array is an invalid setting (shown at interactive start and in `claude doctor`). If it is under `PreToolUse` or `PermissionRequest`, none of that file's other hooks load.
- A hook in a skill's frontmatter appears only after the skill was invoked in the session.
- `matcher` is one string; separate tool names with `|` (for example `"Edit|Write"`). `,` is equivalent from v2.1.191; before that a comma was treated as regex and matched nothing.
- Matching is case-sensitive (`Bash`, `Edit`, `Write`, `Read`); a misspelled name matches nothing and fails silently.
- No `SessionEnd` hook means no end-of-session cleanup runs.
- Editing `settings.json` takes effect in the running session after a brief stability delay; no restart. Before v2.1.257, a `.claude/` folder created after session start was not watched.
- If `/hooks` shows the hook but it does not fire, start with `claude --debug`.

MCP servers (`/mcp` shows status):
- Project servers in `.mcp.json` need one-time approval. If dismissed, run `claude mcp reset-project-choices` and restart; it asks again for every project server.
- `.mcp.json` goes at the repository root (not inside `.claude/`) with servers under `mcpServers` (not `servers`). `settings.json` does not read `mcpServers`.
- A failed server often uses relative paths in `command` or `args`; these resolve against the launch directory. Use absolute paths for local scripts (`npx`/`uvx` on PATH are fine).
- Connected with zero tools: choose Reconnect in `/mcp`, then `claude --debug=mcp` and read stderr in `~/.claude/debug/<session-id>.txt`.
- Stdio servers get Claude Code's environment minus stripped variables; set per-server `env` in the `.mcp.json` entry.

# Notes

Bash deny rules match the literal command string, so `Bash(rm *)` does not block `/bin/rm` or `find -delete`; use a PreToolUse hook or the sandbox for a hard guarantee.
