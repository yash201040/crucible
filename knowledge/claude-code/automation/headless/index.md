# automation/headless

* [Permissions in -p runs](auto-approve-and-permission-modes.md) - --allowedTools, --permission-mode, default Manual mode from v2.1.302, and how Bash allow entries behave in auto mode. **[high]**
* [Waiting for background work at exit](background-work-at-exit.md) - A claude -p run can stay open for background commands, subagents, workflows, Monitor watches and loop wakeups, with a 10-minute idle cap. **[high]**
* [Bare mode (--bare)](bare-mode.md) - --bare skips hooks, skills, plugins, MCP, memory and CLAUDE.md discovery for fast, reproducible scripted runs. **[high]**
* [Continue and resume in -p mode](continue-and-resume-sessions.md) - --continue, --resume with session ID or transcript path, and background-session behavior from v2.1.257. **[high]**
* [Non-interactive mode with -p](print-mode-basics.md) - claude -p runs Claude Code non-interactively; exit codes, option conflicts and the Agent SDK relationship. **[high]**
* [SIGTERM handling and interrupted turns](sigterm-and-resume.md) - Exit code 143 on SIGTERM, what Claude Code does while exiting, and how to resume the interrupted turn. **[high]**
* [Stream system events: api_retry, init, plugin_install](stream-system-events.md) - Fields of system/api_retry, system/init (plugins, mcp_servers and error arrays, capabilities) and system/plugin_install events. **[high]**
* [Output formats, JSON schema and streaming](structured-output-and-streaming.md) - --output-format text/json/stream-json, --json-schema structured_output, and partial-message streaming. **[high]**
* [Following subagent messages in the stream](subagent-stream-messages.md) - Subagent and forked-skill messages carry parent_tool_use_id; --forward-subagent-text adds text and thinking blocks at every depth. **[high]**
* [System prompt flags and commands in -p mode](system-prompt-and-commands.md) - Appending or replacing the system prompt, and which slash commands and forms work non-interactively.
* [--permission-prompts none for unattended runs](unattended-permission-prompts.md) - Deny anything that would prompt, never wait on a permission host; needs v2.1.259 or later. **[high]**
