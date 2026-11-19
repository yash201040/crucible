# gateways/llm-gateway-protocol

* [Gateway API formats, endpoints and streaming rules](api-formats-and-streaming.md) - The three API formats a gateway can expose, their endpoints and forward-unchanged fields, optional endpoints, and streaming requirements. **[high]**
* [Client behavior by connection method](client-behavior-by-connection.md) - How model IDs, anthropic-beta values, request fields, cache TTL and background-task model differ across Bedrock/Agent Platform, Anthropic Messages and Claude apps gateway. **[high]**
* [Feature pass-through, automatic retries and disabling betas](feature-pass-through-and-retries.md) - Beta header and body field pairs that break behind a gateway, Claude Code's own retry recovery per capability, and CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS scope. **[high]**
* [Gateway model discovery via /v1/models](gateway-model-discovery.md) - Opt-in startup query of GET /v1/models that adds claude- or anthropic-named gateway models to the /model picker, with a 3 second default timeout.
* [Request headers and gateway hint headers](request-and-hint-headers.md) - Headers Claude Code sends to a gateway, including session, agent and parent-agent IDs and the opt-in x-claude-code-* routing hint headers. **[high]**
* [Response headers and system prompt attribution block](response-headers-and-attribution.md) - Response headers a gateway must return for retries and limits, and how the attribution block interacts with prompt caching and CLAUDE_CODE_ATTRIBUTION_HEADER. **[high]**
