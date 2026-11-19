---
type: "Concept"
title: "Agent SDK subprocess model and local state"
description: "The SDK spawns one claude CLI subprocess per session over stdio; transcripts, memory files and working-directory artifacts live on local disk and do not survive restarts."
resource: "https://code.claude.com/docs/en/agent-sdk/hosting"
tags: [agent-sdk, subprocess, sessions, state, hosting]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "query()"
  - "cwd"
  - "CLAUDE_CONFIG_DIR"
  - "~/.claude/projects/"
  - "~/.claude/CLAUDE.md"
  - "SessionStore"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-hosting"
    resource: "https://code.claude.com/docs/en/agent-sdk/hosting"
    title: "Hosting the Agent SDK"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`query()` spawns a separate `claude` CLI process and talks to it over stdio; the subprocess owns the shell, working directory and JSONL transcripts. One session means one subprocess, N concurrent sessions means N subprocesses each with its own process tree and transcript. By default all inherit the app's working directory; pass a distinct `cwd` in each `query()` options for separate filesystems. The subprocess does not listen on the network.

# How to use it

| State | Default location |
| - | - |
| Session transcripts | `~/.claude/projects/`, or `projects/` under `CLAUDE_CONFIG_DIR` |
| `CLAUDE.md` memory | `~/.claude/CLAUDE.md` (user tier), session working directory (project tier) |
| Working-directory artifacts | The session's working directory |

None survives a container restart, scale-down or node move. Persist transcripts with a `SessionStore` adapter; memory files and artifacts need a volume or object-store sync.

# Notes

Alternative: Managed Agents (Anthropic hosts the agent loop; tools run in an Anthropic-managed cloud sandbox or a self-hosted sandbox). A hosting cookbook has Dockerfiles and Kubernetes manifests (Docker, Modal, Kubernetes).
