---
type: "Feature"
title: "Approving a workflow launch"
description: "Per-mode approval prompt for workflows and how to allow them unattended in claude -p and the Agent SDK."
resource: "https://code.claude.com/docs/en/workflows"
tags: [workflows, permissions, headless, approval, unattended]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli, headless, sdk, desktop]
requires: ""
identifiers:
  - "Workflow"
  - "Workflow(<name>)"
  - "--permission-prompt-tool"
  - "canUseTool"
  - "PreToolUse"
  - "dontAsk"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "workflows"
    resource: "https://code.claude.com/docs/en/workflows"
    title: "Orchestrate subagents at scale with dynamic workflows"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The CLI prompt shows planned phases with options: Yes, run it; Yes, and don't ask again for `<name>` in `<path>` (offered only for bundled, saved or plugin workflows run by name, not a script written for the current task); View raw script; No. `Ctrl+G` opens the script in your editor; Tab on Yes/No adds a comment.

# How to use it

| Permission mode | When prompted |
| :- | :- |
| Auto | First launch only; any Yes records consent in user settings; skipped when ultracode is on |
| Manual, accept edits | Every run unless "don't ask again" chosen for that workflow in this project |
| Bypass permissions | Never; starts immediately |
| `claude -p`, Agent SDK | Never prompted |

In `claude -p` and the Agent SDK the `Workflow` tool call goes through normal permission evaluation (deny rules, ask rules, `dontAsk` apply). To let it start use any of:
- allow rule `Workflow` (all) or `Workflow(<name>)` (one saved workflow);
- auto permission mode (classifier can approve);
- bypass permissions mode;
- a `PreToolUse` hook returning `"allow"` (in plan mode the hook's approval alone does not start it; use a permission rule or host approval);
- a `--permission-prompt-tool` or SDK `canUseTool` callback.

# Limits and defaults

- Desktop app: an approval card with workflow name, phase list, token-usage caution and Once / Always / Deny.
- Spawned workflow subagents use your permission rules, and their mode follows the subagent permission-mode rules. Add needed tools to allow rules before a long run to avoid prompts.
