---
type: "Reference"
title: "Safety event (no longer sent)"
description: "claude_code.safety_event categories and attributes; sent only by v2.1.307 through v2.1.311 and stopped from v2.1.312."
resource: "https://code.claude.com/docs/en/monitoring-usage"
tags: [events, safety, sandbox, deprecated]
kind: "mixed"
maturity: "deprecated"
since: "2.1.312"
surfaces: [cli]
requires: ""
identifiers:
  - "claude_code.safety_event"
  - "category"
  - "decision_source"
  - "reason_code"
  - "reason_type"
  - "rule_source"
  - "grant_scope"
  - "circuit_breaker"
  - "hook_event"
  - "tool_class"
  - "sandbox_violation_count"
  - "sandbox_enabled"
  - "--permission-prompts none"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "monitoring-usage"
    resource: "https://code.claude.com/docs/en/monitoring-usage"
    title: "Monitoring"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude Code has stopped sending `claude_code.safety_event`. v2.1.312 and later never send it and no setting turns it on. In v2.1.307 through v2.1.311 a session stops sending it at its next feature-flag refresh; sessions that do not fetch feature flags (Amazon Bedrock, Google Cloud's Agent Platform, Microsoft Foundry) can keep sending it. To see refused tool calls now, query `tool_decision`.

# How to use it

It recorded: a check refusing a tool call or requiring a prompt, the sandbox network proxy refusing a connection, or a hook blocking a result or turn end. Attributes: `category`, `decision` (`accept`, `reject`, `sent_back`), `decision_source`, `reason_code` (e.g. `rule:policySettings`, `mode:dontAsk`, `hook:PreToolUse`, `classifier:auto-mode`, `bashMiss:too-complex`, `unknown`), `reason_type`, `rule_source` (`policySettings`, `userSettings`, `projectSettings`, `localSettings`, `flagSettings`, `cliArg`, `session`), `grant_scope` (`once`, `session`), `circuit_breaker` (`dangerousRemoval`, `outsideReadsBlocked`, `claudeSettingsFile`), `classifier_category`, `hook_event`, `tool_class` (`bash`, `powershell`, `file`, `web`, `mcp`, `other`), `tool_name`, `tool_source`, `permission_mode`, `tool_use_id`, `sandbox_violation_count` ("0" to "20"), `sandbox_enabled`.

Categories: `permission_rule`, `managed_policy`, `permission_mode` (dontAsk or plan, or a no-category prompt where prompts cannot show, as with `--permission-prompts none`), `hook`, `auto_mode_block`, `auto_mode_no_verdict`, `safety_check`, `static_analysis`, `sandbox_override`, `user_rejected`, `sandbox_network`, `sandbox_other`, `hook_review`, `other`.

# Notes

Calls refused because nobody could answer a no-category prompt show as `tool_decision` reject with `source` config and no safety event with the same `tool_use_id`; that happens in a `-p` run with neither `--permission-prompt-tool` nor `--permission-prompts none`. Calls approved at a no-category prompt, approved by `canUseTool`/`--permission-prompt-tool` at a hook-only prompt, and `AskUserQuestion` or `ExitPlanMode` calls also have no safety event; check `tool_decision`.
