---
type: "Limit"
title: "Python max_buffer_size JSON decode error"
description: "CLIJSONDecodeError when one CLI message exceeds max_buffer_size (default 1,048,576), and how to recover the work."
resource: "https://code.claude.com/docs/en/agent-sdk/troubleshooting"
tags: [buffer, limits, python, pdf, recovery]
kind: "limit"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: "Python SDK"
identifiers:
  - "CLIJSONDecodeError"
  - "max_buffer_size"
  - "continue_conversation"
  - "resume"
  - "disconnect()"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-troubleshooting"
    resource: "https://code.claude.com/docs/en/agent-sdk/troubleshooting"
    title: "Troubleshoot the Agent SDK"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The Python SDK raises `CLIJSONDecodeError` ("Failed to decode JSON: JSON message exceeded maximum buffer size of 1048576 bytes...") when one message from Claude Code is longer than `max_buffer_size`, default 1,048,576 characters (the error calls them bytes).

# Limits and defaults

- Whole PDFs of about 393 KB or more read with Read can reach it, since the tool result holds base64 twice; screenshot results (Read or MCP) also hold base64 twice.
- Edit and Write messages can reach it on a file well under 1 MB.
- Fix: `ClaudeAgentOptions(max_buffer_size=64 * 1024 * 1024)`, enough for a screenshot and a whole-PDF Read up to Read's 20 MB limit; raise further if it returns.

# How to use it

Changes a tool already made stay in place. To pick up: (1) call `disconnect()` on any open `ClaudeSDKClient` (no more messages arrive but Claude Code keeps running and may still change files); (2) start a new `query()` or `ClaudeSDKClient` with the larger limit and `continue_conversation=True` (most recent session in the cwd), or `resume` set to `data["session_id"]` from the init `SystemMessage`.
