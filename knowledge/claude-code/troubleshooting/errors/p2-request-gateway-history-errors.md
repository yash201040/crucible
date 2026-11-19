---
type: "Reference"
title: "Gateway field and conversation-history 400 errors"
description: "400 errors from beta fields dropped by gateways and from inconsistent history blocks, with built-in retry and the versions that added recovery."
resource: "https://code.claude.com/docs/en/errors"
tags: [errors, gateway, history, rewind, retries]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "context_management"
  - "defer_loading"
  - "tool_reference"
  - "anthropic-beta"
  - "CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS"
  - "/rewind"
  - "redacted_thinking"
  - "encrypted_content"
  - "encrypted_stdout"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "errors"
    resource: "https://code.claude.com/docs/en/errors"
    title: "Error reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

400 errors where the request body or saved conversation no longer matches what the API accepts.

# How to use it

| Error | Behavior and fix |
|---|---|
| `Extra inputs are not permitted` (`context_management`) | Gateway drops `anthropic-beta` or upstream has a different schema. Claude Code resends without the field from v2.1.304. Fallback `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS=1`. A `diagnostics` variant before v2.1.302 appeared after switching providers mid-session. |
| Same error naming `defer_loading` or `tool_reference` | Claude Code resends without tool search fields from v2.1.305. |
| `tool_use.name: String should have at most 200 characters` | Names are cut to 200 characters on arrival and on load (fixed v2.1.281; the tool call then fails as `No such tool available`). |
| Tool use / thinking block mismatch | Variants: tool use concurrency, orphaned `tool_result`, duplicate `tool_use` ID, unexpected `tool_use_id`, thinking blocks cannot be modified. Run `/rewind` or press Esc twice. Opus 4.7 and 4.8 before v2.1.156 could trigger it in normal use; `/rewind` does not clear it there. |
| `Invalid data in redacted_thinking block` | Earlier thinking dropped and retried once (v2.1.282+). |
| `[Unsupported tool content removed]` | Placeholder when loading a saved session connected directly to the Anthropic API (v2.1.246+); content typically came from a third-party proxy. |
| `role 'system' must precede an 'assistant' message` | Claude Code retries once sending reminder text as user messages (v2.1.280+); persistent error usually means a gateway added a system message. |
| `Invalid encrypted_content in search_result block` and siblings | Hosted web search content from a proxy/gateway the API cannot decrypt. Search content dropped and retried once (v2.1.282+); the `encrypted_stdout` form has no recovery. |

# Notes

Claude Code's own WebSearch tool records results as plain text.
