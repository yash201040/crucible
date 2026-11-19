---
type: "Reference"
title: "Display, debug and version flags"
description: "Flags for screen-reader output, debug logging to category or file, and printing the version."
resource: "https://code.claude.com/docs/en/cli-reference"
tags: [debug, accessibility, logging]
kind: "cli_flag"
maturity: "unlabelled"
since: "2.1.181"
surfaces: [cli]
requires: ""
identifiers:
  - "--ax-screen-reader"
  - "CLAUDE_AX_SCREEN_READER"
  - "axScreenReader"
  - "--debug"
  - "--debug-file"
  - "CLAUDE_CODE_DEBUG_LOGS_DIR"
  - "--version"
  - "-v"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "cli-reference"
    resource: "https://code.claude.com/docs/en/cli-reference"
    title: "CLI reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Flags for output rendering and diagnostics.

# How to use it

| Flag | Version | What it does |
| :- | :- | :- |
| `--ax-screen-reader` | v2.1.181+ | Flat, screen-reader friendly output without borders or animations; forces the classic renderer so the `tui` setting has no effect (attached background sessions still render fullscreen). Beats `CLAUDE_AX_SCREEN_READER` and the `axScreenReader` setting |
| `--debug` | | Debug mode with optional category filter: `--debug='mcp,startup'`, `--debug='!mcp'`. The filter binds only in the `=` form |
| `--debug-file <path>` | | Write debug logs to a file; implies debug mode; beats `CLAUDE_CODE_DEBUG_LOGS_DIR` |
| `--version`, `-v` | | Print the version |
