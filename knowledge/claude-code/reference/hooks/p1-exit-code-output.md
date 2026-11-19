---
type: "Concept"
title: "Exit codes and how output is read"
description: "Meaning of exit 0, 2 and other codes for hooks, how stdout is parsed as JSON or plain text, and per-event exceptions."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, exit-codes, stdout, json]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "exit 0"
  - "exit 2"
  - "continue"
  - "systemMessage"
  - "stdio went quiet"
  - "refusing to honor the suspect capture"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Exit code decides whether the triggering action continues.
- **0**: success; JSON fields apply; action goes ahead unless fields block or deny.
- **2**: blocking error on events that can block; message is the hook's stderr (or the reason in decision JSON).
- **Any other code** (or not starting, or invalid JSON): non-blocking error; action goes ahead (unless [onFailure "block"](./p1-onfailure-block-on-hook-failure.md)). A `<hook name> hook error` notice appears on events like `PreToolUse`. Exit 1 is NOT blocking: enforce policy with exit 2.

# How to use it

| Stdout | Exit 0 | Exit 2 | Other |
| :- | :- | :- | :- |
| JSON object passing validation | Fields apply | Blocking; fields still read, but a `PreToolUse` call stays blocked even with `"allow"` or `continue: false` | Success; fields alone decide |
| Unparseable or invalid JSON | Non-blocking error | Blocking; stderr is the reason | Non-blocking error |
| Plain text or nothing | Success | Blocking; stderr is reason | Non-blocking; first stderr line in notice |

Parsing rule for non-async hooks: stdout is JSON only when it is exactly one JSON object (one or many lines) with only whitespace around it. Output not starting with `{` or not ending with `}` is plain text (arrays and quoted strings are plain text). Multiple JSON lines are plain text unless one line is an output object that sets a field, which is then a parse failure. Anything else starting with `{` and ending with `}` that is invalid JSON is a parse failure.

Plain-text stdout reaches Claude as context on `UserPromptSubmit`, `UserPromptExpansion`, `SessionStart`, `PostModelSwitch`; on `PreCompact` it becomes compaction-summary instructions. Claude never sees stderr from an exit-0 hook; on `PostToolUse`/`PostToolUseFailure` exit 2 shows stderr to Claude.

Exit 2 with JSON: `continue: false` takes precedence on events like `Stop`/`SubagentStop` (ends the turn); other valid JSON is still read but even `"allow"` does not let the action through; invalid JSON still blocks with stderr as the reason. On `Elicitation`/`ElicitationResult` exit-2 `hookSpecificOutput` is ignored.

Per-event rules: `WorktreeCreate` any non-zero exit fails creation; `WorktreeRemove` any non-zero exit fails removal if the directory still exists; `Stop`, `SubagentStop`, `TaskCompleted` and a plugin's `UserPromptSubmit` treat exit 2 with empty stdout and a "No such file or directory" stderr as non-blocking; `Elicitation`/`ElicitationResult` apply `hookSpecificOutput` only on exit 0; events that discard output (e.g. `StopFailure`) ignore JSON on any code except side-effect fields like `terminalSequence`.

Example blocked output: `PreToolUse:Bash hook error: [<command>]: Blocked: rm commands are not allowed`. A missing script yields `Failed with non-blocking status code: /bin/sh: ... No such file or directory`.

# Limits and defaults

- Timeouts: a `command`/`http`/`mcp_tool` hook reaching `timeout` is canceled and its output discarded, so most events get no decision. A timed-out `PreToolUse` hook does not block the call (it continues through normal permission flow) unless `onFailure: "block"`. On `PreModelSwitch` a timed-out hook blocks the switch. An Agent SDK callback hook that times out blocks the tool call. Code Mode handles `PreToolUse` timeouts differently (see code-mode docs, "Tool call refused by a hook").
- Choose one approach per hook: exit codes alone, or exit 0 with JSON.
