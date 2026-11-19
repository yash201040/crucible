---
type: "Concept"
title: "What runs outside the sandbox"
description: "The tools, processes and commands that the Bash sandbox does not cover, including file tools, hooks, MCP servers, mods and excluded or retried commands."
resource: "https://code.claude.com/docs/en/sandboxing"
tags: [sandbox, scope, hooks, mcp]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "excludedCommands"
  - "dangerouslyDisableSandbox"
  - "apiKeyHelper"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "sandboxing"
    resource: "https://code.claude.com/docs/en/sandboxing"
    title: "Configure the sandboxed Bash tool"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The sandbox wraps shell commands only. These run outside it:

- Built-in file and web tools (Read, Edit, Write, WebFetch, WebSearch) follow permission rules instead. A `denyRead` entry does not stop the Read tool; `allowedDomains` does not limit WebFetch.
- Other processes Claude Code starts: command hooks, local MCP servers, plugin monitors, LSP servers, and helpers such as the status line command and `apiKeyHelper` run with your full access.
- Mods run their own code inside Claude Code; their file access, network requests and programs started with `$.process` are not sandboxed.

Some shell commands also run outside it:
- Commands you type at the `!` shell-mode prompt (unsandboxed in most sessions).
- Commands matching `excludedCommands`.
- Unsandboxed retries Claude asks for.

# How to use it

To put all of these behind one boundary, run the Claude Code process itself in a container, virtual machine or the sandbox runtime (see [limitations and scope](./limitations-and-scope.md)).

# Notes

Subagents run in the same process as the parent and share its sandbox configuration; background sessions run in their own process and are sandboxed when their settings enable it.
