---
type: "Feature"
title: "PreToolUse hook event and decisions"
description: "Runs before a tool call; can allow, deny, ask or defer, rewrite input, and add context."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, pretooluse, permissions, tool-calls]
kind: "hook"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk]
requires: ""
identifiers:
  - "PreToolUse"
  - "tool_name"
  - "tool_input"
  - "tool_use_id"
  - "mcp_server"
  - "permissionDecision"
  - "permissionDecisionReason"
  - "updatedInput"
  - "additionalContext"
  - "allow"
  - "deny"
  - "ask"
  - "defer"
  - "CLAUDE_CODE_DISABLE_FILE_MENTIONS"
  - "EndConversation"
  - "SubagentHandback"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Runs after Claude creates tool parameters and before the tool call is processed. Matches any tool name except `EndConversation`: built-ins such as `Bash`, `PowerShell`, `Edit`, `Write`, `Read`, `Glob`, `Grep`, `Agent`, `Workflow`, `WebFetch`, `WebSearch`, `AskUserQuestion`, `ExitPlanMode`, and MCP tool names. It does not fire for `EndConversation`, nor for files referenced with `@` in a prompt (their contents are inserted without a tool call, so even `Read` hooks do not fire). To block paths from `@` use a `Read` deny rule, or set `CLAUDE_CODE_DISABLE_FILE_MENTIONS=1` (v2.1.299 or later; ignored in project and local settings; Claude then reads the paths with its tools so hooks run). To react to a file changing on disk use [FileChanged](./p2-filechanged-event.md).

# How to use it

Input adds `tool_name`, `tool_input`, `tool_use_id`. For MCP tools also `mcp_server` (object with `name` and `source`: `plugin`, `sdk`, or a scope such as `user`/`project`; v2.1.274 or later). Base trust on `source`, not on `name` or the `mcp__<server>__` prefix. Per-tool fields: [tool_input reference](./p2-pretooluse-tool-inputs.md).

File tools (`Write`, `Edit`, `Read`) always get absolute `file_path`; `~` and relative paths are expanded first. On Windows paths use backslashes, so normalize separators before comparing (`${FILE_PATH//\\//}` or `replace("\\", "/")`).

Decision goes in `hookSpecificOutput`:

| Field | Description |
| :- | :- |
| `permissionDecision` | `"allow"` skips the prompt (not for actions no mode auto-approves, network-path reads, SDK `always_ask` tools, MCP tools whose `_meta["anthropic/requiresUserInteraction"]` is set); `"deny"` blocks; `"ask"` prompts the user; `"defer"` ends the turn for later (needs `-p`). Deny and ask rules are still evaluated |
| `permissionDecisionReason` | For `ask`: shown to user; for `deny`: shown to Claude; for `allow`/`defer`: debug log only. In `-p` runs where a denial is automatic, Claude reads it in the tool result |
| `updatedInput` | Replaces the whole input object (include unchanged fields). Permission rules and Bash auto-background eligibility use the returned input. Ignored for `defer` |
| `additionalContext` | Added to Claude's context with the tool result; ignored for `defer` |

Precedence among hooks: `deny` > `defer` > `ask` > `allow`. Exit 2 acts like `"deny"` with stderr as the reason. The `ask` prompt is labelled `[settings]`, `[plugin:<name>]` or `[skill]`. Top-level `decision`/`reason` are deprecated for this event (`"approve"`/`"block"` map to `allow`/`deny`).

# Limits and defaults

- An Agent SDK callback hook on PreToolUse that exceeds its timeout blocks the tool call.
- Auto mode with `updatedInput` but no `permissionDecision`: the call may be denied with text "a hook changed this call's input after auto mode reviewed it"; Claude can reissue so the server reviews it; if repeated exactly, your hook still runs but any `updatedInput` is dropped. Command hooks in settings or a plugin's hooks file can change Bash, PowerShell, Monitor, Edit, Write and NotebookEdit calls without this denial in the sessions that show the text, though it can still appear (e.g. earlier call changed by a hook in the same response, or a Bash command asks to run outside the sandbox).
- Auto mode `"ask"` normally goes to the permission prompt without the classifier; calls Claude Code's own checks also flag (protected paths, outside-sandbox commands) can be denied by the classifier first. `SubagentHandback` calls show no prompt and run even if the classifier objects; return `"deny"` to stop one: Claude Code tells the subagent up to three times to retry, then the subagent ends without a report and the waiting conversation gets a note.
- To allow or rewrite a Monitor command see the Monitor matching section of the page.
