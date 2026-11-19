# use-claude-code/sessions

* [Branching a session](branch-a-session.md) - Copy a conversation into a new session with /branch or --fork-session, and what state the branch inherits. **[high]**
* [Export transcripts and access sessions from scripts](export-and-script-access.md) - Use /export for readable text, and claude -p JSON output, --resume, hooks' transcript_path or the Agent SDK for structured access. **[high]**
* [Context commands in a session](manage-context-in-session.md) - /clear, /compact and /context control what is in the context window without leaving the session. **[high]**
* [Naming sessions](name-your-sessions.md) - Ways to name a session, plus the default display name and generated title that Claude Code assigns to unnamed ones. **[high]**
* [Permission mode on resume](permission-mode-on-resume.md) - Which permission mode a resumed session starts in, by resume route, including plan-mode restoration under -p. **[high]**
* [Pinning the project directory name](project-directory-name.md) - CLAUDE_CODE_PROJECT_DIR_NAME fixes the transcript and auto memory directory name for hosts that embed Claude Code. **[high]**
* [Resume by session ID or name](resume-by-id-or-name.md) - Lookup order for session IDs across projects and how exact and ambiguous names resolve. **[high]**
* [The Resume this conversation dialog](resume-conversation-dialog.md) - A usage estimate shown when resuming a long conversation on Pro, Max and Ultra plans.
* [Resume entry points](resume-entry-points.md) - The commands and flags that reopen a saved session: --continue, --resume, --from-pr and /resume. **[high]**
* [Resuming a running background session](resume-running-background-session.md) - How --resume and /resume behave when the target is a background session that is still running, and when Claude Code refuses to attach. **[high]**
* [Where the session picker looks](session-picker-scope.md) - Which sessions the picker and --continue list, and which they hide: /loop, -p, SDK and running background sessions. **[high]**
* [Session picker shortcuts](session-picker-shortcuts.md) - Keyboard shortcuts for navigating, searching and widening the interactive session picker.
* [Transcript storage, retention and deletion](transcript-storage-and-retention.md) - Where session transcripts live, the settings and env vars that move, limit or suppress them, and how to delete them. **[high]**
* [What a resumed session restores](what-a-resume-restores.md) - State carried back on resume (history, model, agent, permission mode, goal, scheduled tasks) and the flags you must pass again. **[high]**
