---
type: "Feature"
title: "Turning off agent view"
description: "disableAgentView and CLAUDE_CODE_DISABLE_AGENT_VIEW disable background agents and agent view entirely."
resource: "https://code.claude.com/docs/en/agent-view"
tags: [agent-view, disable, managed-settings]
kind: "setting"
maturity: "research-preview"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "disableAgentView"
  - "CLAUDE_CODE_DISABLE_AGENT_VIEW"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-view"
    resource: "https://code.claude.com/docs/en/agent-view"
    title: "Manage multiple agents with agent view"
stale_after: "2027-01-19T00:00:00Z"
---

# How to use it

Set the `disableAgentView` setting to `true`, or set the `CLAUDE_CODE_DISABLE_AGENT_VIEW` environment variable. Administrators can enforce it via managed settings. When off, `/fork` starts a forked subagent, `/subtask` is unavailable, and the `Move to background and exit` option is not shown.

# Notes

If `claude agents` prints a count and lists configured subagents instead of opening the view, agent view is unavailable: run `claude update`, then check whether it was turned off.
