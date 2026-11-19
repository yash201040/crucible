---
type: "Guide"
title: "Examples: auto-format and block protected files"
description: "PostToolUse Prettier on Edit|Write and a PreToolUse exit-2 script that blocks edits to .env, package-lock.json and .git/."
resource: "https://code.claude.com/docs/en/hooks-guide"
tags: [hooks, examples, pretooluse, posttooluse]
kind: "hook"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: "jq for the shell examples"
identifiers:
  - "PostToolUse"
  - "PreToolUse"
  - ".claude/hooks/protect-files.sh"
  - "$CLAUDE_PROJECT_DIR"
  - "FileChanged"
  - "Edit(/.env)"
  - "permissions.deny"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks-guide"
    resource: "https://code.claude.com/docs/en/hooks-guide"
    title: "Automate actions with hooks"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Two worked examples. Auto-format: a `PostToolUse` hook with matcher `Edit|Write` running `f=$(jq -r '.tool_input.file_path') && npx prettier --write --ignore-unknown "$f"`, in `.claude/settings.json`. Success shows nothing in the conversation. To reformat a file however it changes (including via `Bash`), use a `FileChanged` hook.

Protect files: a script `.claude/hooks/protect-files.sh` reads stdin JSON, extracts `.tool_input.file_path`, normalizes backslashes, and `exit 2` with a `Blocked:` stderr message if the path contains `.env`, `package-lock.json` or `.git/`. Make it executable (`chmod +x`), register under `PreToolUse` with matcher `Edit|Write` and command `"$CLAUDE_PROJECT_DIR"/.claude/hooks/protect-files.sh`. Claude gets the stderr text as feedback.

# Limits and defaults

Claude can still change protected files through shell commands. Add `Edit` deny rules per path under `permissions.deny` (like `Edit(/.env)`) to block some of those, and use sandboxing to limit which files commands can write.
