---
type: "Feature"
title: "Review changes with /diff"
description: "The /diff command opens a diff panel (fullscreen) or dialog (classic) built from the cc-plugin-diff built-in mod."
resource: "https://code.claude.com/docs/en/interactive-mode#review-changes-with-diff"
tags: [diff, review, git, mod, fullscreen]
kind: "slash_command"
maturity: "unlabelled"
since: "2.1.287"
surfaces: [cli]
requires: "Panel: fullscreen rendering, git repository, terminal at least 110 columns wide"
identifiers:
  - "/diff"
  - "Ctrl+X B"
  - "cc-plugin-diff"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "interactive-mode"
    resource: "https://code.claude.com/docs/en/interactive-mode"
    title: "Interactive mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`/diff` shows uncommitted working-tree changes plus Claude's edits. With fullscreen rendering a panel opens beside the conversation and updates as Claude edits or runs shell commands; in the classic renderer a dialog opens above the prompt. Both come from `cc-plugin-diff`, a built-in mod; disabling it in `/plugin` restores the earlier panel and diff viewer.

# How to use it

- Panel needs v2.1.287+. It auto-opens when Claude edits files in terminals at least 144 columns wide; after you open it once, later sessions open it in any terminal wide enough. Closing it keeps it closed until `/diff` again.
- Panel actions: click a file; `ask` attaches that file's diff to the next prompt (shows `asked ✓`; a second file replaces the first); `source` picker chooses `Current` or a turn `T1`, `T2`, ...; skipped test and generated files and pre-session changes expand on click; `Ctrl+X B` cycles comparison base (this session / uncommitted / since branch split from default branch), remembered per repository; scroll the list with `Alt+Up`/`Alt+Down` or `Ctrl+Up`/`Ctrl+Down`.
- Dialog: Up/Down select, Enter opens a file's diff, Esc goes back or closes, Tab moves to `source` picker or the `ask` button. Compares against `HEAD` or the last base chosen in the panel.

# Limits and defaults

Submodules appear as one entry, only when their commit pointer changes. Turn views come from Claude's file edits, so changes made via shell commands appear only under `Current`. During an unfinished merge, rebase, cherry-pick or revert the panel keeps its last view.
