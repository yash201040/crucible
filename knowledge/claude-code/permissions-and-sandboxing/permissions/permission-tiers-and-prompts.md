---
type: "Concept"
title: "Permission tiers and approval prompts"
description: "Which tool types ask for approval in Manual mode and where a 'Yes, and don't ask again' answer is saved."
resource: "https://code.claude.com/docs/en/permissions"
tags: [permissions, prompts, approval, settings-local]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - ".claude/settings.local.json"
  - "/permissions"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permissions"
    resource: "https://code.claude.com/docs/en/permissions"
    title: "Configure permissions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude Code uses a tiered permission system. The table says whether Manual mode asks before each tool type runs. Other permission modes change which calls ask; in auto mode a classifier reviews actions instead of the user.

# How to use it

| Tool type | Example | Approval required | "Yes, and don't ask again" lasts |
| :- | :- | :- | :- |
| Read-only | File reads, Grep | No, inside the working directory and additional directories | N/A |
| Bash commands | Shell execution | Yes, except a built-in set of read-only commands | Permanently per repository and command |
| File modification | Edit/write files | Yes | Until session end |
| Web fetch | WebFetch | Yes, except preapproved documentation domains | Permanently per repository and domain |
| Web search | WebSearch | Yes | Permanently per repository |

A permanent approval is saved as a rule in `.claude/settings.local.json` at the git repository root, resolved through worktrees to the main checkout. It applies to later sessions anywhere in that repository, including subdirectories and worktrees. A file-modification approval is not saved to the file. Outside a git repository, or on Windows, the repository root is not used and the rule is saved elsewhere (see the settings docs).

# Notes

- Some prompts offer only a one-time approval. "Don't ask again" and session-wide options appear only when the prompt can show everything they would allow. To stop such prompts, add the rule yourself in `/permissions`.
- The third option, "Yes, and switch to auto mode", does not appear on every prompt.
- See [exec wrappers and find actions](./exec-wrappers-and-find-actions.md) for commands that only ever get one-time approval.
