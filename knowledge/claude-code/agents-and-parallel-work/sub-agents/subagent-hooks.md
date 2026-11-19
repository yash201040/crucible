---
type: "Feature"
title: "Hooks for subagents"
description: "Frontmatter hooks, settings-level SubagentStart and SubagentStop hooks, PreToolUse validation scripts and trust rules."
resource: "https://code.claude.com/docs/en/sub-agents"
tags: [subagents, hooks, validation, trust]
kind: "hook"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "hooks"
  - "PreToolUse"
  - "PostToolUse"
  - "Stop"
  - "SubagentStart"
  - "SubagentStop"
  - "agent_type"
  - "shell: powershell"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sub-agents"
    resource: "https://code.claude.com/docs/en/sub-agents"
    title: "Create custom subagents"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Two ways to hook the subagent lifecycle: `hooks` in the subagent's frontmatter (run only while that subagent is active, cleaned up when it finishes) and `settings.json` hooks (session-wide, also fire inside subagents). Hooks from settings files, managed policy settings and plugins all apply inside subagents; tool events fire for subagent tool calls like in the main conversation.

# How to use it

| Event | Matcher input | When |
| :- | :- | :- |
| `PreToolUse` | Tool name | Before the subagent uses a tool |
| `PostToolUse` | Tool name | After it uses a tool |
| `Stop` | none | When it finishes; converted to `SubagentStop` at runtime |
| `SubagentStart` (settings.json) | Agent type name | When a subagent begins |
| `SubagentStop` (settings.json) | Agent type name | When a subagent completes |

All hook events are supported in frontmatter. Matchers for `SubagentStart`/`SubagentStop` use the `name` (or plugin-scoped id such as `my-plugin:db-agent`); a scoped name contains a colon so it is an unanchored regex: anchor with `^my-plugin:db-agent$`.

Validation pattern: a `PreToolUse` hook with matcher `Bash` runs a script that reads the hook JSON from stdin (`.tool_input.command` via `jq`) and exits with code 2 to block, with the reason on stderr. On macOS/Linux `chmod +x` the script or the hook fails instead of blocking. On Windows use PowerShell and `shell: powershell` on the hook entry.

# Limits and defaults

- Frontmatter hooks fire for subagents (Agent tool or @-mention) and for the main session via `--agent` or the `agent` setting (alongside `settings.json` hooks).
- Project-level subagent frontmatter hooks need the workspace trust dialog accepted for the folder containing the agent file; a parent folder's trust is not enough and a `-p` session does not count. Until then the subagent runs but its hooks are skipped with a debug-log error. User-level (`~/.claude/agents/`) and `--agents` hooks run without this. A folder added by `--add-dir` outside the trusted repository needs its own trust.
