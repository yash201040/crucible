---
type: "Feature"
title: "TeammateIdle hook event"
description: "Fires when an agent team teammate is about to go idle; can keep it working or force idle."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, agent-teams, teammateidle, quality-gates]
kind: "hook"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: "agent teams"
identifiers:
  - "TeammateIdle"
  - "teammate_name"
  - "team_name"
  - "agent_id"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Runs when an agent team teammate is about to go idle after its turn. Use for quality gates (passing lint, output files exist). No matchers; fires on every occurrence.

# How to use it

Input adds `teammate_name`, `team_name` (deprecated, will be removed), and `agent_id` (identifies the in-process teammate; may be absent; v2.1.290 or later).

- Exit 2: teammate gets stderr as feedback and keeps working.
- `{"decision": "block", "reason": "..."}`: teammate gets `reason` and keeps working.
- `{"continue": false, "stopReason": "..."}`: teammate goes idle even if another TeammateIdle hook blocks; `stopReason` appears in its transcript.

A prompt hook here: by default the teammate goes idle and the reason shows in its transcript; `continueOnBlock: true` sends the reason and keeps it working.
