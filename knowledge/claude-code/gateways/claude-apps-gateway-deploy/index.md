# gateways/claude-apps-gateway-deploy

* [Gateway IdP registration and deployment](idp-setup-and-deployment.md) - Register an OIDC client, build the gateway container and run it on Kubernetes or Cloud Run behind an L7 proxy, then push the URL to clients.
* [Gateway operations: logs, health, outages, upgrades](operations-logs-health-upgrades.md) - Audit events, log formats, probes, upstream concurrency, drain on SIGTERM, outage behavior, JWT rotation and Postgres tables. **[high]**
* [Gateway security model and data flow](security-and-data-flow.md) - What data the gateway sends where, its threat model and SSRF guard, device-code brute-force limits and compliance answers.
* [Gateway troubleshooting symptoms and fixes](troubleshooting-errors.md) - Symptom, cause and fix table for gateway sign-in, boot, Postgres, TLS and streaming timeout failures, including long-thinking timeouts.
