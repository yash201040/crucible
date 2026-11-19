---
type: "Feature"
title: "SubagentStart and SubagentStop hook events"
description: "Hooks around subagent spawn and finish: inject context into a subagent, or block it from stopping."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, subagents, subagentstart, subagentstop]
kind: "hook"
maturity: "unlabelled"
since: "2.1.271"
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "SubagentStart"
  - "SubagentStop"
  - "agent_id"
  - "agent_type"
  - "agent_transcript_path"
  - "last_assistant_message"
  - "stop_hook_active"
  - "background_tasks"
  - "session_crons"
  - "additionalContext"
  - "general-purpose"
  - "Explore"
  - "Plan"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`SubagentStart` runs when Claude spawns a subagent with the Agent tool, resumes a subagent, and each time an in-process agent team teammate handles a new message. `SubagentStop` runs when a subagent has finished responding. Both match on agent type: built-in names (`general-purpose`, `Explore`, `Plan`) or the `name` field of a custom subagent's frontmatter (not the filename). Plugin subagents use `my-plugin:reviewer`; the colon puts it on the regex path, so anchor with `^my-plugin:reviewer$`.

# How to use it

SubagentStart input adds `agent_id` and `agent_type`. It cannot block creation but can return `hookSpecificOutput.additionalContext`, added to the subagent's context before its first prompt. If the hook runs again for the same subagent, the context is injected only if the subagent does not already hold the earlier copy; the launch copy stays, keeping the subagent's prompt cache intact; after auto-compaction discards it, the next run's context is injected again.

SubagentStop input adds `stop_hook_active`, `agent_id`, `agent_type`, `agent_transcript_path` (nested `subagents/` folder; `transcript_path` is the main session's), `last_assistant_message`, plus the `background_tasks` and `session_crons` arrays (scoped to the parent session; see [Stop](./p2-stop-event.md)).

Decision control is the same as Stop: `decision: "block"` with `reason` keeps the subagent running and delivers `reason` as its next instruction; exit 2 delivers stderr likewise; `hookSpecificOutput.additionalContext` (with `hookEventName: "SubagentStop"`) gives non-error feedback that keeps it running. To inject context into the parent after a subagent returns, use a PostToolUse hook on the `Agent` tool.

# Limits and defaults

- SubagentStop also fires for Claude Code's internal agents (prompt suggestions, `/btw` side questions). There `agent_type` is the agent the session runs as (via `--agent` or the `agent` setting) or an empty string. A matcher naming agent types does not match empty; an omitted, `""`, `"*"` or empty-matching regex matcher does.
- From v2.1.271, with the `SubagentHandback` tool `last_assistant_message` holds the closing text, not the delivered report; read the report from `tool_input.message` of a hook on `SubagentHandback`.
