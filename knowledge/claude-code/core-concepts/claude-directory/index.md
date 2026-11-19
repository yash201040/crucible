# core-concepts/claude-directory

* [Subagent memory directories](agent-memory-directories.md) - Where subagents with a memory frontmatter field keep persistent MEMORY.md notes, and how much loads into their system prompt. **[high]**
* [Application data and automatic cleanup](application-data-retention.md) - Files Claude Code writes under ~/.claude (transcripts, file history, debug logs), cleanupPeriodDays retention and when the sweep is skipped. **[high]**
* [claude purge: delete local project state](claude-purge-command.md) - The claude purge command deletes one project's transcripts, memory and history entries, with dry-run, yes, all and interactive options.
* [Frontmatter fields by file type](frontmatter-fields-by-file.md) - The YAML frontmatter field names accepted by skills, command files, subagents, output styles and rules. **[high]**
* [Global ~/.claude files and when they load](global-config-files.md) - User-scope files under ~/.claude and ~/.claude.json: CLAUDE.md, settings, keybindings, themes, rules, skills, agents, workflows, auto memory.
* [Files kept until deleted and state files to keep](kept-state-files.md) - Paths the retention sweep does not remove (history, stats, remote settings cache, policy limits) and state directories that must not be deleted.
* [Files outside the explorer and choosing the right file](other-files-not-in-explorer.md) - managed-settings.json, CLAUDE.local.md, AGENTS.md, plugin directories, and a table mapping each customization goal to the right file.
* [Reducing transcript exposure](plaintext-storage-and-privacy.md) - Transcripts and history are unencrypted; options to shorten retention or skip writing them, including no-session-persistence for headless and SDK runs. **[high]**
* [Project config files and when they load](project-config-files.md) - Project-scope files (CLAUDE.md, .mcp.json, .worktreeinclude, settings, rules, skills, agents, workflows, output styles) with load timing and precedence. **[high]**
* [Session scratchpad directory](session-scratchpad-directory.md) - A per-session temp directory Claude uses instead of /tmp, its path per OS, retention, hook access via scratchpad_dir, and when a session has one. **[high]**
