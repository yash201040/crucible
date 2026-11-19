---
type: "Reference"
title: "claude import and MCP management errors"
description: "Errors from claude import, claude mcp add/add-json/remove/add-from-claude-desktop, .mcp.json reads, managed scope and plugin-only restrictions."
resource: "https://code.claude.com/docs/en/errors"
tags: [errors, mcp, import, managed-settings]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "claude import"
  - "/import"
  - "claude mcp add"
  - "claude mcp add-json"
  - "claude mcp remove"
  - "claude mcp get"
  - "claude mcp list"
  - "claude mcp add-from-claude-desktop"
  - "--scope managed"
  - "managedMcpServers"
  - "strictPluginOnlyCustomization"
  - ".mcp.json"
  - "DISABLE_TELEMETRY"
  - "DO_NOT_TRACK"
  - "CLAUDE_CODE_DISABLE_FEATURE_FLAGS"
  - "DISABLE_GROWTHBOOK"
  - "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "errors"
    resource: "https://code.claude.com/docs/en/errors"
    title: "Error reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Failures of the commands that configure MCP servers or import configuration.

# How to use it

| Message | Cause | Fix |
|---|---|---|
| `claude import is not yet available in this build` (exit 1; before v2.1.222 it started a session) | Import is behind a cached feature flag that is off: fresh install not yet fetched; Bedrock, Google Cloud Agent Platform, Microsoft Foundry, Claude Platform on AWS or a Claude apps gateway never fetch flags; or flag fetching disabled by `DISABLE_TELEMETRY`, `DO_NOT_TRACK`, `CLAUDE_CODE_DISABLE_FEATURE_FLAGS`, `DISABLE_GROWTHBOOK`, `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` | Start `claude` once, exit, retry; otherwise use `claude mcp add` and create CLAUDE.md, skills, subagents by hand |
| `Could not read Claude Code config` | `claude import` with unparseable `~/.claude.json`; exit 1 (before v2.1.222 it opened an interactive recovery) | Run `claude` with no arguments to recover |
| `Could not import <name>: Invalid name ...` | `claude mcp add-from-claude-desktop`: Desktop allows spaces/periods; `claude mcp` allows only letters, numbers, hyphens, underscores. Other servers still import (since v2.1.205; before, first failure stopped it) | Rename in `claude_desktop_config.json` or use `claude mcp add`/`add-json` |
| `Cannot add MCP server to scope: managed` | `--scope managed` is read-only from the `managedMcpServers` managed setting | Use `local` (default), `user` or `project` |
| `Cannot add MCP server: your organization's managed settings allow only MCP servers that plugins provide` | `strictPluginOnlyCustomization` is `true` or includes `mcp`; exit 1 (before v2.1.284 it saved and reported success). `/import` reports it per server | Install a plugin providing the server, or ask the admin |
| `Can't read .mcp.json: it isn't a regular file or is larger than 2097152 bytes` | Project-scope read of `.mcp.json` (2 MiB cap; before v2.1.257 a FIFO hung and `/dev/zero` grew memory) | Replace with an ordinary JSON file or delete |
| `MCP server "x" was not saved/removed` / `may not have been saved` | See [startup and config file errors](./p3-startup-and-config-file-errors.md) | `claude mcp get <name>` to check |

# Limits and defaults

- `.mcp.json` read limit: 2,097,152 bytes.

# Notes

None of the `claude import` carried configuration except the permission mode lives in `~/.claude/settings.json`; the docs state Claude Code does not read MCP servers from that file.
