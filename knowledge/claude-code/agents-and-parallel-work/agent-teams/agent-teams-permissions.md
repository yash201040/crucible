---
type: "Reference"
title: "Agent team permissions and inter-agent messages"
description: "How teammates inherit the lead's permission mode and rules, which CLI flags propagate to split-pane teammates, and how messages between agents are treated."
resource: "https://code.claude.com/docs/en/agent-teams"
tags: [agent-teams, permissions, auto-mode, flags]
kind: "behavior"
maturity: "experimental"
since: "2.1.317"
surfaces: [cli]
requires: "some split-pane behaviors need v2.1.309 or v2.1.317 or later"
identifiers:
  - "--dangerously-skip-permissions"
  - "--disallowedTools"
  - "--tools"
  - "--allowedTools"
  - "--settings"
  - "permissions.allow"
  - "bypassPermissions"
  - "dontAsk"
  - "acceptEdits"
  - "auto"
  - "SendMessage"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-teams"
    resource: "https://code.claude.com/docs/en/agent-teams"
    title: "Orchestrate teams of Claude Code sessions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Teammates start with the lead's permission mode; per-teammate modes cannot be set at spawn time.

# How to use it

- A new teammate starts with the lead's mode, including `bypassPermissions` (turned on by `--dangerously-skip-permissions`). If the lead is in `dontAsk` mode the teammate starts in Manual mode; for a split-pane teammate of a lead in Manual or `dontAsk` mode this needs v2.1.317 or later.
- Cycle a running teammate's mode with `Shift+Tab`: in its pane for split-pane, or while viewing its session for in-process (it checks the mode at its next turn).
- An in-process teammate not in plan mode runs in the lead's mode while the lead is in `acceptEdits`, `auto` or `bypassPermissions`; switching the teammate to Manual does not change that even if the status bar shows Manual. To make it ask before edits, switch the lead to Manual too (Enter on the `main` row in the agent panel).
- Teammate permission prompts appear in the lead session. You need not approve a teammate's plan.
- An in-process teammate runs under the lead's live allow and deny rules, so `--disallowedTools`, `--tools` and `--allowedTools` all apply.

Split-pane flag propagation:

| Flag | Behavior |
| - | - |
| `--disallowedTools`, `--tools` | teammate starts with the lead's command-line deny rules and tool list; v2.1.309 or later |
| `--allowedTools` | not passed; an action allowed only with it is not pre-approved. Instead put rules under `permissions.allow` in `--settings`, for example `claude --settings '{"permissions":{"allow":["Bash(npm *)"]}}'`; they apply to the lead and each split-pane teammate for that session |

# Limits and defaults

Messages over `SendMessage` are tagged as coming from another Claude session, not from you: a teammate cannot approve a prompt or give consent on your behalf, and a denied teammate cannot relay the action to another to bypass the check. The same applies to messages from your other Claude Code sessions. In auto mode the classifier treats relayed approval claims as untrusted input and reviews messages before delivery, including protocol messages such as shutdown requests; a blocked message is not delivered (some messages skip the review, see the permission-modes classifier section).
