---
type: "Reference"
title: "Cost and token counter attributes"
description: "Attributes on claude_code.cost.usage and claude_code.token.usage: model, query_source, effort, agent, skill, plugin and MCP attribution with redaction rules."
resource: "https://code.claude.com/docs/en/monitoring-usage"
tags: [cost, tokens, attribution, subagents]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "claude_code.cost.usage"
  - "claude_code.token.usage"
  - "query_source"
  - "speed"
  - "effort"
  - "agent.name"
  - "skill.name"
  - "plugin.name"
  - "marketplace.name"
  - "mcp_server.name"
  - "mcp_tool.name"
  - "cacheRead"
  - "cacheCreation"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "monitoring-usage"
    resource: "https://code.claude.com/docs/en/monitoring-usage"
    title: "Monitoring"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Both counters are incremented after each API request. Use them to attribute spend and tokens to models, subagent types, skills and plugins.

# How to use it

| Attribute | Values and redaction |
| - | - |
| `type` (token counter only) | `input` (excludes cache reads/writes), `output`, `cacheRead`, `cacheCreation` (five-minute and one-hour lifetimes together) |
| `model` | model identifier, e.g. `claude-sonnet-5` |
| `query_source` | `main`, `subagent`, `auxiliary`, `plugin_model_complete`, `plugin_model_classify` (the last two are requests a mod makes with `$.model.complete` / `$.model.classify`; counted from v2.1.324, so totals can step up) |
| `speed` | `fast` when fast mode used; absent otherwise |
| `effort` | `low`,`medium`,`high`,`xhigh`,`max`; absent if no effort level is sent |
| `agent.name` | subagent type; built-in and official-marketplace plugin agents verbatim; other user-defined names become `custom` |
| `skill.name` | built-in, bundled, user-defined and official-plugin skills verbatim; third-party plugin skills become `third-party` |
| `plugin.name` | owning plugin; official verbatim, third-party becomes `third-party` |
| `marketplace.name` | only for official-marketplace plugins, even with `OTEL_LOG_TOOL_DETAILS=1` |
| `mcp_server.name`, `mcp_tool.name` | MCP server/tool whose result the request consumed; built-in, claude.ai-proxied and official-registry names verbatim, user-configured become `custom`; from v2.1.312 a plugin-declared fixed-URL remote server shows as `plugin_<plugin>_<server>` (becomes `custom` if the marketplace copy did not come from Anthropic's registered source) |

`OTEL_LOG_TOOL_DETAILS=1` makes the name attributes carry real names. Before v2.1.273 the counters and the `api_request`, `api_error`, `api_refusal` events kept redacted values even with it set. Before v2.1.222, `mcp_server.name` was set on every request after an MCP call, not only requests consuming a tool result, so dashboards show a step down after upgrading.

# Notes

Cost metrics are approximations; official billing data is on the costs page. Each streaming response is counted once, even when a gateway behind `ANTHROPIC_BASE_URL` streams usage across several frames.
