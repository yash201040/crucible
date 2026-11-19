# plugins-reference/plugins-manifest-reference

* [Plugin channels](channels-config.md) - channels declares message channels (e.g. a chat bridge) each bound to one of the plugin's MCP servers, with optional userConfig prompts.
* [Component path forms](component-path-forms.md) - Accepted shapes for agents, skills, outputStyles, workflows, commands, hooks and mcpServers entries in plugin.json, with merge behavior. **[high]**
* [lspServers configuration fields](lspservers-config.md) - Strict per-server fields for lspServers: command, extensionToLanguage, timeouts, restart controls and diagnostics.
* [plugin.json fields](manifest-fields-table.md) - Every top-level plugin.json key with type and behavior; name is the only required field. **[high]**
* [plugin.json manifest file and validation](manifest-file-and-validation.md) - The optional .claude-plugin/plugin.json holds metadata, userConfig and component declarations; unrecognized fields are stripped, strict objects reject unknown keys.
* [Marketplace entries versus plugin.json](marketplace-entries-and-manifest.md) - How a marketplace entry and plugin.json combine under strict true/false, and metadata precedence between them.
* [displayName, version, defaultEnabled, dependencies](metadata-version-and-defaults.md) - Behavior of version pinning, displayName precedence, defaultEnabled persistence, dependency entry shapes and directory-listing fields.
* [Plugin monitors configuration](monitors-config.md) - experimental.monitors declares persistent background commands that start at session start or when a named skill first runs. **[high]**
* [Plugin name rules and reserved names](name-rules.md) - name must be non-empty with no spaces, @, : or path separators; validate errors or warns on names that pass as Anthropic's own.
* [Path rules, containment and defaults](path-rules.md) - Component paths start with ./, resolve inside the plugin root and must exist; each key replaces, adds to or merges with its default location.
* [Plugin path variables](plugin-path-variables.md) - CLAUDE_PLUGIN_ROOT, CLAUDE_PLUGIN_DATA and CLAUDE_PROJECT_DIR: where they resolve, are exported, and how to quote them. **[high]**
* [Plugin standard layout](standard-layout.md) - Default locations of each plugin component type and the bin/ directory that puts executables on the Bash tool PATH. **[high]**
* [Using userConfig values in a plugin](userconfig-references.md) - ${user_config.KEY} substitution and CLAUDE_PLUGIN_OPTION_<KEY> variables; shell-form fields reject ${user_config.*}.
* [userConfig schema](userconfig-schema.md) - userConfig declares values prompted when a plugin is enabled; strict option fields, fixed options lists, storage of sensitive values.
