---
type: "Feature"
title: "Monitor WebSocket source"
description: "Monitor can open a ws:// or wss:// socket in place of a command; event rules, denied addresses and Bash-rule interactions."
resource: "https://code.claude.com/docs/en/tools-reference#websocket-source"
tags: [monitor, websocket, network, permissions]
kind: "tool"
maturity: "unlabelled"
since: "2.1.319"
surfaces: [cli]
requires: ""
identifiers:
  - "ws"
  - "url"
  - "protocols"
  - "timeout_ms"
  - "CLAUDE_CODE_PROXY_RESOLVES_HOSTS"
  - "sandbox.network.deniedDomains"
  - "allowManagedDomainsOnly"
  - "Bash(*)"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "tools-reference"
    resource: "https://code.claude.com/docs/en/tools-reference"
    title: "Tools reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A WebSocket watch takes a `ws` input in place of `command`; one Monitor call cannot combine both.

# How to use it

| `ws` field | Required | Meaning |
| :- | :- | :- |
| `url` | Yes | `ws://` or `wss://`, ASCII only, no embedded credentials or whitespace |
| `protocols` | No | Subprotocol names offered in the handshake; valid tokens, no duplicates |

- Text messages: one event each (even multi-line). Binary messages: not passed, Claude gets a placeholder such as `[binary frame, 512 bytes]`. A message over 1 MiB ends the watch. Socket close ends the watch and Claude gets the close code. `timeout_ms` applies; `TaskStop` cancels early.
- Without a `Monitor` allow rule you are prompted before a socket opens (no option to skip future prompts per host); in auto mode the classifier decides unless an ask rule applies.
- Denied: URLs pointing at private, link-local or cloud-metadata addresses (including hostnames that resolve there), hosts in `sandbox.network.deniedDomains`, and with `allowManagedDomainsOnly` in managed settings any host outside the managed allowlist. Behind a proxy, Claude Code does not check the proxy-resolved address. If a proxied watch fails with `could not resolve <host>`, restart v2.1.319+ with `CLAUDE_CODE_PROXY_RESOLVES_HOSTS=1`.

# Limits and defaults

A `Bash` or `Bash(*)` deny rule also blocks WebSocket watches: if present at session start Claude lacks Monitor; if added mid-session the next call is refused with `Permission to use Monitor has been denied: it runs code as Bash does, and a rule denies Bash.` An ask rule requires approval that no allow rule, `PreToolUse` hook, `bypassPermissions` or auto classifier can give; only a `PermissionRequest` hook can approve; where nobody can answer (such as `dontAsk`) it is denied. Ask rule and mid-session deny coverage need v2.1.319+. Narrow the rule, for example `Bash(rm *)`.
