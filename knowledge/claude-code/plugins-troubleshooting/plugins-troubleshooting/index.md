# plugins-troubleshooting/plugins-troubleshooting

* [Errors when adding or refreshing a marketplace](add-marketplace-errors.md) - Messages, causes and fixes for failed marketplace adds and refreshes: source format, git credentials, timeouts, names, offline and GHES.
* [Policy refusal messages for plugins](blocked-by-organization-errors.md) - User-facing messages when managed settings block marketplaces, plugins, sideload flags, skills-dir or command sources, and the setting behind each. **[high]**
* [Plugin authoring errors and claude plugin validate messages](build-plugin-and-validate-errors.md) - Developer-side failures: component paths, userConfig, skills not loading, strict-mode conflicts, and the validate message table and flags.
* [Plugin dependency error messages](dependency-errors.md) - Dependency messages at install or load time, their meanings, fixes, and the errorDetails types in claude plugin list --json.
* [Errors when installing plugins or loading marketplaces](install-and-marketplace-state-errors.md) - Install-time and load-time messages: not found, archive integrity, reserved or ignored marketplaces, source conflicts, manifest and cache errors.
* [Plugin installed but not working: reload, state files, hooks, MCP, LSP](installed-plugin-not-working.md) - Messages and fixes after a successful install: /reload-plugins, cache and records files, settings, hooks, MCP servers and language servers. **[high]**
* [Marketplace-level validation messages and URL-marketplace pitfalls](marketplace-validation-messages.md) - Marketplace validate errors and warnings, relative-path failures in URL marketplaces, and submodule gaps for root plugins.
* [Where /plugin runs and command spellings](plugin-command-surfaces-and-spellings.md) - Surfaces where /plugin is unavailable, shell mistakes, and the table of nonexistent plugin command spellings with real equivalents.
