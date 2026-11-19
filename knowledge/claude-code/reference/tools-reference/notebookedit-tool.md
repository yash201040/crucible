---
type: "Feature"
title: "NotebookEdit tool behavior"
description: "Cell-level Jupyter edits with replace, insert and delete modes; replacing a code cell clears its outputs."
resource: "https://code.claude.com/docs/en/tools-reference#notebookedit-tool-behavior"
tags: [notebook, jupyter, edit, tools]
kind: "tool"
maturity: "unlabelled"
since: ""
surfaces: [cli, ide]
requires: ""
identifiers:
  - "NotebookEdit"
  - "cell_id"
  - "cell_type"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "tools-reference"
    resource: "https://code.claude.com/docs/en/tools-reference"
    title: "Tools reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Targets cells by `cell_id`; no string replacement across the notebook. Modes: `replace` (default, overwrites source), `insert` (new cell after the target; with no `cell_id` at the start; needs `cell_type` of `code` or `markdown`), `delete`.

# Limits and defaults

Refuses a non-UTF-8 notebook and writes nothing. Permission rules use the `Edit(...)` path format, e.g. `Edit(notebooks/**)`. Replacing a code cell clears its execution count and saved outputs; re-run the cell to restore them.
