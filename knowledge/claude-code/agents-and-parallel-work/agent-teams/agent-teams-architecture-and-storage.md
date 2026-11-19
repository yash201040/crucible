---
type: "Reference"
title: "Agent team architecture and on-disk storage"
description: "Team lead, teammates, task list and mailbox components, the file paths for config, tasks and inboxes, and how teams start."
resource: "https://code.claude.com/docs/en/agent-teams"
tags: [agent-teams, architecture, mailbox, storage]
kind: "file"
maturity: "experimental"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "~/.claude/teams/{team-name}/config.json"
  - "~/.claude/teams/{team-name}/inboxes/{agent-name}.json"
  - "~/.claude/tasks/{team-name}/"
  - "cleanupPeriodDays"
  - "team-lead"
  - "Agent tool"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-teams"
    resource: "https://code.claude.com/docs/en/agent-teams"
    title: "Orchestrate teams of Claude Code sessions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A team has four components: the team lead (main session), teammates (separate instances), a shared task list, and a mailbox for messaging.

# How to use it

How teams start: Claude launches a teammate when it calls the Agent tool with a `name` while teams are enabled, unless the call is a fork or passes `isolation` on the call itself. Claude Code does not ask you to confirm. Claude also names ordinary subagents on its own, so teams can form unasked.

| Item | Location or rule |
| - | - |
| Team name | `session-` plus the first eight characters of the session ID |
| Team config | `~/.claude/teams/{team-name}/config.json`; removed when the session ends |
| Task list | `~/.claude/tasks/{team-name}/`; stays on disk after the session; retention set by `cleanupPeriodDays` |
| Mailbox | per agent, `~/.claude/teams/{team-name}/inboxes/{agent-name}.json` |

# Limits and defaults

- Mailbox entries are validated on read; entries not matching the message format are reported as errors and removed, valid ones still delivered.
- A message counts as sent only when the write to the recipient's mailbox succeeds (plain text or protocol messages such as plan approval or shutdown). On failure (disk full, directory not writable) the sender gets an error and nothing is sent; see the errors page "Failed to write to a teammate's inbox".
- The team config holds runtime state (session IDs, tmux pane IDs). Do not edit or pre-author it: changes are overwritten on the next state update. It has a `members` array with name and agent ID; the lead's agent type is always `team-lead`; a teammate carries the agent type the lead named (built-in type or subagent definition) and omits it if none.
- There is no project-level team config: `.claude/teams/teams.json` is not recognized. To define reusable roles use subagent definitions.
