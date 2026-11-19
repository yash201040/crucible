---
type: "Reference"
title: "Subagent frontmatter fields"
description: "Every frontmatter field a subagent file accepts, with requirements, versions and special behavior."
resource: "https://code.claude.com/docs/en/sub-agents"
tags: [subagents, frontmatter, reference, fields]
kind: "frontmatter"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "name"
  - "description"
  - "tools"
  - "disallowedTools"
  - "model"
  - "permissionMode"
  - "maxTurns"
  - "autoCompactWindow"
  - "skills"
  - "mcpServers"
  - "hooks"
  - "memory"
  - "background"
  - "omitClaudeMd"
  - "effort"
  - "isolation"
  - "color"
  - "initialPrompt"
  - "experimental"
  - "experimental.cacheTtl"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sub-agents"
    resource: "https://code.claude.com/docs/en/sub-agents"
    title: "Create custom subagents"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Frontmatter sits between `---` markers at the top of a subagent file. Only `name` and `description` are required. Multi-word fields are camelCase and must match exactly: unrecognized fields are ignored without error.

# How to use it

| Field | Required | Description |
| :- | :- | :- |
| `name` | Yes | Unique id, at most 256 characters; hooks receive it as `agent_type`; filename need not match; cannot contain `:` (reserved for plugin-scoped ids) |
| `description` | Yes | When Claude should delegate |
| `tools` | No | Allowlist, comma-separated string or YAML list; inherits all subagent tools if omitted; if nothing resolves the launch usually fails (zero-tools error). Preload skills with `skills`, not `Skill` here |
| `disallowedTools` | No | Denylist removed from inherited or specified list; a specifier like `Bash(git push *)` still removes the whole tool |
| `model` | No | `sonnet`, `opus`, `haiku`, `fable`, a full ID such as `claude-opus-5-5`, or `inherit` |
| `permissionMode` | No | `default`, `acceptEdits`, `auto`, `dontAsk`, `bypassPermissions`, `plan`, or `manual` (alias for `default`); ignored for plugin subagents |
| `maxTurns` | No | Max agentic turns; at the limit output is returned marked partial (v2.1.246 or later) and Claude can resume |
| `autoCompactWindow` | No | Token count of `100000` or more to compact earlier; v2.1.296 or later |
| `skills` | No | Skills whose full content is preloaded at startup |
| `mcpServers` | No | Server names or inline definitions; ignored for plugin subagents |
| `hooks` | No | Lifecycle hooks scoped to this subagent; ignored for plugin subagents |
| `memory` | No | `user`, `project` or `local` persistent memory |
| `background` | No | `true` keeps it in the background even when Claude asks to wait |
| `omitClaudeMd` | No | `true` starts without user, project and local CLAUDE.md; managed policy files still load (except for managed subagents); ignored when run as main session agent; v2.1.271 or later |
| `effort` | No | `low`, `medium`, `high`, `xhigh`, `max` (depends on model); overrides session effort but not `CLAUDE_CODE_EFFORT_LEVEL` |
| `isolation` | No | `worktree` runs in a temporary git worktree branched by default from the default branch; auto-cleaned if no changes |
| `color` | No | `red`, `blue`, `green`, `yellow`, `purple`, `orange`, `pink`, `cyan` |
| `initialPrompt` | No | Auto-submitted first user turn when the agent runs as main session agent (`--agent` or `agent` setting); commands and skills processed; ignored for plugin subagents |
| `experimental` | No | Map of experimental options; `cacheTtl` key set to `5m` or `1h` picks the prompt cache lifetime for the subagent's requests; other values ignored; `1h` ignored while a subscription is using usage credits; read only from subagent files; v2.1.248 or later |

# Notes

- Write `cacheTtl` inside `experimental`, not at top level.
- To find misspelled fields: run `claude --debug` and search `~/.claude/debug/<session-id>.txt` for `does not recognize or apply` (names up to five unrecognized top-level fields; v2.1.296 or later).
