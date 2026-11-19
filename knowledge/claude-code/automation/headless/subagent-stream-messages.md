---
type: "Feature"
title: "Following subagent messages in the stream"
description: "Subagent and forked-skill messages carry parent_tool_use_id; --forward-subagent-text adds text and thinking blocks at every depth."
resource: "https://code.claude.com/docs/en/headless"
tags: [headless, subagents, stream-json, nesting]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.265"
surfaces: [headless, sdk]
requires: "Version minimums listed below"
identifiers:
  - "parent_tool_use_id"
  - "--forward-subagent-text"
  - "CLAUDE_CODE_FORWARD_SUBAGENT_TEXT"
  - "forked-command-"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "headless"
    resource: "https://code.claude.com/docs/en/headless"
    title: "Run Claude Code programmatically"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Messages from subagents, and from skills that run in a subagent, appear in the stream as `assistant` and `user` messages. `parent_tool_use_id` says which run each belongs to; main-conversation messages carry `null`. The first message of a forked skill or foreground subagent is a `user` message with the prompt or skill content. After it, by default Claude Code emits the run's `tool_use` and `tool_result` blocks; with `--forward-subagent-text` or `CLAUDE_CODE_FORWARD_SUBAGENT_TEXT` it also emits text and thinking blocks, so each run's transcript can be rebuilt.

# How to use it

With either option enabled, messages from subagents at every nesting depth are forwarded (spawned with the Agent tool or started as a forked skill); a nested subagent's messages carry the ID of the Agent or Skill tool call that started it, so the tree can be rebuilt.

| How the run starts | `parent_tool_use_id` | When messages arrive |
| --- | --- | --- |
| Claude calls Agent tool from main conversation | ID of that Agent `tool_use` block | While the subagent works |
| Claude calls Skill tool for a forked skill | ID of that Skill `tool_use` block | While the forked skill works |
| You pass `/<skill-name>` as the prompt | Value starting `forked-command-` (match on the prefix; the name after can differ) | Together, in order, after the skill finishes |

# Limits and defaults

Minimums if messages are missing: forked skill started by Claude with the Skill tool: v2.1.86+ for `tool_use`/`tool_result`, v2.1.265+ for first `user` message and text/thinking blocks; subagents a forked skill spawns, and forked skills started inside a subagent or another forked skill: v2.1.275+; forked skill started via `/<skill-name>` prompt: v2.1.287+.
