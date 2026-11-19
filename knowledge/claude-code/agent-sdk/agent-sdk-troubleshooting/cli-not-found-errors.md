---
type: "Reference"
title: "CLINotFoundError and missing native binary"
description: "Errors when the SDK cannot find the Claude Code executable in Python or TypeScript, with fixes."
resource: "https://code.claude.com/docs/en/agent-sdk/troubleshooting"
tags: [cli-not-found, startup, binary, cli-path]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "CLINotFoundError"
  - "cli_path"
  - "pathToClaudeCodeExecutable"
  - "Claude Code not found at:"
  - "Native CLI binary for <platform>-<arch> not found"
  - "Claude Code native binary not found at <path>"
  - "Claude Code executable not found at <path>. Is options.pathToClaudeCodeExecutable set?"
  - "claude --version"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-troubleshooting"
    resource: "https://code.claude.com/docs/en/agent-sdk/troubleshooting"
    title: "Troubleshoot the Agent SDK"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The Python SDK launches the Claude Code CLI as a subprocess; with no `claude` executable it raises `CLINotFoundError` ("Claude Code not found at: <path>"). The message includes the path when `ClaudeAgentOptions(cli_path=...)` points at a missing file; otherwise the SDK searches `PATH` and common install locations.

# How to use it

Python: install Claude Code; confirm `cli_path` exists and is the executable; confirm `claude --version` works in the same environment the app runs in (IDEs and service managers often have a different `PATH`).

TypeScript looks in its bundled platform package and in `pathToClaudeCodeExecutable`:
- `Native CLI binary for <platform>-<arch> not found`: the bundled platform package is missing, usually because optional dependencies were skipped. Reinstall, or point `pathToClaudeCodeExecutable` at a native install. In a `bun build --compile` single-file executable the cause and fix differ (see the TypeScript reference, Compile to a single executable).
- `Claude Code native binary not found at <path>` or `Claude Code executable not found at <path>. Is options.pathToClaudeCodeExecutable set?`: the file at that path is missing or inaccessible.
