---
type: "Limit"
title: "SDK hosting known limitations and deployment failures"
description: "No session timeout, memory growth, subagent fanout rate limits, no per-subagent deadline, and common CLI-not-found or launch failures."
resource: "https://code.claude.com/docs/en/agent-sdk/hosting"
tags: [agent-sdk, limits, subagents, timeouts, troubleshooting]
kind: "limit"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "maxTurns"
  - "max_turns"
  - "AgentDefinition"
  - "CLAUDE_ASYNC_AGENT_STALL_TIMEOUT_MS"
  - "pathToClaudeCodeExecutable"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-hosting"
    resource: "https://code.claude.com/docs/en/agent-sdk/hosting"
    title: "Hosting the Agent SDK"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Limitations to design around.

# How to use it

| Limitation | What to do |
| - | - |
| No top-level session timeout | Bound turns with `maxTurns` (TypeScript) or `max_turns` (Python) |
| Memory growth over long sessions | Cap session length or recycle subprocesses periodically |
| Large parallel-subagent fanouts can hit rate limits | Break work into smaller batches |
| No per-subagent wall-clock deadline | Cap each subagent with `maxTurns` in its `AgentDefinition`; `CLAUDE_ASYNC_AGENT_STALL_TIMEOUT_MS` is a stall watchdog (fires when a subagent stops producing output), not a total-runtime deadline |

# Notes

Troubleshooting: CLI not found at service start (Python: different `PATH` in a container or service manager; TypeScript: optional dependencies skipped at image build, or `pathToClaudeCodeExecutable` points at a missing file). CLI present but won't launch: binary mismatched to container architecture or libc, or lost execute permission. Process exits mid-run: error depends on SDK language and whether the CLI reported an error result first (see troubleshooting page, not in this unit).
