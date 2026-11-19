---
type: "Reference"
title: "Tools: agents, messaging, scheduling, tasks"
description: "Built-in tool names for spawning agents, messaging, scheduling, task tracking, workflows and notifications, with permission and version notes."
resource: "https://code.claude.com/docs/en/tools-reference"
tags: [tools, agents, messaging, scheduling, tasks]
kind: "tool"
maturity: "unlabelled"
since: ""
surfaces: [cli, sdk, cloud]
requires: ""
identifiers:
  - "Agent"
  - "ListAgents"
  - "SendMessage"
  - "SubagentHandback"
  - "TaskStop"
  - "TaskCreate"
  - "TaskGet"
  - "TaskList"
  - "TaskUpdate"
  - "TaskOutput"
  - "TodoWrite"
  - "CronCreate"
  - "CronDelete"
  - "CronList"
  - "ScheduleWakeup"
  - "RemoteTrigger"
  - "Workflow"
  - "Skill"
  - "ToolSearch"
  - "WaitForMcpServers"
  - "PushNotification"
  - "SendUserFile"
  - "Artifact"
  - "ReportFindings"
  - "SendFeedback"
  - "ShareOnboardingGuide"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "tools-reference"
    resource: "https://code.claude.com/docs/en/tools-reference"
    title: "Tools reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Tool names are the exact strings used in permission rules, subagent tool lists and hook matchers. This part of the tools table covers orchestration-relevant tools. "Permission" is whether the tool prompts in Manual mode.

# How to use it

| Tool | Permission | What it does |
| :- | :- | :- |
| `Agent` | No | Spawns a subagent in its own context window; with agent teams on, a call with a `name` can launch a teammate. See [Agent tool behavior](./agent-tool-behavior.md). |
| `ListAgents` | No | Lists agents reachable via `SendMessage`: session subagents, agent team teammates, other local sessions, and (with Remote Control) cloud sessions and sessions on other machines. Backs `/list-agents`. Needs v2.1.224+; only where cross-session messaging is enabled; teammate rows need v2.1.239+. |
| `SendMessage` | No | Messages a teammate, a subagent it resumes (by agent ID or name), or another session. Cross-session needs v2.1.224+. Optional `summary` input (typically 5-10 words; over 200 characters is truncated with an ellipsis; defaults to first line for plain-text messages). |
| `SubagentHandback` | No | Delivers a subagent's final report to the receiving conversation. Provided only in auto mode, to locally run subagents other than forks; the classifier reviews the report first. Available in CLI, IDE extensions, cloud sessions, Agent SDK. Needs v2.1.271+. |
| `TaskStop` | No | Stops a background task by ID; also accepts an agent-team teammate or named background agent by ID or name. On no match the error lists running background agents. |
| `TaskCreate`, `TaskGet`, `TaskList`, `TaskUpdate` | No | Task list tools. Provided by default only on some models, see [Task tool availability](./task-tool-availability.md). |
| `TaskOutput` | No | Removed in v2.1.277; Claude now reads a background task's output file with `Read`. |
| `TodoWrite` | No | Session checklist; disabled by default in favor of the four Task tools. `CLAUDE_CODE_ENABLE_TASKS=0` re-enables it. |
| `CronCreate`, `CronDelete`, `CronList` | No | Create, cancel and list session-scoped scheduled tasks (recurring or one-shot); restored on `--resume`/`--continue` if unexpired. |
| `ScheduleWakeup` | No | Claude calls it each iteration of a self-paced `/loop` to pick the next run, one minute to one hour out; `stop: true` cancels. The pending wakeup shows in `session_crons` in Stop hook input. |
| `RemoteTrigger` | No | Creates, updates, runs and lists cloud scheduled tasks (formerly routines) on claude.ai; backs `/schedule`. Needs Pro, Max, Ultra, Team or Enterprise; not accessible from Amazon Bedrock, Claude Platform on AWS, Google Cloud Agent Platform or Microsoft Foundry. |
| `Workflow` | Yes | Runs a dynamic workflow: a script that orchestrates many subagents in the background and returns one consolidated result. |
| `Skill` | Some skills | Runs a skill in the main conversation; can prompt for skills setting `allowed-tools`, `disallowed-tools` or `hooks`. |
| `ToolSearch` | No | Searches for and loads deferred tools when tool search is enabled. |
| `WaitForMcpServers` | No | Waits for MCP servers still connecting; appears only when tool search is disabled. |
| `PushNotification` | No | Desktop notification locally; phone push with Remote Control or in a cloud session. Runs through Anthropic-hosted infrastructure, unavailable on Bedrock, Claude Platform on AWS, Google Cloud Agent Platform, Foundry. |
| `SendUserFile` | No | Sends files with an optional caption to your device; `display` input: `render` (inline), `attach` (download card), unset (client decides). Needs a connected Remote Control client or a cloud session; unavailable on Bedrock, Google Cloud Agent Platform, Foundry. |
| `Artifact` | Yes | Publishes an HTML or Markdown file to claude.ai as a private page. Needs Pro, Max, Ultra, Team or Enterprise plan and `/login`. |
| `ReportFindings` | No | Reports code-review findings as a structured list (file, summary, failure scenario; optional `category` slug). Claude calls it when review instructions say so. |
| `SendFeedback` | No | Drafts a feedback report queued locally; see [SendFeedback](./sendfeedback-tool.md). v2.1.238+. |
| `ShareOnboardingGuide` | Yes | Uploads `ONBOARDING.md` and returns a share link; called from `/team-onboarding`. Team and Enterprise claude.ai subscribers. |

# Notes

The advisor tool is a server tool run by the API, with no name usable in permission rules or hook matchers. Other tools are in [file and shell tools](./tools-files-shell-and-web.md).
