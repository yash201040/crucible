---
type: "Feature"
title: "Update and find artifacts"
description: "Republishing to the same URL, versions, updating from another session, one-step edits, and the /artifacts list and keys."
resource: "https://code.claude.com/docs/en/artifacts"
tags: [artifacts, versions, republish, artifacts-command]
kind: "mixed"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "/artifacts"
  - "CLAUDE_CODE_ARTIFACT_PUBLISH_EDITS"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "artifacts"
    resource: "https://code.claude.com/docs/en/artifacts"
    title: "Share session output as artifacts"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Claude edits the underlying file and publishes again to the same URL, either on request or as a long task makes progress. Anyone with the page open sees the update in place. Each publish becomes a version; the **Share** control in the page header chooses which version viewers see.

To update from a different session, give Claude the URL or attach it with `/artifacts`. Without either, a new session creates a new artifact.

# How to use it

`/artifacts` lists artifacts you own and those shared with you, with the current session's first under **This session**. It reads from your claude.ai account, so it works in a new session and after `/clear`. Keys on a selected artifact:

| Key | Effect |
| --- | --- |
| `Enter` | Opens it in the browser if attached to the current session, otherwise attaches it |
| `o` | Opens in the browser |
| `c` | Copies its link |
| `d` | Outside a cloud session, permanently deletes an artifact you own after confirmation; the link stops working for everyone |

One-step updates are small changes Claude makes to the artifact file as part of a publish instead of via `Edit` or `Write`. Turn them off with `CLAUDE_CODE_ARTIFACT_PUBLISH_EDITS=0` (for example in the `env` block of `~/.claude/settings.json`), then relaunch: a running session does not reread it.
