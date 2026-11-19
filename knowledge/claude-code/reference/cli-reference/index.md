# reference/cli-reference

* [Admin, review, import and maintenance commands](admin-and-maintenance-commands.md) - Subcommands for the gateway, remote control, self-hosted runner, auto mode, ultrareview, import, purge, plugins and doctor.
* [Authentication and token commands](auth-and-token-commands.md) - claude auth login, logout, status, setup-token and MCP login/logout subcommands for signing in, including CI tokens. **[high]**
* [Background session and supervisor commands](background-session-commands.md) - claude agents, attach, logs, respawn, stop, rm and the daemon subcommands for managing background sessions from the shell. **[high]**
* [Display, debug and version flags](flags-display-and-debug.md) - Flags for screen-reader output, debug logging to category or file, and printing the version.
* [Agent, MCP, plugin and integration flags](flags-extensions-and-integrations.md) - Flags that load subagents, MCP servers, plugins, channels, Chrome and IDE integration, or disable skills. **[high]**
* [Model, effort and context flags](flags-model-and-effort.md) - Flags for choosing the model, effort level, fallback chain, advisor model, auto-compact window and API beta headers. **[high]**
* [Permission, tool and settings flags](flags-permissions-and-tool-access.md) - Flags controlling permission modes, allowed and denied tools, extra directories, restricted and safe mode, and settings sources. **[high]**
* [Print-mode and output flags](flags-print-mode-and-output.md) - Flags for non-interactive -p runs: output and input formats, JSON schema, budgets, turn limits, hook events, bare mode, persistence. **[high]**
* [Session, background, cloud and worktree flags](flags-sessions-background-cloud.md) - Flags for continuing, resuming and forking sessions, background agents, cloud and Remote Control sessions, worktrees and team display. **[high]**
* [Core claude launch and print commands](session-start-commands.md) - The basic claude invocations: interactive start, one-shot -p queries, piping, continue, resume, update and install. **[high]**
* [System prompt flags and snapshot behavior](system-prompt-flags.md) - Five flags to replace or append to the system prompt, how combining works, caching boundary marker and recording in resumed sessions. **[high]**
