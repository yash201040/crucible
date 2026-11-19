# agent-sdk-deployment/agent-sdk-secure-deployment

* [Credential management with the proxy pattern](credential-proxy-pattern.md) - Run a proxy outside the agent boundary to inject credentials, via ANTHROPIC_BASE_URL or HTTP_PROXY/HTTPS_PROXY, custom tools, or TLS-terminating traffic forwarding. **[high]**
* [Filesystem configuration for agent containers](filesystem-configuration.md) - Mount code read-only, sanitize credential files, and use tmpfs, overlay or dedicated volumes for writes.
* [Isolation technologies and hardened Docker flags](isolation-technologies.md) - Comparison of sandbox runtime, Docker, gVisor and VMs, with the hardened docker run options and the Unix socket proxy architecture. **[high]**
* [Agent deployment threat model and security principles](threat-model-and-principles.md) - Prompt injection and model error as the threat, built-in features, and the boundary, least-privilege and defense-in-depth principles.
