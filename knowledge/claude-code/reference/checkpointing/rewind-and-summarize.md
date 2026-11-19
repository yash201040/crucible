---
type: "Feature"
title: "Rewind menu and summarize actions"
description: "Open with /rewind or double Esc to restore code and/or conversation, or compress context with Summarize from here or up to here."
resource: "https://code.claude.com/docs/en/checkpointing"
tags: [rewind, summarize, context, sessions]
kind: "slash_command"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "/rewind"
  - "/undo"
  - "/clear"
  - "/resume"
  - "/branch"
  - "claude --continue --fork-session"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "checkpointing"
    resource: "https://code.claude.com/docs/en/checkpointing"
    title: "Checkpointing"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

The rewind menu lists the prompts you sent in the session. Select a point, then an action.

# How to use it

Open with `/rewind` or press `Esc` twice on an empty prompt (in vim mode, twice from NORMAL mode; outside vim mode, double `Esc` with text in the input clears it and saves it to input history, recall with `Up`).

| Action | Effect |
| :- | :- |
| Restore code and conversation | Revert both |
| Restore conversation | Rewind to that message, keep current code |
| Restore code | Revert file changes, keep conversation |
| Summarize from here | Compress conversation from this point forward, freeing context |
| Summarize up to here | Compress conversation before this point, later messages intact |
| Never mind | Back to the list |

- The two code options appear only if the selected checkpoint has tracked file changes; otherwise only Restore conversation, the summarize options and Never mind.
- After restoring the conversation or Summarize from here, the original prompt is restored into the input; Summarize up to here leaves the input empty. Either summarize shows a **Summarized conversation** marker.
- **Guide a summary**: highlight a Summarize option and type instructions at **add context (optional)**, then Enter; selecting by number key summarizes immediately with no instructions.
- **After `/clear`** in the same process, the top entry `/resume <session-id> (previous session)` resumes the pre-clear conversation, until you exit or resume another session.
- **Rewound messages can return if you exit before your next prompt**: send a prompt first (Claude Code saves the rewound conversation with it), or run `/rewind` again, select the same prompt, and choose Restore conversation. Restored files stay as the rewind left them.

# Notes

Summarizing does not change files and original messages stay in the transcript. It keeps the same session and works like a targeted `/compact`; to branch and keep the original intact use `/branch` or `claude --continue --fork-session`.
