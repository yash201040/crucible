---
type: "Limit"
title: "MCP output limits and warnings"
description: "Token and character thresholds for MCP tool output, MAX_MCP_OUTPUT_TOKENS, 16 MiB response cap and image saving."
resource: "https://code.claude.com/docs/en/mcp"
tags: [mcp, output, limits, tokens]
kind: "limit"
maturity: "unlabelled"
since: "2.1.283"
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "MAX_MCP_OUTPUT_TOKENS"
  - "anthropic/maxResultSizeChars"
  - "--no-session-persistence"
  - "CLAUDE_CODE_SKIP_PROMPT_HISTORY"
  - "tool-results"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "mcp"
    resource: "https://code.claude.com/docs/en/mcp"
    title: "Connect Claude Code to tools via MCP"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Limits that keep large MCP results from flooding the context.

# How to use it

`export MAX_MCP_OUTPUT_TOKENS=50000` before `claude`. A server author can raise one tool's text threshold with `_meta["anthropic/maxResultSizeChars"]` on its `tools/list` entry (example `200000`), up to a hard ceiling of 500,000 characters; it works independently of `MAX_MCP_OUTPUT_TOKENS` for text.

# Limits and defaults

| Limit | Value |
|---|---|
| transcript viewer warning | fixed 10,000 tokens |
| `MAX_MCP_OUTPUT_TOKENS` default | 25,000 tokens (for tools without their own limit; image results still obey it) |
| text result persisted to a file | longer than 50,000 characters (unless the tool declares `anthropic/maxResultSizeChars`); unaffected by `MAX_MCP_OUTPUT_TOKENS` |
| HTTP or SSE response | over 16 MiB (after decompression, one JSON body or one stream event) stops reading; request fails |
| WebSocket message | over 16 MiB closes the connection; calls in progress fail |
| error result (`isError: true`) | text longer than about 11,000 characters keeps first 5,000 and last 5,000 with a removed-count marker |

- Over the limit, a successful result with no image is saved to the session's `tool-results` directory under `~/.claude/projects/` and replaced by a message naming the path.
- Images (PNG, JPEG, GIF, WebP): Claude sees an inline copy (may be scaled or compressed); the original bytes are saved to `tool-results` and the path given (needs v2.1.283 or later). With `--no-session-persistence` or `CLAUDE_CODE_SKIP_PROMPT_HISTORY`, no file is written.
- A call moved to a background task reports through the task notification instead.
