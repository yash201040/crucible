---
type: "Reference"
title: "Tools: files, shell, web, plan and MCP"
description: "Built-in tool names for file access, shell, web, worktrees, plan mode, MCP resources and code intelligence, with permission needs."
resource: "https://code.claude.com/docs/en/tools-reference"
tags: [tools, files, shell, web, mcp]
kind: "tool"
maturity: "unlabelled"
since: ""
surfaces: [cli, sdk]
requires: ""
identifiers:
  - "AskUserQuestion"
  - "Bash"
  - "Edit"
  - "EndConversation"
  - "EnterPlanMode"
  - "ExitPlanMode"
  - "EnterWorktree"
  - "ExitWorktree"
  - "Glob"
  - "Grep"
  - "ListMcpResourcesTool"
  - "ReadMcpResourceTool"
  - "LSP"
  - "Monitor"
  - "NotebookEdit"
  - "PowerShell"
  - "Read"
  - "WebFetch"
  - "WebSearch"
  - "Write"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "tools-reference"
    resource: "https://code.claude.com/docs/en/tools-reference"
    title: "Tools reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The remaining rows of the tools table. In auto mode a classifier decides most permission prompts; the Permission column shows Manual-mode behavior for paths inside the working directory. Tools marked No (`Read`, `Grep`, `Glob`) still prompt for paths outside the working directories. `Bash` runs a built-in set of read-only commands without prompting.

# How to use it

| Tool | Permission | What it does |
| :- | :- | :- |
| `AskUserQuestion` | No | Multiple-choice questions to the user. See [AskUserQuestion](./askuserquestion-tool.md). |
| `Bash` | Yes | Runs shell commands. See [Bash behavior](./bash-working-directory-and-env.md). |
| `Edit` | Yes | Exact string replacement. See [Edit](./edit-tool-behavior.md). |
| `EndConversation` | No | Ends the session in rare cases. See [EndConversation](./endconversation-tool.md). |
| `EnterPlanMode` | No | Switches to plan mode. |
| `ExitPlanMode` | Yes | Presents a plan for approval and exits plan mode. |
| `EnterWorktree` | Yes | Creates or enters a git worktree. See [EnterWorktree](./enterworktree-tool.md). |
| `ExitWorktree` | No | Exits a worktree session. Not available to subagents already in their own working directory (such as `isolation: worktree`). Removed or refused once `permissions.blockWritesOutsideWorkingDirectories` is on. |
| `Glob`, `Grep` | No | File-name and content search; absent by default on macOS, Linux, WSL. See [Glob and Grep](./glob-and-grep-tools.md). |
| `ListMcpResourcesTool` | No | Lists MCP server resources, leaving out MCP Apps UI resources. |
| `ReadMcpResourceTool` | No | Reads an MCP resource by URI. |
| `LSP` | No | Language-server code intelligence. See [LSP](./lsp-tool.md). |
| `Monitor` | Yes | Runs a background command (or WebSocket) and feeds each event to Claude. See [Monitor](./monitor-tool.md). |
| `NotebookEdit` | Yes | Edits Jupyter cells. See [NotebookEdit](./notebookedit-tool.md). |
| `PowerShell` | Yes | Native PowerShell. See [PowerShell tool](./powershell-tool.md). |
| `Read` | No | Reads files. See [Read](./read-tool-behavior.md). |
| `WebFetch` | Yes | Fetches a URL. See [WebFetch](./webfetch-tool.md). |
| `WebSearch` | Yes | Web search. See [WebSearch](./websearch-tool.md). |
| `Write` | Yes | Creates or overwrites files. See [Write](./write-tool-behavior.md). |

Skills run through the existing `Skill` tool rather than adding tool entries; custom tools come from MCP servers. Ask Claude "What tools do you have access to?" to check the loaded set, or `/mcp` for exact MCP tool names. The exact tool set depends on provider, platform and settings.
