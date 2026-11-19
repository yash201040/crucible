---
type: "Reference"
title: "When publishing asks for approval"
description: "The cases in which Claude Code asks you, or the auto-mode classifier, before publishing or changing an artifact."
resource: "https://code.claude.com/docs/en/artifacts"
tags: [artifacts, permissions, plan-mode, auto-mode]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "Artifact"
  - "--add-dir"
  - "/add-dir"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "artifacts"
    resource: "https://code.claude.com/docs/en/artifacts"
    title: "Share session output as artifacts"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

A new artifact Claude publishes in response to a prompt you type goes through with no permission prompt or classifier review. In the cases below Claude Code asks you first, or in auto mode has the classifier review the publish.

# How to use it

| When | What Claude Code does |
| --- | --- |
| Session is in plan mode | Asks before the first publish of each artifact |
| Publish declares runtime capabilities (connector calls, file downloads) | Asks before that publish |
| Artifact was shared publicly | Asks at least once per conversation before changing it, and before each reply to a comment |
| Publish happens in a turn started by a session-scoped scheduled task, not a typed prompt | Asks before the first publish of each artifact |
| Claude cannot read the file without approval | Asks before publishing; an allow rule for the `Artifact` tool does not skip this |
| Manual or `acceptEdits` mode, small change to an artifact file it cannot edit unapproved (e.g. a project file in Manual mode) | Asks before publishing; asked even with an allow rule on `Artifact` |

To let Claude read a file outside your working directories without approval, add its folder with `--add-dir` at launch or `/add-dir` in the session. Files in working directories and in the temporary directory it writes pages to are read without asking.

# Notes

A publish prompt that says `Also makes 1 edit to that file on disk.` means Claude changes the artifact file and publishes in one step: approving publishes the page, then writes the change to your file.
