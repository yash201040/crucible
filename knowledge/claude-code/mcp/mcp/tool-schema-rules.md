---
type: "Reference"
title: "Tool input schema rules and exclusions"
description: "How Claude Code flattens root-level combinators, excludes invalid schemas and tools with names over 128 characters."
resource: "https://code.claude.com/docs/en/mcp"
tags: [mcp, schema, validation, limits]
kind: "limit"
maturity: "unlabelled"
since: "2.1.328"
surfaces: [cli, cloud]
requires: ""
identifiers:
  - "anyOf"
  - "oneOf"
  - "allOf"
  - "input schema would be rejected by the Anthropic API"
  - "the API refused this tool's input schema"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "mcp"
    resource: "https://code.claude.com/docs/en/mcp"
    title: "Connect Claude Code to tools via MCP"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Rules applied to an MCP tool's schema and name before the tool goes to the API.

# How to use it

- Root-level `anyOf`/`oneOf`/`allOf` (the API rejects them at the schema root; nested ones in `properties` pass through): Claude Code flattens into one object and prepends a sentence to the description. `allOf`: properties merged, each branch's `required` still applies. `anyOf`/`oneOf`: properties merged, each branch's `required` described in the description. The server still receives whatever arguments Claude chose, so validate combinations server-side.
- Excluded tools (the server's other tools stay): top-level property names must be 1 to 64 characters of ASCII letters, digits, `_`, `.`, `-`; the schema must be valid against JSON Schema draft 2020-12 (checked for schemas with no `$schema` or the 2020-12 one; other dialects skip this check but not the name check). Exclusion is logged in the server log and Claude is told which tools and why; the tool returns after you fix it and Claude Code reloads the tools.
- Full tool name `mcp__<server>__<tool>` over 128 characters: left out of what is sent to Claude.

# Limits and defaults

- When no schema the API accepts can be produced, or feature-flag fetching is on but flags have not arrived, the root-combinator tool is skipped (before v2.1.328 it was also skipped with fetching off). In that same flags-not-arrived state, a rule-breaking tool is not excluded; it is sent unchanged and logged as `input schema would be rejected by the Anthropic API`. Before v2.1.328 tools were not excluded with fetching off; before v2.1.216 no deployment ran these checks.
- If the API refuses a schema, the debug log has `the API refused this tool's input schema` (ending `The API said:` plus the reason); Claude Code resends the request with the tool declared without parameters, so Claude can call it without seeing parameters. Before v2.1.300 each such turn failed with a 400 naming the tool by position.
