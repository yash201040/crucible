# guides/large-codebases

* [Read deny rules for generated code](block-reads-generated-code.md) - Use Read deny rules in permissions.deny to keep checked-in build output and vendored code out of context, with coverage limits. **[high]**
* [Centralize conventions at scale](centralize-conventions.md) - Move conventions from always-loaded CLAUDE.md into skills, plugins and MCP code search, and recommend plugins with a SessionStart hook.
* [Choose where to start Claude](choose-where-to-start.md) - The launch directory decides file access, which CLAUDE.md files load at startup, and which project settings apply. **[high]**
* [Code intelligence plugins](code-intelligence-plugins.md) - LSP-backed plugins let Claude find definitions and references without scanning files; install from the official marketplace.
* [Combined monorepo configuration](combined-monorepo-config.md) - Worked example for packages/api combining sparse worktrees, additionalDirectories and deny rules, with a second deny copy at the root for worktrees.
* [Plan cross-package changes](cross-package-changes.md) - Give Claude a whole cross-package change in one session and plan first in plan mode; the plan file is re-injected after compaction.
* [claudeMdExcludes setting](exclude-claude-md-files.md) - claudeMdExcludes skips CLAUDE.md and rules files by absolute-path glob so they never load.
* [Access across packages and repos](grant-access-across-packages.md) - additionalDirectories, --add-dir and /add-dir grant file access to sibling directories; they differ in whether CLAUDE.md and skills load. **[high]**
* [Layer CLAUDE.md files by directory](layered-claude-md-files.md) - Split instructions into a root CLAUDE.md plus per-directory files so only relevant conventions load; compare with path-scoped rules.
* [Per-directory skills](per-directory-skills.md) - Place skills under .claude/skills/ in a subdirectory, or scope root skills with the paths frontmatter field.
* [Keep skills discoverable](skill-discoverability.md) - Which skills are in scope depends on the launch directory; descriptions can be cut when many skills exist; track usage via OpenTelemetry.
* [Sparse worktrees](worktree-sparse-paths.md) - worktree.sparsePaths uses git sparse-checkout so created worktrees hold only listed directories; symlinkDirectories avoids duplicating node_modules. **[high]**
