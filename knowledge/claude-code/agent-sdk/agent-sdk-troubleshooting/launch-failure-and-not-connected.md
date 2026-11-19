---
type: "Reference"
title: "Failed to start Claude Code and Not connected"
description: "Launch-failure messages in Python and TypeScript, and the ClaudeSDKClient Not connected error."
resource: "https://code.claude.com/docs/en/agent-sdk/troubleshooting"
tags: [startup, launch-failure, client, connect]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "CLIConnectionError"
  - "Failed to start Claude Code: <detail>"
  - "Claude Code executable at <path> exists but failed to launch"
  - "Claude Code native binary at <path> exists but failed to launch"
  - "Failed to spawn Claude Code process: <detail>"
  - "Not connected. Call connect() first."
  - "ClaudeSDKClient"
  - "connect()"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-troubleshooting"
    resource: "https://code.claude.com/docs/en/agent-sdk/troubleshooting"
    title: "Troubleshoot the Agent SDK"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The SDK found a file at the resolved path but could not launch it. Python raises `CLIConnectionError`; TypeScript rejects message iteration with an error carrying no SDK class.

# How to use it

| Message | SDK | Meaning |
| - | - | - |
| `Failed to start Claude Code: <detail>` | Python | rest is the OS error |
| `Claude Code executable at <path> exists but failed to launch` | TypeScript | script at configured path cannot run |
| `Claude Code native binary at <path> exists but failed to launch` | TypeScript | binary cannot run; libc suggestion appended |
| `Failed to spawn Claude Code process: <detail>` | TypeScript | other launch failure |

Usual cause: the path points at a text file, directory or non-executable file. Fixes: point at the real `claude` executable with execute permission; remove `cli_path` / `pathToClaudeCodeExecutable` so the SDK uses its bundled copy; for a bundled binary in a container image, reinstall the SDK during the build or rebuild for the image architecture (mismatch of architecture, libc, or lost execute permission).

Python `ClaudeSDKClient` method calls before connecting or after disconnecting raise `CLIConnectionError` "Not connected. Call connect() first." Call `await client.connect()` or use `async with ClaudeSDKClient() as client:`.
