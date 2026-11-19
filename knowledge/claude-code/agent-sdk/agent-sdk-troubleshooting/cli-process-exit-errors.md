---
type: "Reference"
title: "ProcessError, ResultError and process-exit errors"
description: "What Python and TypeScript raise when the Claude Code process exits nonzero or reports an error result."
resource: "https://code.claude.com/docs/en/agent-sdk/troubleshooting"
tags: [process-exit, errors, stderr, result-error]
kind: "mixed"
maturity: "unlabelled"
since: "0.2.140"
surfaces: [sdk]
requires: ""
identifiers:
  - "ProcessError"
  - "ResultError"
  - "exit_code"
  - "stderr"
  - "Claude Code process exited with code N"
  - "Claude Code process terminated by signal <name>"
  - "Claude Code returned an error result"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-troubleshooting"
    resource: "https://code.claude.com/docs/en/agent-sdk/troubleshooting"
    title: "Troubleshoot the Agent SDK"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Errors meaning the Claude Code process ended while your app used it. They differ by language and by whether the CLI reported an error result before exiting.

# How to use it

- Python `ProcessError`: nonzero exit without an error result. The text "Command failed with exit code 1 (exit code: 1) / Error output: Check stderr output for details" is fixed text, not real stderr; the `exit_code` attribute carries the code. Pass a `stderr` callback in `ClaudeAgentOptions` to capture the CLI's actual stderr.
- Python `ResultError` (subclass of `ProcessError`): raised when the CLI reported an error result; its `data` attribute holds the full error result. Put `except ResultError` before `except ProcessError` to handle them differently. Before `claude-agent-sdk` 0.2.140 these were a plain `Exception`.
- TypeScript: a nonzero exit rejects the `for await` loop with a plain `Error`: `Claude Code process exited with code 1. stderr: <tail>`. No SDK error class exists, so wrap the loop in try/catch and match the message. Pass a `stderr` callback in the query options for the full stream. A signal kill reports `Claude Code process terminated by signal <name>`.
- Both SDKs: when the CLI reported an error result first, the message is `Claude Code returned an error result: <CLI report>`; start with that text.
