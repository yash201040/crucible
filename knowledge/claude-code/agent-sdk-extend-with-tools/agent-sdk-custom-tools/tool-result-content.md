---
type: "Reference"
title: "Tool result content blocks"
description: "Content block types a custom tool can return (text, image, audio, resource, resource_link) and structuredContent, with TypeScript and Python differences."
resource: "https://code.claude.com/docs/en/agent-sdk/custom-tools"
tags: [images, resources, structured-content, tool-results]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "image"
  - "audio"
  - "resource"
  - "resource_link"
  - "resourceLinks"
  - "structuredContent"
  - "mimeType"
  - "resource.uri"
  - "resource.text"
  - "resource.blob"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-custom-tools"
    resource: "https://code.claude.com/docs/en/agent-sdk/custom-tools"
    title: "Give Claude custom tools"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The `content` array accepts mixed `text`, `image`, `audio`, `resource` and `resource_link` blocks (shapes from MCP `CallToolResult`).

# How to use it

| Block | Fields | Behavior |
| --- | --- | --- |
| `image` | `data` (raw base64, no `data:` prefix), `mimeType` (required) | No URL field; fetch and encode yourself. PNG, JPEG, GIF, WebP reach Claude as visual input; other types are saved to disk and Claude gets the file path as text |
| `resource` | `resource.uri`, `resource.text` or `resource.blob` (not both), optional `resource.mimeType` | The URI is a label, not read by the SDK. `blob` is TypeScript only: Python drops binary resources with a logged warning |
| `audio` | | TypeScript saves it to disk and Claude gets a text block with the path; Python drops the block and logs a warning |
| `resource_link` | | Claude gets a text block with name, URI, description. TypeScript apps also get `resourceLinks` on the user message's `tool_use_result`; in Python the key is never produced for in-process tools |

`structuredContent`: optional JSON object beside `content` for exact machine-readable fields. When a TypeScript `tool()` handler sets it, Claude receives the JSON plus image and resource blocks, and text blocks in `content` do not reach Claude.

# Limits and defaults

The Python `@tool` decorator forwards only `content` and `is_error`; to return `structuredContent` from Python, run a standalone MCP server instead of an in-process one.
