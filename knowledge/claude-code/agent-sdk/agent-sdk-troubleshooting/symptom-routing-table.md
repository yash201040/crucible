---
type: "Reference"
title: "SDK symptom to page routing"
description: "Maps Agent SDK symptoms and error strings to the troubleshooting section that covers them."
resource: "https://code.claude.com/docs/en/agent-sdk/troubleshooting"
tags: [troubleshooting, errors, routing, agent-sdk]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "Invalid skill name"
  - "No file checkpoint found"
  - "File rewinding is not enabled"
  - "ProcessTransport is not ready for writing"
  - "CLINotFoundError"
  - "CLIConnectionError"
  - "ProcessError"
  - "CLIJSONDecodeError"
  - "Operation aborted"
  - "Claude Code process aborted by user"
  - "Prompt stream failed; closing stdin"
  - "Image could not be processed"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-troubleshooting"
    resource: "https://code.claude.com/docs/en/agent-sdk/troubleshooting"
    title: "Troubleshoot the Agent SDK"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

This page covers errors in CLI startup, CLI process exit, large tool messages, streaming input and structured outputs. Feature-specific symptoms live on the feature pages.

# How to use it

| Symptom | Go to |
| - | - |
| Skills not found, `Invalid skill name` | skills page, Troubleshooting |
| MCP server `failed`, tools not called, timeouts, tool output over the max tokens | mcp page, Troubleshooting |
| Plugin not loading | plugins page, Troubleshooting |
| Not delegating to subagents, filesystem agents not loading | subagents page, Troubleshooting |
| Checkpointing options not recognized, missing UUIDs, `No file checkpoint found`, `File rewinding is not enabled`, `ProcessTransport is not ready for writing` | file checkpointing, Troubleshooting |
| Hook not firing, matcher, timeout, blocked tool, modified input not applied, session hooks in Python, permission prompts multiplying, recursive hook loops, `systemMessage` missing | hooks page, Fix common issues |
| Works locally, fails in deployed service or container | hosting, Troubleshoot deployment failures |
| `Not logged in`, `Invalid API key`, `API Error`, `429`, `There's an issue with the selected model` | Error reference |
| `CLINotFoundError`, `CLIConnectionError`, `ProcessError`, `Claude Code process exited with code N`, `Claude Code returned an error result`, `CLIJSONDecodeError`, `structured_output` is `None` | sections of this page |
| `Operation aborted`, `Claude Code process aborted by user`, `Prompt stream failed; closing stdin`, Python `query()` loop that stops silently | Streaming input section |
| `Image could not be processed` | its section on this page |

# Notes

Report uncovered issues at the claude-agent-sdk-typescript or claude-agent-sdk-python GitHub repos, with full error text and SDK version.
