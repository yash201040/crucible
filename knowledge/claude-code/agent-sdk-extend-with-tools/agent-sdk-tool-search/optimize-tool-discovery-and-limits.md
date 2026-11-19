---
type: "Limit"
title: "Optimize tool discovery and tool search limits"
description: "Name and describe tools for search, append a category hint to the system prompt, and know the 10,000-tool catalog limit."
resource: "https://code.claude.com/docs/en/agent-sdk/tool-search"
tags: [tool-search, limits, tool-naming, system-prompt]
kind: "limit"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: "Opus 4, Sonnet 4, Haiku 4.5 and later"
identifiers:
  - "systemPrompt"
  - "system_prompt"
  - "append"
  - "preset: \"claude_code\""
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-tool-search"
    resource: "https://code.claude.com/docs/en/agent-sdk/tool-search"
    title: "Scale to many tools with tool search"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Search matches queries against tool names and descriptions, so wording affects discovery.

# How to use it

- Use specific names (`search_slack_messages` surfaces for more requests than `query_slack`) and keyword-rich descriptions ("Search Slack messages by keyword, channel, or date range").
- Add a system prompt section naming tool categories: `systemPrompt: { type: "preset", preset: "claude_code", append: "You can search for tools to interact with Slack, GitHub, and Jira." }` (Python `system_prompt`). `append` adds to the preset instead of replacing it.

# Limits and defaults

- Maximum 10,000 tools in the catalog.
- Up to five most relevant tools returned per search by default.
- Models: Opus 4, Sonnet 4, Haiku 4.5 and later; on Google Cloud's Agent Platform Opus 4.5, Sonnet 4.5, Haiku 4.5 and later. On earlier models definitions load upfront.
