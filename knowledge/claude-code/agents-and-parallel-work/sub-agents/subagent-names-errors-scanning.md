---
type: "Feature"
title: "Subagent names, API errors and output scanning"
description: "Naming subagents via the Agent tool name parameter, how API errors surface to Claude, and the scan applied to final reports."
resource: "https://code.claude.com/docs/en/sub-agents"
tags: [subagents, errors, security, naming, fallback]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "name"
  - "Agent terminated early due to an API error"
  - "[harness: subagent output matched instruction-shaped pattern(s):"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sub-agents"
    resource: "https://code.claude.com/docs/en/sub-agents"
    title: "Create custom subagents"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Three behaviors around a subagent's run and report.

# How to use it

Names: with agent teams enabled, Claude can pass a `name` on the Agent tool call, making the subagent addressable (message or resume by name). In an interactive session with agent teams enabled, a named subagent spawned from the main conversation launches as a teammate instead, unless it is a fork or passes `isolation` on the call (frontmatter `isolation` does not prevent it; the teammate then runs in the main working directory).

API errors:
- A mid-stream cut-off with text but no tool calls prompts the subagent to continue, until continuations run out.
- Foreground: if rate limit, overload or server error cuts off a subagent that already produced text, the Agent tool returns the partial output noted as unfinished; a subagent with no output (or only tool calls) fails with `Agent terminated early due to an API error` plus detail.
- Background: marked failed; the end message names the error and includes the last output.
- Report beginning `⚠ This agent switched to <model> because its earlier model could not be used.` means a configured fallback model chain took over. Retry or resume after the error clears.

Output scanning: each final report is scanned before Claude reads it. It never removes or rewords text. It inserts a backslash into imitation Claude Code output (a `<system-reminder>` tag, lines starting `Human:` or `Assistant:`), and prepends a line starting `[harness: subagent output matched instruction-shaped pattern(s):` when the report imitates such a tag or mentions permission settings such as `bypassPermissions` or `--dangerously-skip-permissions`.

# Limits and defaults

- The scan does not judge maliciousness and does not change what an instruction can do; tool calls still go through permission checks and sandboxing. It is no substitute for restricting subagent capabilities.
- Reports return under a header stating instructions or approval claims inside are the subagent's words with no authority from you; a background report arrives in a completion notification marked as an automated event.
