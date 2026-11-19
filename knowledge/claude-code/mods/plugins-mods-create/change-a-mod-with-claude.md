---
type: "Guide"
title: "Change a mod with Claude"
description: "Start with --plugin-dir at the mod so Claude's edits load in the same session; edits need approval in default and acceptEdits modes."
resource: "https://code.claude.com/docs/en/plugins/mods/create"
tags: [mods, editing, protected-paths, plugin-dir]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "--plugin-dir"
  - "claude plugin validate"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "plugins-mods-create"
    resource: "https://code.claude.com/docs/en/plugins/mods/create"
    title: "Create a mod"
stale_after: "2027-01-19T00:00:00Z"
---

# How to use it

Start the session with `claude --plugin-dir ./first-mod`, then ask for the change. Claude edits the hooks module, runs `claude plugin validate`, and fixes what it reports. A directory loaded with `--plugin-dir` is a protected path, so in `default` and `acceptEdits` modes each edit needs approval. Files saved during the turn reload when the turn ends.
