# reference/tools-reference

* [Agent tool behavior](agent-tool-behavior.md) - How the Agent tool spawns subagents, teammates and forks, resolves tool lists, caps turns and surfaces permission prompts. **[high]**
* [AskUserQuestion tool and question timeout](askuserquestion-tool.md) - Multiple-choice questions to the user, with an optional auto-continue timeout.
* [Background command time limits](background-command-time-limits.md) - Time limits on background Bash/PowerShell commands in unattended sessions, how to raise them and how long -p runs wait. **[high]**
* [Bash timeout and output limits](bash-timeout-and-output-limits.md) - Default and maximum foreground timeouts, inline output ceilings, read-back window and the settings that change them. **[high]**
* [Bash tool: what persists between commands](bash-working-directory-and-env.md) - Each Bash command is a separate process; working directory carries over under conditions, environment variables do not.
* [Edit tool behavior, Perforce mode and non-UTF-8 files](edit-tool-behavior.md) - Exact-string edit rules, read-before-edit requirements, and how non-UTF-8 files are handled.
* [EndConversation tool](endconversation-tool.md) - A tool that ends an interactive session in rare abuse cases; exempt from permission rules and hooks, and absent in headless and SDK runs.
* [EnterWorktree tool behavior](enterworktree-tool.md) - Creates or enters a git worktree; prompt rules for paths outside .claude/worktrees and when the tool is removed. **[high]**
* [Glob and Grep tool behavior](glob-and-grep-tools.md) - Glob and Grep are absent by default on macOS, Linux and WSL; when they return, and their search semantics and limits. **[high]**
* [LSP tool behavior](lsp-tool.md) - Code intelligence from language servers, active only once a code intelligence plugin is installed.
* [Monitor tool](monitor-tool.md) - Runs a background command and streams each output line to Claude as an event, with deadlines and permission rules shared with Bash. **[high]**
* [Monitor WebSocket source](monitor-websocket-source.md) - Monitor can open a ws:// or wss:// socket in place of a command; event rules, denied addresses and Bash-rule interactions.
* [NotebookEdit tool behavior](notebookedit-tool.md) - Cell-level Jupyter edits with replace, insert and delete modes; replacing a code cell clears its outputs.
* [Where tool names are used and rule formats](permission-rule-formats.md) - The places that accept tool names and the ToolName(specifier) formats for permission rules. **[high]**
* [PowerShell tool](powershell-tool.md) - Native PowerShell execution: availability by platform, enabling, Bash deny-rule interaction, shell selection and encoding notes.
* [Read tool behavior and large files](read-tool-behavior.md) - File types Read handles, size and token limits, and allow_large for whole-file reads.
* [SendFeedback tool and Claude-drafted feedback](sendfeedback-tool.md) - Claude drafts feedback reports queued locally for review; controls, retention of drafts and where the tool is absent.
* [Task tool availability](task-tool-availability.md) - Which models get TaskCreate/TaskGet/TaskList/TaskUpdate by default, how to opt in, and behavior in subagents and agent teams. **[high]**
* [Tool memory limit on Linux and WSL](tool-memory-limit-linux.md) - A cgroup memory cap for Bash, PowerShell and Monitor commands, with optional exclusions for other process kinds. **[high]**
* [Tools: agents, messaging, scheduling, tasks](tools-agents-and-sessions.md) - Built-in tool names for spawning agents, messaging, scheduling, task tracking, workflows and notifications, with permission and version notes. **[high]**
* [Tools: files, shell, web, plan and MCP](tools-files-shell-and-web.md) - Built-in tool names for file access, shell, web, worktrees, plan mode, MCP resources and code intelligence, with permission needs. **[high]**
* [WebFetch tool behavior](webfetch-tool.md) - URL fetch with a prompt-driven extraction step, caching, deadlines, domain permission prompts and availability controls.
* [WebSearch tool and session search limit](websearch-tool.md) - Anthropic-backend web search, up to 8 backend searches per call, a 200-call session cap with refill, and per-turn limits in -p and SDK runs. **[high]**
* [Write tool behavior](write-tool-behavior.md) - Whole-file create or overwrite and when a prior read is required.
