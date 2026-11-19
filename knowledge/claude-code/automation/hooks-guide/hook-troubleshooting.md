---
type: "Guide"
title: "Hook troubleshooting"
description: "Fixes for hooks that do not fire, errors, JSON with no effect, and how to inspect what a hook did with debug logs."
resource: "https://code.claude.com/docs/en/hooks-guide"
tags: [hooks, troubleshooting, debug, json]
kind: "behavior"
maturity: "unlabelled"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "claude --debug"
  - "--debug-file"
  - "/debug"
  - "Hook output does not start with {"
  - "Hook JSON output had unrecognized keys"
  - "args"
  - "Ctrl+O"
orchestration: "medium"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks-guide"
    resource: "https://code.claude.com/docs/en/hooks-guide"
    title: "Automate actions with hooks"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Checks by symptom.

# How to use it

- Hook not firing: run `/hooks` for the right event; invoke a skill first if the hook is in its frontmatter; matchers are case-sensitive; check you chose the right event (`PreToolUse` before, `PostToolUse` after).
- "PreToolUse hook error: ...": test by piping sample JSON (`echo '{"tool_name":"Bash","tool_input":{"command":"ls"}}' | ./my-hook.sh; echo $?`); use absolute paths or `${CLAUDE_PROJECT_DIR}`; add `"args": []` to use exec form (spawns the script without a shell); install `jq` or use Python/Node; `chmod +x`; on Windows a message containing `blocking because Git Bash wasn't found` means a failed or timed-out hook blocked the call. A JSON validation or parse message appears even on exit 0; build the payload with a JSON encoder such as `jq`.
- `/hooks` shows nothing: wait for the watcher or restart; JSON must be valid (no trailing commas or comments); check file location.
- JSON has no effect: (1) shell profile output before the JSON (an unconditional `echo` in `~/.zshrc`/`~/.bashrc`, or `BASH_ENV`, since output not starting with `{` is plain text unless the hook is async); search the debug log for `Hook output does not start with {` and wrap echoes in `if [[ $- == *i* ]]`. (2) Fields at the wrong level, such as `permissionDecision` or `additionalContext` at top level instead of inside `hookSpecificOutput`; search for `Hook JSON output had unrecognized keys`.
- Check what a hook did: `Ctrl+O` transcript view. Success shows nothing unless JSON surfaces `systemMessage` or Stop feedback. Blocking error shows the message on most events (not `ConfigChange`, `Elicitation`). A non-blocking error shows `Failed with non-blocking status code:`, not shown for a failing command hook on `Notification`.

# Notes

Debug log: start with `claude --debug-file /tmp/claude.log` and tail it, or run `/debug` mid-session to enable logging and find the path.
