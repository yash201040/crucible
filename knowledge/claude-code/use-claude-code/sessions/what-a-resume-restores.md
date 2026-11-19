---
type: "Concept"
title: "What a resumed session restores"
description: "State carried back on resume (history, model, agent, permission mode, goal, scheduled tasks) and the flags you must pass again."
resource: "https://code.claude.com/docs/en/sessions"
tags: [sessions, resume, state, flags]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "--mcp-config"
  - "--plugin-dir"
  - "--add-dir"
  - "/add-dir"
  - "--settings"
  - "--fallback-model"
  - "--agent"
  - "--system-prompt"
  - "--append-system-prompt"
  - "Conversation compacted"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sessions"
    resource: "https://code.claude.com/docs/en/sessions"
    title: "Manage sessions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Loading a conversation from its transcript restores the conversation plus saved state.

# How to use it

Restored:
- History: messages, tool calls, results. For a compacted session it opens at a `Conversation compacted` row and continues from the last compaction summary, the messages it left unsummarized, and everything since.
- Interrupted tool calls: a tool still running when the process ended (e.g. a crash) is not rerun.
- Model: `--resume`/`--continue` continue on the model the session used (exceptions in model-config).
- Agent: a session started with `--agent` or the `agent` setting continues as that agent with its tool restrictions and model; pass `--agent` to pick another. Claude Code looks for the agent in the session's original directory (if workspace trusted), then the directory you resume from; if not found it resumes with default tools and a warning naming the agent.
- Permission mode: see [permission mode on resume](./permission-mode-on-resume.md).
- Active goal: carries over, but its turn count, timer and token-spend baseline reset.
- Session-scoped scheduled tasks that have not expired are restored; background Bash and monitor tasks are not.
- Background work (background subagent, background Bash, workflow) that ended with the previous process shows as a note that it did not finish; no turn starts from those notes, Claude reads them with your next prompt.

Flags to pass again on `--continue`/`--resume` (not restored): `--mcp-config` (MCP servers), `--plugin-dir` (plugins), `--add-dir` (also for directories added with `/add-dir`), `--settings`, `--fallback-model`. For `--system-prompt` and `--append-system-prompt` see the CLI reference.

# Notes

Exception: do not repeat flags when reopening a running background session, or resuming it by full session ID with `--bg` after it stops.
