---
type: "Reference"
title: "Custom process spawning and setMcpServers result"
description: "SpawnedProcess and SpawnOptions for running Claude Code in VMs or containers, abort signal timing, and McpSetServersResult rules."
resource: "https://code.claude.com/docs/en/agent-sdk/typescript"
tags: [spawn, containers, abort, mcp, isolation]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "SpawnedProcess"
  - "SpawnOptions"
  - "spawnClaudeCodeProcess"
  - "McpSetServersResult"
  - "setMcpServers()"
  - "allowedMcpServers"
  - "deniedMcpServers"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-typescript"
    resource: "https://code.claude.com/docs/en/agent-sdk/typescript"
    title: "Agent SDK reference - TypeScript"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`spawnClaudeCodeProcess(options: SpawnOptions) => SpawnedProcess` lets a host launch Claude Code in a VM, container or remote environment. `SpawnOptions` is `{ command, args, cwd?, env, signal }`. `SpawnedProcess` needs `stdin`, `stdout`, `killed`, `exitCode`, `kill(signal)` and `on`/`once`/`off` for `exit` and `error`; Node's `ChildProcess` already satisfies it.

# How to use it

Pass `signal` to Node `spawn()` or to your VM/container teardown handler. The signal does not fire the instant `Options.abortController` aborts: the SDK first closes the process's stdin and waits about two seconds so the CLI can shut down cleanly, then aborts the signal. To react immediately, listen on your own `abortController.signal`.

`setMcpServers()` returns `McpSetServersResult { added, removed, errors }` and resolves after new stdio, HTTP and SSE servers connect or fail, so their tools are available next turn. `added` lists servers added or replaced even if they failed (also in `errors` with a `failed` row in `mcpServerStatus()`; before v2.1.257 a thrown connect was only in `errors`). A server named again with an identical config keeps its connection; a changed config reconnects and is listed in `added`. Same-named servers from an installation scope such as `.mcp.json` yield to yours (before v2.1.305, a plugin reload could swap them back).

# Limits and defaults

`errors` values starting `Blocked by enterprise`: `Blocked by enterprise policy (allowedMcpServers/deniedMcpServers)` (not in `added`) or `Blocked by enterprise managed policy` (in `added` with a `failed` row).
