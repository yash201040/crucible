---
type: "Guide"
title: "High CPU, memory, hangs and compaction thrashing"
description: "How to reduce resource use, the 2.5GB memory warning, /heapdump output, and recovering from Autocompact thrashing."
resource: "https://code.claude.com/docs/en/troubleshooting"
tags: [memory, performance, compaction, heapdump, diagnostics]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.208"
surfaces: [cli]
requires: ""
identifiers:
  - "/compact"
  - "/clear"
  - "/context"
  - "/heapdump"
  - "/doctor"
  - "/mcp"
  - "/feedback"
  - "claude --safe-mode"
  - "claude --continue"
  - "claude --resume"
  - "claude doctor"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "troubleshooting"
    resource: "https://code.claude.com/docs/en/troubleshooting"
    title: "Troubleshooting"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Troubleshooting for resource usage and stability once Claude Code runs. The page also routes other symptoms to the right page (install, debug-your-config, permission modes, errors reference, VS Code, JetBrains). `/doctor` checks installation, settings, extensions and context usage and proposes fixes after confirmation; if `claude` will not start, run `claude doctor` from the shell; `/mcp` shows MCP server status.

# How to use it

- High CPU or memory: `/compact` regularly (it can return `Not enough messages to compact.` when one big paste filled context), restart between big tasks, add large build dirs to `.gitignore`, or restart with `claude --safe-mode` to test whether a plugin, MCP server or hook is the cause.
- If heap memory passes 2.5GB a critical memory warning appears; restart and run `claude --continue` to resume in a fresh process. Outside fullscreen rendering `/compact` also frees memory. The warning clears below 2.5GB.
- `/heapdump` (hidden from the command menu, type in full) writes `<session-id>.heapsnapshot` and `<session-id>-diagnostics.json` to `~/Desktop` (home directory on Linux without a Desktop folder) and prints a summary with leak indicators. The `.heapsnapshot` contains every string in the process including conversation and credentials: never share it; attach only the `-diagnostics.json` to a GitHub issue.
- Autocompact thrashing: error `Autocompact is thrashing: the context refilled to the limit...` means compaction succeeded but a file or tool output refilled the window several times in a row, so Claude Code stops retrying. Recover by reading big files in chunks, `/compact keep only the plan and the diff` style focus, moving large-file work to a subagent, or `/clear`. If it recurs after `/clear`, use `/context` and compare the `Messages` row with the others.
- Hang: Ctrl+C; restarting keeps the conversation, resume with `claude --resume` in the same directory.

# Limits and defaults

- Markdown tables over 200 rows render only the first 200 plus `… N more rows not shown`; `/copy` copies every row. Before v2.1.208 every row was rendered and resuming such a session could stall.
- Critical memory warning threshold: 2.5GB heap.

# Notes

Subagents give a separate context window, which the page offers as the escape from thrashing.
