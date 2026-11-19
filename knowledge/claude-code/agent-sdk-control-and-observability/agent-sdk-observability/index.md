# agent-sdk-control-and-observability/agent-sdk-observability

* [Agent trace spans (beta)](agent-trace-spans.md) - Span names for interaction, LLM request, tool and hook, their nesting including subagents, and the session.id attribute. **[high]**
* [Enable telemetry export and flush timing](enable-export-and-flush.md) - Turn on CLAUDE_CODE_ENABLE_TELEMETRY with an OTLP exporter, avoid console, surface export errors, and shorten export intervals. **[high]**
* [Trace context propagation into the CLI](link-traces-to-your-app.md) - The SDK injects TRACEPARENT and TRACESTATE so agent spans nest under your application's active span. **[high]**
* [Opt-in variables for sensitive telemetry content](sensitive-data-controls.md) - OTEL_LOG variables that add prompts, tool details, tool output and raw API bodies to exports, with truncation limits and version gates.
* [Tag telemetry and attribute actions to end users](tag-and-attribute-telemetry.md) - Override service.name and add resource attributes per call, including percent-encoded end-user and tenant IDs for audit trails. **[high]**
* [How SDK telemetry flows and its signals](telemetry-architecture-and-signals.md) - The SDK emits no telemetry itself; the bundled CLI exports metrics, log events and beta traces over OTLP using env var configuration. **[high]**
