---
type: "Reference"
title: "Command-specific refusals (/desktop, /recap, /output-style, /feedback)"
description: "Refusals for /desktop, /terminal-setup in Zed, /skill-doctor, /output-style, /recap and /feedback, mostly over Remote Control or relayed messages."
resource: "https://code.claude.com/docs/en/errors"
tags: [errors, slash-commands, remote-control, output-styles]
kind: "slash_command"
maturity: "unlabelled"
since: ""
surfaces: [cli, desktop, mobile, web]
requires: ""
identifiers:
  - "/desktop"
  - "/app"
  - "claude --desktop"
  - "/terminal-setup"
  - "/skill-doctor"
  - "/output-style"
  - "/config outputStyle"
  - "outputStyle"
  - "settingSources"
  - "--setting-sources"
  - ".claude/settings.local.json"
  - "/recap"
  - "/feedback"
  - "/bug"
  - "/share"
orchestration: "low"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "errors"
    resource: "https://code.claude.com/docs/en/errors"
    title: "Error reference"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Messages from individual slash commands that refuse to run in some contexts.

# How to use it

| Command | Message / behaviour | Fix |
|---|---|---|
| `/desktop`, `/app`, `claude --desktop` | `Couldn't open Claude Desktop (...)`: macOS `open` or Windows `rundll32` failed; `claude --desktop` exits 1 (wording changed in v2.1.275 and v2.1.285) | Open Desktop yourself and retry; `/debug` or `--debug-file` for detail |
| `/terminal-setup` in Zed | Leaves `keymap.json` unchanged for unreadable file, non-array content, failed `.bak` backup, or failed verification; prints the binding to add: `{ "context": "Terminal", "bindings": { "shift-enter": ["terminal::SendText", "\u001b\r"] } }`. Before v2.1.247 it replaced the whole file when comments/trailing commas were present | Paste the block manually |
| `/skill-doctor` | `Skill usage reports are not available on this connection.` over Remote Control | Run in the host terminal or `claude -p "/skill-doctor"` |
| `/output-style` over Remote Control or relayed message | Only built-in styles are listed or selected; custom style names get the same reply as unknown names | Pick a built-in style, or set `outputStyle` in `.claude/settings.local.json` |
| `/output-style` or `/config outputStyle=` with setting sources lacking `local` | `Output styles are saved to local settings (.claude/settings.local.json), which this session doesn't load` (Agent SDK `settingSources` or `--setting-sources` without `local`) | Add `local` to sources, or set `outputStyle` in a loaded settings file; in the TypeScript SDK use the inline `settings` object |
| `/recap` | `/recap only runs when you ask for it yourself ...`: relayed Slack/Teams/project messages, cloud scheduled tasks and other programs cannot request it; `claude -p "/recap"` and your own Agent SDK app count as your own input | Run it yourself in the session |
| `/feedback`, `/bug`, `/share` | `/feedback is disabled by your organization's policy`; also lasts 7 days on this machine after the service refused a report (`Feedback has not been enabled for your organization`; since v2.1.319; before v2.1.302 the text said to contact the admin) | Open an issue at github.com/anthropics/claude-code/issues |

# Notes

These are interface-level; the `/recap` and `/output-style` restrictions reflect that relayed or automated input is treated as possibly not from the account owner.
