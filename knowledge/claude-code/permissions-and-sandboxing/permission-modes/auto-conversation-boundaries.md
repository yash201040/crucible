---
type: "Concept"
title: "Boundaries and approvals in conversation"
description: "How the classifier treats user-stated boundaries as blocks and stated approvals as clearing a block, and their limits."
resource: "https://code.claude.com/docs/en/permission-modes"
tags: [auto-mode, classifier, boundaries, approvals, compaction]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "autoMode.allow"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permission-modes"
    resource: "https://code.claude.com/docs/en/permission-modes"
    title: "Choose a permission mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Boundaries: something like "don't push" or "wait until I review before deploying" is a block signal; the classifier blocks matching actions it reviews even if default rules allow them, until the user lifts it in a later message. Claude's own judgment that a condition was met does not lift it. Boundaries are not stored as rules: the classifier re-reads the transcript each check, so context compaction that removes the message can lose a boundary. For a hard guarantee use a deny rule.

Approvals: telling Claude a blocked action is allowed can clear the block.

# How to use it

- Name the action and its specifics (for a force push, the branch); naming only the verb may leave the block.
- An approval covers the one action named unless granted as standing; for routine patterns add them to `autoMode.allow`.
- Some blocks stay regardless (see the classifier precedence order in the auto-mode-config docs); then leave auto mode and answer the prompt.
