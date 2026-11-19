---
type: "Feature"
title: "bypassPermissions mode"
description: "Disables prompts and safety checks; enabling rules, root refusal, warning dialog, background-session and cloud limits."
resource: "https://code.claude.com/docs/en/permission-modes"
tags: [bypass, permissions, unattended, containers, root]
kind: "behavior"
maturity: "unlabelled"
since: "2.1.248"
surfaces: [cli, headless, sdk]
requires: "Isolated environment (container, VM, dev container)"
identifiers:
  - "bypassPermissions"
  - "--dangerously-skip-permissions"
  - "--allow-dangerously-skip-permissions"
  - "--permission-mode bypassPermissions"
  - "skipDangerousModePermissionPrompt"
  - "permissions.disableBypassPermissionsMode"
  - "--restricted"
  - "CLAUDE_CODE_RESTRICTED"
  - "--setting-sources"
  - "isolatePeerMachines"
  - "crossSessionInbound"
  - "claude --bg"
  - "claude agents"
orchestration: "high"
generated: { by: "claude-code/sonnet-5.5", at: "2026-11-19T20:00:00Z" }
sources:
  - id: "permission-modes"
    resource: "https://code.claude.com/docs/en/permission-modes"
    title: "Choose a permission mode"
stale_after: "2027-01-19T00:00:00Z"
---

# What it is

`bypassPermissions` disables prompts and safety checks, including writes to protected paths. The docs warn it offers no protection against prompt injection or unintended actions; use only in isolated environments (containers, VMs, dev containers without internet). Even here the [actions no mode approves](./actions-no-mode-approves.md) still prompt or deny, as do the `Remove-Item` denies. Reading another organization's public artifact needs an approval this mode does not ask for, so Claude cannot read one. Two cross-session messaging safeguards stay: the `isolatePeerMachines` approval prompt for messages beyond this machine, and, when no `crossSessionInbound` value applies, inbound messages from another of your sessions are held for approval unless the sender says it also bypasses prompts (held messages are re-evaluated when you leave the mode).

# How to use it

You cannot enter it from a session started without it enabled. Enable at launch: `permissions.defaultMode: "bypassPermissions"` or `claude --permission-mode bypassPermissions` (equivalent: `--dangerously-skip-permissions`). Administrators block it with `permissions.disableBypassPermissionsMode` = `"disable"`.

First interactive start shows a warning dialog: accept sets `skipDangerousModePermissionPrompt` to `true` in `~/.claude/settings.json` (remove or set `false` to see again); decline exits. With `--setting-sources` lacking `user` the dialog can reappear; use `--setting-sources user,project`. No dialog in non-interactive mode.

# Limits and defaults

- Plan mode: in interactive terminal sessions with bypass available, plan-mode blocks are not enforced (Claude is told to plan but edits/commands run); ask rules and critical-path removals still prompt. Plan mode keeps its blocks in `-p`, Agent SDK and VS Code chat panel; there `--allow-dangerously-skip-permissions` makes bypass selectable later.
- Background sessions (`claude --bg`) honor an acceptance recorded in user or managed settings. With none, `claude --bg --permission-mode bypassPermissions` is refused. With the key only in `.claude/settings.local.json`, the request is ignored: `--allow-dangerously-skip-permissions` leaves bypass out of the cycle; the other flags start Manual. Notice: `Bypass permissions was requested at launch and ignored · if that was you, ~/.claude/settings.json needs "skipDangerousModePermissionPrompt": true`. Fix: add the key to `~/.claude/settings.json`, start a new background session.
- `claude agents` shows the warning even if interactive sessions skip it when the key is only in `.claude/settings.local.json` or a `--settings` file; accept to write it to `~/.claude/settings.json`.
- Linux/macOS: refuses to start as root or under `sudo` (`--dangerously-skip-permissions cannot be used with root/sudo privileges for security reasons`); skipped inside a recognized sandbox. The dev container runs as non-root.
- `--restricted` (v2.1.248+) refuses it: `Error: bypassPermissions not supported in restricted mode`. Start without `--restricted` or `CLAUDE_CODE_RESTRICTED` to keep bypass.
- Cloud sessions ignore `defaultMode: "bypassPermissions"` and `"dontAsk"` from settings files, silently, so checked-in settings cannot start bypass in the cloud.
