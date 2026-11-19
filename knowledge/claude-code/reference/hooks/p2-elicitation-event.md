---
type: "Feature"
title: "Elicitation hook event"
description: "Intercepts an MCP server's mid-task input request so a hook can accept, decline or cancel without a dialog."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, mcp, elicitation, unattended]
kind: "hook"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "Elicitation"
  - "mcp_server_name"
  - "message"
  - "mode"
  - "url"
  - "elicitation_id"
  - "requested_schema"
  - "action"
  - "accept"
  - "decline"
  - "cancel"
  - "content"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Runs when an MCP server requests user input mid-task. By default a dialog is shown; hooks can answer programmatically and skip it. The matcher matches the MCP server name.

# How to use it

Input adds `mcp_server_name`, `message`, and optional `mode` (`form` or `url`), `url`, `elicitation_id`, `requested_schema` (JSON schema; form mode).

Exit 0 and print `hookSpecificOutput` with `hookEventName: "Elicitation"` and an `action`:

| To | Return | Server receives |
| :- | :- | :- |
| Answer for the user | `"action": "accept"` with form values in `content` (keys = `requested_schema` property names) | `accept` with your `content` |
| Decline | `"action": "decline"` | `decline` |
| Cancel | `"action": "cancel"` | `cancel` |
| Leave to the user | No output, exit 0 | The dialog answer |

Other ways to decline (server gets `decline`): exit code 2 (a `hookSpecificOutput` from the same hook is ignored); top-level `"decision": "block"` (overrides an `action` in the same output). When several hooks match, a decline overrides an `accept` or `cancel`.

Example: matcher `issue-tracker`; a script that reads `requested_schema.properties` keys and, if they equal `["project_key"]`, prints an `accept` with `content: {project_key: "DOCS"}`, otherwise prints nothing. Verify with `claude --debug`: the log shows `Elicitation resolved by hook:` and `accept`.

# Limits and defaults

- For a URL-mode request an `accept` skips the dialog, so the URL never opens.
- `reason`, `systemMessage` and `continue` are discarded whichever `action` is returned. Neither the user nor the server sees why a hook declined (stderr and `reason` are not shown).
- Claude Code ignored a top-level `decision` from `Elicitation` and `ElicitationResult` hooks from v2.1.105 until the fix in v2.1.284.
