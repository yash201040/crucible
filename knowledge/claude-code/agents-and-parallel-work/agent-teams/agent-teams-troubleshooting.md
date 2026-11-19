---
type: "Guide"
title: "Agent teams troubleshooting"
description: "Fixes for missing teammates, teammates replacing subagents, permission prompt friction, early stops and orphaned tmux sessions."
resource: "https://code.claude.com/docs/en/agent-teams"
tags: [agent-teams, troubleshooting, tmux, settings]
kind: "behavior"
maturity: "experimental"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS"
  - "tmux ls"
  - "tmux kill-session -t <session-name>"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-teams"
    resource: "https://code.claude.com/docs/en/agent-teams"
    title: "Orchestrate teams of Claude Code sessions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Common problems and the documented remedies.

# How to use it

- Teammates not appearing: in-process, look in the agent panel and press Enter on one. A row that vanished after idling is hidden, not stopped; message the teammate by name to bring it back. The task may not have been complex enough to warrant a team. For split panes check `which tmux`, and for iTerm2 that `it2` is installed and the Python API enabled.
- Claude spawns teammates instead of subagents: set `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` to `"0"` in settings.json `env`. No new session is needed: settings-file `env` values are reapplied on save and the variable is reread on each subagent spawn. A `0` in user settings overrides a shell export, but project settings, local settings, a `--settings` payload (all after user settings) or managed settings that set `1` still win; for managed settings ask the administrator. Afterwards Claude may still name subagents and the name still works as a `SendMessage` address; results arrive on completion.
- Too many permission prompts: teammate requests bubble to the lead; pre-approve common operations in permission settings before spawning.
- Agents stopping early: teammates may stop after errors. Inspect output, then give instructions or spawn a replacement. A message from the lead or another teammate wakes an in-process teammate waiting to retry a failed API request so it retries immediately. The lead may also declare the team finished early; tell it to keep going.
- Orphaned tmux sessions: `tmux ls`, then `tmux kill-session -t <session-name>`.
