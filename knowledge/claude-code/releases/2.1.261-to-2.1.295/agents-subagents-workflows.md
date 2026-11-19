---
type: "Release Digest"
title: "Agents, subagents and workflows, 2.1.261 to 2.1.295"
description: "Release-note entries for subagents, background agents, teammates, the Agent and Workflow tools and agent worktrees from 2.1.261 to 2.1.295."
resource: "https://code.claude.com/docs/en/changelog"
tags: [agents, subagents, workflows, release-notes, background]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "effort"
  - "skills"
  - "CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS"
  - "omitClaudeMd"
  - "--agents"
  - "--append-subagent-system-prompt-file"
  - "agent.spawn"
  - "agentType"
  - "subagentStatusLine"
  - "agent_id"
  - "teammate_id"
  - "TeammateIdle"
  - "claude agents"
  - "claude attach"
  - "claude logs"
  - "/loop"
  - "/batch"
  - "WorktreeCreate"
  - "scriptPath"
  - "script"
  - "CLAUDE_CODE_SUBAGENT_MODEL_FORCE"
  - "disableWorkflows"
  - "/workflows"
  - "/ultrareview"
  - "$.agent.list()"
  - "--bg"
  - "claude --remote-control"
  - "Ctrl+X Ctrl+K"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "changelog"
    resource: "https://code.claude.com/docs/en/changelog"
    title: "Changelog 2.1.261 to 2.1.295"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Release-note rows (bug fixes removed) about subagents, background sessions, in-process teammates, workflow runs and agent worktrees. Newest first.

# How to use it

| Version | Date | What changed | Names |
|---|---|---|---|
| 2.1.295 | 2026-10-08 | A subagent preloads at most 32 skills from its `skills` field, each once; with the Skill tool it can still invoke the rest. | `skills` |
| 2.1.295 | 2026-10-08 | Ctrl+C at the idle prompt of an attached background session leaves a pending `/loop` wakeup alone (twice detaches, loop keeps running; Esc stops it). | `/loop` |
| 2.1.295 | 2026-10-08 | Stopping `claude agents` with its background service (macOS, or Linux without the service installed) now stops running sessions in about a minute unless it is run again. | `claude agents` |
| 2.1.295 | 2026-10-08 | Workflow tool `scriptPath` refusal now says to pass the script inline via `script` (works without a Read tool). | `scriptPath`, `script` |
| 2.1.293 | 2026-10-07 | `agentType` added to the `subagentStatusLine` payload so scripts can tell custom subagent types apart. | `agentType`, `subagentStatusLine` |
| 2.1.293 | 2026-10-07 | Order of agent lists and announced MCP servers: non-ASCII names sort after ASCII names. | |
| 2.1.292 | 2026-10-06 | Agent tool gets an `effort` parameter so Claude can run a sub-agent at a chosen effort level. | `effort` |
| 2.1.292 | 2026-10-06 | Workflow agents are passed to the `agent.spawn` mod hook (with run and index) so a mod can refuse them. | `agent.spawn` |
| 2.1.292 | 2026-10-06 | Agent names limited to 256 characters; longer ones rejected, and a longer skill or plugin file `name` is ignored. | |
| 2.1.292 | 2026-10-06 | After a cloud-session restart Claude is told which stopped background agents it can resume by id. | |
| 2.1.290 | 2026-10-05 | `claude attach <name>` and `claude logs <name>` accept part of a session name instead of the id. | `claude attach`, `claude logs` |
| 2.1.290 | 2026-10-05 | Background sessions whose scheduled task is gone move to Completed about 20 s later and can be updated or shut down when idle. | |
| 2.1.290 | 2026-10-05 | An in-process teammate's `agent_id` in Agent results is now its agent ID (`name@team` stays in `teammate_id`); TeammateIdle hooks no longer fire from its subagents or forks. | `agent_id`, `teammate_id`, `TeammateIdle` |
| 2.1.290 | 2026-10-05 | Background sessions waiting on a `/loop` wakeup are left running through updates and low memory so the wakeup is not lost. | `/loop` |
| 2.1.290 | 2026-10-05 | `/model`, `/effort`, `/rename` sent from `claude agents` to a busy background session apply immediately, without confirmation. | `claude agents` |
| 2.1.290 | 2026-10-05 | Permission prompts from background agents show Ctrl+X Ctrl+K, the shortcut that stops all background agents. | `Ctrl+X Ctrl+K` |
| 2.1.289 | 2026-10-03 | `agent.spawn` for teammates, one agent id across plugin hook events, and idle/waiting states in `$.agent.list()`. | `agent.spawn`, `$.agent.list()` |
| 2.1.288 | 2026-10-02 | Agents view: Ctrl+F finds a session by name, Alt+Up/Down jumps between groups; both and rename rebindable in keybindings.json. | `keybindings.json` |
| 2.1.288 | 2026-10-02 | Agents view `n:` filter and Ctrl+F search: Enter opens the best-matching session, not the top row. | `n:` |
| 2.1.287 | 2026-10-01 | `n:<text>` filter in the agents view matches session names and tasks. | `n:<text>` |
| 2.1.287 | 2026-10-01 | Replies from `claude agents` arrive as queued messages; slash commands other than `/stop` sent mid-turn run when the turn ends. | `claude agents`, `/stop` |
| 2.1.286 | 2026-09-30 | `/exit` Remove worktree runs after Claude Code stops the servers and shells it started there. | `/exit` |
| 2.1.286 | 2026-09-30 | Send-now (ctrl+enter) in a subagent view moves the subagent's running command to the background. | |
| 2.1.286 | 2026-09-30 | Replies from background agents no longer open with a recap of your message. | |
| 2.1.285 | 2026-09-29 | In auto mode a subagent run ends as soon as it hands its report back to its caller. | |
| 2.1.285 | 2026-09-29 | `/tasks` folds Claude Code's own background work under one "System tasks" row. | `/tasks` |
| 2.1.285 | 2026-09-29 | `/resume` and `claude --resume <id> "prompt"` on a session running in the background open it and send the prompt as its next turn. | `claude --resume` |
| 2.1.285 | 2026-09-29 | Code Review PR reviews and `/ultrareview` run when `disableWorkflows` is on, unless an administrator (MDM or managed settings file) set it on the reviewing machine. | `disableWorkflows`, `/ultrareview` |
| 2.1.283 | 2026-09-25 | `/workflows` run list sizes like other lists (half the terminal inline). | `/workflows` |
| 2.1.281 | 2026-09-23 | `/batch` runs where a WorktreeCreate hook provides agent worktrees, not only in a git repository. | `/batch`, `WorktreeCreate` |
| 2.1.281 | 2026-09-23 | `--agents` accepts a path to a JSON file (with `-p`) as well as inline JSON, and allows an empty `prompt`. | `--agents` |
| 2.1.281 | 2026-09-23 | `/workflows` list: `x` stops the run under the pointer; background workflow row shows name, progress bar, agent count, time, tokens. | `/workflows` |
| 2.1.277 | 2026-09-18 | Subagent results reach the main agent under a header marking them as subagent output, result indented. | |
| 2.1.277 | 2026-09-18 | Workflow scripts' computed `agent()` prompts on Bedrock, Vertex and Foundry are framed as script-authored text. | `agent()` |
| 2.1.274 | 2026-09-17 | Safety checks before removing an agent worktree that contains submodule checkouts improved. | |
| 2.1.273 | 2026-09-15 | A session started with `claude --remote-control` or `/remote-control` can be forked from the Claude app; the fork runs as a background session on your computer. | `claude --remote-control` |
| 2.1.271 | 2026-09-14 | `omitClaudeMd` in agent frontmatter and `--agents` JSON lets custom and plugin subagents run without user, project and local CLAUDE.md; managed policy files still load. | `omitClaudeMd`, `--agents` |
| 2.1.271 | 2026-09-14 | Default dynamic workflow size is small on Pro plans; medium size guideline lowered from 15 to 10 agents. | |
| 2.1.271 | 2026-09-14 | Dynamic workflows pause at your usage limit and continue automatically after reset instead of dropping agents. | |
| 2.1.269 | 2026-09-11 | `CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS` (1-256) raises the Workflow tool's per-run concurrent agent limit. | `CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS` |
| 2.1.267 | 2026-09-09 | Subagents and sessions with `--system-prompt` or `--append-system-prompt` record system prompt and tool definitions once (prompt-cache stability). | `--system-prompt`, `--append-system-prompt` |
| 2.1.265 | 2026-09-08 | `--worktree` checks out the new worktree in parallel on large repositories (git 2.32+). | `--worktree` |
| 2.1.265 | 2026-09-08 | `/workflows` agent detail shows tool-call state and the subagent's task list. | `/workflows` |
| 2.1.261 | 2026-09-04 | `--append-subagent-system-prompt-file` reads the subagent system prompt from a file. | `--append-subagent-system-prompt-file` |

# Not found in the documentation pages

- `subagentStatusLine`
- `teammate_id`
