# plugins-reference/plugins-cli-reference

* [Accept a displayed install command](accept-a-displayed-install-command.md) - A failed --json install carries a shownCommand with sha256 that --accept-command accepts in a later run from your own terminal. **[high]**
* [claude plugin marketplace add](marketplace-add.md) - Adds a marketplace from GitHub, git, URL, local directory or file, or claude.ai and declares it in a settings scope.
* [claude plugin marketplace list](marketplace-list.md) - Lists added marketplaces with source; --json gives an array with name, source, repo, url, path, ref and installLocation.
* [claude plugin marketplace remove and update](marketplace-remove-update.md) - remove deletes a marketplace declaration and, from the last scope, its cache and installed plugins; update refreshes one or all marketplaces.
* [claude plugin commands: shared rules](plugin-commands-overview.md) - claude plugin (alias plugins) runs from a shell or script; shared exit codes, plugin argument forms and scope values.
* [claude plugin configure](plugin-configure.md) - Shows an installed plugin's userConfig options or saves JSON values piped on stdin, scriptable with --json.
* [claude plugin details](plugin-details.md) - Shows a loaded plugin's component inventory and projected always-on token cost.
* [claude plugin enable and disable](plugin-enable-disable.md) - Enable or disable a plugin at a scope (auto-detected local, project, user); --all disables everything; dependencies are enforced.
* [claude plugin eval init](plugin-eval-init.md) - Creates an eval suite in the current plugin directory via an interactive authoring interview, or a blank template with --bare or no terminal.
* [claude plugin eval](plugin-eval.md) - Runs a plugin's eval cases several times in isolated sessions, with and without the plugin, and reports scored results with CI exit codes. **[high]**
* [claude plugin init](plugin-init.md) - Scaffolds a plugin at ~/.claude/skills/<name>/ that loads next session as <name>@skills-dir with no install step.
* [claude plugin install](plugin-install.md) - Installs a plugin from a configured marketplace with scope, userConfig, non-interactive acceptance of command sources and JSON output. **[high]**
* [Plugin --json result format](plugin-json-result.md) - With --json the last stdout line is one JSON object with command, outcome and message; marketplace commands use the same shape. **[high]**
* [claude plugin list and its JSON fields](plugin-list.md) - Lists installed plugins with version, scope and status; --json gives per-installation objects, --available adds uninstalled marketplace plugins.
* [claude plugin prune](plugin-prune.md) - Removes auto-installed dependencies that no installed plugin needs; --dry-run previews and -y is required without a TTY.
* [/plugin session commands](plugin-slash-commands.md) - Forms of /plugin inside an interactive session (aliases /plugins, /marketplace) and which shell subcommands have no session form.
* [claude plugin tag](plugin-tag.md) - Creates an annotated git tag <name>--v<version> for a plugin release after checking plugin.json and marketplace versions agree.
* [claude plugin test](plugin-test.md) - Runs every *.test.ts and *.test.tsx file under a mod's directory with no session, sign-in or network; exits 1 on failure.
* [claude plugin uninstall](plugin-uninstall.md) - Removes a plugin from one scope; deletes stored options, secrets and data directory when removed from the last scope unless --keep-data.
* [claude plugin update](plugin-update.md) - Updates a plugin to the latest marketplace version, loaded next session or after /reload-plugins; scope auto-detected including managed.
* [claude plugin validate](plugin-validate.md) - Validates a plugin or marketplace manifest or component files with exit codes 0, 1 and 2, optional --strict and a --json report for CI. **[high]**
* [/reload-plugins](reload-plugins.md) - Applies pending plugin changes to the running session, with a summary line, a cache guard for MCP changes, and limits in non-interactive sessions. **[high]**
* [--plugin-dir and --plugin-url](session-only-plugin-flags.md) - Two repeatable claude flags load a plugin from a directory, .zip or URL for one session without installing it; admins can block them. **[high]**
* [Validate: README install-line advice](validate-readme-advice.md) - An Advice block means a plugin README lacks a marketplace install line; it never changes the verdict or exit code.
