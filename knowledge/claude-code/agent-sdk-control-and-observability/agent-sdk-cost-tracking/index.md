# agent-sdk-control-and-observability/agent-sdk-cost-tracking

* [Accumulating cost across calls and sessions](accumulate-costs-across-calls.md) - Add totals of independent calls yourself; resumed sessions already include earlier spend, so read the latest result. **[high]**
* [Cost fields are client-side estimates](cost-fields-are-estimates.md) - total_cost_usd and costUSD are computed locally from a bundled price table and must not drive billing or financial decisions. **[high]**
* [Output tokens, failed runs and crash recovery](output-tokens-failures-and-crash-recovery.md) - Per-step output_tokens is a placeholder, error results still carry cost, and a crash may zero the final result. **[high]**
* [Per-step and per-model usage breakdown](per-step-and-per-model-usage.md) - Deduplicate assistant messages by ID for step input tokens, and read modelUsage for per-model cost with a costBasis field. **[high]**
* [Cache tokens and 1-hour prompt cache TTL](prompt-cache-tokens-and-ttl.md) - Cache creation and read token fields, and the env vars and settings that choose a 5-minute or 1-hour cache TTL. **[high]**
* [Cost totals in streaming input mode](streaming-input-cost-totals.md) - Which result fields are per-turn or running totals in streaming input, and how /clear, /reset and /new reset them. **[high]**
* [Result cost fields and subagent coverage](total-cost-and-subagent-fields.md) - total_cost_usd and modelUsage include subagent spend while usage excludes it; background subagents are awaited before the result. **[high]**
* [Usage scope: query, step, session](usage-scoping-query-step-session.md) - How token usage is scoped per query() call, per step with shared message IDs, and per resumed session. **[high]**
