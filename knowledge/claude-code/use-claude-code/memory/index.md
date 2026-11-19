# use-claude-code/memory

* [Reading AGENTS.md as project instructions](agents-md-reading.md) - Claude Code reads AGENTS.md directly when no CLAUDE.md is present; rules for which files count, what is read and when it is unavailable.
* [Auto memory](auto-memory.md) - Claude saves its own notes across sessions into a per-repository memory directory with a MEMORY.md index loaded each session. **[high]**
* [CLAUDE.md @path imports](claude-md-imports.md) - Pull other files into CLAUDE.md with @path syntax, with a four-hop depth limit and an approval dialog for external files.
* [CLAUDE.md file locations and scopes](claude-md-locations.md) - Where managed, user, project and local CLAUDE.md files live, in load order from broadest to most specific.
* [CLAUDE.md vs auto memory](claude-md-vs-auto-memory.md) - The two memory systems that carry knowledge across sessions: instructions you write, and notes Claude writes itself. **[high]**
* [How CLAUDE.md files load](how-claude-md-files-load.md) - Hierarchy walk, ordering, on-demand subdirectory loading, comment stripping and loading from --add-dir directories. **[high]**
* [Managed CLAUDE.md and claudeMdExcludes](managed-claude-md-and-excludes.md) - Organization-wide CLAUDE.md via file or the claudeMd setting, and skipping unwanted CLAUDE.md files with claudeMdExcludes.
* [The /memory command](memory-command.md) - Lists and opens CLAUDE.md, CLAUDE.local.md and auto memory files, and toggles auto memory.
* [Memory and instruction size limits](memory-size-limits.md) - Per-file and combined size limits for CLAUDE.md, rules and MEMORY.md, and the 200K/1M context-window character limits for on-demand files.
* [Project instructions setting values](project-instructions-setting.md) - The /config Project instructions setting and its pluginConfigs form that chooses between CLAUDE.md and AGENTS.md loading.
* [Rules in .claude/rules/ and path-scoped rules](rules-directory.md) - Modular instruction files, optionally scoped by a paths glob frontmatter field, with symlink sharing and user-level rules.
* [Troubleshoot instructions not followed](troubleshoot-memory-issues.md) - Debug steps when CLAUDE.md or AGENTS.md is ignored, and what survives /compact.
* [Write effective instructions and audit them](write-effective-instructions.md) - Size, structure and consistency guidance for CLAUDE.md, plus the /doctor prompt-audit check.
