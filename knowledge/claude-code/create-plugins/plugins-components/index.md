# create-plugins/plugins-components

* [Subagents in a plugin](agents-in-plugins.md) - Ship subagents as agents/*.md, with scoped names, subfolder naming, and which frontmatter fields plugin agents support or ignore. **[high]**
* [Channels in a plugin](channels-in-plugins.md) - A plugin channel is an MCP server plus a channels manifest entry that binds to it and can prompt for its own userConfig.
* [Commands in a plugin](commands-in-plugins.md) - The older single-file command format: commands/<file>.md, subdirectory naming, and defining commands inline in the manifest.
* [Plugin executables in bin/](executables-bin-directory.md) - Files in the plugin bin/ directory are put on the Bash tool's PATH while the plugin is enabled.
* [Hooks in a plugin](hooks-in-plugins.md) - Plugin hooks live in hooks/hooks.json, register when the plugin loads, get plugin env vars, and have MCP-tool matcher naming rules. **[high]**
* [LSP servers in a plugin](lsp-servers-in-plugins.md) - Declare language servers in .lsp.json; the plugin configures the connection but does not install the binary.
* [MCP servers in a plugin](mcp-servers-in-plugins.md) - Declare MCP servers in .mcp.json or the mcpServers key, with naming, substitution, reload behavior, and packaged MCPB bundles. **[high]**
* [Monitors in a plugin](monitors-in-plugins.md) - Background shell commands started with the session whose output reaches Claude as notifications; interactive sessions only. **[high]**
* [Plugin component default locations](plugin-component-locations.md) - Where each plugin component lives by default, how it is named for the user, and which manifest key replaces or adds to the folder. **[high]**
* [Plugin path variables and data directory](plugin-paths-and-data-directory.md) - CLAUDE_PLUGIN_ROOT, CLAUDE_PLUGIN_DATA and CLAUDE_PROJECT_DIR substitutions and installing dependencies into the persistent data directory.
* [Plugin userConfig values](plugin-user-configuration.md) - Declare values users must supply in userConfig; the dialog appears in interactive /plugin flows, and shell installs take --config or --values-stdin.
* [Skills in a plugin](skills-in-plugins.md) - Put a SKILL.md in its own directory under skills/ to ship a skill, with command naming, extra directories, and root-skill rules. **[high]**
* [Plugin themes and output styles](themes-and-output-styles.md) - Plugins can ship color themes and output styles that appear in /theme and /output-style, with the manifest keys that replace the folder scan.
