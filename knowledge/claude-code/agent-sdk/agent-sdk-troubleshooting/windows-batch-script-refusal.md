---
type: "Limit"
title: "Refusal to run .bat or .cmd CLI on Windows"
description: "The Python SDK refuses a batch-script CLI path on Windows for security; use a native claude.exe."
resource: "https://code.claude.com/docs/en/agent-sdk/troubleshooting"
tags: [windows, security, cli-path, python]
kind: "behavior"
maturity: "unlabelled"
since: "0.2.124"
surfaces: [sdk]
requires: "Windows, Python SDK"
identifiers:
  - "CLIConnectionError"
  - "Refusing to execute batch script"
  - "cli_path"
  - "claude.cmd"
  - "irm https://claude.ai/install.ps1 | iex"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-troubleshooting"
    resource: "https://code.claude.com/docs/en/agent-sdk/troubleshooting"
    title: "Troubleshoot the Agent SDK"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

On Windows, a `CLIConnectionError` "Refusing to execute batch script ..." occurs when the CLI path the Python SDK uses is a `.bat` or `.cmd` file, including npm's `claude.cmd` shim. This is deliberate hardening: `cmd.exe` re-parses the command line, so an argument could execute injected commands.

# How to use it

The Windows x64 wheel of `claude-agent-sdk` bundles `claude.exe`; the SDK prefers the bundled CLI, then any native `claude.exe`, before a batch shim. The refusal appears when `cli_path` is set to a batch file, or when no bundled or native `claude.exe` exists (for example a source install on ARM64 Windows). Fixes: point `cli_path` at a `claude.exe` or remove it (the SDK skips discovery while `cli_path` is set); install natively with `irm https://claude.ai/install.ps1 | iex`; or install the x64 wheel.

# Notes

Before `claude-agent-sdk` 0.2.124 the Python SDK spawned batch scripts through `cmd.exe` without this check.
