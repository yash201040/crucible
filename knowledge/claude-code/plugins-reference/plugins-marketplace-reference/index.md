# plugins-reference/plugins-marketplace-reference

* [archive plugin source](archive-plugin-source.md) - Zip-over-HTTPS plugin source with optional sha256 integrity pin and its URL restrictions.
* [command plugin source](command-plugin-source.md) - A plugin source whose directory is printed by a shell command, with timeout, copy and link modes and failure conditions.
* [Entry vs plugin.json, display fields and strict mode](entry-vs-plugin-json-and-strict.md) - How a marketplace entry combines with a plugin's own plugin.json, which fields users see, and what strict true or false does.
* [github, url, git-subdir and npm source details](git-and-npm-source-details.md) - Field rules and refusals for github, url, git-subdir and npm plugin sources, with examples.
* [Marketplace file location and reserved names](marketplace-file-and-reserved-names.md) - Where marketplace.json lives, how marketplace roots resolve, and which marketplace names are reserved or refused.
* [Marketplace source fields and policy-only values](marketplace-source-fields.md) - Per-type marketplace source fields (ref, path, sparsePaths, skipLfs, headers) and values valid only in strictKnownMarketplaces and blockedMarketplaces.
* [Marketplace source types](marketplace-source-types.md) - Marketplace source objects (url, github, git, npm, file, directory, settings, skills-dir, hostPattern, pathPattern) and how each behaves in three settings keys.
* [Plugin entry fields](plugin-entry-fields.md) - Fields of an item in the marketplace plugins array, including strict, engines, defaultEnabled, headers and headersHelper.
* [Plugin source types](plugin-source-types.md) - The seven plugin source types (relative path, github, url, git-subdir, npm, archive, command) with fields and the shared ref and sha pins.
* [Relative path sources, pluginRoot and submodules](relative-path-and-submodules.md) - How relative plugin paths resolve, the bare-name pluginRoot shortcut, and which git submodules Claude Code fetches.
* [marketplace.json top-level fields](top-level-fields.md) - Every top-level key Claude Code reads from marketplace.json, with types and version requirements.
* [claude plugin validate marketplace messages](validation-messages.md) - Errors and warnings printed by claude plugin validate for marketplace.json, mapped to the field they name, plus failures validation misses.
