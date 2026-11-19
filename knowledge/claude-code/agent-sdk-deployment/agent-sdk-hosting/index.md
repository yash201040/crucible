# agent-sdk-deployment/agent-sdk-hosting

* [SDK hosting known limitations and deployment failures](known-limitations-and-troubleshooting.md) - No session timeout, memory growth, subagent fanout rate limits, no per-subagent deadline, and common CLI-not-found or launch failures. **[high]**
* [Multi-tenant isolation in a shared SDK container](multi-tenant-isolation.md) - Use settingSources empty, CLAUDE_CODE_DISABLE_AUTO_MEMORY, per-tenant CLAUDE_CONFIG_DIR and cwd, and per-tenant egress rules to keep tenants apart. **[high]**
* [Provisioning, scaling, auth and observability for hosted agents](provisioning-scaling-observability.md) - Runtime dependencies, resource baseline, scaling formula, cost, OpenTelemetry environment variables and auth/secrets guidance. **[high]**
* [Agent SDK session patterns: ephemeral, long-running, hybrid, multi-agent](session-patterns.md) - Four container lifecycle patterns with the SDK calls each uses, including streamInput, startup, prewarm, ClaudeSDKClient and resume with a SessionStore. **[high]**
* [Agent SDK subprocess model and local state](subprocess-model-and-state.md) - The SDK spawns one claude CLI subprocess per session over stdio; transcripts, memory files and working-directory artifacts live on local disk and do not survive restarts. **[high]**
