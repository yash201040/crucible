# manage-plugins-for-your-organization/plugins-org

* [Plugin audit, suggestions and policy troubleshooting](audit-recommend-and-troubleshoot.md) - OpenTelemetry events and the Analytics API for plugin usage, the suggestion allowlist key, and checks when plugin policy misbehaves.
* [Require and pre-install plugins by managed settings](require-and-preinstall-plugins.md) - Managed settings register marketplaces and force-enable plugins on every machine, or per repository, with delivery by server, MDM or file. **[high]**
* [Plugin policy keys and marketplace allowlist/blocklist](restrict-marketplace-sources.md) - Control matrix of managed plugin policy keys plus the strictKnownMarketplaces allowlist and blockedMarketplaces blocklist source objects and matching rules. **[high]**
* [Plugin seed directories for containers and CI](seed-containers-and-ci.md) - Pre-populate a plugins directory at build time and point CLAUDE_CODE_PLUGIN_SEED_DIR at it so runtime needs no cloning. **[high]**
* [Plugin update policy and release channels](update-policy-and-channels.md) - Set marketplace auto-update per marketplace or fleet-wide and give user groups stable or early-access marketplaces.
