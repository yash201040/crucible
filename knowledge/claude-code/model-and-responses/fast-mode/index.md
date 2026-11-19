# model-and-responses/fast-mode

* [Fast mode behind proxies and LLM gateways](fast-mode-behind-gateways.md) - Claude Code checks fast mode availability directly at api.anthropic.com; skip variables fix gateway and proxy failures.
* [Fast mode pricing and where spend shows](fast-mode-cost.md) - Per-MTok fast mode rates by model, the uncached-context charge when first enabled, and where to see the spend. **[high]**
* [Fast mode in cloud sessions](fast-mode-in-cloud-sessions.md) - Fast mode works in cloud sessions with /fast on for that session only, on Anthropic-managed or self-hosted runners.
* [Fast mode on Google Cloud Agent Platform](fast-mode-on-agent-platform.md) - Fable 5.2 fast mode on Agent Platform needs v2.1.322, a global/us/eu region, and launch flags in non-interactive mode.
* [Fast mode per-session opt-in and rate-limit fallback](fast-mode-organization-controls.md) - fastModePerSessionOptIn makes every session start with fast mode off; rate limits and exhausted credits fall back to standard speed. **[high]**
* [Fast mode overview](fast-mode-overview.md) - A faster configuration of supported models, up to 2.5x faster at higher per-token cost, toggled with /fast. **[high]**
* [Fast mode requirements and blockers](fast-mode-requirements.md) - Provider, billing, usage-credit, Owner-enablement and organization settings needed for fast mode, with the messages /fast shows. **[high]**
* [Toggle fast mode and switch models](toggle-fast-mode.md) - Turn fast mode on with /fast or the fastMode setting, how it persists, behaves in -p mode and follows model switches. **[high]**
