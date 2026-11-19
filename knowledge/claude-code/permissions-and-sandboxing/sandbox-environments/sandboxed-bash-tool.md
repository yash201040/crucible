---
type: "Feature"
title: "Sandboxed Bash tool scope"
description: "The built-in per-command sandbox restricts Bash, PowerShell and Monitor commands only; MCP servers, hooks and monitors run unconstrained."
resource: "https://code.claude.com/docs/en/sandbox-environments"
tags: [sandboxing, bash, scope, mcp, hooks]
kind: "slash_command"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: "macOS, Linux or WSL2 (no native Windows)"
identifiers:
  - "/sandbox"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sandbox-environments"
    resource: "https://code.claude.com/docs/en/sandbox-environments"
    title: "Choose a sandbox environment"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The sandboxed Bash tool is built into Claude Code and uses operating system primitives to restrict filesystem and network access of Bash, PowerShell and Monitor tool commands. Run `/sandbox` to open the panel and choose a mode.

# Limits and defaults

- Native Windows is not supported; use WSL2 or a container or VM.
- Other built-in tools (Read, Edit, WebFetch) run inside the Claude Code process and spawn no arbitrary code; permission rules for path or domain gate them instead.
- MCP servers, command hooks and plugin monitors are separate processes that run unconstrained on the host.
- To put built-in tools, MCP servers and hooks behind one OS boundary run the whole process inside the sandbox runtime, the dev container or a custom container.
