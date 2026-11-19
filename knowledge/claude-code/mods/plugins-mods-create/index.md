# mods/plugins-mods-create

* [Change a mod with Claude](change-a-mod-with-claude.md) - Start with --plugin-dir at the mod so Claude's edits load in the same session; edits need approval in default and acceptEdits modes.
* [Generated mod type definitions](mod-type-definitions.md) - Claude Code writes TypeScript declaration files into .claude-plugin/types/ matching the running version for editor autocomplete and type-checking.
* [Share and version a mod](share-your-mod.md) - A mod is a plugin: share by folder, marketplace, managed settings or directory; develop against --plugin-dir not the installed copy.
* [Test a mod with claude plugin test](test-a-mod-claude-plugin-test.md) - claude plugin test runs tests that fire events at a mod's hooks with no session, sign-in or network.
* [Validate a mod with claude plugin validate](validate-a-mod.md) - Static analysis lists a mod's hooks, API calls, env and state access, and enforces rules on how hooks and calls are written.
* [Mods and asking Claude to write one](what-a-mod-is-and-ask-claude.md) - A mod is a plugin with a hooks module; Claude writes one from a description using the plugin-authoring skill into the session's dev-mods folder. **[high]**
* [When Claude-written mods load or cannot load](when-mods-load-without-asking.md) - auto and bypassPermissions load mods without asking; dontAsk, untrusted workspaces, --safe-mode, --bare and disableAllHooks prevent loading. **[high]**
* [Write a mod yourself](write-a-mod-yourself.md) - Three files (plugin.json, hooks/hooks.json with a modules key, register.js) make a mod; load with --plugin-dir and edits hot-reload. **[high]**
