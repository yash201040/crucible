---
type: "Concept"
title: "Precedence of hooks, rules and mods"
description: "PreToolUse hooks cannot override deny or ask rules, a blocking hook beats allow rules, and mods can approve more in unmanaged setups."
resource: "https://code.claude.com/docs/en/permissions"
tags: [permissions, hooks, pretooluse, mods, precedence]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.292"
surfaces: [cli, sdk]
requires: ""
identifiers:
  - "PreToolUse"
  - "tool.check"
  - "--permission-prompt-tool"
  - "canUseTool"
  - "requiresUserInteraction"
  - "CLAUDE_CODE_OAUTH_TOKEN"
  - "ExitPlanMode"
  - "updatedInput"
  - "EndConversation"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permissions"
    resource: "https://code.claude.com/docs/en/permissions"
    title: "Configure permissions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

PreToolUse hooks run before the permission prompt for every tool except `EndConversation`. A hook can deny a call, force a prompt, or skip the prompt, but its decision never bypasses rules.

# How to use it

- Deny and ask rules are evaluated regardless of the hook: a matching deny blocks, a matching ask still prompts even if the hook returned `"allow"` or `"ask"` (managed-settings deny rules included).
- A hook that exits with code 2 stops the call before rules are evaluated, so the block applies even if an allow rule matches. To allow all Bash except a few commands: allow `"Bash"` and register a PreToolUse hook that rejects those commands.
- A mod handling the `tool.check` event answers after PreToolUse hooks run. With managed settings, a `managed-mcp.json` file, or a Team/Enterprise `/login` credential, the built-in guard loads by default and these hold when a non-organization mod approves: deny stays refused; ask rules still prompt; a call a PreToolUse hook or `permissions.blockReadsOutsideWorkingDirectories` would prompt for still prompts; a call a PreToolUse hook blocked stays blocked; calls going to `--permission-prompt-tool` or the SDK `canUseTool` callback still go there.
- Without those, a mod can approve a call a PreToolUse hook blocked and some denied calls, and skip ask prompts, hook prompts, the blockReads prompt and the prompt tool or callback. Extra outcomes: auto mode may run without classifier check; plan mode, the mod cannot approve non-read-only calls; `dontAsk`, the mod can approve a call only the mode would deny. A session on an API key or long-lived `CLAUDE_CODE_OAUTH_TOKEN` is not using the login.
- Tools requiring user interaction (`AskUserQuestion`, MCP tools marked `requiresUserInteraction`) still prompt despite a mod's approval (v2.1.292+), a hook `"allow"`, network-path reads, and connector tools your organization set to `ask`.

# Notes

Plan mode: except `ExitPlanMode`, a PreToolUse `"allow"` has no effect on a file edit or other non-read-only call (same prompt/block/approval as without the hook; `updatedInput` is still applied). If the hook answers `ExitPlanMode` with `"allow"` and `updatedInput`, it runs without a prompt. A plan-mode mod cannot approve such calls but can block them. Approve the plan or switch mode to lift this.
