# gateways/llm-gateway

* [Pin a managed machine to one gateway with allowedProviders](allowed-providers-pin.md) - Set allowedProviders to [customEndpoint] plus a pinned ANTHROPIC_BASE_URL in managed settings so Claude Code refuses any other destination. **[high]**
* [Gateway credential variables versus claude.ai login](gateway-subscription-interaction.md) - An active gateway credential variable or apiKeyHelper replaces the subscription login; ANTHROPIC_BASE_URL alone keeps it and needs Authorization and OAuth beta forwarded.
* [Other LLM gateways: what a gateway provides and rollout sequence](other-gateways-overview.md) - Value of a gateway (credentials, usage, budgets, audit, provider switching) and the four-step rollout for a gateway product the organization already runs. **[high]**
