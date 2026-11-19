---
type: "Reference"
title: "Code intelligence (LSP) plugins"
description: "Official language server plugins, their binaries, install steps and what Claude gains (diagnostics and the LSP tool)."
resource: "https://code.claude.com/docs/en/plugins/code-intelligence"
tags: [lsp, code-intelligence, plugins, diagnostics]
kind: "tool"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: "Language server binary on PATH; terminal sessions only"
identifiers:
  - "LSP"
  - "clangd-lsp"
  - "csharp-lsp"
  - "gopls-lsp"
  - "jdtls-lsp"
  - "kotlin-lsp"
  - "liquid-lsp"
  - "lua-lsp"
  - "php-lsp"
  - "pyright-lsp"
  - "ruby-lsp"
  - "rust-analyzer-lsp"
  - "swift-lsp"
  - "typescript-lsp"
  - "/plugin install typescript-lsp@claude-plugins-official"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-code-intelligence"
    resource: "https://code.claude.com/docs/en/plugins/code-intelligence"
    title: "Code intelligence plugins"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Each plugin connects Claude Code to one language server over LSP. The plugin only says which command starts the server and which file extensions it handles; the binary must be installed separately. Claude then gets diagnostics after edits and a read-only `LSP` tool for symbol lookup instead of text search.

# How to use it

| Language | Plugin | Binary |
| :- | :- | :- |
| C/C++ | `clangd-lsp` | `clangd` |
| C# | `csharp-lsp` | `csharp-ls` |
| Go | `gopls-lsp` | `gopls` |
| Java | `jdtls-lsp` | `jdtls` |
| Kotlin | `kotlin-lsp` | `kotlin-lsp` |
| Liquid | `liquid-lsp` | `shopify` (Shopify CLI) |
| Lua | `lua-lsp` | `lua-language-server` |
| PHP | `php-lsp` | `intelephense` |
| Python | `pyright-lsp` | `pyright-langserver` |
| Ruby | `ruby-lsp` | `ruby-lsp` |
| Rust | `rust-analyzer-lsp` | `rust-analyzer` |
| Swift | `swift-lsp` | `sourcekit-lsp` |
| TypeScript and JavaScript | `typescript-lsp` | `typescript-language-server` |

Steps: (1) install the binary and confirm it is on the `PATH` of the shell that starts `claude` (TypeScript example: `npm install -g typescript-language-server typescript`); (2) `/plugin install typescript-lsp@claude-plugins-official` (replace with your plugin; the result says whether `/reload-plugins` is needed); (3) the server starts the first time Claude edits a matching file.

# Limits and defaults

- Works in terminal sessions. In cloud sessions Claude Code does not start plugin language servers, so there are no diagnostics or navigation.
- Anthropic maintains every plugin except `liquid-lsp` (Shopify maintains it; the official marketplace lists it).
- Diagnostics: after each edit or write of a handled file, Claude gets the errors and warnings. The conversation shows `Found N new diagnostic issues in M files (ctrl+o to expand)`; press Ctrl+O to read them.
- If none appears, open the **Errors** tab in `/plugin`; a row `Executable not found in $PATH: "<binary>"` names the missing binary. After installing it, Claude Code retries at the next matching edit; if the binary's directory is not on `PATH`, start a new session from a shell where it is.

# Notes

Troubleshooting topics: server not starting, high memory while indexing, and false-positive unresolved imports in a monorepo.
