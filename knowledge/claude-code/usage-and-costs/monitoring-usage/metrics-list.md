---
type: "Reference"
title: "Exported metrics"
description: "The eight claude_code.* metrics with units, plus session, lines-of-code, PR, commit, decision and active-time counter details."
resource: "https://code.claude.com/docs/en/monitoring-usage"
tags: [metrics, counters, usage, telemetry]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "claude_code.session.count"
  - "claude_code.lines_of_code.count"
  - "claude_code.pull_request.count"
  - "claude_code.commit.count"
  - "claude_code.cost.usage"
  - "claude_code.token.usage"
  - "claude_code.code_edit_tool.decision"
  - "claude_code.active_time.total"
  - "com.anthropic.claude_code"
  - "start_type"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "monitoring-usage"
    resource: "https://code.claude.com/docs/en/monitoring-usage"
    title: "Monitoring"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Metrics exported when `OTEL_METRICS_EXPORTER` is set. Every metric carries the standard attributes. Count metrics have no unit.

# How to use it

| Metric | Unit | Notes / extra attributes |
| - | - | - |
| `claude_code.session.count` | none | Incremented at each session start. `start_type`: `"fresh"`, `"resume"`, `"continue"`, `"agents_view"` (the `claude agents` dashboard process, a user-launched UI, not a conversational session) |
| `claude_code.lines_of_code.count` | none | `type` (`added`,`removed`), `model` |
| `claude_code.pull_request.count` | none | PRs or merge requests created via shell command or MCP tool |
| `claude_code.commit.count` | none | Git commits created |
| `claude_code.cost.usage` | USD | See [cost and token counters](./cost-and-token-counters.md) |
| `claude_code.token.usage` | tokens | See [cost and token counters](./cost-and-token-counters.md) |
| `claude_code.code_edit_tool.decision` | none | `tool_name` (`Edit`,`Write`,`NotebookEdit`), `decision` (`accept`,`reject`), `source` (`config`,`hook`,`user_permanent`,`user_temporary`,`user_abort`,`user_reject`), `language` (e.g. `TypeScript`; `unknown` for unrecognized extensions) |
| `claude_code.active_time.total` | s | Active time excluding idle; `type` is `user` (keyboard) or `cli` (tool execution and AI responses) |

# Limits and defaults

When `prometheus` is the only exporter, Claude Code omits the `USD`, `tokens` and `s` units so the scrape is valid Prometheus text; names do not change. Combined exporters such as `otlp,prometheus` keep units. Meter name: `com.anthropic.claude_code`.
