# agents-and-parallel-work/agent-view

* [Attach to and detach from a session](attach-and-detach.md) - Attach with Enter or claude attach for the full session; detach keys never stop the session.
* [/background and /fork inside a session](background-and-fork-commands.md) - /background (/bg) moves a session to the background; /fork copies it into a new background session. **[high]**
* [Configuration flags accepted by claude agents](config-flags-for-agent-view.md) - Flags that load settings, plugins, MCP servers and directories in agent view and pass through to dispatched sessions. **[high]**
* [Deleting sessions and their worktrees](deleting-sessions-and-worktrees.md) - What Ctrl+X twice and claude rm remove, when deletion is refused, and the retry flags.
* [Dispatching sessions from agent view](dispatch-from-agent-view.md) - Dispatch input prefixes, in-view commands, and how to target a different directory. **[high]**
* [Dispatch from the shell with --bg](dispatch-from-shell.md) - claude --bg starts a background session directly; combines with --agent, --resume, --name, --model and --exec for shell jobs. **[high]**
* [claude agents --json and reading state from scripts](json-listing-and-state-for-scripts.md) - JSON fields and state values for polling background sessions from a script or supervising session. **[high]**
* [Agent view keyboard shortcuts](keyboard-shortcuts.md) - Shortcuts for navigating, dispatching, pinning, renaming and stopping sessions in agent view.
* [Backgrounding with the left arrow](left-arrow-backgrounding.md) - Pressing left arrow on an empty prompt backgrounds a foreground session and opens agent view, with defined waiting rules.
* [Agent view limitations](limitations.md) - Rate limits, local-only sessions, and worktree deletion caveats of the agent view research preview. **[high]**
* [Model, effort and fast mode for dispatched sessions](model-effort-and-fast-mode.md) - Set the model, effort and fast mode for sessions dispatched next, per agent view window or per session. **[high]**
* [Organize, filter and resume in the list](organize-and-filter-list.md) - Grouping, pinning, reordering, renaming, deleting, filter prefixes, and bringing back past sessions.
* [Agent view overview and quick start](overview-and-quick-start.md) - claude agents opens one screen listing all background sessions; dispatch, peek, attach and bring in existing sessions. **[high]**
* [Peek panel and replies](peek-and-reply.md) - Space opens a peek panel to read a session's latest output and reply without attaching; reply routing depends on state. **[high]**
* [Permission mode and dispatch defaults](permission-mode-and-dispatch-defaults.md) - How a background session picks its permission mode and the claude agents flags that set defaults for every dispatch. **[high]**
* [Pull request label on rows](pull-request-status.md) - Rows link to the session's pull or merge request with a colour-coded #N or !N label.
* [Row summaries and their cost](row-summaries-and-cost.md) - One-line row summaries are written by a Haiku-class model, with throttled updates and a small per-summary request cost.
* [Agent view session states and icons](session-states-and-icons.md) - State icons, row shapes, notifications and persistence of background sessions across sleep and updates. **[high]**
* [Settings, provider and LLM gateway in background sessions](settings-provider-and-gateway.md) - Which settings, environment, PATH, provider variables and gateway endpoints reach a background session. **[high]**
* [Shell commands for background sessions](shell-session-commands.md) - claude agents, attach, logs, stop, respawn, rm and daemon subcommands for scripting background sessions. **[high]**
* [The supervisor process](supervisor-process.md) - The background service that hosts sessions: lifecycle rules, idle shutdown, restarts and keeping sessions alive. **[high]**
* [Troubleshooting restarts, resume and macOS permissions](troubleshooting-resume-and-macos.md) - Shutdown recovery, conversation already open, missing transcript, dead terminal host, macOS folder and LAN access.
* [Troubleshooting supervisor, auth and gateway errors](troubleshooting-supervisor-and-auth.md) - Fixes for unresponsive background service, authentication resolution failures, No LLM gateway and failed starts.
* [Turning off agent view](turn-off-agent-view.md) - disableAgentView and CLAUDE_CODE_DISABLE_AGENT_VIEW disable background agents and agent view entirely.
* [Agent view version history](version-history.md) - Versions in which agent view flags and behaviours were added or changed, v2.1.139 to v2.1.323.
* [What carries over when you background](what-carries-over-when-backgrounding.md) - Which background work and launch flags carry into a backgrounded session, and what happens to dynamic workflows. **[high]**
* [Worktree isolation of background edits](worktree-isolation-for-edits.md) - Dispatched background sessions move into their own git worktree before editing; setting and exceptions. **[high]**
