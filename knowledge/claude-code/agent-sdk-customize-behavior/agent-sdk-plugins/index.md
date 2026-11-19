# agent-sdk-customize-behavior/agent-sdk-plugins

* [Load local plugins in the SDK](load-local-plugins.md) - Pass local plugin directories in the plugins option of query() so a session gets their skills, agents, hooks and MCP servers. **[high]**
* [Plugin directory structure](plugin-directory-structure.md) - Layout of a plugin directory the SDK can load: optional manifest, skills, commands, agents, hooks and MCP definitions.
* [Reload and add plugins in a running session](reload-and-add-plugins.md) - Apply plugin changes or add plugin folders to a live SDK session with reloadPlugins() (TypeScript) or /reload-plugins (Python). **[high]**
* [Invoke plugin skills by namespace](use-plugin-skills.md) - Plugin skills are namespaced with the plugin name and can be dispatched by sending /plugin-name:skill-name as the prompt.
* [Verify plugins in the init message](verify-plugin-loading.md) - Loaded plugins, plugin skills and commands show up in the system init message; plugin_errors explains a plugin that failed.
