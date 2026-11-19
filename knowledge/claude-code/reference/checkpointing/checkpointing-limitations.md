---
type: "Limit"
title: "Checkpointing limitations"
description: "What rewind does not track: Bash-only edits, subagent edits, external changes, mid-turn messages, symlinks and hard links."
resource: "https://code.claude.com/docs/en/checkpointing"
tags: [checkpointing, limits, subagents, bash]
kind: "limit"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "context: fork"
  - "background: false"
  - "/code-review --fix"
  - "No files were restored"
  - "Restored the code, but skipped N files"
  - "/debug"
  - "~/.claude/debug/<session-id>.txt"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "checkpointing"
    resource: "https://code.claude.com/docs/en/checkpointing"
    title: "Checkpointing"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Checkpoints give quick session-level recovery, not permanent history; keep using version control such as Git.

# Limits and defaults

- **Bash changes**: once Claude has edited a file with its file editing tools, `/rewind` also undoes later Bash changes to that file. A file only Bash commands changed is not tracked and stays; revert with version control. The menu counts changes to files Claude had already edited, whatever made them.
- **Subagent edits**: usually not captured in session checkpoints. A foreground forked skill (`context: fork`, run in the foreground with `background: false`; a few situations force foreground) edits your working tree during your own turn, so rewinding restores it. Any other subagent: only files Claude had already edited in your conversation are restored; other subagent edits stay. This includes a forked skill running in the background (the default) and a background `/code-review --fix` run.
- **External changes**: manual edits outside Claude Code and edits from other concurrent sessions are normally not captured, unless they touch the same files.
- **Mid-turn messages**: a message typed while Claude was working can be marked **No code restore** (no checkpoint of its own). To undo the edits after it, select the prompt that started the turn and choose Restore code or Restore code and conversation; that reverts the whole turn's edits, including earlier ones.
- **Symlinks and hard links**: not rewound. Restore code skips any tracked symlink or hard link and shows `Restored the code, but skipped N files`; skipped files keep current contents (dotfile-manager symlinks and pnpm hard links qualify). Turn on `/debug` before restoring to have `~/.claude/debug/<session-id>.txt` name each skipped path.
