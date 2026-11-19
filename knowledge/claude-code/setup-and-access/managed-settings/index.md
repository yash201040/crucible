# setup-and-access/managed-settings

* [How managed sources are combined](combining-managed-sources.md) - Source ranking, managedSourcesBehavior first-wins vs merge, cross-source keys, login keys, policyHelper and parent settings. **[high]**
* [Deploying managed settings and delivery mechanisms](deploy-settings-file-and-mechanisms.md) - Quick file deployment, the four delivery mechanisms, storage locations, managed-settings.d drop-ins and which surfaces read policy. **[high]**
* [Keys only a managed source can set](managed-only-keys.md) - Managed-only settings for permission, plugin, MCP, sandbox and delivery controls, with version requirements. **[high]**
* [Turning telemetry off for an organization](org-telemetry-off.md) - Deliver DISABLE_TELEMETRY through managed env to stop Anthropic operational telemetry, with side effects on analytics and feature flags.
* [Verifying policy and handling invalid managed entries](verify-and-invalid-entries.md) - Reading /status and claude doctor, parse failures that stop startup, fail-closed keys and sandbox field handling. **[high]**
