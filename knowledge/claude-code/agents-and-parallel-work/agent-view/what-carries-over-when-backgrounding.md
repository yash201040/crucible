---
type: "Concept"
title: "What carries over when you background"
description: "Which background work and launch flags carry into a backgrounded session, and what happens to dynamic workflows."
resource: "https://code.claude.com/docs/en/agent-view"
tags: [agent-view, backgrounding, workflows, carry-over]
kind: "behavior"
maturity: "research-preview"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "--mcp-config"
  - "--strict-mcp-config"
  - "--settings"
  - "--setting-sources"
  - "--add-dir"
  - "--plugin-dir"
  - "--fallback-model"
  - "--allow-dangerously-skip-permissions"
  - "/add-dir"
  - "Background this session?"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-view"
    resource: "https://code.claude.com/docs/en/agent-view"
    title: "Manage multiple agents with agent view"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

When a session is backgrounded, in-flight work falls in three classes.

| Class | Work |
| :- | :- |
| Carries over | Running background shell commands, backgrounded subagents (only if everything they started can move), `/loop` scheduled tasks |
| Continues only when Claude relaunches it | A running dynamic workflow |
| Stops | Work that cannot move, e.g. a running monitor (a backgrounded subagent owning a monitor stops with it) |

When any such work would stop, the `Background this session?` dialog appears (also for workflows with running subagents, with the count, and for Claude automatically replying to artifact comments); `/tasks` shows everything; choose `Stay` to let it finish. Once backgrounded, the session can start new subagents, monitors and background commands that survive detach and reattach.

Flags carried from the original launch: `--mcp-config`, `--strict-mcp-config`, `--settings`, `--setting-sources`, `--add-dir`, `--plugin-dir`, `--fallback-model`, `--allow-dangerously-skip-permissions` (keeps `bypassPermissions` reachable but still needs the accepted disclaimer), plus directories added with `/add-dir`.

# Notes

Dynamic workflows: if the workflow has not continued, ask Claude to relaunch it; Claude Code may ask you to approve the relaunch and shows a notice `could not be resumed`. Subagents still running restart from the beginning and spend tokens again. The notice `was carried into this session and not resumed` names a background subagent not running; Claude replies on its own.
