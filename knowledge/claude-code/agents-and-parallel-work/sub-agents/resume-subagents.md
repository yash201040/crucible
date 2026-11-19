---
type: "Feature"
title: "Resuming subagents"
description: "Resume a finished subagent by ID or name with SendMessage; transcripts persist per session and are cleaned up after cleanupPeriodDays."
resource: "https://code.claude.com/docs/en/sub-agents"
tags: [subagents, resume, sendmessage, transcripts, sessions]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.299"
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "SendMessage"
  - "TaskStop"
  - "cleanupPeriodDays"
  - "~/.claude/projects/{project}/{sessionId}/subagents/"
  - "agent-{agentId}.jsonl"
  - "agent-{agentId}.meta.json"
  - "stop_task"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sub-agents"
    resource: "https://code.claude.com/docs/en/sub-agents"
    title: "Create custom subagents"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Each invocation creates a new instance; to continue earlier work Claude resumes the subagent. A resumed subagent keeps its full conversation history (tool calls, results, reasoning, and results of its own background subagents). Claude gets the agent ID when a subagent completes.

# How to use it

- Claude uses `SendMessage` with the agent ID or name as `to`. `SendMessage` does not need agent teams enabled (only structured team-protocol messages like `shutdown_request` and `plan_approval_response` do). Where cross-session messaging is enabled the same tool can message your other sessions, including on other machines.
- A message to a completed subagent, or one Claude stopped with `TaskStop` once its run exited, resumes it in the background with no new Agent call, keeping its original tool set and able to read the prompt cache the original run warmed.
- A subagent with `SendMessage` can resume another; in an interactive session the resumed agent reports back to the resumer, which waits for the result.
- A subagent stopped by you (`x` in `/tasks` or an SDK `stop_task` request) does not auto-resume; messages are refused and Claude is told it was cancelled. While its panel row is still shown you can type into its transcript to resume it.
- Resuming starts a new run under the same ID; it shows as running again in task list and SDK task events.
- Name safety: `SendMessage` refuses a send if a newer agent has taken the name and reports which agent the name now reaches; address the older agent by ID. The check resets on `/clear`.
- A subagent treats messages from its launcher as normal task direction (incl. mid-task corrections) within its own permissions. No agent message counts as your approval of a pending permission prompt, and none can change permission settings, CLAUDE.md or configuration.

# Limits and defaults

- Explore and Plan return no ID and cannot be resumed. Output stopped at `maxTurns` is marked partial and resumable.
- Transcripts at `~/.claude/projects/{project}/{sessionId}/subagents/agent-{agentId}.jsonl`; unaffected by main-conversation compaction; persist within the session (resume the session to resume the subagent); deleted after `cleanupPeriodDays` (default 30 days).
- After a restart, names Claude gave since the last compaction survive (v2.1.299 or later); older ones do not. Look up an ID in `agent-{agentId}.meta.json`. After one message by ID the name works again. Teammates: see agent team limitations.
- Before v2.1.304 a subagent messaged right after finishing could forget its latest work.
