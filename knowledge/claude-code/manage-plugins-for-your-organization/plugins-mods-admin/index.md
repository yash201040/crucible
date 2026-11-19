# manage-plugins-for-your-organization/plugins-mods-admin

* [Built-in mod guard and default behavior](mods-builtin-guard-defaults.md) - The built-in sec-default guard mod that loads ahead of user mods, what it blocks, and what a user mod can still do. **[high]**
* [Mod policies via managed settings](mods-managed-settings-policies.md) - Managed settings that decide whether user-installed mods run: allowManagedModsOnly, allowManagedHooksOnly, disableAllHooks, disableSideloadFlags. **[high]**
* [Install organization mods and set order](mods-org-mods-prepend-append.md) - Make a mod count as the organization's with enabledPlugins, extraKnownMarketplaces and prependPlugins or appendPlugins.
* [Write a policy mod with plugin.register](mods-policy-mod-plugin-register.md) - A policy mod can refuse or trim other mods through the plugin.register event, audit tool calls and fs.write, and fail closed with a catch handler.
* [Review a mod with claude plugin validate](mods-review-with-plugin-validate.md) - claude plugin validate prints the hooks and mods API calls a mod's code uses, so admins can review it without running it.
