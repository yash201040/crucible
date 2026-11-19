---
type: "Feature"
title: "Comments and automatic replies"
description: "Claude reads and replies to comment threads on a shared artifact and, from v2.1.228, is notified and replies on its own within caps."
resource: "https://code.claude.com/docs/en/artifacts"
tags: [artifacts, comments, watch, tasks]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.221"
surfaces: [cli]
requires: "Artifact shared within the organization; Claude Code v2.1.221+ to read comments, v2.1.228+ for automatic replies"
identifiers:
  - "/tasks"
  - "Send to Claude"
  - "@claude"
  - "Ctrl+X Ctrl+K"
  - "Auto-replied to comment thread on Artifact: <name>"
  - "Comments are waiting on Artifact: <name>"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "artifacts"
    resource: "https://code.claude.com/docs/en/artifacts"
    title: "Share session output as artifacts"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

People an artifact is shared with inside the organization can comment on the page. Claude reads comments when you ask (give it the URL) or when someone who can edit the artifact sends a thread with **Send to Claude** or mentions `@claude`; that activates the thread. Claude can reply to or resolve only an activated thread. Replies are attributed to Claude via you. Public-link-only viewers neither see nor add comments; existing threads remain for you and editors.

# How to use it

After your session publishes an artifact, Claude Code watches it. A sent comment reaches the session immediately (v2.1.228+; off if feature-flag fetching is off). Behavior follows your permission mode:

- Replies on its own when the mode lets it post: shows `Auto-replied to comment thread on Artifact: <name>`.
- Waits for you outside plan mode when posting needs approval: `Comments are waiting on Artifact: <name>`, then asks to read and to post.
- Pauses in plan mode with the same waiting message.

`/tasks` shows watches: the ones Claude Code started appear under **System tasks** (Enter lists them); ones you asked for appear under **Monitors**.

# Limits and defaults

- Auto replies stop for an artifact after 60 sent comments or thread activations within an hour (message shown once; resumes as they age out).
- Stop replies: Ctrl+C once at an idle empty prompt (pauses all watched artifacts until your next message); stop the task in `/tasks` (persists, even on resume, and republishing does not restart it); press `Ctrl+X Ctrl+K` twice within 3 seconds (also stops every background subagent; stops replies for the rest of the session and cannot be undone by asking).
- A self-started watch can end after several hours without activity; republish or ask Claude to watch again. If the comment service is unavailable Claude Code retries for a while, then stops watching.
- If Claude cannot read comments: check version 2.1.221+, that it is not your first session after install or upgrade, and that feature-flag fetching is not off.
