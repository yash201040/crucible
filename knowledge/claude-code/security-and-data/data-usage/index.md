# security-and-data/data-usage

* [Local and cloud data flow and encryption at rest](data-flow-and-encryption.md) - How data moves for local, cloud and Remote Control sessions, and encryption at rest per model provider.
* [Feedback commands and session quality surveys](feedback-and-surveys.md) - What /feedback and the session survey send, how to disable them, and the related environment variables and settings.
* [Telemetry, error reporting and defaults by API provider](telemetry-defaults-by-provider.md) - What metrics and error reports Claude Code sends, opt-out variables, and the default on/off table per provider. **[high]**
* [Data training and retention policies](training-and-retention-policy.md) - Training policy by plan, Development Partner Program, retention periods, local transcript caching and cleanupPeriodDays.
* [WebFetch domain safety check](webfetch-domain-safety-check.md) - WebFetch sends the requested hostname to api.anthropic.com for a blocklist check regardless of provider; opt out with skipWebFetchPreflight.
