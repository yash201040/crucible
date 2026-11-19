---
type: "Feature"
title: "Agent tool behavior"
description: "How the Agent tool spawns subagents, teammates and forks, resolves tool lists, caps turns and surfaces permission prompts."
resource: "https://code.claude.com/docs/en/tools-reference#agent-tool-behavior"
tags: [subagents, agent-tool, tools, permissions, maxturns]
kind: "tool"
maturity: "unlabelled"
since: ""
surfaces: [cli, sdk]
requires: ""
identifiers:
  - "Agent"
  - "maxTurns"
  - "tools"
  - "disallowedTools"
  - "isolation: worktree"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "tools-reference"
    resource: "https://code.claude.com/docs/en/tools-reference"
    title: "Tools reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The Agent tool starts a subagent in a separate context window. The parent sees only its final result, not intermediate tool calls. It can also launch a teammate (agent teams enabled and a `name` given; reports via team messages) or a fork (where fork mode is on; inherits the full parent conversation).

# How to use it

- Cap turns with `maxTurns` in the subagent definition; at the limit the result is marked partial and Claude can resume the subagent.
- Tool resolution for non-fork subagents: neither field set means inherit all tools available to subagents; `tools` only means just those; `disallowedTools` only means every parent tool except those; both set means `disallowedTools` wins. The result is always limited to tools available to subagents. `SubagentHandback` is added when its conditions hold, even if omitted from `tools` or listed in `disallowedTools`.
- If every entry in `tools` fails to match, the Agent tool usually errors naming the entries instead of launching (see the "Agent would be spawned with zero tools" error).
- Launching does not prompt; the subagent's own tool calls are checked against permission rules.

# Limits and defaults

Subagents run in the background by default, apart from specific cases that run in the foreground. Foreground subagents show permission prompts in place; background subagents surface prompts in the main session naming the subagent, and `Esc` denies that one call without stopping the subagent. To limit reach, narrow `tools` (for example leave off Bash) or set deny rules.
