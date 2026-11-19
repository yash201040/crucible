---
type: "Limit"
title: "WebSearch tool and session search limit"
description: "Anthropic-backend web search, up to 8 backend searches per call, a 200-call session cap with refill, and per-turn limits in -p and SDK runs."
resource: "https://code.claude.com/docs/en/tools-reference#websearch-tool-behavior"
tags: [websearch, limits, headless, subagents, refill]
kind: "env_var"
maturity: "unlabelled"
since: "2.1.290"
surfaces: [cli, headless, sdk]
requires: "Claude API, Claude Platform on AWS, Claude Models on Google Cloud (Anthropic managed) or Microsoft Foundry; not Amazon Bedrock"
identifiers:
  - "WebSearch"
  - "CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION"
  - "CLAUDE_CODE_WEB_SEARCH_REFILLS_PER_HOUR"
  - "allowed_domains"
  - "blocked_domains"
  - "/clear"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "tools-reference"
    resource: "https://code.claude.com/docs/en/tools-reference"
    title: "Tools reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Runs a query against Anthropic's web search backend and returns titles and URLs, not page contents (use WebFetch for that). It may issue up to eight backend searches per call. `allowed_domains` or `blocked_domains` scope results; they cannot be combined in one call. Overload is retried with backoff. The backend is not configurable; use an MCP server for another provider. Permission rules take no specifier (a bare `WebSearch`). On Google Cloud Agent Platform it works with Opus 4, Sonnet 4, Haiku 4.5 and later.

# How to use it

- Interactive terminal session limit: 200 WebSearch calls, shared by the main conversation and subagents (such as a parallel research fan-out). At the limit searches appear as calls that did nothing and Claude is told to continue with what it has and ask you to raise the limit.
- Raise the cap: `CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION` to a positive whole number (e.g. `500`); it cannot be turned off.
- Refill: on v2.1.290+ an interactive session refills about 100 calls per hour; change with `CLAUDE_CODE_WEB_SEARCH_REFILLS_PER_HOUR` (e.g. `50`).
- `/clear` resets the count, unless work that can still spawn subagents survives (such as a running workflow), then it carries over.

# Limits and defaults

In `-p` mode and the Agent SDK the limit is per turn (from a message you send until Claude finishes responding), reset by the next message or a new `claude -p` run, even with `--continue` or `--resume`.
