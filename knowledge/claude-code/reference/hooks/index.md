# reference/hooks

* [Adding context for Claude from a hook](p1-additional-context.md) - additionalContext injects a string into Claude's context as a system reminder; where it lands per event and how it persists across resume. **[high]**
* [Hooks that start a background process](p1-background-process-hooks.md) - How to launch long-running programs from a hook without hanging it or losing a deny decision.
* [Command hook fields: exec form and shell form](p1-command-hook-exec-and-shell-form.md) - Command-hook fields (command, args, async, asyncRewake, shell, onFailure) and the difference between exec form and shell form. **[high]**
* [Common hook input fields](p1-common-input-fields.md) - JSON fields every hook receives on stdin or as POST body, plus agent identity fields and environment notes. **[high]**
* [Decision control patterns by event](p1-decision-control.md) - Which decision fields each hook event accepts (top-level decision, permissionDecision, decision.behavior, worktree path) and which events can rewrite content. **[high]**
* [Exit code 2 behavior per event](p1-exit-code-2-per-event.md) - Table of which hook events can block and what exit code 2 does on each. **[high]**
* [Exit codes and how output is read](p1-exit-code-output.md) - Meaning of exit 0, 2 and other codes for hooks, how stdout is parsed as JSON or plain text, and per-event exceptions. **[high]**
* [Hook handler types and common fields](p1-handler-types-and-common-fields.md) - The five handler types and fields shared by all of them: type, if, timeout, statusMessage, once, with timeout defaults and parallelism. **[high]**
* [Hook events and when they fire](p1-hook-events-overview.md) - All hook event names, the three cadences they fall into, and when each one fires. **[high]**
* [Hook locations, scope and managed restrictions](p1-hook-locations-and-scope.md) - Where hooks can be defined, how they merge, and the managed settings that restrict hooks and HTTP hook URLs. **[high]**
* [Hooks in skill and subagent frontmatter](p1-hooks-in-skills-and-agents.md) - Hooks declared in skill or subagent frontmatter, their lifetime, trust rules, plugin-only lock and per-source hook limits. **[high]**
* [The /hooks menu and disabling hooks](p1-hooks-menu-and-disabling.md) - Read-only /hooks browser and the disableAllHooks setting, including its precedence and managed-hook behavior.
* [How a hook resolves](p1-how-a-hook-resolves.md) - Event, matcher, optional if filter and handler fit together; worked PreToolUse example that blocks rm -rf.
* [HTTP hooks and response handling](p1-http-hooks.md) - HTTP hook fields, header env-var interpolation, and how status codes and bodies are interpreted. **[high]**
* [Universal JSON output fields and terminalSequence](p1-json-output-fields.md) - JSON fields every hook may print (continue, stopReason, systemMessage, terminalSequence), the 10,000-character cap and terminal notification rules. **[high]**
* [Matching MCP tools and Monitor commands](p1-match-mcp-and-monitor.md) - How to write matchers for MCP server tools (including plugin-scoped names) and how Bash matchers interact with the Monitor tool.
* [Matcher evaluation rules](p1-matcher-patterns.md) - How a hook matcher string is evaluated: match-all, exact list, or JavaScript regex, with narrower rules for FileChanged and StopFailure.
* [What each event's matcher filters](p1-matcher-values-per-event.md) - Per-event table of the field a matcher is tested against and its allowed values.
* [MCP tool hooks](p1-mcp-tool-hooks.md) - Hook handler type mcp_tool that calls a tool on a configured MCP server, with timing and availability limits. **[high]**
* [Block the action when a hook fails (onFailure)](p1-onfailure-block-on-hook-failure.md) - onFailure: block makes a failed or timed-out command or http hook block the action; includes Windows without Git Bash behavior. **[high]**
* [Referencing hook scripts by path](p1-path-placeholders.md) - Placeholders for project and plugin directories in hook commands, and how they behave inside worktrees. **[high]**
* [Prompt and agent hook fields](p1-prompt-and-agent-hook-fields.md) - Fields for prompt hooks (single-turn model evaluation) and agent hooks (subagent verification, experimental). **[high]**
* [Agent-based hooks (type: agent)](p2-agent-hooks.md) - Experimental hooks that spawn a subagent with tools (up to 50 turns) to verify a condition and return ok. **[high]**
* [Agent tool input and response fields](p2-agent-tool-hook-fields.md) - tool_input for the Agent tool and the run telemetry a PostToolUse hook gets back, including async_launched and SubagentHandback notes. **[high]**
* [Async (background) command hooks](p2-async-hooks.md) - async: true runs a command hook in the background without blocking; output is delivered on a later turn. **[high]**
* [bashEditDiff in PostToolUse](p2-bash-edit-diff.md) - Best-effort list of files a Bash command changed in a Git repo, delivered to PostToolUse in tool_response.bashEditDiff.
* [classifierContext for auto mode](p2-classifier-context.md) - A PostToolUse note aimed at the auto mode classifier instead of Claude, with trust rules and a 2,000-character cap. **[high]**
* [CLAUDE_ENV_FILE persisted environment](p2-claude-env-file.md) - Hooks write export lines to CLAUDE_ENV_FILE so later Bash and PowerShell commands in the session see them.
* [PreCompact and PostCompact hook events](p2-compact-hooks.md) - Hooks around context compaction: PreCompact can block it or add summary instructions; PostCompact sees the summary. **[high]**
* [ConfigChange hook event](p2-configchange-event.md) - Fires when a settings, managed policy or skill file changes mid-session; can block non-policy changes.
* [CwdChanged hook event](p2-cwdchanged-event.md) - Fires when a shell command in the main conversation changes directory; can return watchPaths and use CLAUDE_ENV_FILE.
* [Debugging hooks](p2-debug-hooks.md) - Where hook execution is logged (--debug, --debug-file), the log line format for timing, and verbose matcher logging.
* [Defer a tool call for later (-p)](p2-defer-tool-call.md) - A PreToolUse hook returns defer so a claude -p run pauses at a tool call and resumes later with the answer. **[high]**
* [DirectoryAdded hook event](p2-directoryadded-event.md) - Runs in the background after /add-dir or an SDK register_repo_root request adds a working directory.
* [Elicitation hook event](p2-elicitation-event.md) - Intercepts an MCP server's mid-task input request so a hook can accept, decline or cancel without a dialog. **[high]**
* [ElicitationResult hook event](p2-elicitationresult-event.md) - Runs after the user answers an MCP elicitation; can pass, rewrite, decline or cancel the response.
* [FileChanged hook event and watch list](p2-filechanged-event.md) - Fires on filesystem changes to watched files regardless of who changed them; matcher builds the watch list.
* [InstructionsLoaded hook event](p2-instructionsloaded-event.md) - Observability-only event fired when a CLAUDE.md or .claude/rules file is loaded, eagerly or lazily.
* [MessageDisplay hook event](p2-messagedisplay-event.md) - Rewrites assistant text as it streams to the screen; display-only, transcript and Claude keep the original.
* [Notification hook event and types](p2-notification-event.md) - Notification hook matchers (permission_prompt, idle_prompt, quota_auto_resume_*, agent_*) with timing and version notes.
* [Permission update entries](p2-permission-update-entries.md) - The array format used by updatedPermissions and permission_suggestions: types, fields, modes and destinations. **[high]**
* [PermissionDenied hook event](p2-permissiondenied-event.md) - Fires when auto mode denies a tool call; a hook can set retry to tell the model it may try again. **[high]**
* [PermissionRequest hook event](p2-permissionrequest-event.md) - Fires when Claude Code is about to ask for permission; hook can allow or deny on the user's behalf. **[high]**
* [PostModelSwitch hook event](p2-postmodelswitch-event.md) - Runs after the session model changes, including automatic fallback and resume; adds guidance for the next request. **[high]**
* [PostToolBatch hook event](p2-posttoolbatch-event.md) - Fires once after every tool call in a parallel batch resolves, before the next model request.
* [PostToolUse hook event](p2-posttooluse-event.md) - Runs after a tool succeeds; can add feedback, replace the tool output Claude sees, and handle interrupts. **[high]**
* [PostToolUseFailure hook event](p2-posttoolusefailure-event.md) - Fires when a started tool fails; gives error and is_interrupt and can add context for Claude.
* [Running hooks in PowerShell on Windows](p2-powershell-hooks.md) - shell: powershell on a command hook; placeholder rewriting for CLAUDE_PROJECT_DIR and friends.
* [PreModelSwitch hook event](p2-premodelswitch-event.md) - Runs before a requested model switch; can block or confirm it using cache-cost fields in the input. **[high]**
* [PreToolUse hook event and decisions](p2-pretooluse-event.md) - Runs before a tool call; can allow, deny, ask or defer, rewrite input, and add context. **[high]**
* [tool_input fields per tool](p2-pretooluse-tool-inputs.md) - The tool_input fields that PreToolUse and PostToolUse hooks receive for Bash, PowerShell, Write, Edit, Read, Glob, Grep, WebFetch, WebSearch, AskUserQuestion, ExitPlanMode.
* [Answering AskUserQuestion and ExitPlanMode from a hook](p2-pretooluse-user-interaction.md) - In -p runs these interactive tools need a permission host or a PreToolUse hook that returns allow with updatedInput. **[high]**
* [Prompt-based hooks and event support matrix](p2-prompt-hooks.md) - type: prompt hooks have an LLM return ok/reason; lists which events support which hook types and what ok:false does per event. **[high]**
* [Hook security and workspace trust](p2-security-workspace-trust.md) - Hooks run with your full user permissions; settings-file hooks run only after workspace trust, but -p and SDK sessions treat folders as trusted. **[high]**
* [SessionEnd hook event and timeout](p2-sessionend-event.md) - Cleanup hook at session end with reason matchers and a 1.5 second default budget. **[high]**
* [SessionStart hook event](p2-sessionstart-event.md) - Fires when a session starts, resumes, clears, compacts or forks; input carries source, model and resume-cost fields. **[high]**
* [SessionStart output fields and skill reload](p2-sessionstart-output.md) - Fields a SessionStart hook can return: additionalContext, initialUserMessage, sessionTitle, watchPaths, reloadSkills. **[high]**
* [Setup hook event](p2-setup-event.md) - Fires only with --init-only, or --init/--maintenance under -p, for explicit one-time install or cleanup runs. **[high]**
* [Stop hook event and background task data](p2-stop-event.md) - Runs when the main agent finishes; can block stopping, with an 8-continuation cap and background_tasks/session_crons input. **[high]**
* [StopFailure hook event and error types](p2-stopfailure-event.md) - Runs instead of Stop when a turn ends on an API error; input error values for matching and logging. **[high]**
* [SubagentStart and SubagentStop hook events](p2-subagent-hooks.md) - Hooks around subagent spawn and finish: inject context into a subagent, or block it from stopping. **[high]**
* [TaskCreated and TaskCompleted hook events](p2-task-hooks.md) - Hooks that can block creating or completing a task; no matchers; also drive teammate behavior. **[high]**
* [TeammateIdle hook event](p2-teammateidle-event.md) - Fires when an agent team teammate is about to go idle; can keep it working or force idle. **[high]**
* [UserPromptExpansion hook event](p2-userpromptexpansion-event.md) - Fires when a user-typed slash command or MCP prompt expands into a prompt; can block or add context.
* [UserPromptSubmit hook event](p2-userpromptsubmit-event.md) - Runs before Claude processes a prompt; can add context, set the session title or block the prompt. **[high]**
* [WorktreeCreate hook event](p2-worktreecreate-event.md) - Replaces Claude Code's default git worktree creation; the hook must return the new worktree path. **[high]**
* [WorktreeRemove hook event](p2-worktreeremove-event.md) - Cleans up worktrees that a WorktreeCreate hook made; exit code decides success, with git fallback rules. **[high]**
