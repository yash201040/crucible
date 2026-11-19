---
type: "Feature"
title: "Session-only subagents via --agents"
description: "Pass subagent definitions as JSON (or a JSON file in non-interactive mode) when launching Claude Code; they are not saved to disk."
resource: "https://code.claude.com/docs/en/sub-agents"
tags: [subagents, cli, json, headless, automation]
kind: "cli_flag"
maturity: "unlabelled"
since: "2.1.281"
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "--agents"
  - "--append-subagent-system-prompt"
  - "--append-subagent-system-prompt-file"
  - "prompt"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sub-agents"
    resource: "https://code.claude.com/docs/en/sub-agents"
    title: "Create custom subagents"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`--agents` takes a JSON object whose top-level keys are agent names (do not start a name with `-`) and whose values are definitions. They exist only for that session, useful for tests and automation scripts. Multiple agents can be defined in one call.

# How to use it

```bash
claude --agents '{"code-reviewer":{"description":"...","prompt":"...","tools":["Read","Grep","Glob","Bash"],"model":"sonnet"}}'
```

PowerShell uses a `@' ... '@` here-string.

Non-interactive mode also accepts a file path: `claude -p --agents ./agents.json "Review my changes"` (file form needs v2.1.281 or later; an interactive session refuses a file path).

A definition accepts `prompt` (system prompt, equivalent to the markdown body) plus these frontmatter fields: `description`, `tools`, `disallowedTools`, `model`, `permissionMode`, `mcpServers`, `hooks`, `maxTurns`, `autoCompactWindow`, `skills`, `initialPrompt`, `memory`, `effort`, `background`, `omitClaudeMd`, `isolation`. `color` and `experimental` are ignored, not rejected.

# Limits and defaults

- `prompt` may be empty (v2.1.281 or later). Selecting an agent with an empty prompt and no `memory` via `--agent` leaves the session system prompt unchanged.
- Appending to every subagent's system prompt (nested included, but not a fork, which reuses the conversation's prompt): non-interactive `--append-subagent-system-prompt` (v2.1.205 or later) or `--append-subagent-system-prompt-file <path>` (v2.1.261 or later).
- `--strict-mcp-config` does not filter servers passed inline via `--agents` or the SDK `agents` option, since they are explicit caller input.
- Invalid values: see the `Invalid --agents configuration` error entry.
