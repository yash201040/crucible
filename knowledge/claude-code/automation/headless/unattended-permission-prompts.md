---
type: "Feature"
title: "--permission-prompts none for unattended runs"
description: "Deny anything that would prompt, never wait on a permission host; needs v2.1.259 or later."
resource: "https://code.claude.com/docs/en/headless"
tags: [headless, permissions, unattended, scheduled]
kind: "cli_flag"
maturity: "unlabelled"
since: "2.1.259"
surfaces: [headless, sdk]
requires: "Claude Code v2.1.259+ (earlier versions reject it as an unknown option)"
identifiers:
  - "--permission-prompts none"
  - "permissions.denyInsteadOfPrompting"
  - "canUseTool"
  - "--permission-prompt-tool"
  - "AskUserQuestion"
  - "Elicitation"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "headless"
    resource: "https://code.claude.com/docs/en/headless"
    title: "Run Claude Code programmatically"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Pass `--permission-prompts none` when nobody can answer permission prompts, such as a scheduled job. It matters most when the run has a permission host: an Agent SDK app with a `canUseTool` callback, or an MCP tool via `--permission-prompt-tool`. Without the flag or the `permissions.denyInsteadOfPrompting` setting, the run waits for the host on each permission request.

# How to use it

`claude -p "Update the dependency pins and run the tests" --permission-mode auto --permission-prompts none`

With the flag the run does not consult or wait on the host. Anything that would prompt is denied unless a `PermissionRequest` hook allows it; Claude is told nobody can approve and not to retry; the run continues. Permission rules, `PermissionRequest` hooks and the permission mode still decide every call first. Tools needing a person, such as `AskUserQuestion`, are removed so Claude cannot call them, and any MCP elicitation request no `Elicitation` hook answers is cancelled. In a `-p` run with no host these requests are denied anyway; the flag adds the do-not-retry message.

# Limits and defaults

The flag lasts one run. To make later runs deny instead of prompting, set `permissions.denyInsteadOfPrompting` to `true` in user or managed settings. With `stream-json`, denials appear as `permission_denied` messages and in `permission_denials`.
