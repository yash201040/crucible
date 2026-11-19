---
type: "Feature"
title: "Invoke and detect subagents"
description: "Claude delegates automatically from descriptions or on explicit mention; detect Agent tool_use blocks, parent_tool_use_id and agent_id in the stream."
resource: "https://code.claude.com/docs/en/agent-sdk/subagents"
tags: [subagents, detection, parent-tool-use-id, agent-id]
kind: "api"
maturity: "unlabelled"
since: "0.3.292"
surfaces: [sdk]
requires: "agent_id needs TypeScript Agent SDK v0.3.292 or later"
identifiers:
  - "Agent"
  - "Task"
  - "parent_tool_use_id"
  - "agent_id"
  - "task_id"
  - "tool_use"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-subagents"
    resource: "https://code.claude.com/docs/en/agent-sdk/subagents"
    title: "Subagents in the SDK"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude decides when to invoke a subagent from the task and each `description`; you can also name it ("Use the code-reviewer agent to check the authentication module").

# How to use it

- Detect invocation: a `tool_use` block whose `name` is `"Agent"`. It appears as `"Task"` in the `system:init` tools list, and before Claude Code v2.1.63 `tool_use` blocks also said `"Task"`; match both.
- Messages from inside a subagent have `parent_tool_use_id`. In TypeScript each assistant and user message from a subagent also has `agent_id`, equal to the `task_id` of its task events and stable across resume.
- Python reads blocks from `message.content`; TypeScript from `message.message.content`.

# Notes

If Claude does not delegate: mention the subagent by name and write a clear description. Filesystem agents not loading: Claude Code watches `~/.claude/agents/` and `.claude/agents/` and picks up edits within seconds, but a new `agents` directory created after session start needs a restart; also check invalid frontmatter or a duplicate `name`; sessions started with `--disable-slash-commands` do not watch and need a restart; directories added via `add_dirs`/`additionalDirectories`, `--add-dir` or `/add-dir` are loaded but not watched; a programmatic agent of the same name overrides.
