# create-plugins/plugins-measure

* [Analytics API plugins endpoint](analytics-api-plugins-endpoint.md) - GET /v1/organizations/analytics/plugins returns per-plugin per-day install and invocation counts for Enterprise organizations, without an exporter.
* [Check whether a plugin is used](check-whether-plugin-is-used.md) - Usage is recorded per machine; users can see it in /plugin, /skill-doctor, /doctor and /usage, and admins via telemetry.
* [Measure plugin cost with plugin details](measure-plugin-token-cost.md) - claude plugin details prints the component inventory and projected always-on and on-invoke token cost of a loaded plugin. **[high]**
* [OpenTelemetry events for plugins](opentelemetry-plugin-events.md) - Events and attributes that answer plugin install, load, skill activation, hook and cost questions, and how names are redacted. **[high]**
