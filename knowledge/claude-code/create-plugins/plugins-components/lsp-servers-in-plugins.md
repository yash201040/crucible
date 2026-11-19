---
type: "Feature"
title: "LSP servers in a plugin"
description: "Declare language servers in .lsp.json; the plugin configures the connection but does not install the binary."
resource: "https://code.claude.com/docs/en/plugins/components"
tags: [plugins, lsp, code-intelligence]
kind: "file"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - ".lsp.json"
  - "lspServers"
  - "extensionToLanguage"
  - "restartOnCrash"
  - "maxRestarts"
  - "--debug"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-components"
    resource: "https://code.claude.com/docs/en/plugins/components"
    title: "Add components to a plugin"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

An LSP server gives Claude diagnostics and code navigation. If an official code intelligence plugin covers the language, install that instead. Otherwise declare the server in `.lsp.json` at the plugin root: a map of server name directly to config (no wrapper), with `command`, `args`, and `extensionToLanguage` (at least one extension, each starting with `.`).

# How to use it

The `lspServers` manifest key takes the same map inline, a path, or an array; its servers add to `.lsp.json`, and a same-named manifest server replaces the file's.

# Limits and defaults

- `claude plugin validate` does not read `.lsp.json`. If any entry is invalid the whole file is skipped and `Invalid LSP server config for ".lsp.json"` appears in the `/plugin` Errors tab.
- The plugin does not install the binary; `command` is started by name from the user's `PATH`. A missing binary logs `LSP server <name> failed to start` under `claude --debug`.
- One server per file extension: if two enabled servers claim the same extension, the first registered wins and the Errors tab warns `LSP server "<name>" is not used for <ext> files`.
- Send server logs to stderr. Stdout is protocol only; headers up to 64 KiB and bodies up to 32 MiB are accepted. Exceeding either, or writing non-protocol output to stdout, disconnects the server and counts as a crash for `restartOnCrash` and `maxRestarts`.
