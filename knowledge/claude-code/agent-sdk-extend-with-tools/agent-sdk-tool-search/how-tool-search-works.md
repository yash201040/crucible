---
type: "Feature"
title: "How SDK tool search works"
description: "Tool definitions are withheld from context and the agent searches a catalog, loading up to five relevant tools at a time."
resource: "https://code.claude.com/docs/en/agent-sdk/tool-search"
tags: [tool-search, context, mcp, deferral]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [sdk]
requires: ""
identifiers:
  - "ToolSearch"
  - "alwaysLoad"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-sdk-tool-search"
    resource: "https://code.claude.com/docs/en/agent-sdk/tool-search"
    title: "Scale to many tools with tool search"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Tool search lets an agent work with hundreds or thousands of tools: instead of loading all definitions upfront, the agent gets a summary of available tools and searches when it needs a capability not loaded. It addresses context use (50 tools can use 10-20K tokens) and selection accuracy (degrades with more than 30-50 tools loaded at once).

# How to use it

On by default (exceptions under [configure](./configure-tool-search.md)). Up to five most relevant tools load per search by default and stay available on later turns until the SDK compacts the messages where they were discovered; after that compaction the agent searches again.

# Limits and defaults

- Each search costs one extra round-trip; with fewer than about 10 tools that fit comfortably, loading everything upfront is typically faster.
- Not supported on Microsoft Foundry deployments hosted on Azure, which reject it server-side; the SDK detects this and loads definitions upfront, and `ENABLE_TOOL_SEARCH` cannot override it.

# Notes

Applies to all registered tools, remote MCP servers and custom SDK MCP servers alike. See [optimize discovery](./optimize-tool-discovery-and-limits.md).
