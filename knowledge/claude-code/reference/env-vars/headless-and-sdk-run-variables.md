---
type: "Reference"
title: "Headless and SDK run-control variables"
description: "Variables for non-interactive runs: turn caps, exit delay, session state events, startup failure results, structured output retries and cloud bundling."
resource: "https://code.claude.com/docs/en/env-vars"
tags: [headless, sdk, print-mode, automation]
kind: "env_var"
maturity: "unlabelled"
since: ""
surfaces: [headless, sdk]
requires: ""
identifiers:
  - "CLAUDE_CODE_MAX_TURNS"
  - "CLAUDE_CODE_EXIT_AFTER_STOP_DELAY"
  - "CLAUDE_CODE_EMIT_SESSION_STATE_EVENTS"
  - "CLAUDE_CODE_STARTUP_FAILURE_RESULTS"
  - "MAX_STRUCTURED_OUTPUT_RETRIES"
  - "CLAUDE_AGENT_SDK_MCP_NO_PREFIX"
  - "CLAUDE_CODE_USER_DIALOG_TIMEOUT_MS"
  - "CCR_FORCE_BUNDLE"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "env-vars"
    resource: "https://code.claude.com/docs/en/env-vars"
    title: "Environment variables"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Controls that matter for `claude -p`, the Agent SDK and other unattended runs.

# How to use it

| Variable | What it does |
| :- | :- |
| `CLAUDE_CODE_MAX_TURNS` | Caps agentic turns when no explicit limit is passed; same as `--max-turns`, which wins. A non-positive-integer value is rejected at startup with an error. |
| `CLAUDE_CODE_EXIT_AFTER_STOP_DELAY` | Ms to wait after the query loop goes idle before exiting automatically; for scripts and SDK mode. |
| `CLAUDE_CODE_EMIT_SESSION_STATE_EVENTS` | `1` adds `session_state_changed` messages to the stream. Needs the Agent SDK, or `--print` with `--output-format stream-json` and `--verbose`. |
| `CLAUDE_CODE_STARTUP_FAILURE_RESULTS` | `1` makes a `--output-format stream-json` session write a result message naming why startup was refused, for failures that otherwise end with stderr only. Requires v2.1.274+. |
| `MAX_STRUCTURED_OUTPUT_RETRIES` | Attempts allowed when the response fails validation against `--json-schema` in `-p` mode (default 5: first attempt plus four retries); then the run fails. Same cap for a workflow subagent's structured output. |
| `CLAUDE_AGENT_SDK_MCP_NO_PREFIX` | `1` skips the `mcp__<server>__` prefix on tool names from SDK-created MCP servers. SDK only. |
| `CLAUDE_CODE_USER_DIALOG_TIMEOUT_MS` | Deadline before Claude Code cancels a dialog forwarded to a remote client (Remote Control or SDK host) or an approval dialog for a held cross-session message; permission prompts and `AskUserQuestion` have their own flows. From v2.1.236 also bounds the mid-session Fable usage-credits consent prompt in possibly unattended sessions. Beats the `dialogExpiry` setting; `0` or negative disables; ignored in project and local settings. |
| `CCR_FORCE_BUNDLE` | `1` forces `claude --cloud` to bundle and upload the local repository instead of cloning from its remote. |
