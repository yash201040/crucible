---
type: "Feature"
title: "LSP tool behavior"
description: "Code intelligence from language servers, active only once a code intelligence plugin is installed."
resource: "https://code.claude.com/docs/en/tools-reference#lsp-tool-behavior"
tags: [lsp, code-intelligence, plugins, tools]
kind: "tool"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: "Code intelligence plugin and language server binary"
identifiers:
  - "LSP"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "tools-reference"
    resource: "https://code.claude.com/docs/en/tools-reference"
    title: "Tools reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

After each file edit it reports type errors and warnings automatically. Claude can also jump to definitions, find references, get type info, list file symbols, search symbols workspace-wide, find implementations and trace call hierarchies.

# Limits and defaults

Inactive until a code intelligence plugin is installed for the language; the plugin supplies server configuration but you install the server binary. In cloud sessions plugin language servers are not started, so the tool stays inactive. A call on a file whose server cannot start returns an error result.
