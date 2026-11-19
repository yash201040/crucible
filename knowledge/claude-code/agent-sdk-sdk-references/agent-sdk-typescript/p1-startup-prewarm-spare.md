---
type: "Feature"
title: "startup(), prewarm() and spare processes"
description: "Pre-spawn the Claude Code subprocess with startup() (WarmQuery) or prewarm() (alpha SpareProcess) to take spawn cost off the critical path."
resource: "https://code.claude.com/docs/en/agent-sdk/typescript"
tags: [startup, prewarm, latency, subprocess, pooling]
kind: "api"
maturity: "unlabelled"
since: "0.3.282"
surfaces: [sdk]
requires: "prewarm() is alpha and needs TypeScript Agent SDK v0.3.282+; extra hook time in startup() needs v0.3.304+"
identifiers:
  - "startup()"
  - "prewarm()"
  - "WarmQuery"
  - "SpareProcess"
  - "claim()"
  - "initializeTimeoutMs"
  - "claimed"
  - "exited"
  - "option_not_applied"
  - "not_claimed"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-typescript"
    resource: "https://code.claude.com/docs/en/agent-sdk/typescript"
    title: "Agent SDK reference - TypeScript"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`startup({ options?, initializeTimeoutMs? })` spawns the CLI subprocess and completes the initialize handshake before a prompt exists. It returns `Promise<WarmQuery>`; `warm.query(prompt)` writes the prompt to the ready process (once per WarmQuery), `warm.close()` discards it. `WarmQuery` implements `AsyncDisposable` (`await using`).

`prewarm()` (alpha) starts a spare Claude Code process before you know the session or working directory. It returns a `SpareProcess` you bind later with `claim({ prompt, options })`.

# How to use it

- `startup`: call on app boot, then `.query()` when a prompt is ready.
- `prewarm`: `const spare = await prewarm({ options })`; later `spare.claim({ prompt, options: { cwd } })` (`options.cwd` required; returns a `Query` synchronously; claim once). A claim may also set `additionalDirectories`, `model`, `permissionMode`, `maxThinkingTokens`, `settings` (flag overlay), `appendSystemPrompt`, `title`, `agents`, and per-session tokens in `env`.
- `SpareProcess` members: `claimed` (resolves `{ cwd, sessionId, parkedMs?, sdkMcpSettled }`; rejects on refusal, early exit, or message starting `option_not_applied`), `exited` (settles when process exits; replace unclaimed spares that exit), `close()`.
- A refused claim (e.g. nonexistent folder, or project settings that set `env`, `agent` or `model`) gives an error result starting `not_claimed` and the returned query throws; wrap the loop in try. After a rejection other than `option_not_applied` the prompt did not run: use `query()`.

# Limits and defaults

- `initializeTimeoutMs` default `60000`; rejects with a timeout error.
- `startup()`: if unset, time in slow SessionStart and Setup command hooks does not count toward the 60s, up to 10 minutes total (11 minutes max). If you set any value (even 60000) it is the limit. Needs v0.3.304+. Held `hook_started`/`hook_progress` messages (only the newest progress) reach you once you call `.query()` and iterate.
- `prewarm()` always counts Setup hook time toward `initializeTimeoutMs`. It rejects if `options` has `resume`, `continue` or `forkSession`.
- A spare waits in a private temp directory under the Claude Code config dir, or `options.cwd`; with `spawnClaudeCodeProcess` on another machine or container pass a `cwd` that exists there. Each spare uses roughly 230 to 260 MB.
- Not done until `claim()`: cd to the claim's cwd, SessionStart hooks, stdio MCP servers, loading CLAUDE.md and git context.
- A claim cannot change `mcpServers`, `hooks`, `canUseTool`, `settingSources`, `plugins`; keep one spare per distinct set.
