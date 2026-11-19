---
type: "Reference"
title: "Mods API access namespaces"
description: "$.fs, $.process, $.http, $.store, $.env, $.settings, $.session and $.mcp give a mod file, process, network, state and settings access with user permissions."
resource: "https://code.claude.com/docs/en/plugins/mods/api"
tags: [mods, filesystem, process, http, permissions]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "$.fs"
  - "$.process"
  - "$.http"
  - "$.store"
  - "$.env"
  - "$.settings"
  - "$.session"
  - "$.mcp"
  - "$.process.run"
  - "$.process.spawn"
  - "$.http.fetch"
  - "$.session.messages"
  - "$.session.usage"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-api"
    resource: "https://code.claude.com/docs/en/plugins/mods/api"
    title: "Use the mods API"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A mod reaches the file system, processes and network through the mods API, with the same permissions as the user. The hooks module itself has no Node.js APIs, no timer globals such as `setTimeout`, and no network or file access. Standard JavaScript and web APIs such as `URL`, `TextEncoder`, `AbortController`, `crypto.subtle` are available.

# How to use it

| Namespace | What it does |
| :- | :- |
| `$.fs` | `read(path)`, `write(path, text)`, `exists(path)`, `stat(path)`, `list(path)` |
| `$.process` | `run(['git','status'])` runs and resolves on exit; `spawn` streams a long-running command |
| `$.http` | `fetch(url, init)` over http or https; resolves `{ status, ok, headers, text }` |
| `$.store` | JSON key-value store of the plugin's own, kept between sessions |
| `$.env` | `get` and `set` environment variables; name must be a string literal |
| `$.settings` | `read()` merged settings, or one source/key |
| `$.session` | `messages()` transcript as `{ role, text, toolUses }`, working directory, model, `usage()` context window use and plan limits, and more |
| `$.mcp` | `call` a tool on a connected MCP server |

# Limits and defaults

- Relative paths resolve against the working directory of the session, or of the subagent whose event is being handled.
- `$.fs.list` returns `{ name, kind, size, isLink }` entries, not recursive.
- `$.process.run` takes an argument list (no shell), resolves `{ exitCode, stdout, stderr }` whatever the exit code, rejects if the program cannot start or is still running at the timeout (default 30 seconds); wrap in `try`/`catch`.
- `$.http.fetch` follows up to five redirects; on a cross-origin redirect it keeps only `accept`, `accept-language`, `content-type`, `user-agent` request headers (so `Authorization` can fail after it).
- Every call is itself an event named for namespace and method without `$.` (e.g. `fs.read`); a mod earlier in the chain can observe, rewrite or refuse it, which is how an organization restricts mods.
- A mod can refuse `$.process.spawn` after the command produced output or exited; nothing is undone. The call rejects with a message ending in `$.process.spawn started, and a plugin withheld its result:` (output not read to the end; the command is stopped if running) or `$.process.spawn ran, and a plugin withheld its result:` (command had exited), plus the refusing mod's reason.
