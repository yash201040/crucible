# agents-and-parallel-work/sub-agents

* [Session-only subagents via --agents](agents-cli-flag-json.md) - Pass subagent definitions as JSON (or a JSON file in non-interactive mode) when launching Claude Code; they are not saved to disk. **[high]**
* [Built-in subagents](built-in-subagents.md) - Explore, Plan, general-purpose and helper agents Claude Code uses automatically, with their models and tools, and how to disable them. **[high]**
* [Choosing a subagent's model](choose-subagent-model.md) - Model order for subagents, nested subagent model, forcing one model for all, alias versions and allowlist substitution. **[high]**
* [Common subagent patterns and when to use them](common-patterns-and-when-to-use.md) - Isolating high-volume output, parallel research, chaining, and choosing between subagents, main conversation, skills and /btw.
* [Concurrent subagent limit](concurrent-subagent-limit.md) - At 20 running subagents, spawning another with the Agent tool fails; change it with CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS. **[high]**
* [Create your first subagent](create-first-subagent.md) - Quickstart: ask Claude to write a user-level subagent file in ~/.claude/agents/ and delegate to it.
* [Delegation, @-mention and --agent](delegation-and-explicit-invocation.md) - Automatic delegation by description, @-mention syntax, running a whole session as a subagent with --agent or the agent setting. **[high]**
* [Disabling specific subagents](disable-specific-subagents.md) - Deny Agent(name) entries in permissions.deny or --disallowedTools to stop Claude using built-in or custom subagents. **[high]**
* [Example subagent definitions](example-subagents.md) - Four sample subagents: code-reviewer, debugger, data-scientist and a db-reader with a read-only SQL hook.
* [Foreground and background subagents](foreground-and-background-subagents.md) - Subagents Claude spawns start in the background by default; how waiting, permissions, notifications and panel rows behave. **[high]**
* [Forking the current conversation](fork-conversation.md) - A fork is a subagent that inherits the full conversation and prompt cache; start one with /subtask or let Claude fork in fork mode. **[high]**
* [Subagent frontmatter fields](frontmatter-fields.md) - Every frontmatter field a subagent file accepts, with requirements, versions and special behavior. **[high]**
* [Nested subagents and depth limit](nested-subagents.md) - Subagents can spawn subagents up to three layers deep by default; the depth is set with CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH. **[high]**
* [Observing and steering running forks](observe-and-steer-forks.md) - Panel keys and follow-up messaging for running forks and subagents, and which commands act on the viewed agent.
* [Preloading skills into subagents](preload-skills-into-subagents.md) - The skills field injects full skill content into a subagent's context at startup, up to 32 names. **[high]**
* [Restricting which subagents can be spawned](restrict-spawnable-subagents.md) - Agent(agent_type) allowlist syntax in tools for an agent running as the main thread with --agent; Task was renamed Agent in 2.1.63. **[high]**
* [Restricting a subagent's tools](restrict-subagent-tools.md) - Use tools as an allowlist and disallowedTools as a denylist, including MCP server wildcards and double-underscore server names. **[high]**
* [Resuming subagents](resume-subagents.md) - Resume a finished subagent by ID or name with SendMessage; transcripts persist per session and are cleaned up after cleanupPeriodDays. **[high]**
* [Scoping MCP servers to a subagent](scope-mcp-to-subagent.md) - The mcpServers field gives a subagent its own inline or referenced MCP servers, subject to folder trust and managed MCP policy. **[high]**
* [Subagent files Claude Code skips](skipped-subagent-files.md) - Frontmatter problems that make Claude Code skip an agent file, and how to validate an agents directory.
* [Subagent auto-compaction](subagent-auto-compaction.md) - Subagents compact as their own context fills; autoCompactWindow lowers the window per subagent. **[high]**
* [Tools available to subagents](subagent-available-tools.md) - Which tools every subagent loses, and the smaller built-in tool set of background subagents. **[high]**
* [Hooks for subagents](subagent-hooks.md) - Frontmatter hooks, settings-level SubagentStart and SubagentStop hooks, PreToolUse validation scripts and trust rules. **[high]**
* [Subagent names, API errors and output scanning](subagent-names-errors-scanning.md) - Naming subagents via the Agent tool name parameter, how API errors surface to Claude, and the scan applied to final reports. **[high]**
* [Subagent permission modes](subagent-permission-modes.md) - How the permissionMode field interacts with the main conversation's mode, including auto, plan, dontAsk and bypassPermissions. **[high]**
* [Subagent persistent memory](subagent-persistent-memory.md) - The memory field gives a subagent a directory that persists across conversations, at user, project or local scope. **[high]**
* [Subagent scopes and priority](subagent-scopes-and-priority.md) - Where subagent definitions live (managed, --agents, project, user, plugin), their priority order and discovery rules. **[high]**
* [Subagents overview](subagents-overview.md) - Subagents run in their own context window with their own prompt, tools and permissions, and return only a summary to the parent. **[high]**
* [Thinking and effort in subagents](thinking-and-effort.md) - Subagents inherit extended thinking; effort comes from the effort field, a per-invocation parameter or the session level. **[high]**
* [What a subagent loads at startup](what-loads-at-startup.md) - Initial context of a non-fork subagent: system prompt, task message, CLAUDE.md, git status, skills and sibling roster, plus what never reaches it. **[high]**
* [Writing subagent files and hot reload](write-subagent-files.md) - Subagent file format, live reload of agent directories, prompt contents, working directory behavior and worktree isolation checks. **[high]**
