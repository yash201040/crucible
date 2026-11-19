# gateways/llm-gateway-connect

* [Route to a cloud provider through a gateway](cloud-provider-routes.md) - Provider-specific base URL and skip-auth variables for Bedrock, Agent Platform, Foundry and Claude Platform on AWS gateways.
* [Set the gateway base URL and credential](credential-and-base-url.md) - Point Claude Code at a gateway with ANTHROPIC_BASE_URL plus ANTHROPIC_AUTH_TOKEN, ANTHROPIC_API_KEY or apiKeyHelper, verify with curl and /status. **[high]**
* [Additional gateway variables: headers, discovery, helper, quiet mode](extra-gateway-settings.md) - Custom headers, gateway model discovery, apiKeyHelper caching and the switch that turns off traffic outside the gateway path. **[high]**
* [Gateway error troubleshooting table](gateway-troubleshooting.md) - Common errors behind a gateway (401, 400 beta fields, adaptive thinking, context limits, fast mode, WAF 403, TLS) with cause and fix. **[high]**
* [Gateway configuration per surface](surface-configuration.md) - How gateway variables reach VS Code, Desktop, GitHub Actions, the Agent SDK, Slack and cloud sessions, Remote Control and voice dictation. **[high]**
