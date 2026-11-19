---
type: "Feature"
title: "Use Claude Code as an MCP server"
description: "claude mcp serve exposes Claude Code's tools over stdio; Claude Desktop config and reading backgroundOutputPath."
resource: "https://code.claude.com/docs/en/mcp"
tags: [mcp, serve, stdio, background]
kind: "cli_flag"
maturity: "unlabelled"
since: "2.1.295"
surfaces: [cli]
requires: ""
identifiers:
  - "claude mcp serve"
  - "backgroundOutputPath"
  - "run_in_background"
  - "spawn claude ENOENT"
  - "Read"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "mcp"
    resource: "https://code.claude.com/docs/en/mcp"
    title: "Connect Claude Code to tools via MCP"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`claude mcp serve` starts Claude Code as a stdio MCP server for other applications. It prints nothing; a silent blocked terminal means it is waiting for a client.

# How to use it

Claude Desktop config: `{"mcpServers":{"claude-code":{"type":"stdio","command":"claude","args":["mcp","serve"],"env":{}}}}`. If `claude` is not on PATH use the full path (`which claude`), otherwise you get `spawn claude ENOENT`.

Background commands: a `backgroundOutputPath` field in a Bash or PowerShell result (in the result's JSON text, v2.1.295 or later) means the command is running in the background (client set `run_in_background: true`, or a foreground command hit its timeout). To read output so far, open the file or pass it as `file_path` to the server's `Read` tool. To detect completion, append an `echo` of a fixed string (`npm test; echo DONE`) and look for it; Claude Code adds no closing line and sends no notification. To read the end of a long file: `Read` with `offset` and `limit` both 1 to get `totalLines`, then `offset` = `totalLines` minus 9, `limit` 10.

# Notes

The server exposes only Claude Code's tools; the client must implement user confirmation for each tool call.
