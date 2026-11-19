---
type: "Feature"
title: "Define subagents programmatically"
description: "Use the agents option of query() to define subagents Claude spawns through the Agent tool; also filesystem agents and the built-in general-purpose agent."
resource: "https://code.claude.com/docs/en/agent-sdk/subagents"
tags: [subagents, agents-option, agent-tool, sdk]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "agents"
  - "AgentDefinition"
  - "Agent"
  - "general-purpose"
  - ".claude/agents/"
  - "CLAUDE_AGENT_SDK_DISABLE_BUILTIN_AGENTS"
  - "subagent_type is required"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-subagents"
    resource: "https://code.claude.com/docs/en/agent-sdk/subagents"
    title: "Subagents in the SDK"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Subagents are separate agent instances the main agent spawns for focused subtasks. Three creation routes: programmatic (`agents` parameter in `query()` options; recommended for SDK apps), filesystem (markdown files in `.claude/agents/`), and the built-in `general-purpose` subagent.

# How to use it

- Pass `agents: { "code-reviewer": { description, prompt, tools, model } }` (Python: `AgentDefinition(...)`). Claude invokes them through the `Agent` tool, so include `"Agent"` in `allowedTools` to auto-approve.
- Programmatic agents take precedence over filesystem agents with the same name.
- Definitions can be built at runtime by a factory function (e.g. different `model` and prompt by strictness level).
- Benefits: context isolation (only the final message returns to the parent), parallelization, specialized prompts, tool restrictions.

# Limits and defaults

When Claude calls the Agent tool without a `subagent_type` it gets the built-in `general-purpose` subagent, even with no agents defined. `CLAUDE_AGENT_SDK_DISABLE_BUILTIN_AGENTS=1` removes that default; such a call then fails with `subagent_type is required`.

# Notes

Field list: [AgentDefinition fields](./agentdefinition-fields.md). Invocation: [invoke and detect](./invoke-and-detect-subagents.md).
