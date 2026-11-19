# plugins-troubleshooting/plugins-loading

* [enabledPlugins sources and precedence](enabled-plugins-precedence.md) - The six settings sources for enabledPlugins in order of precedence, and why a disabled or project-enabled plugin still loads or not. **[high]**
* [Plugin name conflict precedence](name-conflicts.md) - Which plugin wins when enabled plugins share a manifest name, and how same-name hooks and session-only plugins behave.
* [Plugin files on disk and Node dependency install](on-disk-layout-and-dependencies.md) - Layout under the plugins root, in-place versus cached loading, escape rules, 14-day cleanup and the lockfile-based npm/Bun dependency install. **[high]**
* [Plugin load stages, origins and repository plugins](stages-origins-and-repo-plugins.md) - The declared, fetched and loaded stages, plugin id origin suffixes, and trust and component limits for repository plugins. **[high]**
* [Plugins synced from claude.ai](synced-plugins-from-claude-ai.md) - Plugins turned on for a claude.ai account load in Claude Code as name@synced, with sync timing, sign-in requirements and controls. **[high]**
* [Plugin versions, refresh and auto-update rules](versions-and-auto-update.md) - How the plugin version is computed, when a marketplace refreshes before install, and which marketplaces auto-update and when. **[high]**
