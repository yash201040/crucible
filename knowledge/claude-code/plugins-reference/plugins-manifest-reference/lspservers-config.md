---
type: "Reference"
title: "lspServers configuration fields"
description: "Strict per-server fields for lspServers: command, extensionToLanguage, timeouts, restart controls and diagnostics."
resource: "https://code.claude.com/docs/en/plugins/manifest-reference"
tags: [plugins, lsp, config, timeouts]
kind: "file"
maturity: "unlabelled"
since: "2.1.288"
surfaces: [cli]
requires: ""
identifiers:
  - "command"
  - "extensionToLanguage"
  - "args"
  - "transport"
  - "env"
  - "initializationOptions"
  - "settings"
  - "workspaceFolder"
  - "startupTimeout"
  - "shutdownTimeout"
  - "requestTimeout"
  - "restartOnCrash"
  - "maxRestarts"
  - "diagnostics"
  - ".lsp.json"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-manifest-reference"
    resource: "https://code.claude.com/docs/en/plugins/manifest-reference"
    title: "Plugin manifest reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`lspServers` takes a `.json` file path, an inline map of server name to config, or an array of either. `.lsp.json` at the plugin root loads first, then each declared config; a later server name replaces an earlier one. Each server config is a strict object; an unknown key fails validation.

# How to use it

| Field | Required | Description |
| :- | :- | :- |
| `command` | Yes | Language server binary; no spaces unless the value starts with `/`; put arguments in `args` |
| `extensionToLanguage` | Yes | Map of file extension (starting with a dot, e.g. `".go"`) to LSP language ID, at least one entry |
| `args` | No | Arguments |
| `transport` | No | `stdio` (default) or `socket`; `socket` is accepted but every server runs over stdio, so stdout protocol rules apply to all |
| `env` | No | Environment variables |
| `initializationOptions` | No | Options in the initialize request |
| `settings` | No | Sent by `workspace/didChangeConfiguration` |
| `workspaceFolder` | No | Workspace folder path |
| `startupTimeout` | No | ms to wait for startup, positive integer |
| `shutdownTimeout` | No | ms for graceful shutdown, positive integer; on timeout the process is terminated; unset means no timeout |
| `requestTimeout` | No | ms to wait for an answer, positive integer; default `60000`. v2.1.288 or later |
| `restartOnCrash` | No | Restart after a crash; default `true` |
| `maxRestarts` | No | Restart attempts before giving up, zero or more |
| `diagnostics` | No | Push diagnostics into context after edits; default `true` |

Example: `"lspServers": { "go": { "command": "gopls", "args": ["serve"], "extensionToLanguage": { ".go": "go" } } }`.
