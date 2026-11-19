---
type: "Release Digest"
title: "Agents, subagents and workflows (2.1.101 to 2.1.260)"
description: "Release notes 2.1.101 to 2.1.260 on subagents, background agents, agent view, workflows, goals and cross-session messaging."
resource: "https://code.claude.com/docs/en/changelog"
tags: [subagents, workflows, background-agents, release-notes]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: []
requires: ""
identifiers:
  - "agent({schema})"
  - "Workflow"
  - "/workflows"
  - "CLAUDE_CODE_SUBAGENT_MODEL_FORCE"
  - "CLAUDE_CODE_SUBAGENT_MODEL"
  - "claude --resume <session-id> --bg"
  - "/fork"
  - "model"
  - "claude attach"
  - "claude logs"
  - "claude stop"
  - "claude respawn"
  - "claude rm"
  - "experimental.cacheTtl"
  - "workflow-authoring"
  - "SendMessage"
  - "ListAgents"
  - "maxTurns"
  - "/goal"
  - "/tasks"
  - "/list-agents"
  - "crossSessionInbound"
  - "notify_when_idle"
  - "CLAUDE_CODE_GOAL_CHECKIN_MINUTES"
  - "--worktree"
  - "claude agents"
  - "subagent_type"
  - "/code-review"
  - "CLAUDE_CODE_WORKFLOW_PREFIX_STAGGER_MS"
  - "dialogExpiry"
  - "CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH"
  - "workflowSizeGuideline"
  - "context: fork"
  - "background: false"
  - "CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS"
  - "CLAUDE_CODE_MAX_SUBAGENTS_PER_SESSION"
  - "/subtask"
  - "Task"
  - "claude agents --json"
  - "Agent"
  - "workflow.run_id"
  - "workflow.name"
  - "/agents"
  - "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS"
  - "TeamCreate"
  - "TeamDelete"
  - "team_name"
  - "ultracode"
  - "--agent"
  - "EnterWorktree"
  - "claude --bg --exec"
  - "--strict-mcp-config"
  - "--agents"
  - "/bg"
  - "agent_id"
  - "parent_agent_id"
  - "/resume"
  - "--add-dir"
  - "--settings"
  - "--mcp-config"
  - "--plugin-dir"
  - "--permission-mode"
  - "--model"
  - "--effort"
  - "--dangerously-skip-permissions"
  - "worktree.bgIsolation"
  - "--fallback-model"
  - "claude agents --cwd"
  - "x-claude-code-agent-id"
  - "x-claude-code-parent-agent-id"
  - "worktree.baseRef"
  - "CLAUDE_CODE_FORK_SUBAGENT"
  - "permissionMode"
  - "tools"
  - "disallowedTools"
  - "mcpServers"
  - "hooks"
  - "path"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "changelog"
    resource: "https://code.claude.com/docs/en/changelog"
    title: "Changelog 2.1.101 to 2.1.260"
stale_after: "2027-01-19T00:00:00Z"
---

# Changes by version

| Version | Date | What changed | Names |
|---|---|---|---|
| 2.1.260 | 2026-09-03 | Workflow agent({schema}) rejects a JSON Schema that can never be satisfied up front; retry-cap errors name the last validation failure | `agent({schema})`, `Workflow` |
| 2.1.260 | 2026-09-03 | Removed the one-hour limit on background commands started by subagents; they run until they exit or are stopped |  |
| 2.1.260 | 2026-09-03 | Deleting a background session whose worktree has unpushed commits names the branch and commit count; deleting again discards the worktree |  |
| 2.1.259 | 2026-09-02 | Results of nested background subagents are saved in the parent subagent's transcript so resumed subagents keep them |  |
| 2.1.259 | 2026-09-02 | /workflows agent detail pretty-prints JSON outcomes and folds long ones | `/workflows` |
| 2.1.257 | 2026-09-01 | CLAUDE_CODE_SUBAGENT_MODEL_FORCE applies CLAUDE_CODE_SUBAGENT_MODEL (or the main model) to every subagent, ignoring per-spawn and agent-definition model overrides | `CLAUDE_CODE_SUBAGENT_MODEL_FORCE`, `CLAUDE_CODE_SUBAGENT_MODEL` |
| 2.1.257 | 2026-09-01 | claude --resume <session-id> --bg continues that session under its own ID when nothing runs it; a copy is announced | `claude --resume <session-id> --bg` |
| 2.1.257 | 2026-09-01 | /fork keeps the original conversation's prompt cache in the new background session | `/fork` |
| 2.1.251 | 2026-08-28 | Foreground subagent tool calls and results stream live to Remote Control clients (background subagents still show status only) |  |
| 2.1.251 | 2026-08-28 | CLAUDE_CODE_SUBAGENT_MODEL is now only the default subagent model; an agent definition's model: and an explicit per-spawn model take precedence | `CLAUDE_CODE_SUBAGENT_MODEL`, `model` |
| 2.1.251 | 2026-08-28 | claude --help lists attach, logs, stop, respawn and rm; --resume of a running background session names claude attach <id> | `claude attach`, `claude logs`, `claude stop`, `claude respawn`, `claude rm` |
| 2.1.251 | 2026-08-28 | Messages from your own subagents are framed as from a worker in this session; prompt placeholder reads Message @name while viewing a subagent transcript |  |
| 2.1.248 | 2026-08-27 | experimental.cacheTtl (5m or 1h) in agent frontmatter sets a per-agent prompt cache TTL when no subagent TTL setting exists | `experimental.cacheTtl` |
| 2.1.248 | 2026-08-27 | Workflow tool description shrank from about 5.7k to about 1k tokens; the script-writing reference moved to a bundled workflow-authoring skill | `Workflow`, `workflow-authoring` |
| 2.1.248 | 2026-08-27 | Cross-session SendMessage and ListAgents work on Bedrock, Vertex, Foundry and with telemetry disabled; a subagent's SendMessage result says replies go to the parent session | `SendMessage`, `ListAgents` |
| 2.1.247 | 2026-08-26 | Cross-session peer messages collapse to a one-line preview; Ctrl+O expands them |  |
| 2.1.246 | 2026-08-25 | A subagent that stops at maxTurns returns its output marked partial with a hint to continue it via SendMessage | `maxTurns`, `SendMessage` |
| 2.1.246 | 2026-08-25 | /goal: idle sessions start at most three check-ins on long background work per goal; your next message allows three more | `/goal` |
| 2.1.243 | 2026-08-25 | /tasks and agent detail dialogs show the model and effort each subagent ran on | `/tasks` |
| 2.1.239 | 2026-08-21 | /goal repeat check-ins back off 30 min, 1 h, then every 2 h; resuming from the picker restores the active goal | `/goal` |
| 2.1.239 | 2026-08-21 | ListAgents tells a session its own name and lists live teammates (also /list-agents); cross-session messaging arrives on Windows | `ListAgents`, `/list-agents`, `SendMessage` |
| 2.1.238 | 2026-08-20 | Sending to a session that refuses inbound messages now reports refused; a session whose inbox drops messages tells the sender | `crossSessionInbound` |
| 2.1.236 | 2026-08-19 | notify_when_idle on SendMessage asks another local session for one notice when it next goes idle (macOS and Linux) | `notify_when_idle`, `SendMessage` |
| 2.1.236 | 2026-08-19 | /goal parked behind background work checks in after 30 min (then 1 h, 2 h); SendMessage refuses a burst that would overflow the recipient inbox | `/goal`, `SendMessage` |
| 2.1.235 | 2026-08-18 | SendMessage refuses messages too large for cross-session delivery up front | `SendMessage` |
| 2.1.234 | 2026-08-17 | Typing @ in the prompt mentions another session by name and Claude uses SendMessage; SendMessage and ListAgents say when the session list was too long to check | `SendMessage`, `ListAgents` |
| 2.1.234 | 2026-08-17 | /goal clears itself on an unrecoverable error; CLAUDE_CODE_GOAL_CHECKIN_MINUTES=0 opts out of the 30-minute background check-in | `/goal`, `CLAUDE_CODE_GOAL_CHECKIN_MINUTES` |
| 2.1.234 | 2026-08-17 | Removed the Default teammate model setting: agent-team teammates use the leader's model unless the spawn names one; background task notifications arrive in system-reminder tags |  |
| 2.1.233 | 2026-08-14 | GitLab merge request URLs accepted by --worktree and shown as !N in claude agents | `--worktree`, `claude agents` |
| 2.1.232 | 2026-08-13 | Subagent forking is on by default (subagent_type fork inherits the conversation and prompt cache); non-teammate spawns in interactive sessions run in the background by default | `subagent_type` |
| 2.1.232 | 2026-08-13 | SendMessage delivers to a bare name matching exactly one live session; interactive session names are kept unique per machine (name-word-word) | `SendMessage` |
| 2.1.232 | 2026-08-13 | /code-review at high, xhigh and max runs in a background agent; completed subagents hide from the agent panel with a /tasks hint | `/code-review`, `/tasks` |
| 2.1.229 | 2026-08-12 | Workflow fan-outs stagger same-prefix sibling agents to read the cached prefix; CLAUDE_CODE_WORKFLOW_PREFIX_STAGGER_MS=0 disables | `CLAUDE_CODE_WORKFLOW_PREFIX_STAGGER_MS` |
| 2.1.229 | 2026-08-12 | ListAgents marks disconnected Remote Control sessions offline and your cloud sessions cloud | `ListAgents` |
| 2.1.225 | 2026-08-08 | SendMessage can start a conversation with your Remote Control sessions on other machines by name | `SendMessage`, `ListAgents` |
| 2.1.224 | 2026-08-07 | Cross-session SendMessage with ListAgents discovery, on any of your machines (macOS and Linux); crossSessionInbound and dialogExpiry settings hold or deliver messages | `SendMessage`, `ListAgents`, `crossSessionInbound`, `dialogExpiry` |
| 2.1.224 | 2026-08-07 | Removed the 200-subagent-per-session spawn cap; concurrency and depth limits still apply |  |
| 2.1.223 | 2026-08-06 | Warning when a workflow agent, forked skill, slash command or resumed background agent asks for a restricted subagent model and the parent model runs instead |  |
| 2.1.222 | 2026-08-04 | In auto mode, SendMessage to other agent sessions is classified before dispatch | `SendMessage` |
| 2.1.221 | 2026-08-04 | Sessions forked with /fork create their own worktree | `/fork` |
| 2.1.219 | 2026-07-24 | Subagents can spawn nested subagents to depth 3 by default (was 1); CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH=1 disables nesting | `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` |
| 2.1.219 | 2026-07-24 | Dynamic workflows default to a medium size guideline (fewer than 15 agents); workflowSizeGuideline settings key sets it from any settings file | `workflowSizeGuideline` |
| 2.1.218 | 2026-07-22 | Skills with context: fork run in the background by default; background: false opts out; agent names containing a colon are rejected | `context: fork`, `background: false` |
| 2.1.217 | 2026-07-21 | Cap on concurrently running subagents, default 20, override CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS; nesting off by default until 2.1.219 | `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS`, `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` |
| 2.1.212 | 2026-07-17 | Per-session cap on subagent spawns, default 200, override CLAUDE_CODE_MAX_SUBAGENTS_PER_SESSION; /clear resets the budget | `CLAUDE_CODE_MAX_SUBAGENTS_PER_SESSION` |
| 2.1.212 | 2026-07-17 | /fork copies the conversation into a new background session and the in-session subagent it used to launch is now /subtask; Task tool mode parameter deprecated and ignored (subagents inherit the parent permission mode) | `/fork`, `/subtask`, `Task` |
| 2.1.212 | 2026-07-17 | SendMessage bodies are no longer duplicated in replayed history; agent view and claude agents --json show sessions waiting on prompts as Needs input | `SendMessage`, `claude agents --json` |
| 2.1.210 | 2026-07-14 | Agent tool hardened against indirect prompt injection from content a subagent read | `Agent` |
| 2.1.208 | 2026-07-14 | Completed background agents stay in /tasks until cleanup; attaching to a stopped background agent shows its transcript at once | `/tasks` |
| 2.1.203 | 2026-07-07 | Subagents are less likely to re-delegate their whole task |  |
| 2.1.202 | 2026-07-06 | Dynamic workflow size setting in /config; workflow.run_id and workflow.name OTel attributes on workflow-spawned agents | `workflow.run_id`, `workflow.name` |
| 2.1.198 | 2026-07-01 | Subagents run in the background by default; Explore agent inherits the main model (capped at opus); subagents and compaction inherit extended thinking; /agents wizard removed | `/agents` |
| 2.1.198 | 2026-07-01 | Subagents treat messages from the launching agent as task direction, never as user approval; background agents from claude agents commit, push and open a draft PR after code work in a worktree | `claude agents` |
| 2.1.196 | 2026-06-29 | Background agents killed by a daemon restart are resumed automatically when the agents view next opens |  |
| 2.1.186 | 2026-06-22 | Background subagents surface permission prompts in the main session instead of auto-denying; status filter f in /workflows detail | `/workflows` |
| 2.1.181 | 2026-06-17 | Subagent panel hides idle subagents after 30s and caps at 5 rows |  |
| 2.1.178 | 2026-06-15 | Agent teams: TeamCreate and TeamDelete removed; with CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1 every session has one implicit team and teammates are spawned with the Agent tool name parameter; team_name is ignored | `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS`, `TeamCreate`, `TeamDelete`, `team_name` |
| 2.1.178 | 2026-06-15 | Auto mode classifier evaluates subagent spawns before launch; in nested .claude directories the closest agent, workflow and output style wins |  |
| 2.1.172 | 2026-06-10 | Sub-agents can spawn their own sub-agents up to 5 levels deep |  |
| 2.1.160 | 2026-06-02 | Dynamic-workflow trigger keyword renamed from workflow to ultracode | `ultracode` |
| 2.1.157 | 2026-05-29 | Workflow keyword trigger setting in /config; claude agents honors the agent field in settings.json with --agent to override; EnterWorktree switches between Claude-managed worktrees | `--agent`, `EnterWorktree` |
| 2.1.154 | 2026-05-28 | Dynamic workflows: Claude orchestrates tens to hundreds of background agents; /workflows lists runs; claude agents accepts ! <command> and claude --bg --exec runs a shell command as a background session | `/workflows`, `claude --bg --exec` |
| 2.1.153 | 2026-05-28 | --strict-mcp-config no longer strips inline mcpServers from --agents or SDK agents; /bg while responding continues in the background | `--strict-mcp-config`, `--agents`, `/bg` |
| 2.1.147 | 2026-05-21 | Pinned background sessions (Ctrl+T in claude agents) stay alive when idle and are shed last under memory pressure |  |
| 2.1.145 | 2026-05-19 | claude agents --json lists live sessions; agent_id and parent_agent_id on claude_code.tool OTel spans | `claude agents --json`, `agent_id`, `parent_agent_id` |
| 2.1.144 | 2026-05-19 | /resume lists background sessions (marked bg); completion notifications show elapsed duration | `/resume` |
| 2.1.143 | 2026-05-15 | claude agents accepts --add-dir, --settings, --mcp-config, --plugin-dir, --permission-mode, --model, --effort, --dangerously-skip-permissions; worktree.bgIsolation none; /bg preserves flags and fallback model | `--add-dir`, `--settings`, `--mcp-config`, `--plugin-dir`, `--permission-mode`, `--model`, `--effort`, `--dangerously-skip-permissions`, `worktree.bgIsolation`, `--fallback-model` |
| 2.1.141 | 2026-05-13 | claude agents --cwd scopes the list to a directory | `claude agents --cwd` |
| 2.1.140 | 2026-05-12 | Agent tool subagent_type matching is case- and separator-insensitive | `subagent_type` |
| 2.1.139 | 2026-05-11 | Agent view (Research Preview): claude agents lists every session; /goal sets a completion condition; subagent API requests carry x-claude-code-agent-id and x-claude-code-parent-agent-id headers | `claude agents`, `/goal`, `x-claude-code-agent-id`, `x-claude-code-parent-agent-id` |
| 2.1.133 | 2026-05-07 | worktree.baseRef (fresh or head) picks whether worktrees branch from origin default or local HEAD | `worktree.baseRef` |
| 2.1.128 | 2026-05-04 | EnterWorktree creates the branch from local HEAD instead of origin default (reversed by worktree.baseRef in 2.1.133) | `EnterWorktree` |
| 2.1.121 | 2026-04-28 | CLAUDE_CODE_FORK_SUBAGENT=1 works in SDK and claude -p | `CLAUDE_CODE_FORK_SUBAGENT` |
| 2.1.119 | 2026-04-23 | --agent honors the agent definition permissionMode for built-in agents; --print honors the agent tools: and disallowedTools: | `--agent`, `permissionMode`, `tools`, `disallowedTools` |
| 2.1.117 | 2026-04-22 | Forked subagents can be enabled on external builds with CLAUDE_CODE_FORK_SUBAGENT=1; agent frontmatter mcpServers load for --agent sessions | `CLAUDE_CODE_FORK_SUBAGENT`, `mcpServers` |
| 2.1.116 | 2026-04-20 | Agent frontmatter hooks fire when running as a main-thread agent via --agent | `hooks` |
| 2.1.113 | 2026-04-17 | Subagents that stall mid-stream fail with a clear error after 10 minutes |  |
| 2.1.105 | 2026-04-13 | EnterWorktree gets a path parameter to switch into an existing worktree; worktrees of squash-merged PRs are cleaned up | `EnterWorktree`, `path` |

# Not found in the documentation pages

These identifiers occur only in the release notes, not in the saved documentation pages:

- `agent({schema})`
- `experimental.cacheTtl`
- `TeamCreate`
- `TeamDelete`
