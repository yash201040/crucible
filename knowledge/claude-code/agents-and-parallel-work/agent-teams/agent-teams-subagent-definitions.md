---
type: "Reference"
title: "Using subagent definitions for teammates"
description: "Which subagent frontmatter fields (tools, model, disallowedTools, effort, autoCompactWindow, body, skills, mcpServers) apply to in-process and split-pane teammates."
resource: "https://code.claude.com/docs/en/agent-teams"
tags: [agent-teams, subagents, frontmatter, teammates]
kind: "frontmatter"
maturity: "experimental"
since: "2.1.296"
surfaces: [cli]
requires: "autoCompactWindow on teammates needs v2.1.296 or later"
identifiers:
  - "tools"
  - "model"
  - "disallowedTools"
  - "effort"
  - "autoCompactWindow"
  - "skills"
  - "mcpServers"
  - "SendMessage"
  - "TaskCreate"
  - "TaskGet"
  - "TaskList"
  - "TaskUpdate"
  - ".claude/agents/"
  - "--add-dir"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-teams"
    resource: "https://code.claude.com/docs/en/agent-teams"
    title: "Orchestrate teams of Claude Code sessions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A teammate can be spawned from a subagent definition (project, user, managed or plugin scope) so one role, such as security-reviewer or test-runner, serves as both delegated subagent and teammate. Name it in the prompt: "Spawn a teammate using the security-reviewer agent type to audit the auth module."

# How to use it

| Definition part | In-process teammate | Split-pane teammate |
| - | - | - |
| `tools` | limits to the list; adds `SendMessage`, and in a session with Task tools adds `TaskCreate`, `TaskGet`, `TaskList`, `TaskUpdate` | limits to the list |
| `model` | used when the spawn prompt names none | same |
| `disallowedTools` | removed from the set; `SendMessage` and added Task tools stay available even if listed | not stated |
| `effort` | applied under the frontmatter effort rules | not stated |
| `autoCompactWindow` | applied (v2.1.296 or later) | ignored |
| Body | appended to the default system prompt as extra instructions | used in place of the default system prompt |
| `skills` | not applied; skills load from project and user settings | not applied |
| `mcpServers` | ignored; loads from project and user settings | applied under the subagent MCP-scoping rules |

# Limits and defaults

- When Claude messages an in-process teammate that is no longer running, Claude Code brings it back in the same session, restores any saved conversation and delivers the message as its next prompt. After resuming a session teammates are not brought back this way.
- For a revived teammate, a definition from a project's `.claude/agents/` or an `--add-dir` directory is re-applied only if you trusted the folder containing the agent file; trusting a parent folder does not count. Until then the teammate returns with none of the definition's tools or instructions, only the tools added to every in-process teammate (notice: "the teammate's agent definition was not restored" on the errors page).
