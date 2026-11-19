---
type: "Feature"
title: "Comment on a permission prompt"
description: "Attach a note to Claude when approving or denying a single action with Tab in the prompt."
resource: "https://code.claude.com/docs/en/permissions"
tags: [permissions, prompts, comments, interactive]
kind: "ui"
maturity: "unlabelled"
since: "2.1.235"
surfaces: [cli]
requires: ""
identifiers: []
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permissions"
    resource: "https://code.claude.com/docs/en/permissions"
    title: "Configure permissions"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

On most permission prompts (Bash, PowerShell, file, MCP), move to Yes or No and press `Tab` to open a comment field on that option. WebFetch and browser prompts have no field, and neither do the options that allow for the rest of the session or save a rule.

# How to use it

| Key in the field | Effect |
| :- | :- |
| `Enter` | Submit the answer with the comment (empty field submits no comment) |
| `Tab` | Close the field without answering; press `Tab` again before answering to send the text |
| `Shift+Tab` | On a file prompt (Edit/Write), same as `Tab` |

Delivery: Yes runs the action, then sends the comment to Claude after the result. No sends the comment as the denial reason and Claude keeps working. No without a comment on a main-conversation prompt stops the turn.

# Notes

Before v2.1.235, `Shift+Tab` inside the field chose the option that allows the action for the rest of the session and discarded the comment.
