---
type: "Feature"
title: "permissions.denyInsteadOfPrompting"
description: "Makes a session with no human present deny calls that would prompt, so the turn continues; also removes question and plan tools and cancels elicitations."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [permissions, unattended, headless, automation]
kind: "setting"
maturity: "unlabelled"
since: "2.1.319"
surfaces: [cli, headless, sdk, ide, desktop]
requires: "v2.1.319"
identifiers:
  - "permissions.denyInsteadOfPrompting"
  - "--permission-prompts none"
  - "AskUserQuestion"
  - "EnterPlanMode"
  - "ExitPlanMode"
  - "canUseTool"
  - "--permission-prompt-tool"
  - "PermissionRequest"
  - "Elicitation"
  - "permission_denied"
  - "error_during_execution"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A Boolean that keeps a session running when nobody can answer a permission prompt. Claude Code denies a tool call that would otherwise wait on a prompt and the turn continues.

# How to use it

Scope: `User or managed`, and `--settings`; a repository cannot set it. Default unset. `false` equals unset, but calls are still denied if another source sets `true`. Applies in `-p` runs, interactive terminals, VS Code, local Desktop sessions, subagents and agent teams.

```json
{ "permissions": { "defaultMode": "auto", "denyInsteadOfPrompting": true } }
```

A call still goes ahead if an allow rule, the permission mode, or the auto-mode classifier approves it. To approve calls from code, answer from a `PermissionRequest` hook. For a single non-interactive run use `--permission-prompts none` with `-p`.

# Limits and defaults

Also stopped when the setting is on:
- Tools `AskUserQuestion`, `EnterPlanMode`, `ExitPlanMode` are left out, so a plan-mode session cannot leave plan mode on its own (agent-team teammates keep the two plan tools).
- MCP elicitation requests are cancelled unless an `Elicitation` hook answers.
- The `canUseTool` callback and `--permission-prompt-tool` are not asked. Some calls are denied before any hook is asked (such as a critical-path removal in `auto` mode with no ask rule).
- The classifier-billing notice dialog is not shown and the actions needing those requests are denied.

A session can still wait on the workspace trust dialog and on project MCP server approval; answer both beforehand.

Messages: the denial text starts `Permission for this tool use was denied. It requires approval, and this session has no approval surface`; in `stream-json` output `permission_denied` messages carry `decision_reason` `no approval surface in this session; permission request denied automatically`. In auto mode the turn ends after 20 consecutive refused calls with `20 actions were refused and no work went ahead in between, so Claude stopped.`, reported by a `-p` run as `error_during_execution`.
