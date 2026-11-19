---
type: "Feature"
title: "MCP servers, plugins and deny rules vs cache"
description: "How connecting MCP servers, toggling plugins and denying whole tools affect cached tool definitions, with and without tool search."
resource: "https://code.claude.com/docs/en/prompt-caching"
tags: [prompt-caching, mcp, plugins, deny-rules, tool-search]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.260"
surfaces: [cli, headless, sdk, desktop]
requires: "/reload-plugins in non-interactive sessions needs v2.1.260 or later; --plugin-dir live apply needs v2.1.265 or later"
identifiers:
  - "/reload-plugins"
  - "/reload-plugins --force"
  - "--plugin-dir"
  - "WaitForMcpServers"
  - "/advisor"
  - "/cd"
  - "mcp__*"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "prompt-caching"
    resource: "https://code.claude.com/docs/en/prompt-caching"
    title: "How Claude Code uses prompt caching"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Tool definitions live in the system prompt layer, so the cache invalidates when the set of definitions in a request changes. Exception: toggling `/advisor` keeps the prefix (its definition sits after the cache breakpoint).

# How to use it

**Tool search on (default on supported models).** Claude Code keeps the first request's tool list for the whole conversation; servers connecting or dropping mid-session do not disturb the cache, and late servers supply deferred definitions. A bare-tool deny rule also leaves the prefix intact.

**Tool search off or unavailable** (examples: Google Cloud Agent Platform models earlier than Opus 4.5, Sonnet 4.5, Haiku 4.5; a Foundry deployment hosted on Azure that rejects tool search):

| Mid-session change | Cache |
| - | - |
| Server connects, or dynamic tool update adds tools | Invalidated |
| Server drops with no action (e.g. stdio process exits) | Kept; calls to its tools error unless Claude Code restarts the server |
| Remote server auto-reconnects | Kept, unless a request during reconnect adds `WaitForMcpServers` (invalidates once; stays listed) |
| You remove a tool (deny rule, disabling server in `/mcp`) | Invalidated |

Editing MCP config does not change the cache; it takes effect after restart. When resuming, a still-connecting server's recorded definitions are included as recorded.

**Plugins.** Skills, commands, agents, hooks, monitors and themes never invalidate the cache; content is appended. Plugins with MCP servers follow the MCP rules. Changes in `/plugin` run `/reload-plugins` on menu close; with a full re-read, Claude Code warns and does not apply it until `/reload-plugins --force`. `/cd` (v2.1.246+) applies the new directory's plugins without the warning; `--plugin-dir` folder changes apply immediately in interactive sessions (v2.1.265+), or are held with a notice. `/reload-plugins` also works in desktop, Agent SDK and `-p` sessions when typed in (v2.1.260+), applying everything except plugin MCP changes (next session). Disabling a plugin enabled earlier restores the old request shape; if still in cache lifetime it reads the old entry.

**Deny rules.** A bare tool name (`Bash`, `WebFetch`), the `Bash(*)` form, or a tool-name glob like `"*"` or `"mcp__*"` blocks the tool from the next request, including a mid-turn `/permissions` rule. Without tool search the definition is removed (invalidates, and so does removing the rule). Scoped deny rules like `Bash(rm *)`, and all allow and ask rules, do not change visible tools.
