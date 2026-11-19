# gateways/claude-apps-gateway-config

* [Gateway admin, enforcement and pricing settings](admin-enforcement-pricing.md) - gateway.yaml keys that enable the spend-limit Admin API, fail-open or fail-closed enforcement, pooled budgets and contracted-rate pricing. **[high]**
* [gateway.yaml structure, secrets and listener](gateway-yaml-structure-listen.md) - Layout of gateway.yaml: five required sections, optional sections, secret expansion forms and the listen block.
* [Gateway managed policies by IdP group](managed-policies.md) - The managed block serves per-user Claude Code settings and a Claude Desktop overlay, chosen by IdP group or email domain. **[high]**
* [Gateway oidc, session and store settings](oidc-session-store.md) - Identity provider sign-in options, certificate client auth, proxy egress, gateway bearer-token session and Postgres store settings.
* [Gateway telemetry relay, HTTP tuning, load test mode](telemetry-http-tuning-loadtest.md) - OTLP forwarding with per-signal opt-in, access control and rate limits, request limits, and load_test_mode for unmetered load tests. **[high]**
* [Gateway upstreams, failover and per-team routing](upstreams-routing-failover.md) - How the gateway forwards inference to Anthropic, Bedrock, Mantle, AWS, Google Cloud or Foundry upstreams, fails over, and routes by group. **[high]**
