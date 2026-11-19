---
type: "Reference"
title: "Universal JSON output fields and terminalSequence"
description: "JSON fields every hook may print (continue, stopReason, systemMessage, terminalSequence), the 10,000-character cap and terminal notification rules."
resource: "https://code.claude.com/docs/en/hooks"
tags: [hooks, json-output, terminal, limits]
kind: "api"
maturity: "unlabelled"
since: ""
surfaces: [cli, sdk]
requires: ""
identifiers:
  - "continue"
  - "stopReason"
  - "suppressOutput"
  - "systemMessage"
  - "terminalSequence"
  - "additionalContext"
  - "initialUserMessage"
  - "hookSpecificOutput"
  - "hookEventName"
  - "decision"
  - "reason"
  - "SDKInformationalMessage"
  - "allow-passthrough"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "hooks"
    resource: "https://code.claude.com/docs/en/hooks"
    title: "Hooks reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Exit 0 and print one JSON object to stdout for finer control than exit codes. Three kinds of fields: universal fields (below), top-level `decision`/`reason` (some events), and `hookSpecificOutput` (requires `hookEventName` set to the event name). Print nothing else to stdout: stray text (e.g. shell profile echo) stops the object being read as JSON for non-async hooks.

# How to use it

| Field | Default | Description |
| :- | :- | :- |
| `continue` | `true` | If `false`, Claude stops entirely after the hook. Does not block a `PreToolUse` call; also return `permissionDecision: "deny"` |
| `stopReason` | none | Shown to the user when `continue` is false; stays in the conversation |
| `suppressOutput` | `false` | Has no effect |
| `systemMessage` | none | Warning shown to the user; in Agent SDK and `--output-format stream-json` it can arrive as an `SDKInformationalMessage` |
| `terminalSequence` | none | Terminal escape sequence for Claude Code to emit; allowlisted OSC `0`/`1`/`2`/`9`/`99`/`777` and BEL; ignored if anything outside the allowlist |

Stop example: `{ "continue": false, "stopReason": "Build failed, fix errors before continuing" }`. For `PreToolUse`/`PostToolUse` the stop applies even when the call fails or completes while streaming, but not when the permission check refuses the `PreToolUse` call.

`terminalSequence` allowlist: OSC 0/1/2 titles; OSC 9 (iTerm2, ConEmu, Windows Terminal, WezTerm notifications, incl. `9;4` taskbar progress); OSC 99 Kitty; OSC 777 urxvt, Ghostty, Warp; bare BEL; terminated by BEL or ST. Rejected: CSI cursor/color, OSC palette, OSC 8 hyperlinks, OSC 52 clipboard, OSC 1337. Works on events that discard `systemMessage` and `continue` (`Notification`, `StopFailure`).

# Limits and defaults

- `additionalContext`, `systemMessage`, `initialUserMessage` strings and plain stdout are each capped at 10,000 characters (each field measured separately, even across several hooks). Over the cap (except `PreCompact` stdout) the output is saved to a file in the session directory and replaced by the path plus a preview of the first 2,000 characters; Claude is not asked to read it. No setting raises this cap.
- `terminalSequence`: emitted only in an interactive session with the interface open; ignored in `-p` mode and the Agent SDK; not for background hooks (`async`/`asyncRewake`); a `WorktreeCreate` command hook cannot return JSON (stdout is the path) but an HTTP one can.
- tmux 3.3+: add `set -g allow-passthrough on` to `~/.tmux.conf` and run `tmux source-file ~/.tmux.conf`; `all` instead of `on` (tmux 3.4+) lets other attached panes send them. GNU screen: keep Claude Code's window showing.
