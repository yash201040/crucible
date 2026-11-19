# create-plugins/plugins-publish

* [Plugin distribution routes](choose-how-to-distribute.md) - Compare no-marketplace, own marketplace and Anthropic's directory by who can install, requirements, and auto-update.
* [Prepare a plugin for release](prepare-plugin-for-release.md) - Pre-release checklist: permanent name, versioning choice, strict validation, local marketplace install, metadata, and evals. **[high]**
* [Publish through your own marketplace](publish-through-own-marketplace.md) - Add a .claude-plugin/marketplace.json with a source of ./ and tell users the add and install commands, with version requirements for one-command forms.
* [Ship updates, renames and removals](releases-renames-removals.md) - Increment version to release, tag git releases for dependents, and use the marketplace renames map instead of changing a published name.
* [Share a plugin without a marketplace](share-without-a-marketplace.md) - Send the folder or zip, or point --plugin-url at a release zip; users load it per session or from ~/.claude/skills/.
* [Submit to Anthropic's directory](submit-to-anthropics-directory.md) - Submit a validated plugin from the developer portal on a paid claude.ai plan; it reaches Claude Code as <name>@synced.
