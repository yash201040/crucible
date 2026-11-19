---
type: "Reference"
title: "Tool annotations for server authors"
description: "_meta and annotations a server sets on a tool: requiresUserInteraction, idempotentHint, readOnlyHint, alwaysLoad."
resource: "https://code.claude.com/docs/en/mcp"
tags: [mcp, annotations, permissions, server-author]
kind: "api"
maturity: "unlabelled"
since: "2.1.285"
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "anthropic/requiresUserInteraction"
  - "idempotentHint"
  - "readOnlyHint"
  - "anthropic/alwaysLoad"
  - "--permission-prompt-tool"
  - "canUseTool"
  - "dontAsk"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "mcp"
    resource: "https://code.claude.com/docs/en/mcp"
    title: "Connect Claude Code to tools via MCP"
stale_after: "2027-01-19T00:00:00Z"
---

# How to use it

| Annotation (in the `tools/list` entry) | Effect |
|---|---|
| `_meta["anthropic/requiresUserInteraction"]: true` (must be Boolean `true`) | permission prompt on every call, even in `acceptEdits`, `auto`, `bypassPermissions`; no "don't ask again"; allow rules do not skip it; `dontAsk` mode or a `-p` run with nothing to answer denies |
| `annotations.idempotentHint: true` | changes state but is safe to repeat; Claude Code may repeat a call pending when a connection closed, once, on a new connection (HTTP and claude.ai connector servers) |
| `annotations.readOnlyHint: true` | changes nothing; also repeatable, and runs in parallel with other read-only calls |
| `_meta["anthropic/alwaysLoad"]` true / false | load upfront or stay deferred (see [tool search](./mcp-tool-search.md)) |

An unmarked call that fails can surface `connection closed before the tool call was answered`.

# Limits and defaults

- With `--permission-prompt-tool` in non-interactive mode, an `allow` from the prompt tool for a flagged tool becomes a deny: `MCP tool requires user interaction; not supported via --permission-prompt-tool`. The Agent SDK `canUseTool` callback does receive such calls and can approve them.
- On Remote Control and Agent SDK apps that offer one-tap approval, the tap is withheld and the full prompt shown; same for any request only the terminal dialog can render fully (safety warning, always-allow option).
