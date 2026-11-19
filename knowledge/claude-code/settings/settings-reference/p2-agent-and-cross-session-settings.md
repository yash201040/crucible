---
type: "Reference"
title: "Agent, cross-session and process settings"
description: "Settings for the default main-thread agent, cross-session messaging, agent view, background process wrapper and teammate display."
resource: "https://code.claude.com/docs/en/settings-reference"
tags: [settings, agents, cross-session, teammates]
kind: "setting"
maturity: "unlabelled"
since: "2.1.224"
surfaces: [cli]
requires: ""
identifiers:
  - "agent"
  - "--agent"
  - "crossSessionInbound"
  - "disableAgentView"
  - "CLAUDE_CODE_DISABLE_AGENT_VIEW"
  - "isolatePeerMachines"
  - "processWrapper"
  - "CLAUDE_CODE_PROCESS_WRAPPER"
  - "teammateMode"
  - "--teammate-mode"
  - "SendMessage"
  - "claude agents"
  - "--bg"
  - "/background"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "settings-reference"
    resource: "https://code.claude.com/docs/en/settings-reference"
    title: "All settings"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

Any-file settings for agents and sessions unless noted.

# How to use it

| Name | Type / values | Default | What it does |
| :- | :- | :- | :- |
| `agent` | string, built-in or custom agent name | unset | Runs the main thread as that subagent (its system prompt, tool limits, model) and sets the default agent for sessions dispatched from `claude agents`. `--agent` overrides per session |
| `crossSessionInbound` | `"accept"`, `"hold"`, `"refuse"` | unset: decided per message from permission-mode classes | `accept` delivers, `hold` shows a notice without delivering, `refuse` drops. Resolution: managed, then `--settings`, then user; first found applies. `refuse` is stricter than `hold` than `accept`. Project or local `hold`/`refuse` applies only when stricter, or when no trusted source sets a value. `/config` row Messages from your other sessions (v2.1.232+) writes user settings |
| `disableAgentView` | Boolean | unset (available) | Turns off background agents and agent view: `claude agents`, `--bg`, `/background`, the on-demand supervisor. `CLAUDE_CODE_DISABLE_AGENT_VIEW` per session; neither can undo the other |
| `isolatePeerMachines` | Boolean | unset | `true` requires approval before Claude's `SendMessage` reaches your sessions beyond this machine, even in `bypassPermissions` mode. A `true` from any scope applies, so a project file can turn it on but not off. Needs v2.1.224+ |
| `processWrapper` | string argv prefix; user or managed | unset | macOS and Linux: corporate launcher placed before background processes Claude Code starts; it must exec into Claude Code. Ignored on Windows. `CLAUDE_CODE_PROCESS_WRAPPER` overrides per session. Needs v2.1.210+ |
| `teammateMode` | `"in-process"`, `"auto"`, `"tmux"`, `"iterm2"` | `"in-process"` | Where agent-team teammates display. `auto`: split panes inside tmux, or iTerm2 with `it2` on PATH or tmux installed; else in-process. `iterm2` uses the `it2` CLI. `--teammate-mode` overrides per session. Reads an old `~/.claude.json` value |

# Limits and defaults

An unrecognized `crossSessionInbound` value triggers a warning and, while present in a user, project, local or `--settings` file, inbound messages are held even if a higher source says `accept` (a `refuse` elsewhere still applies). In managed settings an unrecognized value acts as `refuse` until fixed. Before v2.1.248 it was ignored silently.
