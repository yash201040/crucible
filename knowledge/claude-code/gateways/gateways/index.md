# gateways/gateways

* [Claude apps gateway (Anthropic's self-hosted gateway)](claude-apps-gateway-overview.md) - A gateway built into the claude binary with IdP sign-in, per-group model and managed-settings control, and OTLP usage metrics; no service-token flow for CI. **[high]**
* [How a gateway sits between Claude Code and the provider](gateway-architecture.md) - A gateway is an organization-run proxy that holds the provider credential, so developers authenticate to it and usage, budgets and audit live in one place. **[high]**
* [What a gateway does not control](gateway-separate-configuration.md) - Model choice, non-gateway network traffic, client telemetry, corporate proxies and telemetry destinations are configured outside the gateway.
* [Gateway credentials versus claude.ai subscriptions](gateway-subscriptions-billing.md) - Gateway credential traffic bills at API rates to the provider account; setting only ANTHROPIC_BASE_URL keeps the claude.ai login and its limits.
* [Using a gateway product you already run](other-gateways-pointer.md) - Any existing LLM or API gateway can be used; Anthropic does not endorse, maintain or audit them and does not support routing to non-Claude models.
