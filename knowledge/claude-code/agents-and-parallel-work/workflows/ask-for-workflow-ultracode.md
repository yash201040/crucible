---
type: "Feature"
title: "Asking for a workflow and ultracode"
description: "Trigger workflows with the ultracode keyword, a direct request, or /effort ultracode for every substantive task."
resource: "https://code.claude.com/docs/en/workflows"
tags: [workflows, ultracode, effort, keyword]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.284"
surfaces: [cli, ide, desktop, sdk]
requires: "ultracode availability per model config"
identifiers:
  - "ultracode"
  - "/effort ultracode"
  - "/effort ultracode off"
  - "--effort ultracode"
  - "Option+W"
  - "Alt+W"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "workflows"
    resource: "https://code.claude.com/docs/en/workflows"
    title: "Orchestrate subagents at scale with dynamic workflows"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Two ways to have Claude write a workflow: ask in your prompt (include the keyword `ultracode`, or say "use a workflow" / "run a workflow"), or enable ultracode, a setting that makes Claude plan a workflow for each substantive task at whichever effort level the session runs. The keyword only changes how work is structured; agents' tool calls get the same permission checks and sandboxing.

# How to use it

- One task: `ultracode: audit every API endpoint under src/routes/ for missing auth checks`. The keyword is highlighted.
- Session: `/effort ultracode`; launch with `claude --effort ultracode` (also sets effort to `xhigh`); or flip the Ultracode toggle with Tab on the `/effort` slider then Enter. Persist with the `ultracode` setting. Turn off with `/effort ultracode off`.
- Dismiss the highlight: `Option+W` (macOS) / `Alt+W` (Windows, Linux), or backspace right after the keyword. Disable the trigger: turn off Ultracode keyword trigger in `/config`.

# Limits and defaults

- The keyword opts in only for a prompt you type yourself (interactive prompt, IDE panel, Remote Control client, or an Agent SDK app stamping input `origin` as `{ kind: "human" }`). It does not start a workflow from: a prompt passed with `-p`, an SDK prompt not stamped human, a scheduled task prompt, or a webhook payload or pull request comment relayed into the conversation.
- Ultracode: each request uses more tokens and time and draws on subscription usage limits sooner. While on: no `Large workflow` warning; the concurrent subagent limit is not enforced for Agent-tool subagents; in auto permission mode the first workflow launch is not prompted.
- Before v2.1.284, `/effort ultracode` set the session to `xhigh` and `/effort ultracode off` failed with `Invalid argument`.
