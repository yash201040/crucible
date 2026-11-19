---
type: "Feature"
title: "Process wrapper (corporate launcher) coverage"
description: "CLAUDE_CODE_PROCESS_WRAPPER or the processWrapper setting runs every process Claude Code starts from its own binary through a required launcher."
resource: "https://code.claude.com/docs/en/corporate-launcher"
tags: [launcher, process-wrapper, background-service, managed-settings]
kind: "mixed"
maturity: "unlabelled"
since: "2.1.208"
surfaces: [cli]
requires: "Claude Code v2.1.208+ for the env var; v2.1.210+ for the processWrapper setting; not supported on Windows"
identifiers:
  - "CLAUDE_CODE_PROCESS_WRAPPER"
  - "processWrapper"
  - "claude daemon stop --any"
  - "claude daemon status"
  - "claude agents"
  - "disableDeepLinkRegistration"
  - "CLAUDE_CODE_SHELL_PREFIX"
  - "/status"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "corporate-launcher"
    resource: "https://code.claude.com/docs/en/corporate-launcher"
    title: "Run Claude Code behind a corporate launcher"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

For organizations that require every process to start through a mandatory launcher (sandbox, network controls, credential injection). `CLAUDE_CODE_PROCESS_WRAPPER` makes Claude Code run your launcher with the Claude Code command as its arguments for every process it starts from its own binary. A launcher wrapping `claude` on `PATH` cannot reach the background service or its sessions, which start from the binary path.

# How to use it

Covered (when set): the background service started by `claude agents` and background sessions; the terminal host and session in each agent view row, including warm standby sessions; sessions respawned after an update or crash; Claude Code's self-relaunch for updates; Remote Control session processes (v2.1.210+); split-pane agent-team teammate sessions in tmux or iTerm2 (v2.1.210+).

Not covered: a session you start yourself in a terminal (put a `claude` script earlier on `PATH` that runs the launcher; do not replace the managed symlink); sessions from `claude-cli://` deep links (set `disableDeepLinkRegistration` to `"disable"` before a new user's first run; does not remove an existing handler); the relaunch from `--worktree` with `--tmux`; the Claude in Chrome native-messaging host.

Setup:
1. Write an executable launcher at an absolute path ending in `exec "$@"`.
2. Set it in the `env` block of a settings file (a shell export is not enough, as the service outlives the shell): `{"env": {"CLAUDE_CODE_PROCESS_WRAPPER": "/opt/corp/launcher"}}`. Managed settings override `~/.claude/settings.json` and shell exports. The top-level `processWrapper` key carries the same value (env var wins if both set); it appears on the security approval dialog for remote managed settings.
3. Restart: `claude daemon stop --any`, then restart sessions. The first new session after a settings push retires a stale unwrapped on-demand service.
4. Verify: `/status` Self-exec entry (warns on mismatch) or `claude daemon status`.

# Limits and defaults

- Project and local settings (`.claude/settings.json`, `.claude/settings.local.json`) cannot set it; ignored with a debug-log warning.
- Windows: variable ignored, processes start unwrapped, only a debug-log warning.
- Earlier versions silently ignore the env var (before v2.1.208) or the setting key (before v2.1.210).
- With a launcher, `ps` no longer shows `claude bg-pty-host` and `claude bg-spare` labels.
- `CLAUDE_CODE_SHELL_PREFIX` is different: it wraps shell commands Claude runs (Bash tool, hooks, stdio MCP server starts) as one shell-quoted string in `$1`; a launcher for one does not work as the other.
