---
type: "Reference"
title: "Agent teams compared with subagents"
description: "Side-by-side of context, communication, coordination, best use and token cost for subagents versus agent teams, with the recommended use cases."
resource: "https://code.claude.com/docs/en/agent-teams"
tags: [agent-teams, subagents, comparison, use-cases]
kind: "behavior"
maturity: "experimental"
since: ""
surfaces: [cli]
requires: ""
identifiers: []
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-teams"
    resource: "https://code.claude.com/docs/en/agent-teams"
    title: "Orchestrate teams of Claude Code sessions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Both parallelize work but differ in structure.

# How to use it

| | Subagents | Agent teams |
| - | - | - |
| Context | own window; results return to the caller | own window; fully independent |
| Communication | return a result to the caller; subagents Claude named at spawn can also message each other | teammates message each other directly |
| Coordination | main agent manages all work | self-coordination via messages, plus a shared task list for agents that have the Task tools |
| Best for | focused tasks where only the result matters | complex work needing discussion and collaboration |
| Token cost | lower, results summarized back | higher, each teammate is a separate instance |

Strongest use cases: research and review; new modules or features each owned by a teammate; debugging with competing hypotheses; cross-layer coordination (frontend, backend, tests). Example prompts: a three-teammate parallel PR review (security, performance, test coverage) and a five-teammate adversarial debugging debate that updates a findings doc.

# Notes

For sessions that pass messages without a team, see cross-session messaging. For manual parallel sessions without automated coordination, see git worktrees.
