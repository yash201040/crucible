---
type: "Feature"
title: "Dispatch from the shell with --bg"
description: "claude --bg starts a background session directly; combines with --agent, --resume, --name, --model and --exec for shell jobs."
resource: "https://code.claude.com/docs/en/agent-view"
tags: [agent-view, headless, bg, exec]
kind: "cli_flag"
maturity: "research-preview"
since: ""
surfaces: [cli]
requires: ""
identifiers:
  - "--bg"
  - "--background"
  - "--exec"
  - "--agent"
  - "--name"
  - "--resume"
  - "--continue"
  - "--fork-session"
  - "claude logs <id>"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "agent-view"
    resource: "https://code.claude.com/docs/en/agent-view"
    title: "Manage multiple agents with agent view"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`--bg` (long form `--background`) starts a session that goes straight to the background. The prompt is a positional argument, not a `-p` value. `--bg` with `-p`/`--print` is rejected before any session is created (since v2.1.198), because print mode never starts the interactive session that `claude agents` attaches to.

# How to use it

```bash
claude --bg "investigate the flaky SettingsChangeDetector test"
claude --agent code-reviewer --bg "address review comments on PR 1234"
claude --resume <full-session-id> --bg "pick up where you left off"
claude --bg --name "flaky-test-fix" "investigate the flaky test"
claude --bg --exec 'pytest -x'
```

Output: `backgrounded · 7c5dcf5d · flaky-test-fix` plus hints for `claude agents`, `claude attach <id>`, `claude logs <id>`, `claude stop <id>`. May print `Starting background service…` first. Use `--model` with `--bg` to pick a model per session.

# Limits and defaults

- Untrusted directory: the trust dialog appears; where none can appear (scripts) it exits with the `Workspace not trusted` error (v2.1.281+).
- `--agent` with an unknown name prints `no agent named` and still reports backgrounded, but the session exits at once with `--agent '<name>' not found` (v2.1.191). On resume or restart the agent and tool restrictions are restored, searching the session's own directory first (trusted workspace); a vanished agent gives a warning and default tools.
- `--resume <id> --bg` (v2.1.257+): continues under the same ID or starts a copy under a new ID with a `note:` line. `--continue`, bare `--resume`, or `--resume` with name/path always start a copy; add `--fork-session` to do so deliberately.
- A prompt containing `--bg` is delivered as text; the flag is read only before a bare `--` and outside another flag's value (v2.1.299). Ambiguous positions exit with `Couldn't tell whether --bg is a flag or text here`.
- `--exec` shell jobs: PTY-backed, appear as a row with latest output line as status; no model invoked, output goes to no session. Output is in memory only (not on disk); row and output clean up about five minutes after the command exits. Read via attach, `Space`, or `claude logs <id>`. Such rows are never restarted.
