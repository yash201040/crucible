---
type: "Release Digest"
title: "Agents, subagents and workflows, 2.1.296 to 2.1.328"
description: "Release-note changes to subagents, fork subagents, teammates, workflows, background sessions and agent view between 2.1.296 and 2.1.328."
resource: "https://code.claude.com/docs/en/changelog"
tags: [subagents, workflows, fork, teammates, background-agents, release-notes]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk, desktop, ide]
requires: ""
identifiers:
  - "CLAUDE_CODE_FORK_SUBAGENT"
  - "CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS"
  - "CLAUDE_CODE_DISABLE_AGENT_PROGRESS_SUMMARIES"
  - "CLAUDE_CODE_SUBAGENT_EFFORT"
  - "CLAUDE_CODE_WORKFLOW_SUBAGENT_MODEL"
  - "CLAUDE_CODE_AUTO_COMPACT_WINDOW"
  - "autoCompactWindow"
  - "subagent_type"
  - "SendMessage"
  - "ExitWorktree"
  - "discard_changes"
  - "EnterWorktree"
  - "WorktreeCreate"
  - "agent.spawn"
  - "turn.start"
  - "e.agentId"
  - "--agents"
  - "--bg"
  - "--worktree"
  - "--safe-mode"
  - "--add-dir"
  - "/list-agents"
  - "/tasks"
  - "/model"
  - "--disallow-tools"
  - "claude plugin eval"
  - "disallowed_tools"
  - "$.model.fork"
  - "$.ui.view"
  - "CLAUDE_CODE_RESUME_INTERRUPTED_TURN_MAX_AGE_MS"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "changelog"
    resource: "https://code.claude.com/docs/en/changelog"
    title: "Changelog 2.1.296 to 2.1.328"
stale_after: "2027-01-19T00:00:00Z"
---

# What changed

| Version | Date | What changed | Names |
|---|---|---|---|
| 2.1.328 | 2026-11-19 | In -p, SDK, desktop and VS Code, subagents wait for their own subagents by default when fork subagents are off. | `CLAUDE_CODE_FORK_SUBAGENT=0` |
| 2.1.328 | 2026-11-19 | With fork subagents off, claude -p counts a background subagent and those it waits for against one 10-minute wait; the ceiling can be raised. | `CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS` |
| 2.1.328 | 2026-11-19 | Subagent progress summaries on the Anthropic API are written by the small fast model from short notes, also with telemetry off, using far fewer tokens. | |
| 2.1.328 | 2026-11-19 | Starting several in-process teammates at once now fails far less often with "Lock file is already being held". | |
| 2.1.328 | 2026-11-19 | /list-agents shows its list to the user only. | `/list-agents` |
| 2.1.327 | 2026-11-17 | ExitWorktree asks before removing a worktree that may hold unsaved work; refused in don't-ask mode or with nobody to answer unless an allow rule, auto or bypass mode allows it. | `ExitWorktree` |
| 2.1.327 | 2026-11-17 | A subagent resumed by a sibling's message follows the session's permission settings, so it may ask or be refused where nobody can answer. | `SendMessage` |
| 2.1.327 | 2026-11-17 | Subagents launched without a model stay on the model they started on when resumed, including after /model. | `/model` |
| 2.1.327 | 2026-11-17 | The first subagent on a model waits up to 1.5 seconds (10 in claude -p) for that model's settings from Anthropic. | |
| 2.1.327 | 2026-11-17 | Restarted background subagents and self-started turns wait for plugins to load. | |
| 2.1.327 | 2026-11-17 | Subagent progress summaries on Bedrock, Vertex AI and Foundry are written from short notes with far fewer tokens. | |
| 2.1.327 | 2026-11-17 | Subagent answers that hit the output token limit twice now more often come back whole or say up front they are partial. | |
| 2.1.327 | 2026-11-17 | If Claude cannot read a completed subagent's output file after compaction, it is told to ask the agent with SendMessage. | `SendMessage` |
| 2.1.327 | 2026-11-17 | --worktree with a relative --add-dir beside or above the launch folder changes which folder the Bash sandbox (and a --bg session) gets. | `--worktree`, `--add-dir`, `--bg` |
| 2.1.327 | 2026-11-17 | Prompt history leaves out most launch prompts of sessions started by another Claude Code session, such as claude --bg run by Claude. | `--bg` |
| 2.1.326 | 2026-11-16 | Code Mode can be turned on while agent teams are enabled; sessions with teams on start in Code Mode if it was already on. | |
| 2.1.326 | 2026-11-16 | Subagents isolated in a worktree refuse some git commands in Bash that can rewrite branches shared with the checkout; sessions are not affected. | |
| 2.1.326 | 2026-11-16 | ExitWorktree refuses to remove a worktree while a background subagent or shell command may still run in it, unless Claude passes discard_changes. | `ExitWorktree`, `discard_changes` |
| 2.1.326 | 2026-11-16 | Quitting agent view with Ctrl+C twice, Ctrl+D twice or /exit after pressing the left arrow in an empty conversation ends that session instead of leaving it running 5 minutes. | |
| 2.1.326 | 2026-11-16 | The card approving a subagent's plan has two choices: switch to default (ask each time) for this session, or No. | |
| 2.1.326 | 2026-11-16 | With more than 20 subagents running, token counts of background agents whose transcript is not open update every 5 seconds. | |
| 2.1.326 | 2026-11-16 | Footer after Ctrl+C stops background agents offers a hint to resume a stopped subagent. | |
| 2.1.325 | 2026-11-13 | Subagents cut off at the output token limit are asked again for the whole answer, more briefly. | |
| 2.1.325 | 2026-11-13 | Worktree isolation refuses git bisect run, git maintenance register or start, and scalar set-up commands in an isolated worktree session or agent. | |
| 2.1.325 | 2026-11-13 | EnterWorktree refuses a WorktreeCreate hook path that goes through a symlink inside the project. | `EnterWorktree`, `WorktreeCreate` |
| 2.1.325 | 2026-11-13 | tmux and iTerm2 teammates and new sessions from the agents view start in the session's folder. | |
| 2.1.323 | 2026-11-12 | Added Code Mode, an experimental opt-in in which Claude writes JavaScript to call its tools. | |
| 2.1.323 | 2026-11-12 | Memory use with many subagents improved: a finished subagent's transcript is freed sooner. | |
| 2.1.323 | 2026-11-12 | Split-pane agent teammates check that requests come from their team lead; an orphaned teammate's asks are refused and plan approvals must be re-sent after /clear or /resume. | |
| 2.1.323 | 2026-11-12 | After safeguards stop a forked skill or a workflow agent, Claude is told to retry with a narrower prompt or tell the user rather than do the work itself. | |
| 2.1.323 | 2026-11-12 | A prompt an app marks as not typed no longer reaches workflow agents as the user's request. | |
| 2.1.323 | 2026-11-12 | Workflows in the desktop app's Code tab pause at a usage limit and continue after it resets. | |
| 2.1.321 | 2026-11-09 | Headless sessions reload mods in .claude/skills when files change; CLAUDE_CODE_PLUGIN_DIR_WATCH=0 turns it off. | `CLAUDE_CODE_PLUGIN_DIR_WATCH` |
| 2.1.321 | 2026-11-09 | Auto mode in headless, desktop and VS Code answers reports from background subagents that wait together in one model call. | |
| 2.1.321 | 2026-11-09 | Agent view row for a failed claude --bg --worktree session shows the error from its beginning. | `--bg`, `--worktree` |
| 2.1.319 | 2026-11-06 | /tasks has an "Earlier in this session" row listing finished subagents to reopen and message. | `/tasks` |
| 2.1.319 | 2026-11-06 | After safeguards stop a subagent, Claude is told to retry narrower or tell the user. | |
| 2.1.318 | 2026-11-04 | Subagents stop instead of switching models when "Switch models when a message is flagged" is "Ask each time". | |
| 2.1.318 | 2026-11-04 | Background subagents move a shell command to the background after 3 minutes on all providers so the prompt cache does not expire. | |
| 2.1.318 | 2026-11-04 | On Bedrock, Vertex, Foundry or telemetry off, a progress summary on a cold prompt cache can wait up to 5 minutes for the subagent's pending response. | |
| 2.1.318 | 2026-11-04 | A mod's $.model.fork gains an effort option to run a side job at low effort. | `$.model.fork` |
| 2.1.317 | 2026-11-03 | SendMessage to a running background agent arrives earlier: its running command moves to the background without being stopped. | `SendMessage` |
| 2.1.317 | 2026-11-03 | Subagents and teammates on a different model than the main conversation use that model's saved or default effort, not the session's. | |
| 2.1.317 | 2026-11-03 | Exit skips the "Background work is running" prompt for plugin monitors. | |
| 2.1.316 | 2026-10-31 | Added CLAUDE_CODE_SUBAGENT_EFFORT to set the effort subagents run at when nothing else names one. | `CLAUDE_CODE_SUBAGENT_EFFORT` |
| 2.1.314 | 2026-10-30 | Memory use improved in long headless and SDK turns that run many subagents. | |
| 2.1.312 | 2026-10-27 | Prompt and agent hooks run at most 24 at a time per session (subagents included), plus at most 12 that waited longer than their event's timeout; a timeout under 1 second counts as 1. | |
| 2.1.312 | 2026-10-27 | A subagent's autoCompactWindow lowers the window set by CLAUDE_CODE_AUTO_COMPACT_WINDOW; it never raises it. | `autoCompactWindow`, `CLAUDE_CODE_AUTO_COMPACT_WINDOW` |
| 2.1.307 | 2026-10-21 | Fork subagents launched together are each told which launch is their own. | |
| 2.1.304 | 2026-10-19 | Responsiveness and throughput improved with many subagents running at once; VS Code shows background sub-agents as one status line. | |
| 2.1.302 | 2026-10-16 | Fork subagents (subagent_type fork) are on by default in claude -p, the Agent SDK, desktop and VS Code; CLAUDE_CODE_FORK_SUBAGENT=0 turns them off; claude mcp serve never offers them. | `subagent_type`, `CLAUDE_CODE_FORK_SUBAGENT` |
| 2.1.302 | 2026-10-16 | Desktop and VS Code always run the main conversation's subagents in the background; a subagent's own Agent calls in -p, SDK, desktop and VS Code run in the foreground by default. | |
| 2.1.302 | 2026-10-16 | At most 12 prompt and agent hooks of one event run at a time. | |
| 2.1.300 | 2026-10-14 | The agent.spawn mod hook can rewrite a workflow agent's prompt and model; $.ui.view({ agentId }) shows an agent's transcript in the main view. | `agent.spawn`, `$.ui.view` |
| 2.1.299 | 2026-10-14 | The turn.start mod hook also hears subagents' and teammates' turns; tell them apart by e.agentId. | `turn.start`, `e.agentId` |
| 2.1.299 | 2026-10-14 | Agent tools: lists take only the named MCP server's tools; list a server with __ in its name as mcp__<whole name>__*. | `tools` |
| 2.1.299 | 2026-10-14 | Added --disallow-tools and a disallowed_tools case field to claude plugin eval to keep tools such as Agent out of eval runs. | `--disallow-tools`, `disallowed_tools`, `claude plugin eval` |
| 2.1.299 | 2026-10-14 | Background agent notifications say when an agent only waits on its own background work, got a message too late, or was stopped by a usage limit. | |
| 2.1.299 | 2026-10-14 | Agent view gets /effort and /fast to set what new sessions start with; the peek panel shows a safe-mode line for --safe-mode sessions. | `/effort`, `/fast`, `--safe-mode` |
| 2.1.296 | 2026-10-09 | Added autoCompactWindow to subagent frontmatter and --agents definitions. | `autoCompactWindow`, `--agents` |
| 2.1.296 | 2026-10-09 | Added CLAUDE_CODE_WORKFLOW_SUBAGENT_MODEL to run every workflow agent on one model. | `CLAUDE_CODE_WORKFLOW_SUBAGENT_MODEL` |
| 2.1.296 | 2026-10-09 | Moving a session to the background with the left arrow now stops a turn or ! command started during the move. | |
| 2.1.296 | 2026-10-09 | --debug output names unrecognized frontmatter fields in custom agent files. | `--debug` |

# Not found in the documentation pages

- `CLAUDE_CODE_DISABLE_AGENT_PROGRESS_SUMMARIES`
- `CLAUDE_CODE_SUBAGENT_EFFORT`
- `CLAUDE_CODE_WORKFLOW_SUBAGENT_MODEL`
- `--disallow-tools`
- `$.ui.view`
