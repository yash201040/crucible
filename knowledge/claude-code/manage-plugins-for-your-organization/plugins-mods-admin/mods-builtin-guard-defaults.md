---
type: "Concept"
title: "Built-in mod guard and default behavior"
description: "The built-in sec-default guard mod that loads ahead of user mods, what it blocks, and what a user mod can still do."
resource: "https://code.claude.com/docs/en/plugins/mods/admin"
tags: [mods, guard, security, permissions, defaults]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.299"
surfaces: [cli]
requires: "managed settings or managed-mcp.json, or a Team/Enterprise /login"
identifiers:
  - "sec-default@builtin"
  - "cc-plugin-sec-default"
  - "managed-mcp.json"
  - "$.fs"
  - "$.process"
  - "$.tool.call"
  - "$.mcp.call"
  - "$.http.fetch"
  - "CLAUDE_CODE_DISABLE_WEB_FETCH"
  - "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC"
  - "CLAUDE_CODE_OAUTH_TOKEN"
  - "tool.describe"
  - "session.append"
  - "settings.read"
  - "prompt.compose"
  - "prompt.section"
  - "prompt.context"
  - "prompt.attachment"
  - "skill.prompt"
  - "attribution.text"
  - "session.compact"
  - "classic.<Event>"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-admin"
    resource: "https://code.claude.com/docs/en/plugins/mods/admin"
    title: "Manage mods for your organization"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

With no mod settings, mods are on and a built-in guard mod (`sec-default@builtin`, listed as `cc-plugin-sec-default` in `/plugin` and the debug log) loads ahead of every user mod and cannot be turned off. It loads when the machine has managed settings or a `managed-mcp.json`, or the session uses `/login` credentials for a Team or Enterprise plan. API key or Bedrock/Agent Platform/Foundry users get it only on machines with managed settings or `managed-mcp.json`; a session on a long-lived `CLAUDE_CODE_OAUTH_TOKEN` does not count as that login. Guard source is public in the `mods/sec-default` directory of the Claude Code repository.

# Limits and defaults

When the guard loads, a user's mod cannot rewrite: the system prompt, managed `CLAUDE.md` and other managed instructions, the answer to a settings read, or the tool list and descriptions of a connected managed MCP server. On v2.1.323+ a user mod can still keep a managed MCP server from connecting (`/mcp` shows it held by that mod). When a user mod approves a call: `deny` rules still refuse, `ask` rules still prompt, and a blocked `PreToolUse` hook stays blocked (override deny via `allowModsToOverrideDenyRules`).

Apart from that, a user mod acts as the user: files, processes, network; can rewrite tool calls and prompts, deny tool calls, add or remove tools, draw UI. A mod's own calls can skip checks: `$.fs`/`$.process` calls skip permission rules and `PreToolUse` hooks (a mod can read a `Read(.env)`-denied file); `$.tool.call`/`$.mcp.call` skip permission rules, prompts, a hook's `ask` and the auto mode classifier.

Hooks of a user mod that never run where the guard loads (v2.1.299+ shows a note in `/plugin` Errors tab): `classic.<Event>` (e.g. `classic.Stop`), `prompt.compose`, `prompt.section`, `prompt.context`, `prompt.attachment`, `skill.prompt`, `attribution.text`, `session.compact`, `settings.read`, and `session.append` filtered to door `attachment`, `hook-context` or `compaction`. Some others (e.g. `tool.describe` for org tool descriptions) are passed over without a note. To let such hooks run, install the mod as the org's own, or leave `sec-default@builtin` out of `prependPlugins` (loses the whole guard).

Other controls: managed `PreToolUse` hooks run before any mod's `tool.call` hook and run again on a rewritten call; settings-file hooks run alongside mods; WebFetch policy denial also refuses every mod's `$.http.fetch`, but `CLAUDE_CODE_DISABLE_WEB_FETCH` or a `WebFetch` deny rule does not; `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` stops only built-in mods and `$.http.fetch` carrying Anthropic credentials (before v2.1.288 it stopped every mod's fetch). Nothing covers a program a mod starts with `$.process.run`.

The guard fails closed: if it cannot read managed settings it refuses every user mod at load; if it cannot check deny rules for a call a user mod approved, it refuses the call.
