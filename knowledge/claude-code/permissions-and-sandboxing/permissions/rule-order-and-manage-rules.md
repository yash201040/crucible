---
type: "Concept"
title: "Allow, ask and deny rules and their order"
description: "Rules are evaluated deny, then ask, then allow; /permissions edits them live and a bare tool-name deny removes the tool."
resource: "https://code.claude.com/docs/en/permissions"
tags: [permissions, deny-rules, precedence, slash-permissions]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.234"
surfaces: [cli]
requires: ""
identifiers:
  - "/permissions"
  - "permissions.allow"
  - "permissions.ask"
  - "permissions.deny"
  - "--disallowedTools"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permissions"
    resource: "https://code.claude.com/docs/en/permissions"
    title: "Configure permissions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`/permissions` lists every rule and the settings file it comes from. Allow rules let a tool run without approval, ask rules prompt, deny rules block. Evaluation order is deny, then ask, then allow; the first match decides and specificity does not change the order.

# How to use it

- A broad deny such as `Bash(aws *)` blocks every matching call even if `Bash(aws s3 ls)` is allowed. An allow cannot carve an exception out of a deny. The same holds between ask and allow: a matching ask prompts even if a narrower allow matches.
- A bare tool name deny (for example `Bash`) removes the tool from Claude's context. Adding it mid-session makes the tool uncallable from the next tool call. A scoped deny such as `Bash(rm *)` keeps the tool and blocks matching calls.
- Bare-name removal applies to every tool except `EndConversation`: a deny cannot remove it while any other tool remains, and an ask never prompts for it.
- The dialog can be opened while Claude works; added or removed rules apply from Claude's next tool call in the same turn. Before v2.1.234 the command was queued until the turn ended.
- With auto mode available, the dialog has an Auto mode tab showing classifier rules.

# Notes

Rules are enforced by Claude Code, not the model. Prompts or `CLAUDE.md` text shape what Claude tries but do not change rules. To grant or revoke access use `/permissions`, rules, a permission mode, or a PreToolUse hook.
