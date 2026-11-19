---
type: "Feature"
title: "Use MCP resources with @ mentions"
description: "Reference MCP resources in prompts as @server:protocol://path; plain text in claude -p; UI resources excluded from listings."
resource: "https://code.claude.com/docs/en/mcp"
tags: [mcp, resources, mentions, headless]
kind: "ui"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "@server:protocol://resource/path"
  - "ui://"
  - "text/html;profile=mcp-app"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "mcp"
    resource: "https://code.claude.com/docs/en/mcp"
    title: "Connect Claude Code to tools via MCP"
stale_after: "2027-01-19T00:00:00Z"
---

# How to use it

Type `@` to see resources from connected servers alongside files (fuzzy-searchable). Reference with `@server:protocol://resource/path`, for example `@github:issue://123` or `@docs:file://api/authentication`; several per prompt are allowed. Resources are fetched and attached automatically; Claude Code provides tools to list and read resources when servers support them.

# Limits and defaults

With `claude -p`, a resource mention stays plain text. MCP Apps UI resources (`ui://` URI or `text/html;profile=mcp-app` media type) are for a host to render: they do not show in `@` suggestions or the list tool's results (a server offering only UI resources shows an empty list), but reading one by URI still works.
