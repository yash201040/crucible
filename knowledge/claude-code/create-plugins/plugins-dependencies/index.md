# create-plugins/plugins-dependencies

* [Bundle plugins for a team](bundle-plugins-for-a-team.md) - A plugin with only a name and a dependencies array installs a curated plugin set with one command.
* [How constraints resolve and combine](constraint-resolution-and-conflicts.md) - Highest matching tag wins; several plugins' ranges intersect, conflicts block installs, and auto-update honors all ranges.
* [Cross-marketplace dependency allowlist](cross-marketplace-dependencies.md) - A dependency from another marketplace is installed only if the root marketplace lists it in allowCrossMarketplaceDependenciesOn or it is already enabled.
* [Declare plugin dependencies](declare-plugin-dependencies.md) - List dependencies in plugin.json as names or objects with a semver version range and optional marketplace. **[high]**
* [Dependencies for plugins synced from claude.ai](dependencies-synced-from-claude-ai.md) - A plugin turned on in claude.ai loads as <name>@synced, and a marketplace-named dependency is met by an installed copy or a same-name claude.ai plugin.
* [Version constraints on non-git sources](non-git-source-constraints.md) - For npm, archive and command plugin sources the constraint is only checked at load time, and command or headersHelper dependencies are never installed by Claude Code.
* [Tag plugin releases with claude plugin tag](tag-releases-for-dependents.md) - Constraints resolve against git tags named <plugin-name>--v<version>; claude plugin tag validates and creates them.
* [Test a plugin with its dependency locally](test-plugin-and-dependency-locally.md) - Load both with --plugin-dir; the local copy satisfies the dependency and version constraints are not checked against it.
