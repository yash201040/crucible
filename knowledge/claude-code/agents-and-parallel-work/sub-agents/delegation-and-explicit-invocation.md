---
type: "Feature"
title: "Delegation, @-mention and --agent"
description: "Automatic delegation by description, @-mention syntax, running a whole session as a subagent with --agent or the agent setting."
resource: "https://code.claude.com/docs/en/sub-agents"
tags: [subagents, delegation, mention, agent-flag]
kind: "cli_flag"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "--agent"
  - "agent"
  - "@agent-<name>"
  - "claude plugin eval"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sub-agents"
    resource: "https://code.claude.com/docs/en/sub-agents"
    title: "Create custom subagents"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude delegates based on the request, each subagent's `description` and context; phrases like "use proactively" in a description encourage it. Three explicit routes escalate: natural language, @-mention (one task), session-wide.

# How to use it

- Natural language: "Use the test-runner subagent to fix failing tests".
- @-mention: pick from typeahead, e.g. `@"code-reviewer (agent)" look at the auth changes`, or type `@agent-<name>`; plugin subagents `@agent-my-plugin:code-reviewer`. Your full message still goes to Claude, which writes the task prompt. Running named background subagents also appear in the typeahead.
- Session-wide: `claude --agent code-reviewer` (plugin agents: `claude --agent security-reviewer`, or scoped `my-plugin:security-reviewer`, `my-plugin:review:security`). Default for a project: `{"agent": "code-reviewer"}` in `.claude/settings.json`; the CLI flag overrides.
- Measure delegation reliability for a plugin's subagent with `claude plugin eval` (runs each prompt with and without the plugin).

# Limits and defaults

- With `--agent`, a custom agent's system prompt replaces the default Claude Code system prompt (like `--system-prompt`) unless its prompt is empty. CLAUDE.md files and project memory still load, even with `omitClaudeMd`. With `-p` and a custom agent that has its own prompt, the git status snapshot is also omitted.
- The header shows `@<name>`. The choice persists on resume (tool restrictions and model restored); if the agent no longer exists the session continues with default tools and a warning.
