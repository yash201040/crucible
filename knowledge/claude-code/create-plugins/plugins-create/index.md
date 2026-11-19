# create-plugins/plugins-create

* [Convert a .claude/ setup into a plugin](convert-claude-setup-to-plugin.md) - Copy commands, agents, skills and the settings hooks object into a plugin; originals stay loaded alongside and hooks run twice.
* [Create your first plugin](first-plugin-walkthrough.md) - Minimal steps to build, validate and run a one-skill plugin with --plugin-dir, including the manifest fields.
* [Load a plugin for one session](load-plugin-for-one-session.md) - --plugin-dir, --plugin-url and CLAUDE_CODE_PLUGIN_DIRS load plugins from disk, zip or URL without a marketplace. **[high]**
* [Plugin starter layout](plugin-layout-table.md) - The directories most plugins start with and what the manifest-less default does.
* [Ways to share a finished plugin](share-a-plugin-routes.md) - Three routes: send the folder or zip, list it in your own marketplace, or submit to Anthropic's directory.
* [Skills-directory plugins and plugin init](skills-directory-plugins.md) - A folder with .claude-plugin/plugin.json under ~/.claude/skills/ auto-loads every session; claude plugin init scaffolds one.
* [Test and debug a plugin](test-and-debug-plugin.md) - Ordered checks for a plugin that does not load: validate, reload, /plugin tabs, plugin list, plus common failure causes. **[high]**
* [When to make a plugin](when-to-make-a-plugin.md) - Standalone .claude/ setups suit one project or person; a plugin adds sharing, multi-project install and versioned releases, with plugin-name prefixes. **[high]**
